# Setup

Install Python and PIP:

    apt install python3 python3-pip

Install requirements:

    pip3 install -r requirements.txt

# Usage

Load data:

    ./getdata.py --output data.json # (data.json already included)

Run analysis:

    ./metaculus-1060.py --input data.json --interval 30

