import rclpy
from rclpy.node import Node

class TemperatureSimulator(Node):
    def __init__(self):
        super().__init__('temperature_simulator')
        self.get_logger().info('Temperature Simulator Node started.')

def main():
    rclpy.init()
    node = TemperatureSimulator()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()

