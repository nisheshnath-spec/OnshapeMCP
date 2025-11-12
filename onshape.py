"""
FastMCP Echo Server
"""

from fastmcp import FastMCP
from util import *
import json
from typing import Literal

# Create server
mcp = FastMCP("Echo Server")


get_endpoint_template = [
    "/", 
    "/{did}", 
    "/{did}/acl", 
    "/{did}/permissionset",
    "/{did}/w/{wid}/mergePreview",
    "/d/{did}/{wm}/{wmid}/documenthistory",
    "/d/{did}/{wv}/{wvid}/currentmicroversion",
    "/d/{did}/{wv}/{wvid}/insertables",
    "/d/{did}/{wvm}/{wvmid}/contents",
    "/d/{did}/{wvm}/{wvmid}/elements",
    "/d/{did}/{wvm}/{wvmid}/unitinfo",
    "/d/{did}/externaldata/{fid}",
    "/d/{did}/versions",
    "/d/{did}/versions/{vid}",
    "/d/{did}/workspaces",
]

@mcp.tool(
    name="get_document_tool",
    description="""This tool is used for any type of GET requests to Onshape /documents.
    If the request requires an ID, use the / endpoint to retrieve it.
    did refers to the given document ID, replace it with that. If ever you are asked to input prefixes, like did, 
    wid, wm, wmid, wv, wvm, or fid in brackets make sure you replace it with the actual value of the id
    and not pass in the endpoint containing one of the prefixes. This is the format for endpoints. 
    "/", 
    "/d/{did}",
    "/{did}/acl", 
    "/{did}/permissionset",
    "/{did}/w/{wid}/mergePreview",
    "/d/{did}/{wm}/{wmid}/documenthistory",
    "/d/{did}/{wv}/{wvid}/currentmicroversion",
    "/d/{did}/{wv}/{wvid}/insertables",
    "/d/{did}/{wvm}/{wvmid}/contents",
    "/d/{did}/{wvm}/{wvmid}/elements",
    "/d/{did}/{wvm}/{wvmid}/unitinfo",
    "/d/{did}/externaldata/{fid}",
    "/d/{did}/versions",
    "/d/{did}/versions/{vid}",
    "/d/{did}/workspaces" """ 
    )
def get_document_tool(api_endpoint) -> str:
    result = document_GET(api_endpoint)
    
    if result is None:
        return json.dumps({"error": "Invalid HTTP request type"}, indent=2)
    
    try:
        return json.dumps(result.json(), indent=2)
    except Exception:
        return result.text

AllowedPostDocumentEndpoints = [
    "/",
    "/{did}",
    "/{did}/acl/anonymousAccess",
    "/{did}/acl/public",
    "/{did}/share",
    "/{did}/shareWithSupport",
    "/{did}/w/{wid}/restore/{vm}/{vmid}",
    "/{did}/workspaces/{wid}/copy",
    "/{did}/workspaces/{wid}/merge",
    "/d/{did}/{wv}/{wvid}/e/{eid}/export",
    "/d/{did}/versions",
    "/d/{did}/w/{wid}/e/{eid}/latestdocumentreferences",
    "/d/{did}/w/{wid}/moveelement",
    "/d/{did}/w/{wid}/revertunchangedtorevisions",
    "/d/{did}/w/{wid}/syncAppElements",
    "/d/{did}/workspaces",
    "/search",

]

@mcp.tool(
    name="post_document_tool",
    description="""Identify the correct endpoint from the following. Do not add anything else to the endpoint, as the API 
    call will not function properly. If the request requires an ID, use the get_document_tool to retrieve it.
    did refers to the given document ID, replace it with that. To restore the version, get the workspace ID and the versions of the selected
    document ID. Make sure to acknowledge if the endpoint contains /d/. Allowed endpoints are (where values in braces can be replaced).
    Make sure that the payload HAS A VALUE and that is in a valid JSON string format.
    This is the endpoint template:
    "/",
    "/{did}",
    "/{did}/acl/anonymousAccess",
    "/{did}/acl/public",
    "/{did}/share",
    "/{did}/shareWithSupport",
    "/{did}/w/{wid}/restore/{vm}/{vmid}",
    "/{did}/workspaces/{wid}/copy",
    "/{did}/workspaces/{wid}/merge",
    "/d/{did}/{wv}/{wvid}/e/{eid}/export",
    "/d/{did}/versions",
    "/d/{did}/w/{wid}/e/{eid}/latestdocumentreferences",
    "/d/{did}/w/{wid}/moveelement",
    "/d/{did}/w/{wid}/revertunchangedtorevisions",
    "/d/{did}/w/{wid}/syncAppElements",
    "/d/{did}/workspaces",
    "/search",
    """
)
def post_document_tool(payload, api_endpoint) -> str:
    if isinstance(payload, str):
        try:
            payload = json.loads(payload)
        except json.JSONDecodeError:
            return json.dumps({"error": "Payload must be a valid JSON string for search"}, indent=2)
            
    if api_endpoint == "/search":
        if not isinstance(payload, dict):
            return json.dumps({"error": "Payload must be a valid JSON object for search"}, indent=2)

        if 'sortColumn' not in payload:
            payload['sortColumn'] = 'name'
        if 'sortOrder' not in payload:
            payload['sortOrder'] = 'asc'

    result = document_POST(api_endpoint, payload)
    
    if result is None:
        return json.dumps({"error": "Invalid HTTP request type"}, indent=2)
    
    try:
        return json.dumps(result.json(), indent=2)
    except Exception:
        return result.text


AllowedDeleteDocumentEndpoints = [
    "/{did}",                      # Delete document
    "/{did}/share/{eid}",
    "/{did}/shareWithSupport", # Unshare document with support
    "/d/{did}/workspaces/{wid}",   # Delete workspace
]

@mcp.tool(
    name="delete_document_tool",
    description="""Identify the correct endpoint from the following. If the request requires an ID, 
    use the get_document_tool to retrieve it. did refers to the given document ID, replace it with that.
    Allowed endpoints are (where values in braces can be replaced): 

    "/{did}",                      # Delete document
    "/{did}/share/{eid}",
    "/{did}/shareWithSupport", # Unshare document with support
    "/d/{did}/workspaces/{wid}", 
    """
)
def delete_document_tool(api_endpoint) -> str:
    result = document_DELETE(api_endpoint)

    if result is None:
        return json.dumps({"error": "Invalid HTTP request type"}, indent=2)
    
    try:
        return json.dumps(result.json(), indent=2)
    except Exception:
        return result.text

AllowedGetPartStudioEndpoints = [
    "/d/{did}/{wvm}/{wvmid}/e/{eid}/bodydetails",
    "/d/{did}/{wvm}/{wvmid}/e/{eid}/boundingboxes",
    "/d/{did}/{wvm}/{wvmid}/e/{eid}/compare",
    "/d/{did}/{wvm}/{wvmid}/e/{eid}/features",
    "/d/{did}/{wvm}/{wvmid}/e/{eid}/featurescriptrepresentation",
    "/d/{did}/{wvm}/{wvmid}/e/{eid}/featurespecs",
    "/d/{did}/{wvm}/{wvmid}/e/{eid}/fstable",
    "/d/{did}/{wvm}/{wvmid}/e/{eid}/gltf",
    "/d/{did}/{wvm}/{wvmid}/e/{eid}/massproperties",
    "/d/{did}/{wvm}/{wvmid}/e/{eid}/parasolid",
    "/d/{did}/{wvm}/{wvmid}/e/{eid}/shadedviews",
    "/d/{did}/{wvm}/{wvmid}/e/{eid}/stl",
    "/d/{did}/{wvm}/{wvmid}/e/{eid}/tessellatededges",
    "/d/{did}/{wvm}/{wvmid}/e/{eid}/tessellatedfaces",
    "/d/{did}/e/{eid}/namedViews"
]

@mcp.tool(
    name="get_partstudio_tool",
    description="""GET methods to get the features of a Part Studio element. Use a template of the following
    endpoints and wherever you see a prefix such as, did, wvm, wvmid, eid, etc. be sure to get the actual id
    number that corresponds to the prefix. If you do not know any of the ids, call the get_document_tool 
    and get the necessary ids for the specified document. The endpoints already begin with /partstudios,
    so here are the endpoints to choose from:
    "/d/{did}/{wvm}/{wvmid}/e/{eid}/bodydetails",
    "/d/{did}/{wvm}/{wvmid}/e/{eid}/boundingboxes",
    "/d/{did}/{wvm}/{wvmid}/e/{eid}/features",
    "/d/{did}/{wvm}/{wvmid}/e/{eid}/featurescriptrepresentation",
    "/d/{did}/{wvm}/{wvmid}/e/{eid}/fstable",
    "/d/{did}/{wvm}/{wvmid}/e/{eid}/gltf",
    "/d/{did}/{wvm}/{wvmid}/e/{eid}/massproperties",
    "/d/{did}/{wvm}/{wvmid}/e/{eid}/parasolid",
    "/d/{did}/{wvm}/{wvmid}/e/{eid}/shadedviews",
    "/d/{did}/{wvm}/{wvmid}/e/{eid}/stl",
    "/d/{did}/{wvm}/{wvmid}/e/{eid}/tessellatededges",
    "/d/{did}/{wvm}/{wvmid}/e/{eid}/tessellatedfaces",
    "/d/{did}/e/{eid}/namedViews"
    """
)
def get_partstudio_tool(api_endpoint) -> str:
    result = partstudio_GET(api_endpoint)

    if result is None:
        return json.dumps({"error": "Invalid HTTP request type"}, indent=2)
    
    try:
        return json.dumps(result.json(), indent=2)
    except Exception:
        return result.text


@mcp.tool(
    name="circle_sketch",
    description="""This is the POST to ADD features to a Part Studio element (cylinders). Use a template of the following
    endpoints and wherever you see a prefix such as, did, wvm, wvmid, eid, etc. be sure to get the actual id
    number that corresponds to the prefix. If you do not know any of the ids, call the get_document_tool 
    and get the necessary ids for the specified document. Allowed endpoints are (where values in braces can be replaced).
    Here are the possible endpoints:
    /d/{did}/{wvm}/{wvmid}/e/{eid}/features
    
    To create 3D objects, first create a sketch, then extrude that sketch.
    
    IMPORTANT: GEOMETRY RULES — BUILD ON EXISTING FACES (Do NOT use global planes)

    • Do NOT sketch on Top/Front/Right for stacked geometry.
    • Do NOT use:
        query=qCreatedBy(makeId(<extrudeId>), EntityType.FACE)
    (Ambiguous: can pick the wrong cap.)

    Instead, set the sketch plane to the **top cap face** of the previous extrude using qCapEntity:

    1) Call get_partstudio_tool to read /features and get the previous extrude’s featureId (e.g., <PREV_EXTRUDE_FEATURE_ID>).
    2) Use that exact id in the sketchPlane query:
        "query = qCapEntity(id + '<PREV_EXTRUDE_FEATURE_ID>', CapType.END);"
    3) Create the new circle/geometry on that face.


    Minimal sketch template (insert the real extrude id):

    {
    "btType": "BTFeatureDefinitionCall-1406",
    "feature": {
        "btType": "BTMSketch-151",
        "featureType": "newSketch",
        "name": "<Next Sketch>",
        "parameters": [
        {
            "btType": "BTMParameterQueryList-148",
            "parameterId": "sketchPlane",
            "queries": [
            {
                "btType": "BTMIndividualQuery-138",
                "queryString": "query = qCapEntity(id + '<PREV_EXTRUDE_FEATURE_ID>', CapType.END);"
            }
            ]
        }
        ],
        "entities": [ /* circle/arc/etc. */ ],
        "constraints": [ /* optional CONCENTRIC to prior edge/center */ ]
    }
    }

    NOTE: All sketch definitions MUST be wrapped in the "BTFeatureDefinitionCall-1406" object.

    IMPORTANT — PLANE CHANGES X/Y DIRECTION

    In Onshape sketches, the plane you choose (`Front`, `Right`, or `Top`) determines the meaning and
    orientation of the `xCenter` and `yCenter` coordinates.

        • Front plane:  x = left/right,   y = up/down
        • Right plane:  x = forward/back, y = up/down
        • Top plane:    x = left/right,   y = forward/back

    Because of this, when generating geometry (circles, arcs, etc.), you must never assume global
    axes— all xCenter, yCenter, xDir, yDir, and radian start/end parameters must follow the plane’s
    local coordinate system.

     Always confirm what plane the sketch is on
     Never reuse coordinates from another plane
     Never guess X/Y direction without plane context
    
    Example payloads include:
    For creating a circle sketch:
    {
  "btType": "BTFeatureDefinitionCall-1406",
  "feature" : {
    "btType": "BTMSketch-151", 
    "featureType": "newSketch", 
    "name": "Sketch 1", 
    "parameters": [
      {
        "btType": "BTMParameterQueryList-148",
        "queries": [
          {
            "btType": "BTMIndividualQuery-138",
            "queryString": "query=qCreatedBy(makeId(\"Front\"), EntityType.FACE);"
          }
        ],
        "parameterId": "sketchPlane" 
      }
    ],
        "entities": [
        {
            "btType": "BTMSketchCurve-4",
            "entityId": "circle-entity",
            "geometry": {
            "btType": "BTCurveGeometryCircle-115",
            "radius": 0.025,  
            "xCenter": 0.05,
            "yCenter": 0.05,  
            "xDir": 1,
            "yDir": 0, 
            "clockwise": false 
            },
            "centerId": "circle-entity.center"
        }  
        ],
        "constraints": [      
        ]
    }
    }

    """
)
def circle_sketch(api_endpoint, payload) -> str:
    if isinstance(payload, str):
        try:
            payload = json.loads(payload)
        except json.JSONDecodeError:
            return json.dumps({"error": "Payload must be a valid JSON string for search"}, indent=2)

    result = partstudio_POST(api_endpoint, payload)

    if result is None:
        return json.dumps({"error": "Invalid HTTP request type"}, indent=2)
    
    try:
        return json.dumps(result.json(), indent=2)
    except Exception:
        return result.text



@mcp.tool(
    name="create_3pt_arc_and_2pt_line",
    description="""

    Purpose:
    This tool creates sketch geometry (either a **2-point line** or a **3-point arc**) inside a Part Studio.

    Default behavior
    - When called with minimal parameters, the tool:
    - **creates a new sketch**, and
    - adds **one** line or arc entity.
    This default is intended to mimic the interactive user experience in Onshape (click → place one line/arc).

    Misconception (NOT ACTUALLY A LIMITATION)
    While the default payload shows only one curve in `"entities"`, the API does **not** restrict you to a single line/arc.

    You can:
    ✔ Add **multiple** lines/arcs to the same sketch  
    ✔ Append geometry to an **existing** sketch  
    ✔ Build **closed profiles** (squares, polygons, etc.)

    Full capability (not obvious from default docs)
    When using the tool via the API, you can control:
    - **Which sketch you add to** (`featureId`)
    - **How many geometry entities you include** (`entities` array can hold >1)
    - **Line or arc placement** using actual coordinates
    Make sure that the payload HAS A VALUE and that is in a valid JSON string format.

    PLANE RULES (critical!)
    Onshape sketches have their OWN local XY system depending on the sketch plane:
        • Front plane:  x = left/right,   y = up/down
        • Right plane:  x = forward/back, y = up/down
        • Top plane:    x = left/right,   y = forward/back
    NEVER assume global XYZ coordinates.  
    All arc coordinates MUST be relative to the chosen plane.

    This tool creates a new sketch and adds a 3-point arc using Onshape's arc geometry
    (`BTMSketchCurveSegment-155 + BTCurveGeometryCircle-115`). Arc geometry in the
    API is ALWAYS expressed as a circle arc defined by:
        • radius
        • center point (xCenter, yCenter)
        • startParam (radians)
        • endParam   (radians)
    ────────────────────────────────────────────────────────
    get information about features
    using the correct tool and calculate and interpret the inputs based off of the user's prompt.

    Plane:              <Front | Right | Top>
    SketchName:         <string>
    EntityId:           <string (unique arc id)>
    radius:             <float, meters>
    xCenter:            <float, meters>
    yCenter:            <float, meters>
    startParam:         <float radians>  (π allowed, ex: 1.5*pi)
    endParam:           <float radians>
    

    ────────────────────────────────────────────────────────
    ARC GEOMETRY RULES
    1. You must supply a valid arc definition via center, radius, startParam, endParam.
    Do NOT guess values.
    2. This tool does NOT compute or infer points.  
    (If user wants “3-point arc between A, B, C”, caller must compute center/radius/angles.)
    3. Angle direction:
        startParam → endParam
    defines the visible arc.
    ────────────────────────────────────────────────────────
    OUTPUT (this is an example template output for 3-point arc if user asks for arc)
    {
    "btType": "BTFeatureDefinitionCall-1406",
    "feature": {
        "btType": "BTMSketch-151",
        "featureType": "newSketch",
        "name": "<SketchName>",
        "parameters": [
        {
            "btType": "BTMParameterQueryList-148",
            "parameterId": "sketchPlane",
            "queries": [
            {
                "btType": "BTMIndividualQuery-138",
                "queryString":
                "query=qCreatedBy(makeId('<Plane>'), EntityType.FACE);"
            }
            ]
        }
        ],
        "entities": [
        {
            "btType": "BTMSketchCurveSegment-155",
            "entityId": "<EntityId>",
            "geometry": {
            "btType": "BTCurveGeometryCircle-115",
            "radius": <radius>,
            "xCenter": <xCenter>,
            "yCenter": <yCenter>,
            "xDir": 1.0,
            "yDir": 0.0,
            "clockwise": false
            },
            "centerId": "<EntityId>.center",
            "startParam": <startParam>,
            "endParam": <endParam>
        }
        ],
        "constraints": []
    }
    }


    This is a sample template to CREATE A NEW SKETCH with multiple lines/arcs
    {
    "btType": "BTFeatureDefinitionCall-1406",
    "feature": {
        "btType": "BTMSketch-151",
        "featureType": "newSketch",
        "name": "MySketch",
        "parameters": [
        {
            "btType": "BTMParameterQueryList-148",
            "parameterId": "sketchPlane",
            "queries": [
            {
                "btType": "BTMIndividualQuery-138",
                "queryString": "query=qCreatedBy(makeId('Top'), EntityType.FACE);"
            }
            ]
        }
        ],
        "entities": [
        {
            "btType": "BTMSketchCurveSegment-155",
            "entityId": "line1",
            "geometry": {
            "btType": "BTCurveGeometryLine-117",
            "pntX": -0.005, "pntY": 0.0,
            "dirX": 1.0,  "dirY": 0.0
            },
            "startPointId": "line1.start",
            "endPointId": "line1.end",
            "startParam": 0.0,
            "endParam": 0.01
        },
        {
            "btType": "BTMSketchCurveSegment-155",
            "entityId": "line2",
            "geometry": {
            "btType": "BTCurveGeometryLine-117",
            "pntX": 0.005, "pntY": -0.005,
            "dirX": 0.0,  "dirY": 1.0
            },
            "startPointId": "line2.start",
            "endPointId": "line2.end",
            "startParam": 0.0,
            "endParam": 0.01
        }
        ],
        "constraints": []
    }
    }

    This is a template to Append geometry to an existing sketch template:
    {
    "btType": "BTFeatureDefinitionCall-1406",
    "feature": {
        "btType": "BTMSketch-151",
        "featureType": "editSketch",
        "featureId": "INSERT_EXISTING_SKETCH_ID",
        "entities": [
        {
            "btType": "BTMSketchCurveSegment-155",
            "entityId": "newLine",
            "geometry": {
            "btType": "BTCurveGeometryLine-117",
            "pntX": 0.005, "pntY": 0.005,
            "dirX": -1.0, "dirY": 0.0
            },
            "startPointId": "newLine.start",
            "endPointId": "newLine.end",
            "startParam": 0.0,
            "endParam": 0.01
        }
        ]
    }
    }
"""
)
def create_3pt_arc_and_2pt_line(api_endpoint, payload) -> str:
    if isinstance(payload, str):
        try:
            payload = json.loads(payload)
        except json.JSONDecodeError:
            return json.dumps({"error": "Payload must be a valid JSON string for search"}, indent=2)

    result = partstudio_POST(api_endpoint, payload)

    if result is None:
        return json.dumps({"error": "Invalid HTTP request type"}, indent=2)
    
    try:
        return json.dumps(result.json(), indent=2)
    except Exception:
        return result.text
    


@mcp.tool(
    name = "extrusion_tool",
    description = """
    This tool is used to extrude any sketch. Make sure that there is a payload.

    PLANE RULES (critical!)
    Onshape sketches have their OWN local XY system depending on the sketch plane:
        • Front plane:  x = left/right,   y = up/down
        • Right plane:  x = forward/back, y = up/down
        • Top plane:    x = left/right,   y = forward/back
    NEVER assume global XYZ coordinates.  
    All arc coordinates MUST be relative to the chosen plane.

    SOLIDS (adding material):
    • operationType = "NEW" or "ADD"
    • Extrude BLIND **away from the face** using a **positive depth**.

    HOLES / CUTS (removing material):
    • operationType = "REMOVE"
    • Extrude BLIND must go INTO the solid — NEVER rely on the default direction.
    Onshape defaults to extruding along the sketch face's normal direction,
    which may be OUTWARD.
    • You MUST explicitly set the direction by making the initial value you use NEGATIVE. The direction
    must be negative if you want to create a hole starting from the top face of an object.
    • Do NOT assume the UI arrow default is correct.
    • If the preview does not intersect the solid, the cut will create no geometry.

    
    
    Extruding a sketch (in this case, into a cylinder):
    {
          "btType": "BTFeatureDefinitionCall-1406",
          "feature": {
            "btType": "BTMFeature-134",
            "featureType": "extrude",
            "name": "Extrude 1",
            "parameters": [
              {
                "btType": "BTMParameterEnum-145",
                "value": "SOLID",
                "enumName": "ExtendedToolBodyType",
                "parameterId": "bodyType"
              },
              {
                "btType": "BTMParameterEnum-145",
                "value": "NEW",
                "enumName": "NewBodyOperationType",
                "parameterId": "operationType"
              },
              {
                "btType": "BTMParameterQueryList-148",
                "queries": [
                  {
                    "btType": "BTMIndividualSketchRegionQuery-140",
                    "featureId": "{featureId}"
                  }
                ],
                "parameterId": "entities"
              },
              {
                "btType": "BTMParameterEnum-145",
                "value": "BLIND",
                "enumName": "BoundingType",
                "parameterId": "endBound"
              },
              {
                "btType": "BTMParameterQuantity-147",
                "expression": "1 in",
                "parameterId": "depth"
              }
                ],
            "returnAfterSubfeatures": false,
            "suppressed": false
          }
        }

    For any extrusion extrusion symetrically has these properties:
    "endBound": "BLIND"
    "depth": "4 mm"
    "hasSecondDirection": true
    "secondDirectionBound": "BLIND"
    "secondDirectionDepth": "4 mm"

    Extrude template (upward from that face):
    {
    "btType": "BTFeatureDefinitionCall-1406",
    "feature": {
        "btType": "BTMFeature-134",
        "featureType": "extrude",
        "name": "<Next Extrude>",
        "parameters": [
        { "btType": "BTMParameterEnum-145", "parameterId": "bodyType", "enumName": "ExtendedToolBodyType", "value": "SOLID" },
        { "btType": "BTMParameterEnum-145", "parameterId": "operationType", "enumName": "NewBodyOperationType", "value": "NEW" },
        { "btType": "BTMParameterQueryList-148", "parameterId": "entities", "queries": [ { "btType": "BTMIndividualSketchRegionQuery-140", "featureId": "<Next Sketch>" } ] },
        { "btType": "BTMParameterEnum-145", "parameterId": "endBound", "enumName": "BoundingType", "value": "BLIND" },
        { "btType": "BTMParameterQuantity-147", "parameterId": "depth", "expression": "<thickness>" }
        ]
    }
    }

    Extrude - Hole template:

    {
    "btType": "BTFeatureDefinitionCall-1406",
    "feature": {
        "btType": "BTMFeature-134",
        "featureType": "extrude",
        "name": "Cup Inner Cut",
        "parameters": [
        {
            "btType": "BTMParameterEnum-145",
            "enumName": "ExtendedToolBodyType",
            "parameterId": "bodyType",
            "value": "SOLID"
        },
        {
            "btType": "BTMParameterEnum-145",
            "enumName": "NewBodyOperationType",
            "parameterId": "operationType",
            "value": "REMOVE"
        },
        {
            "btType": "BTMParameterQueryList-148",
            "parameterId": "entities",
            "queries": [
            {
                "btType": "BTMIndividualSketchRegionQuery-140",
                "featureId": "FNrtjtac3VTg1sI_1"
            }
            ]
        },
        {
            "btType": "BTMParameterEnum-145",
            "enumName": "BoundingType",
            "parameterId": "endBound",
            "value": "BLIND"
        },
        {
            "btType": "BTMParameterQuantity-147",
            "parameterId": "depth",
            "expression": "-48 mm"
        }
        ]
    }
    }
    """
)
def extrusion_tool(api_endpoint, payload) -> str:
    if isinstance(payload, str):
        try:
            payload = json.loads(payload)
        except json.JSONDecodeError:
            return json.dumps({"error": "Payload must be a valid JSON string for search"}, indent=2)

    result = partstudio_POST(api_endpoint, payload)

    if result is None:
        return json.dumps({"error": "Invalid HTTP request type"}, indent=2)
    
    try:
        return json.dumps(result.json(), indent=2)
    except Exception:
        return result.text
    
@mcp.tool(
  name="delete_feature_tool",
  description="""This tool deletes a specific feature from a Part Studio element.
  Make sure to provide the correct endpoint in the format:
  /d/{did}/w/{wid}/e/{eid}/features/featureid/{fid}
  
  where:
    - did: Document ID
    - wid: Workspace ID
    - eid: Element ID
    - fid: Feature ID
  """
)
def delete_feature_tool(api_endpoint) -> str:
    result = document_DELETE(api_endpoint)

    if result is None:
        return json.dumps({"error": "Invalid HTTP request type"}, indent=2)
    
    try:
        return json.dumps(result.json(), indent=2)
    except Exception:
        return result.text

@mcp.tool(
  name="update_feature_tool",
  description="""This tool updates a specific feature in a Part Studio element.
  Make sure to provide the correct endpoint in the format:

  /d/{did}/w/{wid}/e/{eid}/features/featureid/{fid}

  where:
    - did: Document ID
    - wid: Workspace ID
    - eid: Element ID
    - fid: Feature ID
  Also, ensure that the payload is a valid JSON string representing the feature update.
  """
)
def update_feature_tool(api_endpoint, payload) -> str:
    if isinstance(payload, str):
        try:
            payload = json.loads(payload)
        except json.JSONDecodeError:
            return json.dumps({"error": "Payload must be a valid JSON string for feature update"}, indent=2)

    result = document_POST(api_endpoint, payload)

    if result is None:
        return json.dumps({"error": "Invalid HTTP request type"}, indent=2)
    
    try:
        return json.dumps(result.json(), indent=2)
    except Exception:
        return result.textg