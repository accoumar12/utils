#!/bin/bash

SHARE="//192.168.0.51/datasets"
USER="maccou"
PASSWORD="Nautilus12@"
REMOTE_PATH="3D/stp"
LOCAL_PATH="./downloaded_files"

mkdir -p "$LOCAL_PATH"

# Explicitly define the list of directories
DIR_LIST=("Airbus" "Renault" "Mecachrome" "Renault_parts")

# Function to retrieve files from a directory
retrieve_files() {
	  local dir=$1
	    echo "Retrieving files from $dir..."

	      smbclient "$SHARE" -U "$USER%$PASSWORD" -c "cd $REMOTE_PATH/$dir; lcd $LOCAL_PATH/$dir; prompt; mget *"
      }

      # Create local directories for each remote directory
      for dir in "${DIR_LIST[@]}"; do
	        mkdir -p "$LOCAL_PATH/$dir"
	done

	# Retrieve files from each directory
	for dir in "${DIR_LIST[@]}"; do
		  retrieve_files "$dir"
	  done

	  echo "File retrieval complete."
	  
