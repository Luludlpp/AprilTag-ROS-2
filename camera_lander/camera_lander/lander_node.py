from geometry_msgs.msg import Vector3, Point, PointStamped
from tf2_msgs.msg import TFMessage
from rclpy.node import Node

from gtts import gTTS
import random
import pygame
import rclpy
import time

from pysinewave import SineWave


class LanderNode(Node):

    def __init__(self):
        # Call the rclpy Node supercalss constructor (black b>ox low-level shit, look into if you want)
        super().__init__('lander_node')

        # create a subscriber object to get april tag TFs from the april tag node
        self.april_tag_subscriber_ = self.create_subscription(
            msg_type = TFMessage,
            topic = "tf",
            callback = self.listener_calllback,
            qos_profile = 10
            )
        
        # system state parameters
        self.error = Vector3() # current positional error
        self.position = Vector3() # current position of camera
        self.goal_position = Vector3() # goal landing position


        # initialize google tts and sound output stuff
        pygame.init()
        pygame.mixer.init()
        db_per_sec = 100
        self.sounds_dir_path = "src/AprilTag-ROS-2/camera_lander/resource/sounds/"
        self.freq_LR = 200
        self.sine_LR_fixed = SineWave(channels=2, channel_side="l", pitch_per_second=10, frequency=self.freq_LR, decibels_per_second=db_per_sec)
        self.sine_LR = SineWave(channels=2, channel_side="l", pitch_per_second=10, frequency=self.freq_LR, decibels_per_second=db_per_sec)
        self.freq_FB = 300
        self.sine_FB_fixed = SineWave(channels=2, channel_side="r", pitch_per_second=10, frequency=self.freq_FB, decibels_per_second=db_per_sec)
        self.sine_FB = SineWave(channels=2, channel_side="r", pitch_per_second=10, frequency=self.freq_FB, decibels_per_second=db_per_sec)



        # goal position stuff
        self.pick_goal_pos()
    
    def pick_goal_pos(self):
        """
        Randomly choose and use TTS to notify the user of goal landing position.
        Publish the goal landing position to /camera_lander/landing_pos ROS2 topic (pointstamped msg).
        """
        # define landing spot positions
        grid_size = .06 # m
        landing_spots = {
            "A": Vector3(x=-grid_size, y=0.0,        z=0.0),
            "B": Vector3(x=0.0,        y=grid_size,  z=0.0),
            "C": Vector3(x=grid_size,  y=0.0,        z=0.0),
            "D": Vector3(x=0.0,        y=-grid_size, z=0.0),
        }

        # choose random landing spot (A, B, C, or D)
        # spot_ID, self.goal_position = random.choice(list(landing_spots.items()))
        spot_ID = "C"; self.goal_position = landing_spots[spot_ID]

        # # DEBUG (I couldn't get this to work or it wouldnt show up in rviz anyway...)
        # print(spot_ID, self.goal_position)
        # goal_pub = self.create_publisher(PointStamped, "camera_lander/landing_pos", 10)
        # ps = PointStamped()
        # ps.header.stamp = self.get_clock().now().to_msg()
        # ps.header.frame_id = 'camera2'
        # ps.point.x = self.goal_position.x
        # ps.point.y = self.goal_position.y
        # ps.point.z = 0.0
        # goal_pub.publish(ps)

        # announce the goal position
        text = "you will be guided to land at position " + spot_ID  # google voice will say this
        sound = gTTS(text=text, lang="en", slow=False)              # generate TTS audio
        sound.save(self.sounds_dir_path + "intro.mp3")              # save sound to file
        pygame.mixer.music.load(self.sounds_dir_path + "intro.mp3") # load sound into pygame
        pygame.mixer.music.play()                                   # play sound with pygame

        while pygame.mixer.music.get_busy():
            pass

        # Frequency init
        self.sine_LR_fixed.play(); self.sine_LR.play()
        self.sine_FB_fixed.play(); self.sine_FB.play()


    
    def listener_calllback(self, msg: TFMessage):
        """
        Callback function to run whenever the node picks up a new April Tag detection msg.
        Calculate the camera lander's error from goal position and run the auditory
        user guidance method.

        Args:
            msg (TFMessage): Array of april tag TFs
        """
        # If no tags were picked up, immediately return
        if not msg.transforms:
            return
        
        # get tf data from msg
        transforms = msg.transforms

        # get camera's position
        for tf in transforms: # Iterate throught list of transforms (TFMessage)
            if tf.header.frame_id == "camera2": # find the camera2 tf
                self.position = tf.transform.translation
        
        # get positional error
        self.error.x = -self.goal_position.x + self.position.x
        self.error.y = -self.goal_position.y + self.position.y
        self.error.z = -self.goal_position.z + self.position.z

        # debug
        x_print = ["{:6.3f}".format(self.position.x), "{:6.3f}".format(self.error.x)]
        y_print = ["{:6.3f}".format(self.position.y), "{:6.3f}".format(self.error.y)]
        print(f"x: {x_print[0]} error: {x_print[1]} y: {y_print[0]} error: {y_print[1]}")
        # print(f"y: {y_print[0]} error: {y_print[1]}")

        # run user guidance method
        # self.play_sound()
        if self.error.z < 0.25 and abs(self.error.x) < 0.01 and abs(self.error.y) < 0.01:
            pygame.mixer.music.load(self.sounds_dir_path + "vine-boom.mp3")
            pygame.mixer.music.play()
            self.landing_sequence()
        else:
            self.user_guidance()
            print(self.error.z)
        
        # if abs(self.error.x) < 0.01 and abs(self.error.y) < 0.01 and not pygame.mixer.music.get_busy():
        #     pygame.mixer.music.load(self.sounds_dir_path + "vine-boom.mp3")
        #     pygame.mixer.music.play()
        
    def user_guidance(self):
        """
        Guide the user to land the camera rig by playing two monaural beat signals,
        one per ear. User listens through headphones. One channel provides guidance
        for left/right error, the other for forward/back error. As user moves closer
        to being directly over the goal position, the beat frequencies are modulated
        to sync up more and more, beating slower ad the camera aligns with the goal
        position. A beep beep beep is played when the user should lower the craft.
        """
        self.sine_FB.set_frequency(self.freq_FB - 100*self.error.y)
        self.sine_LR.set_frequency(self.freq_LR - 100*self.error.x)
        
        pass

    def landing_sequence(self):
        """
        Call when z level gets close to zero and the user should land.
        Play beep beep beep tone, fade out x/y guidance, terminate node
        """
        # stop L/R guidance sounds
        self.sine_FB.set_volume(-100)
        self.sine_LR.set_volume(-100)
        self.sine_FB_fixed.set_volume(-100)
        self.sine_LR_fixed.set_volume(-100)

        time.sleep(2)

        # shutdown
        self.destroy_node()
        rclpy.shutdown()

    def play_sound(self): 
        if abs(self.error.x) > 0.0075:
            if self.error.x > 0:
                print ("Right")
                if not pygame.mixer.music.get_busy():
                    pygame.mixer.music.load(self.sounds_dir_path + "right.mp3")
                    pygame.mixer.music.play()
            else: 
                print ("Left")
                if not pygame.mixer.music.get_busy():
                    pygame.mixer.music.load(self.sounds_dir_path + "left.mp3")
                    pygame.mixer.music.play()
        elif abs(self.error.y) > 0.0075:
            if self.error.y > 0:
                print ("Back")
                if not pygame.mixer.music.get_busy():
                    pygame.mixer.music.load(self.sounds_dir_path + "back.mp3")
                    pygame.mixer.music.play()
            else: 
                print ("Forward")
                if not pygame.mixer.music.get_busy():
                    pygame.mixer.music.load(self.sounds_dir_path + "forward.mp3")
                    pygame.mixer.music.play()
        elif abs(self.error.x) < 0.0075 and abs (self.error.y) < 0.0075:
            print ("Descend")
            if not pygame.mixer.music.get_busy():
                pygame.mixer.music.load(self.sounds_dir_path + "descend.mp3")
                pygame.mixer.music.play()
        else: 
            pass 

def main(args=None):
    rclpy.init(args=args)

    lander_node = LanderNode()

    rclpy.spin(lander_node)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    lander_node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
