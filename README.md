# goal 

- to provide declarative options for creating CRDs and k8s objects, so that complex k8s object structures can be built easier than hammer out yaml files-
  - such as defining normal python classes and having them be able to generate CRDs
    - and having normal object instances be able to generate k8s objs
  - and having the same capacity to integrate with SQLmodel (and therefore sqlalchemy and pydantic) such that as well as being able to drive k8s CRD class and k8s object creation, you can have regular ORM persitence
- 
- to integrate with kopf so that k8s object event handlers can be stood up via kopf in a natural python class oriented way
