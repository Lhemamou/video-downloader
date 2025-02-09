#!/bin/bash

# Directory containing the .wav files
AUDIO_DIR="/media/leohemamou/ssd2/standup/audio/fr/"

# Check if the directory exists
if [ ! -d "$AUDIO_DIR" ]; then
    echo "Error: Directory $AUDIO_DIR does not exist."
    exit 1
fi

# Loop through each .wav file in the directory
for AUDIO_PATH in "$AUDIO_DIR"/*.wav; do
    # Check if the file exists (in case no .wav files are found)
    if [ ! -f "$AUDIO_PATH" ]; then
        echo "No .wav files found in $AUDIO_DIR."
        break
    fi

    echo "Processing $AUDIO_PATH..."
    
    CUDA_VISIBLE_DEVICES=0 python -m uss.inference \
        --audio_path="$AUDIO_PATH" \
        --levels 1 2 3 \
        --config_yaml="./scripts/train/ss_model=resunet30,querynet=at_soft,data=full.yaml" \
        --checkpoint_path="./downloaded_checkpoints/ss_model=resunet30,querynet=at_soft,data=full,devices=8,step=1000000.ckpt"
done