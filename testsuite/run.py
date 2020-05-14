from rdflib import Graph
from pyshacl import validate

# concatenate all Shape files into a single file
sg = Graph()
sg.parse("../shapes/profile.shape.ttl", format="turtle")
sg.parse("../shapes/resourcedescriptor.shape.ttl", format="turtle")

# list the implementations for testing
IMPLEMENTATIONS = [
    {
        "id": "",
        "name": "",
        "description": "",
        "implementers": "",
        "location_online": ""
    }
]

# for each implementation, validate it against the Shapes
for impl in IMPLEMENTATIONS:
    r = validate(
        data_graph,
        shacl_graph=sg,
        inference='rdfs',
        abort_on_error=False,
        meta_shacl=True,
        debug=False
    )
    conforms, results_graph, results_text = r
