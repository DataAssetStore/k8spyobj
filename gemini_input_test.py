import pytest
from your_module import CRDBase, crd_spec  # Replace 'your_module' with the name of your module


def test_crd_class_creation():
    """Test that the MyCRD class is created dynamically and correctly."""
    MyCRD = CRDBase.__class__("MyCRD", (CRDBase,), {}, **crd_spec)

    # Basic assertions to check class attributes
    assert hasattr(MyCRD, "spec")
    assert hasattr(MyCRD, "model")
    assert issubclass(MyCRD.model, SQLModel)

    # Check if spec fields are created as expected
    spec_model = MyCRD.SpecModel  # Get the Pydantic model for spec
    assert hasattr(spec_model, "replicas")
    assert hasattr(spec_model, "image")
    # ... Add more assertions for other spec fields
    
def test_crd_object_creation():
    """Test creating a CRD object and validating its fields."""
    MyCRD = CRDBase.__class__("MyCRD", (CRDBase,), {}, **crd_spec)
    
    # Example CRD data
    crd_data = {
        "apiVersion": "my.api/v1",  # Replace with your API group and version
        "kind": "MyCRD",
        "metadata": {"name": "my-crd-instance"},
        "spec": {
            "replicas": 3,
            "image": "my-custom-image",
            "resources": {
                "requests": {"cpu": "100m", "memory": "200Mi"},
                "limits": {"cpu": "200m", "memory": "400Mi"}
            },
            "containers": [
                {
                    "name": "my-container",
                    "image": "my-custom-image:latest",
                    "command": ["python", "app.py"]
                }
            ]
        }
    }

    # Create the CRD object
    my_crd = MyCRD(**crd_data)

    # Assertions for the created CRD object
    assert my_crd.apiVersion == "my.api/v1"
    assert my_crd.kind == "MyCRD"
    assert my_crd.metadata.name == "my-crd-instance"
    
    # Validate spec fields using Pydantic
    spec_model = MyCRD.SpecModel(**my_crd.spec)  # Validate spec fields

    # Add more specific assertions for spec fields
    assert spec_model.replicas == 3
    assert spec_model.image == "my-custom-image"
    # ... and so on


def test_crd_serialization():
    """Test serialization and deserialization of the CRD object."""
    # Create a CRD object
    # ... (same as in test_crd_object_creation)

    # Serialize the CRD object
    serialized_crd = my_crd.model.from_orm(my_crd).dict()

    # Deserialize the serialized CRD
    deserialized_crd = MyCRD(**serialized_crd)

    # Assertions to check if serialization and deserialization work correctly
    assert deserialized_crd == my_crd

