import requests
from dotenv import load_dotenv
import json
import os
import math

load_dotenv()

BASE_URL = "https://cad.onshape.com/api/v10"
ACCESS_KEY = os.getenv("ONSHAPE_ACCESS_KEY")
SECRET_KEY = os.getenv("ONSHAPE_SECRET_KEY")

payload={
  "btType": "BTFeatureDefinitionCall-1406",
  "feature": {
    "btType": "BTMSketch-151",
    "featureType": "newSketch",
    "name": "Hexagon 10mm (Front)",
    "parameters": [
      {
        "btType": "BTMParameterQueryList-148",
        "parameterId": "sketchPlane",
        "queries": [
          {
            "btType": "BTMIndividualQuery-138",
            "queryString": "query=qCreatedBy(makeId('Front'), EntityType.FACE);"
          }
        ]
      }
    ],
    "entities": [
      {
        "btType": "BTMSketchCurveSegment-155",
        "entityId": "hex_line_1",
        "geometry": {
          "btType": "BTCurveGeometryLine-117",
          "pntX": 0.005,
          "pntY": 0.008660254037844387,
          "dirX": -1.0,
          "dirY": 0.0
        },
        "startPointId": "hex_line_1.start",
        "endPointId": "hex_line_1.end",
        "startParam": 0.0,
        "endParam": 0.01
      },
      {
        "btType": "BTMSketchCurveSegment-155",
        "entityId": "hex_line_2",
        "geometry": {
          "btType": "BTCurveGeometryLine-117",
          "pntX": -0.005,
          "pntY": 0.008660254037844387,
          "dirX": -0.5,
          "dirY": -0.8660254037844386
        },
        "startPointId": "hex_line_2.start",
        "endPointId": "hex_line_2.end",
        "startParam": 0.0,
        "endParam": 0.01
      },
      {
        "btType": "BTMSketchCurveSegment-155",
        "entityId": "hex_line_3",
        "geometry": {
          "btType": "BTCurveGeometryLine-117",
          "pntX": -0.01,
          "pntY": 0.0,
          "dirX": 0.5,
          "dirY": -0.8660254037844386
        },
        "startPointId": "hex_line_3.start",
        "endPointId": "hex_line_3.end",
        "startParam": 0.0,
        "endParam": 0.01
      },
      {
        "btType": "BTMSketchCurveSegment-155",
        "entityId": "hex_line_4",
        "geometry": {
          "btType": "BTCurveGeometryLine-117",
          "pntX": -0.005,
          "pntY": -0.008660254037844387,
          "dirX": 1.0,
          "dirY": 0.0
        },
        "startPointId": "hex_line_4.start",
        "endPointId": "hex_line_4.end",
        "startParam": 0.0,
        "endParam": 0.01
      },
      {
        "btType": "BTMSketchCurveSegment-155",
        "entityId": "hex_line_5",
        "geometry": {
          "btType": "BTCurveGeometryLine-117",
          "pntX": 0.005,
          "pntY": -0.008660254037844387,
          "dirX": 0.5,
          "dirY": 0.8660254037844386
        },
        "startPointId": "hex_line_5.start",
        "endPointId": "hex_line_5.end",
        "startParam": 0.0,
        "endParam": 0.01
      },
      {
        "btType": "BTMSketchCurveSegment-155",
        "entityId": "hex_line_6",
        "geometry": {
          "btType": "BTCurveGeometryLine-117",
          "pntX": 0.01,
          "pntY": 0.0,
          "dirX": -0.5,
          "dirY": 0.8660254037844386
        },
        "startPointId": "hex_line_6.start",
        "endPointId": "hex_line_6.end",
        "startParam": 0.0,
        "endParam": 0.01
      }
    ],
    "constraints": []
  }
}






try:
    response = requests.post(
        BASE_URL + "/partstudios/d/7f592dc620c4d28fa1999e58/w/7a28b2daedf5c7675a7eb667/e/7c6c60fbc23e129c57019f6a/features",
        json=payload,
        auth=(ACCESS_KEY, SECRET_KEY),
        headers={'Accept': 'application/json;charset=UTF-8;qs=0.09',
            'Content-Type': 'application/json'}
    )
except requests.exceptions.RequestException as e:
    print(e)

print(response.json())