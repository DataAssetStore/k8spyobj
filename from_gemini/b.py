from typing import List, Union
import kopf
import kubernetes

@kopf.on.field('your-crd-group', 'your-crd-version', 'your-crd-plural', field='spec.tokens')
def tokens_handler(tokens: Union[List[str], List[List[str]]], logger, **kwargs):
    """
    Handles lists of tokens, potentially nested, spawns pods for "SPAWN" tokens.
    """
    def log_tokens_recursively(token_list):
        """Recursively logs tokens and spawns a Pod when "SPAWN" is found."""
        for token in token_list:
            if isinstance(token, list):
                log_tokens_recursively(token)
            else:
                logger.info(f"Token found: {token}")
                if token == "SPAWN":
                    spawn_pod(logger, **kwargs)

    log_tokens_recursively(tokens)

def spawn_pod(logger, body, **_):
    """
    Creates and deploys a new Kubernetes Pod owned by the CRD.
    """
    api = kubernetes.client.CoreV1Api()

    pod_manifest = {
        "apiVersion": "v1",
        "kind": "Pod",
        "metadata": {
            "generateName": f"{body['metadata']['name']}-",
            "ownerReferences": [
                {
                    "apiVersion": body['apiVersion'],
                    "kind": body['kind'],
                    "name": body['metadata']['name'],
                    "uid": body['metadata']['uid'],
                }
            ],
        },
        "spec": {
            "containers": [
                {
                    "name": "spawned-container",
                    "image": "busybox",  # Replace with your desired image
                    "command": ["echo", "Hello from spawned Pod!"],
                }
            ]
        },
    }

    try:
        api.create_namespaced_pod(namespace="default", body=pod_manifest)
        logger.info("Pod spawned successfully as a child of the CRD!")
    except kubernetes.client.rest.ApiException as e:
        logger.error(f"Failed to spawn Pod: {e}")

@kopf.on.startup()
def configure(settings: kopf.OperatorSettings, **_):
    """
    Sets up the operator settings and loads the CRD.
    """
    settings.persistence.progress_storage = kopf.AnnotationsProgressStorage(prefix='kopf.zalando.org')
    settings.persistence.finalizer = 'kopf.zalando.org/finalizer'

if __name__ == "__main__":
    kopf.run(standalone=True)
