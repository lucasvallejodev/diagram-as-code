from diagrams import Cluster, Diagram
from diagrams.aws.general import SDK
from diagrams.onprem.vcs import Git
from diagrams.custom import Custom
from diagrams.programming.language import Javascript

with Diagram("", show=False):
    with Cluster("Application"):
      server = Custom("Server", "./res/server.png")

    with Cluster("Development"):
        dev = Custom("Developer", "./res/dev.png")
        with Cluster("CI/CD"):  
          git = Git("Repository")
          rack = Custom("Automated Build", "./res/build.png")
          binaries = SDK("Binaries")
          deploy = Custom("Automated Deploy", "./res/deploy.png")
          test = Custom("Automated Test", "./res/test.png")

    dev >> git >> rack >> binaries >> deploy >> test
    deploy >> server
