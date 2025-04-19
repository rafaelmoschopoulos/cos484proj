import os
import transformers

# List of models to download
model_names = [

    "roberta-large-openai-detector",
    "meta-llama/Llama-3.2-3B",
    "gpt2",
    "gpt2-medium",
    "gpt2-large",
    "gpt2-xl",
    "facebook/opt-2.7b",
    "EleutherAI/gpt-neo-2.7B",
    "EleutherAI/gpt-j-6B",
    "sberbank-ai/mGPT",
    "stanford-crfm/pubmedgpt",
    "t5-small",
    "t5-base",
    "t5-large",
    "t5-3b",
    "roberta-base-openai-detector",
    "google/mt5-xl",
    "t5-11b"
]

token = "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"

# Specify your cache directory (ensure it exists)
cache_dir = "/scratch/gpfs/tu8435/model_cache"
if not os.path.exists(cache_dir):
    os.makedirs(cache_dir)

print("Downloading models and tokenizers...")

for model_name in model_names:
    try:
        print(f"Downloading {model_name} ...")
        # For causal language models or sequence-to-sequence models, use AutoModelFor... as appropriate.
        # Here we choose AutoModelForCausalLM for models that generate text (like gpt2 variants, OPT, GPT-Neo/J/NeoX, etc.)
        if "roberta" in model_name.lower():
            model = transformers.AutoModelForSequenceClassification.from_pretrained(model_name, cache_dir=cache_dir)
        if 't5' in model_name.lower():
            # For T5 models and other sequence-to-sequence models, load the seq2seq variant.
            model = transformers.AutoModelForSeq2SeqLM.from_pretrained(model_name, cache_dir=cache_dir, token=token)
        else:
            model = transformers.AutoModelForCausalLM.from_pretrained(model_name, cache_dir=cache_dir, token=token)
    except Exception as e:
        print(f"Error downloading model weights for {model_name}: {e}")
    try:
        print(f"Downloading tokenizer for {model_name} ...")
        tokenizer = transformers.AutoTokenizer.from_pretrained(model_name, cache_dir=cache_dir, token=token)
    except Exception as e:
        print(f"Error downloading tokenizer for {model_name}: {e}")

print("All specified models and tokenizers have been downloaded to the cache directory.")

