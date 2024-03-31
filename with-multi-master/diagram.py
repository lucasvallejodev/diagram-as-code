from diagrams import Cluster, Diagram
from diagrams.aws.compute import ECS
from diagrams.aws.database import RDS
from diagrams.aws.network import ELB
from diagrams.programming.language import Javascript

with Diagram("", show=False):
    with Cluster("Front-end"):
      web_app = Javascript("Web App")

    with Cluster("Back-end"):
      with Cluster("Server"):
        load_balancer = ELB("Load Balancer")
        instances = [ECS("Instance 1"),
                     ECS("Instance 2"),
                     ECS("Instance 3")]
      
      with Cluster("Database Cluster", direction="TB"):
        db_node_1 = RDS("Node 1")
        db_node_2 = RDS("Node 2")
        
    # connections
    web_app >> load_balancer >> instances >> db_node_1
    db_node_1 - db_node_2

