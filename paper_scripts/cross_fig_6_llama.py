python run.py --cache_dir /scratch/gpfs/tu8435/model_cache --output_name cross --base_model_name gpt2-xl --scoring_model_name meta-llama/Llama-3.2-3B --mask_filling_model_name t5-3b --n_perturbation_list 50 --n_samples 200 --pct_words_masked 0.3 --span_length 2   --skip_baselines
python run.py --cache_dir /scratch/gpfs/tu8435/model_cache --output_name cross --base_model_name EleutherAI/gpt-neo-2.7B --scoring_model_name meta-llama/Llama-3.2-3B --mask_filling_model_name t5-3b --n_perturbation_list 50 --n_samples 200 --pct_words_masked 0.3 --span_length 2   --skip_baselines
python run.py --cache_dir /scratch/gpfs/tu8435/model_cache --output_name cross --base_model_name EleutherAI/gpt-j-6B --scoring_model_name meta-llama/Llama-3.2-3B --mask_filling_model_name t5-3b --n_perturbation_list 50 --n_samples 200 --pct_words_masked 0.3 --span_length 2   --skip_baselines

python run.py --cache_dir /scratch/gpfs/tu8435/model_cache --output_name cross --base_model_name meta-llama/Llama-3.2-3B --scoring_model_name gpt2-xl --mask_filling_model_name t5-3b --n_perturbation_list 50 --n_samples 200 --pct_words_masked 0.3 --span_length 2   --skip_baselines
python run.py --cache_dir /scratch/gpfs/tu8435/model_cache --output_name cross --base_model_name meta-llama/Llama-3.2-3B --scoring_model_name EleutherAI/gpt-neo-2.7B --mask_filling_model_name t5-3b --n_perturbation_list 50 --n_samples 200 --pct_words_masked 0.3 --span_length 2   --skip_baselines
python run.py --cache_dir /scratch/gpfs/tu8435/model_cache --output_name cross --base_model_name meta-llama/Llama-3.2-3B --scoring_model_name EleutherAI/gpt-j-6B --mask_filling_model_name t5-3b --n_perturbation_list 50 --n_samples 200 --pct_words_masked 0.3 --span_length 2   --skip_baselines



python run.py --cache_dir /scratch/gpfs/tu8435/model_cache --output_name cross --base_model_name gpt2-xl --scoring_model_name meta-llama/Llama-3.2-3B --mask_filling_model_name t5-3b --n_perturbation_list 50 --n_samples 200 --pct_words_masked 0.3 --span_length 2   --skip_baselines --dataset writing
python run.py --cache_dir /scratch/gpfs/tu8435/model_cache --output_name cross --base_model_name EleutherAI/gpt-neo-2.7B --scoring_model_name meta-llama/Llama-3.2-3B --mask_filling_model_name t5-3b --n_perturbation_list 50 --n_samples 200 --pct_words_masked 0.3 --span_length 2   --skip_baselines --dataset writing
python run.py --cache_dir /scratch/gpfs/tu8435/model_cache --output_name cross --base_model_name EleutherAI/gpt-j-6B --scoring_model_name meta-llama/Llama-3.2-3B --mask_filling_model_name t5-3b --n_perturbation_list 50 --n_samples 200 --pct_words_masked 0.3 --span_length 2   --skip_baselines --dataset writing

python run.py --cache_dir /scratch/gpfs/tu8435/model_cache --output_name cross --base_model_name meta-llama/Llama-3.2-3B --scoring_model_name gpt2-xl --mask_filling_model_name t5-3b --n_perturbation_list 50 --n_samples 200 --pct_words_masked 0.3 --span_length 2   --skip_baselines --dataset writing
python run.py --cache_dir /scratch/gpfs/tu8435/model_cache --output_name cross --base_model_name meta-llama/Llama-3.2-3B --scoring_model_name EleutherAI/gpt-neo-2.7B --mask_filling_model_name t5-3b --n_perturbation_list 50 --n_samples 200 --pct_words_masked 0.3 --span_length 2   --skip_baselines --dataset writing
python run.py --cache_dir /scratch/gpfs/tu8435/model_cache --output_name cross --base_model_name meta-llama/Llama-3.2-3B --scoring_model_name EleutherAI/gpt-j-6B --mask_filling_model_name t5-3b --n_perturbation_list 50 --n_samples 200 --pct_words_masked 0.3 --span_length 2   --skip_baselines --dataset writing



python run.py --cache_dir /scratch/gpfs/tu8435/model_cache --output_name cross --base_model_name gpt2-xl --scoring_model_name meta-llama/Llama-3.2-3B --mask_filling_model_name t5-3b --n_perturbation_list 50 --n_samples 200 --pct_words_masked 0.3 --span_length 2   --skip_baselines --dataset squad --dataset_key context
python run.py --cache_dir /scratch/gpfs/tu8435/model_cache --output_name cross --base_model_name EleutherAI/gpt-neo-2.7B --scoring_model_name meta-llama/Llama-3.2-3B --mask_filling_model_name t5-3b --n_perturbation_list 50 --n_samples 200 --pct_words_masked 0.3 --span_length 2   --skip_baselines --dataset squad --dataset_key context
python run.py --cache_dir /scratch/gpfs/tu8435/model_cache --output_name cross --base_model_name EleutherAI/gpt-j-6B --scoring_model_name meta-llama/Llama-3.2-3B --mask_filling_model_name t5-3b --n_perturbation_list 50 --n_samples 200 --pct_words_masked 0.3 --span_length 2   --skip_baselines --dataset squad --dataset_key context

python run.py --cache_dir /scratch/gpfs/tu8435/model_cache --output_name cross --base_model_name meta-llama/Llama-3.2-3B --scoring_model_name gpt2-xl --mask_filling_model_name t5-3b --n_perturbation_list 50 --n_samples 200 --pct_words_masked 0.3 --span_length 2   --skip_baselines --dataset squad --dataset_key context
python run.py --cache_dir /scratch/gpfs/tu8435/model_cache --output_name cross --base_model_name meta-llama/Llama-3.2-3B --scoring_model_name EleutherAI/gpt-neo-2.7B --mask_filling_model_name t5-3b --n_perturbation_list 50 --n_samples 200 --pct_words_masked 0.3 --span_length 2   --skip_baselines --dataset squad --dataset_key context
python run.py --cache_dir /scratch/gpfs/tu8435/model_cache --output_name cross --base_model_name meta-llama/Llama-3.2-3B --scoring_model_name EleutherAI/gpt-j-6B --mask_filling_model_name t5-3b --n_perturbation_list 50 --n_samples 200 --pct_words_masked 0.3 --span_length 2   --skip_baselines --dataset squad --dataset_key context

