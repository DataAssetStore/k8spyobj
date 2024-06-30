

class K8sBase:

    k8s_name: str             # maps to the name field in the k8s object
    k8s_namespace: str             # maps to the name field in the k8s object

class K8sCrdBase:
    """
    extend this class for creating a CRD

    """
    pass