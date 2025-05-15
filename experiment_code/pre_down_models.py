import os
import transformers

# List of models to download
model_names = [
#    "roberta-large-openai-detector",
#    "roberta-base-openai-detector",

#    "gpt2",
#    "gpt2-medium",
#    "gpt2-large",
#    "gpt2-xl",

#    "facebook/opt-2.7b",
#    "meta-llama/Llama-3.2-3B",

#    "EleutherAI/gpt-neo-2.7B",
#    "EleutherAI/gpt-j-6B",
#    "EleutherAI/gpt-neox-20b",

#    "sberbank-ai/mGPT",
#    "stanford-crfm/pubmedgpt",

#    "t5-small",
#    "t5-base",
#    "t5-large",
#    "t5-3b",
   "t5-11b",
   "google/mt5-xl",
]

token = ""
cache_dir = ""

if not os.path.exists(cache_dir):
    os.makedirs(cache_dir)

print("Downloading models and tokenizers...")

for model_name in model_names:
    folder = model_name.replace("/", "--")
    save_path = os.path.join(cache_dir, folder)
    os.makedirs(save_path, exist_ok=True)
    try:
        print(f"Downloading {model_name} ...")
        if "roberta" in model_name.lower():
            model = transformers.AutoModelForSequenceClassification.from_pretrained(model_name, cache_dir=cache_dir, force_download=True)
        if 't5' in model_name.lower():
            model = transformers.AutoModelForSeq2SeqLM.from_pretrained(model_name, cache_dir=cache_dir, token=token)
        else:
            model = transformers.AutoModelForCausalLM.from_pretrained(model_name, cache_dir=cache_dir, token=token, force_download=True)
        model.save_pretrained(save_path, from_pt=True)
    except Exception as e:
        print(f"Error downloading model weights for {model_name}: {e}")
    try:
        print(f"Downloading tokenizer for {model_name} ...")
        tokenizer = transformers.AutoTokenizer.from_pretrained(model_name, cache_dir=cache_dir, token=token)
        tokenizer.save_pretrained(save_path, from_pt=True)
    except Exception as e:
        print(f"Error downloading tokenizer for {model_name}: {e}")

print("All specified models and tokenizers have been downloaded to the cache directory.")

