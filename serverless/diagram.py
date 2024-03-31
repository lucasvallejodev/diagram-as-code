from diagrams import Cluster, Diagram
from diagrams.aws.compute import Lambda
from diagrams.aws.network import APIGateway
from diagrams.aws.storage import S3
from diagrams.custom import Custom
from diagrams.programming.language import Javascript

with Diagram("", show=False):
    with Cluster("Front-end"):
      web_app = Javascript("Web App")

    with Cluster("Back-end"):
      api_gateway = APIGateway("API Gateway")
      with Cluster("Serverless Functions"):
        functions = [Lambda("Function 1"),
                     Lambda("Function 2"),
                     Lambda("Function 3")]
      with Cluster("Static Files Storage"):
        bucket = S3("Storage Bucket")
      with Cluster("Database Cluster", direction="TB"):
        db_node_1 = Custom("Node 1", "./res/database.png")
        db_node_2 = Custom("Node 2", "./res/database.png")

    # connections
    web_app >> api_gateway >> functions >> db_node_1
    bucket >> api_gateway
    db_node_1 - db_node_2

