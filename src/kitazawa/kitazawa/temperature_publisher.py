import rclpy
from rclpy.node import Node
from std_msgs.msg import String  # メッセージ型をインポート

class TemperaturePublisher(Node):
    def __init__(self):
        super().__init__('temperature_publisher')
        self.publisher_ = self.create_publisher(String, 'temperature_topic', 10)
        self.timer = self.create_timer(1.0, self.publish_temperature)
        self.get_logger().info('Temperature Publisher Node started.')

    def publish_temperature(self):
        msg = String()
        msg.data = "Temperature: 25.0°C"
        self.publisher_.publish(msg)
        self.get_logger().info(f'Publishing: "{msg.data}"')

def main():
    rclpy.init()
    node = TemperaturePublisher()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()

