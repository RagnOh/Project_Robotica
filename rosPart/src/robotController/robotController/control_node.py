import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64MultiArray

class controlNode(Node):

    def __init__(self):
        super().__init__('control_node')
        self.publisher = self.create_publisher(Float64MultiArray,"/forward_position_controller/commands",10)
        self.timer = self.create_timer(1.0,self.timer_callback)

    def timer_callback(self):

        msg = Float64MultiArray()
        msg.data =[0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]
        self.publisher.publish(msg)
        self.get_logger().info("Pubblico array:")# [%.2f,%.2f]",msg.data[0],msg.data[1])

def main():
    rclpy.init()
    node = controlNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()            
