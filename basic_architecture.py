from diagrams import Cluster, Diagram
from diagrams.aws.general import User
from diagrams.custom import Custom
from diagrams.programming.language import Javascript

with Diagram("", show=False):
    with Cluster("User"):
      user = User("User")
      web_browser = Custom("Web Browser", "./res/browser.png")

    with Cluster("Application"):
      with Cluster("Front-end"):
        web_app = Javascript("Web App")

      with Cluster("Back-end"):
        server = Custom("Server", "./res/server.png")
        db = Custom("Database", "./res/database.png")

    # connections
    user >> web_browser >> web_app >> server >> db
    db >> server
