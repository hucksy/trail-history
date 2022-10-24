from .. import config
from oauthlib.oauth2 import BackendApplicationClient
from requests_oauthlib import OAuth2Session


# set up credentials
client = BackendApplicationClient(client_id=config.get_env_config().SENTINEL_CLIENT_ID)
oauth = OAuth2Session(client=client)

# get an authentication token
sentinel_token = oauth.fetch_token(token_url='https://services.sentinel-hub.com/oauth/token',
                          client_id=config.get_env_config().SENTINEL_CLIENT_ID,
                          client_secret=config.get_env_config().SENTINEL_CLIENT_SECRET)


# build request inputs
SENTINEL_BASE_URL = "https://services.sentinel-hub.com/api/v1/process"
sentinel_headers = {
    'Authorization': f'Bearer {sentinel_token["access_token"]}',
    'Conent-Type': 'application/json'
}

print(sentinel_headers)

# //VERSION=3\n\nlet minVal = 0.0;\nlet maxVal = 0.4;\n\nlet viz = new HighlightCompressVisualizer(minVal, maxVal);\n\nfunction evaluatePixel(samples) {\n    let val = [samples.B08, samples.B04, samples.B03];\n    val = viz.processList(val);\n    val.push(samples.dataMask);\n    return val;\n}\n\nfunction setup() {\n  return {\n    input: [{\n      bands: [\n        \"B03\",\n        \"B04\",\n        \"B08\",\n        \"dataMask\"\n      ]\n    }],\n    output: {\n      bands: 4\n    }\n  }\n}"
evalscript = """
VERSION=3
let minVal = 0.0;
let maxVal = 0.4;
let viz = new HighlightCompressVisualizer(minVal, maxVal);
function evaluatePixel(samples) {
    let val = [samples.B08, samples.B04, samples.B03];
        val = viz.processList(val);
            val.push(samples.dataMask);
                return val;
                }
                
                function setup() {
                  return {
                      input: [{bands: ["B03", "B04", "B08", "dataMask"]}],
                      output: {bands: 4}
                      }
}

function updateOutputMetadata(scenes, inputMetadata, outputMetadata) {
    outputMetadata.userData = { "scenes":  scenes.orbits }
}
"""

sentinel_request_body = {
  "input": {
    "bounds": {
      "bbox": [
        -105.38189,
        40.104008,
        -105.318706,
        40.13948
      ]
    },
    "data": [
      {
        "dataFilter": {
          "timeRange": {
            "from": "2017-10-18T02:55:36.067504+00:00",  #"2017-09-19T00:00:00Z",
            "to": "2017-10-20T02:55:36.067504+00:00"  #"2017-12-19T23:59:59Z"
          }
        },
        "type": "sentinel-2-l1c"
      }
    ]
  },
  "output": {
    "width": 976.8203188457022,
    "height": 716.9700625464429,
    "responses": [
      {
        "identifier": "default",
        "format": {
          "type": "image/jpeg"
        }
      }
    ]
  },
  "evalscript": evalscript
}
