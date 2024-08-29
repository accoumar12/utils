#!/bin/bash

# Variables
SHARE="//192.168.0.51/datasets"
USER="maccou"
PASSWORD="Nautilus12@"

# Connect to the share and download files
smbclient $SHARE -U $USER%$PASSWORD <<EOF
cd 3D/stp/Renault  
prompt
mget $(cat files_to_download.txt)
quit
EOF

