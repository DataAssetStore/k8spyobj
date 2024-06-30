from k8spyobj import *

class Address:
  street: str
  city: str

class Customer: 
  first: str
  last: str

  address: Address

if __name__ == '__main__':

  # this should load with the default k8s connection configuration
  with k8spyobj.connect_default_cluster() as kconn:
    
    with kconn.new_session() as ksess:
      for i in [Address,Customer]:
        # this ensures that the cluster has a CRD for the class, and creates on if not
        crd = ksess.ensure_crd(i)                                      
        
        for index in range(10):                       # generate 10 fake objects for each class
          o = i()        

          # create obj manifests for this object

          # k[crd] should present the objects in the cluster as a dict that is keyed on k8s object type
          ksess[crd].append(o)                            # add this object to the set of objects in the clusters

    ksess.commit()       # commit the underlying transaction