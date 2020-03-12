## Overview
This is a test service written in Python 3; for now, it is a proof-of-concept echo server to test against the backend.

## Setup and Run
[Python 3+](https://www.python.org/downloads/) and [Flask](https://palletsprojects.com/p/flask/) need to be installed. Flask can be installed by using pip:

    pip install flask

Alternatively, if `pip` is not in your path, you can also run:

    python -m pip install flask

### Standalone
Run the file `source.py`; the service will be running at port `3000`. Note that you cannot interact with it directly; it only responds to POST requests containing a JSON file with a `name` field; cURL can be used to send POST JSON, as shown [here](https://gist.github.com/subfuzion/08c5d85437d5d4f00e58#post-applicationjson)
### NRG-Platform
TBD
## How to contribute
TBD
## Commit Message Convention
Use this [description](https://gist.github.com/mithi/33b0e9426c6ba378807304dfb5e7d566)
## Features
### To be Implemented 
- Echo the string
- Logging connections
## Code Style
PEP 8 should be followed at all times; the `pycodestyle` linter can be used to ensure code is PEP 8 compliant, and can be installed via `pip`.
## Troubleshooting
TBD
## Contact
TBD
