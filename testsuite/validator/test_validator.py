from pathlib import Path
from rdflib import Graph
from pyshacl import validate

validator_graph = Graph().parse(Path(__file__).parent.parent.resolve().parent / "prof/rdf/validator.ttl")

for f in sorted(Path(Path(__file__).parent / "data").glob("*.ttl")):

    v = validate(str(f), shacl_graph=validator_graph)
    if "invalid" in str(f.name):
        assert not v[0], f"File {f.name} is valid but should be invalid"
    else:
        assert v[0], f"File {f.name} is invalid but should be valid: {v[2]}"
