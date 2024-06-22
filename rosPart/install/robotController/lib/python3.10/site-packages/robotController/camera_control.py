import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
from rclpy.qos import qos_profile_sensor_data

import cv2


class CameraControllo(Node):
  
  def __init__(self):

    super().__init__('camera_control')

    
    self.bridge = CvBridge()
    self.image_sub = self.create_subscription(Image,'/camera', self.image_callback,10)

  def image_callback(self,msg):

    cv_Image = self.bridge.imgmsg_to_cv2(msg)

    cv2.imshow('ros', cv_Image)  
    cv2.waitKey(1)

def main():
    rclpy.init()
    CameraControl_node=CameraControllo()
    rclpy.spin(CameraControl_node)
    
    rclpy.shutdown()

if __name__ == '__main__':
    main()                
