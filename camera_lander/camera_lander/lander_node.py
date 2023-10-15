import rclpy
from rclpy.node import Node

from std_msgs.msg import String
from tf2_msgs.msg import TFMessage
from geometry_msgs.msg import TransformStamped, Transform, Vector3


class LanderNode(Node):

    def __init__(self):
        # Call the rclpy Node supercalss constructor (black box low-level shit, look into if you want)
        super().__init__('lander_node')

        # create a subscriber object to get april tag TFs from the april tag
        self.april_tag_subscriber_ = self.create_subscription(
            msg_type = TFMessage,
            topic = "tf",
            callback = self.listener_calllback,
            qos_profile = 10
            )
        
        # system state parameters
        self.goal_position = Vector3(x=0.0, y=0.0, z=0.0) # goal landing position
        self.position = Vector3 # current position of camera        
        self.error = Vector3 # current positional error
    
    def listener_calllback(self, msg: TFMessage):

        if not msg.transforms:
            return
        
        # get tf data from msg
        transforms = msg.transforms

        # get camera's position
        for tf in transforms: # Iterate throught list of transforms (TFMessage)
            if tf.header.frame_id == "camera2": # find the camera2 tf
                self.position = tf.transform.translation
                self.get_logger().info(f"camera position: {self.position}")
        
        # get positional error
        self.error = self.goal_position[] - self.position
    
    def audio_feedback(self):
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
