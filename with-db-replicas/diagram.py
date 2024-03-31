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
        instances = [ECS("Instance 3"),
                     ECS("Instance 2"),
                     ECS("Instance 1")]
        
      
      with Cluster("Database Cluster"):
        db_master = RDS("Master")
        db_replicas = [RDS("Replica 3"),
                    RDS("Replica 2"),
                    RDS("Replica 1")]
        
    # connections
    web_app >> load_balancer >> instances >> db_master
    db_master - db_replicas

