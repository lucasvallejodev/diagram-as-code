from diagrams import Cluster, Diagram
from diagrams.aws.compute import ECS
from diagrams.aws.network import ELB
from diagrams.custom import Custom
from diagrams.programming.language import Javascript

with Diagram("", show=False):
    with Cluster("Front-end"):
      web_app = Javascript("Web App")

    with Cluster("Back-end"):
      db = Custom("Database", "./res/database.png")
      with Cluster("Server"):
        load_balancer = ELB("Load Balancer")
        instances = [ECS("Instance 1"),
                     ECS("Instance 2"),
                     ECS("Instance 3")]

    # connections
    web_app >> load_balancer >> instances >> db

