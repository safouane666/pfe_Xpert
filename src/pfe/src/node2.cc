#include "rclcpp/rclcpp.hpp"
#include "std_msgs/msg/string.hpp"

class Node2 : public rclcpp::Node {
public:
    Node2() : Node("node2") {
        publisher_ = this->create_publisher<std_msgs::msg::String>("chatter", 10);
        subscription_ = this->create_subscription<std_msgs::msg::String>(
            "chatter", 10,
            [this](std_msgs::msg::String::SharedPtr msg) {
                RCLCPP_INFO(this->get_logger(), "Node2 heard: '%s'", msg->data.c_str());
            });
        timer_ = this->create_wall_timer(std::chrono::seconds(1),
                                         [this]() {
                                             std_msgs::msg::String msg;
                                             msg.data = "Hello I am node2";
                                             publisher_->publish(msg);
                                             RCLCPP_INFO(this->get_logger(), "Publishing: '%s'", msg.data.c_str());
                                         });
    }

private:
    rclcpp::Publisher<std_msgs::msg::String>::SharedPtr publisher_;
    rclcpp::Subscription<std_msgs::msg::String>::SharedPtr subscription_;
    rclcpp::TimerBase::SharedPtr timer_;
};

int main(int argc, char * argv[]) {
    rclcpp::init(argc, argv);
    rclcpp::spin(std::make_shared<Node2>());
    rclcpp::shutdown();
    return 0;
}
