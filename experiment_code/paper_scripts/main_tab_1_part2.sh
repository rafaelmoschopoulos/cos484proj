python run.py --cache_dir /scratch/gpfs/tu8435/model_cache --output_name main_table_1 --base_model_name gpt2-xl --mask_filling_model_name t5-3b --n_perturbation_list 100 --n_samples 312 --pct_words_masked 0.3 --span_length 2 --dataset squad --dataset_key context
python run.py --cache_dir /scratch/gpfs/tu8435/model_cache --output_name main_table_1 --base_model_name gpt2-xl --mask_filling_model_name t5-3b --n_perturbation_list 100 --n_samples 500 --pct_words_masked 0.3 --span_length 2 --dataset writing
python run.py --cache_dir /scratch/gpfs/tu8435/model_cache --output_name main_table_1 --base_model_name EleutherAI/gpt-j-6B --mask_filling_model_name t5-3b --n_perturbation_list 100 --n_samples 500 --pct_words_masked 0.3 --span_length 2

