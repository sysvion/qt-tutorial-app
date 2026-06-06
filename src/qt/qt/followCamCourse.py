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
                        <h1> Creating your first package </h1>
                         
                        Ros2 project are strucured in a packages that can easaly be stored in a version control system like git or mercurial. And there is
                        a build system that build all project in the correct order. The place where you store the packages are dependend on which build system used. Here i explain
                        <code>colcon</code>. a teminal command. 
                         
                         <h3>Creating a workspace</h3>
                         A colcon workspace is just a diractory which has the following content:
                         <pre>
+--+ src/
|  +-- your_package
|  +-- vendor package
|
+--+ install/
|  + -- setup.bash
|
+-- build
|     build artifects. You can ignore what the contents of this dirac

+-- log
|
                         </pre>

                         To create a package from schrech you just need to create a src diractory where it is fine to be cluttert with the diractories above. It is also customary to
                         give the diractory where src is the "_WS" suffix simbolising that this is a colcon workspace.

                         <details>
                         <summary>
                         test
                         </summary>
                         Open the terminal.

                         type
                         </details>

                         <h3> create a package </h3>
                         A package is at minimum python or c++ source code and a manifest file that explains how to load dependacies and how to build the executable.
                         Luckaly you don't neet to write all the configuration by hand. Ros has a cli tool that creates the files for you. It only asks about which programming 
                         language you want to use. And what the package should be called.<br>
                         <br>
                         But first you neet a way to call Ros2. To do that you need to source the ros2 setup file. sourceing a script is like running the commends directly on your shell.
                         
                         <blockquote>
                         <code>
$ source /opt/ros/jazzy/setup.bash 
                         </code>
                         </blockquote>

                        You can use the <code>ros2 pkg create</code> to create the framework. You can pas the <code>--help</code> flag to see all available options. For the tutorial i will assume you have a python project with the node scafaultng that is given bu the following command(s)
                         
                        <blockquote>
                        <code>
<span style="color:gray;">practicum@practicum-ubuntu:~/tutorial_ws</span>$ cd src/ <br>
<span style="color:gray;">practicum@practicum-ubuntu:~/tutorial_ws/src</span>$ ros2 pkg create --build-type ament_python --node-name main follow_hand
                        </code>
                        </blockquote>

                        With this command you have 3 parts build files (<code>package.xml</code><code>setup.cfg</code> and <code>setup.py</code>). A diractory where automated tests can be written. And a diractory with the same name as the package.
                        Here in lives lives the sources of the program. There in is main.py. (Or what you have writen after --node-name.) Here is a entry point of your program. To run the created hallo world program you need to build it. Herefore you need to be at the root of the workspace and ros must be sourced. And run `colcon build`. When that is done. You can run your program using `ros2 run follow_hand main`
                        <blockquote>
                        <code>
 <br>
<span style="color:gray;">practicum@practicum-ubuntu:~/tutorial_ws/src</span>$ cd ..

<span style="color:gray;">practicum@practicum-ubuntu:~/tutorial_ws</span>$ colcon build --symlink-install
                        </code>
                        </blockquote>
                        """)

        
       
        layout.addWidget(browser2)
        
        package_widget.setLayout(layout)
        package_layout = QVBoxLayout()
        package_layout.addWidget(package_widget)


        publisher_previewer = QVBoxLayout()
        # browser3 = QTextBrowser()
        # browser3.setHtml
        # ("""
        #                 <h1>First ros2 node</h1>
        #                 Now that you have a method to run code in the ros2 enviroment.
        # 
        #                  """)
        # publisher.addWidget(browser3)
 
        self.topic_selector = QComboBox()

        self.topic_selector.currentTextChanged.connect(self.changeCamaraSubscription)
        
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_camara_options)
        self.timer.start(1000) #ms
        
       
        

        self.camara_viewer = QLabel()
        publisher_previewer.addWidget(self.topic_selector)
        publisher_previewer.addWidget(self.camara_viewer)


        reciever = QVBoxLayout()

        slides = [
            introduction,
            package_layout,
            publisher_previewer
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

        



