"""




"""





class K8sBase(metaclass=CRDMeta):
    k8s_name: str
    k8s_namespace: str

    k8s_children_list: list[K8sBase]


class Actor(K8sBase): pass


class Plan(K8sBase): pass

class PlanNode(K8sBase): pass

class PlanEdge(K8sBase): pass

class PlanExecutor(K8sBase): pass


class Operation: pass
    
class Goal: pass

class Objective: pass

class State: pass


class Mission: 
    """



    """
    pass

class Evaluation: pass

class End: pass


class Agent: 
    """

    An agent has:

    - a set of tools
    - a specific plan
      - that runs until an End 

    """
    
    pass



class Tool: pass

class Feed(Tool): pass



class Customer(Actor): pass



class BaseContainerRun(K8sBase):

    image: str
    commnad: str
    args: list[str]

class BaseDeployment(BaseContainerRun):
    k8s_type = "deployment"

class BaseJob(BaseContainerRun):
    k8s_type = "job"

class BaseBuild(BaseJob):
    """
    this runs as a job
    
    """
    pass

class StandardIngressedDeployment(BaseDeployment):
    pass

class WebApp(StandardIngressedDeployment):
    k8s_type = "deployment"

class WebBuild(StandardBuild):
    pass

class WebPublish(StandardDeployment):
    pass
