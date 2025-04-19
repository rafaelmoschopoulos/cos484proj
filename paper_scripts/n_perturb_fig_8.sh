python run.py --output_name n_perturb --base_model_name gpt2-xl --mask_filling_model_name t5-large --n_perturbation_list 1,10,100,1000 --n_samples 100 --pct_words_masked 0.3 --span_length 2 --skip_baselines --cache_dir ./cache
python run.py --output_name n_perturb --base_model_name gpt2-xl --mask_filling_model_name t5-large --n_perturbation_list 1,10,100,1000 --n_samples 100 --pct_words_masked 0.3 --span_length 2 --dataset squad --dataset_key context --skip_baselines --cache_dir ./cache
python run.py --output_name n_perturb --base_model_name gpt2-xl --mask_filling_model_name t5-large --n_perturbation_list 1,10,100,1000 --n_samples 100 --pct_words_masked 0.3 --span_length 2 --dataset writing --skip_baselines --cache_dir ./cache

python run.py --output_name n_perturb --base_model_name EleutherAI/gpt-j-6B --mask_filling_model_name t5-large --n_perturbation_list 1,10,100,1000 --n_samples 100 --pct_words_masked 0.3 --span_length 2 --skip_baselines --cache_dir ./cache
python run.py --output_name n_perturb --base_model_name EleutherAI/gpt-j-6B --mask_filling_model_name t5-large --n_perturbation_list 1,10,100,1000 --n_samples 100 --pct_words_masked 0.3 --span_length 2 --dataset squad --dataset_key context --skip_baselines --cache_dir ./cache
python run.py --output_name n_perturb --base_model_name EleutherAI/gpt-j-6B --mask_filling_model_name t5-large --n_perturbation_list 1,10,100,1000 --n_samples 100 --pct_words_masked 0.3 --span_length 2 --dataset writing --skip_baselines --cache_dir ./cache

