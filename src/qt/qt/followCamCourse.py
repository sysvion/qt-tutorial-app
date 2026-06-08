from .courseMeta import CourseMeta
from PySide6.QtWidgets import QTextBrowser, QVBoxLayout, QLabel, QScrollArea, QHBoxLayout, QComboBox
from PySide6.QtGui import QPixmap, QImage
from sensor_msgs.msg import CompressedImage
from PySide6.QtCore import Qt, QByteArray, QTimer
from .dialog import Dialog

#from .application import MainWindow

from typing import List, Tuple
from rclpy import subscription
from rclpy.node import Node

class FolowHandMeta(CourseMeta):

    def get_course_title(self):
        return "Basics of ros"

    def get_course_description(self):
        return "Learn the basics of ros2 by following a hand"
    
    def get_course_widget(self, app): # app will be an instance of Main window but i can't import it. Thanks python            

        return course(app)
    

class course(Dialog):


    app: Node
    camara_subscription: subscription = None
    def __init__(self, app,  parent=None):
        self.app = app

        # main
        introduction = QVBoxLayout()

        browser = QTextBrowser()

        browser.setHtml("""
                        <h1>Preamble 1: contents </h1>
                        
                        Ros2 is a system that facilitate the interchange of messages between large commurtial projects and your application 
                        Where it is posable to proof that the program always reacts the same way regartless of the input. Ros also allows for interchanging 
                        components so you can easely setup a test envioroment. <br>
                        <br>    
                        In this course you will be seting up a full pipeline where you import a webcam an hand tracking. Structured in the following slides:

                        <ul>
                            <li> Creating a package </li>
                            <li> Creating a publisher </li>
                            <li> Reading from a topic </li>
                        </ul>
                        """)
    
        introduction.addWidget(browser)


        package_widget = QScrollArea()
        package_widget.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        layout = QVBoxLayout()

        browser2 = QTextBrowser()
        
        browser2.setHtml("""
                        <h1> Preamble 2: workspace </h1>

                        Ros2 projects are structured in packages that can easily be stored in a version control system like Git or Mercurial. And there is
                        a build system that build all project in the correct order. The place where you store the packages are dependend on which build system used. Here i explain
                        <code>colcon</code>. a terminal command. 
                         
                         <h3>Creating a workspace</h3>
                         A colcon workspace is just a directory that has the following content:
                         <pre>
+--+ src/
|     source code that can be entirely be in a version control system
|
+--+ install/
|  |  A directory of generated content to link build programs where the setup.bash is the most important file.
|  + -- setup.bash
|          script that need to be sourced to run the code
|
+-- build
|     build artifacts. You may need to remove this.

+-- log
|   Build logs
                         </pre>

                         To create a package from scratch, you just need to create a src directory where it is fine to be cluttered with the directories listed above. It is also customary to
                         give the directory where src is the "_ws" suffix, symbolizing that this is a colcon workspace.

                         <blockquote>
                         <code>
$ mkdir -p ~/ Desktop/tutorial_ws/src
                         </code>
                         </blockquote>


                         language you want to use. And what the package should be called.<br>
                         <br>
                         But first you need a way to call ros2. To do that you need to source the ros2 setup file. Sourcing a script is like running the commands directly on your shell. Like running cd. And changing environment variables. You can also do this automatically by adding it to the .bashrc file.
                         
                         <blockquote>
                         <code>
$ source /opt/ros/jazzy/setup.bash 
                         </code>
                         </blockquote>

                        You can use the <code>ros2 pkg create</code> to create the framework. You can pass the <code>--help</code> flag to see all available options. For the tutorial, I will assume you have a python project with the node scaffolding that is given by the following command(s)
                         
                        <blockquote>
                        <code>
<span style="color:gray;">practicum@practicum-ubuntu:~/Desktop/tutorial_ws</span>$ cd src/ <br>
<span style="color:gray;">practicum@practicum-ubuntu:~/Desktop/tutorial_ws/src</span>$ ros2 pkg create --build-type ament_python --node-name main follow_hand
                        </code>
                        </blockquote>

                        With this command you get 3. One part is build files (<code>package.xml</code><code>setup.cfg</code> and <code>setup.py</code>). And another one is a directory where automated tests can be written. And a directory with the same name as the package.
                        Herein lives the source of the program. There is main.py. (Or what you have written after --node-name.) Here is an entry point of your program currently containing a Hello world program. To run the created program you need to build it. Therefore, you need to be at the root of the workspace and ros must be sourced. And run `colcon build`. When that is done. You can run your program using `ros2 run follow_hand main`
                        <blockquote>
                        <code>
 <br>
<span style="color:gray;">practicum@practicum-ubuntu:~/Desktop/tutorial_ws/src</span>$ cd ..

<span style="color:gray;">practicum@practicum-ubuntu:~/Desktop/tutorial_ws</span>$ colcon build --symlink-install
                        </code>
                        </blockquote>
                        """)

        
       
        layout.addWidget(browser2)
        
        package_widget.setLayout(layout)
        package_layout = QVBoxLayout()
        package_layout.addWidget(package_widget)

        publisher = QVBoxLayout()
        browser3 = QTextBrowser()
        browser3.setHtml("""
                       <h1>chapter 1: publisher</h1>
                        Now you know how to properly create and run code within the ros environment it is time to interact with other systems that uses ros.
                        On the next slide you will find a image previewer which gets updated every time it receives a message. Your job is to publish a camara feed so it could pick it up. 
                        Later we use video stream to detect a object so a robot moves relative to it.

                        <h3> Nodes </h3> 
                        Nodes are the cornerstone of the ros ecosystem. It is a python and c++ class that handles communication and timing of everything that happens in ros. You need to register everything that you transmit. And
                        for recieving you need to tell which function to call. It is best practice to give a node a single purpose. To create a node create a class that extends Node from rclpy (or rclcpp for c++ projects). And call the parent constructor to it give a name.
                        
                        <code>
                        <pre>
from rclpy.node import Node

class camara_publisher(Node):
    def __init__(self):
        super().__init__("my_webcam")
                         </pre>
                        </code>
                        
                        To create a publisher you need to call the <code>Node.create_publisher</code> function and store the return value so it doesn't get destroyed. The parameters you need to pass is the message type. Topic name (the address where the message is published.) And <a href="https://docs.ros.org/en/jazzy/Concepts/Intermediate/About-Quality-of-Service-Settings.html">Quality of Service settings</a> (later referred to as QoS). <br>
                         
  <br>
Everything that has been sent through a publisher will be stored for some time. The QoS settings also dictate how much will be stored. But because there is a lot of options that need to be set. There are convenient presents that can be used which contain the following:

< TODO fill the presets in from the qos documentation >
                         <br>
                         <br>
                         You can publish only datatype per publisher. But the structure can contain a lot. Arrays, numbers, chars. Every datastructure is defined by a msg files. And there is a lot of sets of standard messages. geometric data from geometry_msgs. sensor data from sensor_msgs. And msg that only contain primitives (std_msgs).<br> 

                         <code>
                         <pre>
from sensor_msgs.msg import CompressedImage
from rclpy.qos import QoSPresetProfiles
                         
class camara_publisher(Node):
    def __init__(self):
        super().__init__("my_webcam")
        self.camara_pub = self.create_publisher(
                CompressedImage,
                "/my/camera",
                QoSPresetProfiles.SYSTEM_DEFAULT.value,
                )
                         </pre>
                        </code>
                         
                        <h3> publishing the first messages </h3>
                        To publish a message you first need a ros running and creating a instance of the node. This should be in the main function. 
                         
                         <code>
                         <pre>
import rclpy
def main():
    rclpy.init()
    node = camara_publisher()
    
    // code

    rclpy.shutdown()
        
if __name__ == '__main__':
    main()                
                         </pre>
                         </code>
                         
                        You can publish msg by calling publish(msg=msg) on the poblisher what you have stored somewhere. On the code example given it is node.camara_pub.publish(msg=msg). But first you need to make a message. You can do it by constructing the class and filling in its parameters. But for standard messages there are ways to translate it from known structures like opencv to ros2 msg with a project like cv_bridge. 
                        For a vm you need to pastrough the camara to it. For VirtualBox the setting can be find in the Devices tab. <br>
                        <br>
                        In the next tab you will see all listed compressedImages Topic and a previewer.                   
                        """)
        browser3.setOpenExternalLinks(True)
        publisher.addWidget(browser3)

        publisher_previewer = QVBoxLayout()
 
        self.topic_selector = QComboBox()
        self.topic_selector.currentTextChanged.connect(self.changeCamaraSubscription)
        
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_camara_options)
        self.timer.start(1000) #ms

        self.camara_viewer = QLabel()
        publisher_previewer.addWidget(self.topic_selector)
        publisher_previewer.addWidget(self.camara_viewer)


        reciever = QVBoxLayout()
        browser4 = QTextBrowser()
        browser4.setHtml("""
                         <h1>chapter 2: Executor</h1>
                         In this chapter, you learn how to receive messages that are sent through ros. To do that, you need a executor.  And for the follow the object example. You will translate an image to a 3d coordinate. 
 
                         <h3>Subscriping to a topic</h3>
                         If you want to receive messages, you need to register them to a node just like you did as a receiver. Call <code>Node.create_subscription()</code> and give the same type of parameters as create_publisher. But you also need to give a 
                         callback function that has one  parameter, the received message. The create_subscription() will register this to the node so that the spun executor can fetch the messages and call the function. <br>
                         <br>
                         <b>create a new node that contains a subscripter for the images of your camara. Also create  a Pose publisher. Here is some starting code </b>
                         <code>
                         <pre>
from geometry_msgs.msg import Pose
class recv(Node):
    def __init__(self):
        super().__init__('recv')
        
        self.subscription = self.create_subscription(
            CompressedImage,
            'camara',
            self.on_recieve_images,
            QoSPresetProfiles.DEFAULT,
        )
        self.pose_pub = self.create_publisher(
            Pose
            # you pick the other parameters
        )
        self.opencv_bridge = CvBridge()
        
        

    def on_recieve_images(self, msg: CompressedImage):
        image = self.opencv_bridge.compressed_imgmsg_to_cv2()
        
        # sample object detection
        cv2.HoughCircles(
            # sam
        )
        
        response = Pose()
        # A Quaternion rotation
        response.pose.orientation.w = 1.0
        
        # please calculate a coordinate to a safe place. Please not to a wall. 0, 0, 0, is the base of the robot. Mesuremnts <i>should</i> be meters. 
        response.position.x = 0.5 
        response.position.y = 0.5
        response.position.z = 0.5

        self.pose_pub.publish(response)
                         
                         </pre>
                         </code>

                         As you may or may not noiticed there is no funcution to manually fetch data. To do actualy run the code you must spin the node. By spinning a note means running the job scueduler for it. The instance of the loop is colloquially called the <a href="https://docs.ros.org/en/jazzy/Concepts/Intermediate/About-Executors.html"><code>executor</code></a>. The executor goes though the following dession tree and calls the correct callback function    

                         The executor is a first in first out scheduler which runs your callbacks. With the order of execution: <br>
                         <img width="800" src="file://home/practicum/Downloads/executors_scheduling_semantics.png">
                        
                         There are a lot of ways to spin a node. There is the default that continualy runs (spin). There is a run once (spin_once). Spin until something compleats (spin_until_future_complete). All of those can also accept the executor parameter which chanches the method of execution (sigle or multithreading). Or which algorithom it using. (Sill use the table that you see above).<br>
                         
                         Example of spinning a signle node
                         <code>
                         <pre>
def main():
    rclpy.init()
    node = reciever()

    rclpy.spin(node)

    rclpy.shutdown()
                        </pre>
                        <code>
                        """)
        browser4.setOpenExternalLinks(True)

        reciever.addWidget(browser4)

        moveit = QVBoxLayout()
        browser5 = QTextBrowser()
        browser5.setHtml("""
                        <h1>moveit</h1>
                         ToDo. In person. code not tested.

                         <code>
                         <pre>
rclpy.init()

moveit_instance = None # I will the way to create this in person

my_node = Node('sub')
from geometry_msgs.msg import Pose, PoseStamped
planner = moveit_instance.get_planning_component("manipulator") # or ur_manipulator

def on_recieve(msg: Pose):
    pose_goal = PoseStamped()
    pose_goal.pose = msg
    pose_goal.header.frame_id = "tool" 
    planner.set_goal_state(pose_stamped_msg=pose_goal, pose_link="tool")
    plan_result = planner.plan()
    robot_trajectory = plan_result.trajectory
    moveit_instance.execute(robot_trajectory, controllers=[])    
                         
s = my_node.create_subscription(
    Pose,
    #name,
    self.on_recieve,
    QoSPresetProfiles.DEFAULT,
)

rclpy.spin(my_node)
                         </pre>
                         </code>
                         """)
        moveit.addWidget(browser5)



        slides = [
            introduction,
            package_layout,
            publisher,
            publisher_previewer,
            reciever,
            moveit
        ]
        super().__init__(slides,parent=parent)


    def update_camara_options(self):
        current = self.topic_selector.currentText()
        self.topic_selector.clear()

        topic: Tuple[str, List[str]]
        for topic in self.app.get_topic_names_and_types():
            for type in topic[1]:
                if (type == "sensor_msgs/msg/CompressedImage"):
                    self.topic_selector.addItem(topic[0])

                    if topic[0] == current:
                        self.topic_selector.setCurrentText(topic[0])


    def changeCamaraSubscription(self, topic):
        print("on change")
        print(topic)
        if self.camara_subscription is not None:
            res = self.app.destroy_subscription(self.camara_subscription)
            self.camara_subscription = None

        if topic == "":
            return
            

        self.camara_subscription = self.app.create_subscription(
            CompressedImage,
            topic,
            self.camara_callback,
            1
        )
        

    def camara_callback(self, msg: CompressedImage):
        img = QImage.fromData(
                QByteArray(bytes(msg.data)),
                msg.format
        )
        self.camara_viewer.setPixmap(
            QPixmap(img)
        )

        



