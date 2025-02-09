# DESTINATION FOLDER
DESTINATION_FOLDER="/media/leohemamou/ssd2/"


python src/normalize_name.py -i /media/leohemamou/ssd2/standup/download/ -r

python src/extract_audio.py -i /media/leohemamou/ssd2/standup/download/fr/ -o /media/leohemamou/ssd2/standup/audio/fr/ -v



CUDA_VISIBLE_DEVICES=0 python -m uss.inference     --audio_path=/media/leohemamou/ssd2/standup/audio/fr/alexandra_pizzagali_disney.wav     --levels 1 2 3     --config_yaml="./scripts/train/ss_model=resunet30,querynet=at_soft,data=full.yaml"     --checkpoint_path="./downloaded_checkpoints/ss_model=resunet30,querynet=at_soft,data=full,devices=8,step=1000000.ckpt"