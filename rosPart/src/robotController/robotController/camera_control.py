import rclpy
from rclpy.node import node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2


class CameraControl(Node)
  
  def __init__(self):
    self.bridge = CvBridge()
    self.image_sub = self.create_subscription(Image,'', self.image_callback,10)

  def image_callback(self,msg):

    cv_Image = self.bridge.imgmsg_to_cv2(msg)

    cv2.imshow('ros', cv_image)  
    cv2.waitKey(1)

def main():
        