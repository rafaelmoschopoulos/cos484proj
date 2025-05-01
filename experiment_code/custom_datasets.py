import random
import os
import datasets

SEPARATOR = '<<<SEP>>>'


DATASETS = ['writing', 'english', 'german', 'pubmed']


def load_pubmed(cache_dir):
    data = datasets.load_dataset('pubmed_qa', 'pqa_labeled', split='train', cache_dir=cache_dir)

    # combine question and long_answer
    data = [f'Question: {q} Answer:{SEPARATOR}{a}' for q, a in zip(data['question'], data['long_answer'])]

    return data


def process_prompt(prompt):
    return prompt.replace('[ WP ]', '').replace('[ OT ]', '')


def process_spaces(story):
    return story.replace(
        ' ,', ',').replace(
        ' .', '.').replace(
        ' ?', '?').replace(
        ' !', '!').replace(
        ' ;', ';').replace(
        ' \'', '\'').replace(
        ' ’ ', '\'').replace(
        ' :', ':').replace(
        '<newline>', '\n').replace(
        '`` ', '"').replace(
        ' \'\'', '"').replace(
        '\'\'', '"').replace(
        '.. ', '... ').replace(
        ' )', ')').replace(
        '( ', '(').replace(
        ' n\'t', 'n\'t').replace(
        ' i ', ' I ').replace(
        ' i\'', ' I\'').replace(
        '\\\'', '\'').replace(
        '\n ', '\n').strip()

def download_writing_prompts():
    """
    Downloads the Kaggle writing prompts dataset into the ./data folder
    if it is not already present.
    """
    data_folder = './data'
    if not os.path.exists(data_folder):
        os.makedirs(data_folder)

    kaggle_config_dir = os.getcwd()  # assumes kaggle.json is here
    os.environ['KAGGLE_CONFIG_DIR'] = kaggle_config_dir

    kaggle_json_path = os.path.join(kaggle_config_dir, 'kaggle.json')
    if not os.path.exists(kaggle_json_path):
        raise OSError(
            f"Could not find kaggle.json in {kaggle_config_dir}. "
            "Please ensure that your kaggle.json file is in this folder or copy it to ~/.kaggle."
        )

    # Automatically adjust file permissions to 600, if possible.
    try:
        os.chmod(kaggle_json_path, 0o600)
    except Exception as e:
        print(f"Warning: Unable to change permissions on {kaggle_json_path}. {e}")

    from kaggle.api.kaggle_api_extended import KaggleApi
    api = KaggleApi()
    api.authenticate()

    dataset_dir = os.path.join(data_folder, 'writingPrompts')
    if not os.path.exists(dataset_dir):
        print("Downloading ratthachat/writing-prompts dataset to", data_folder)
        api.dataset_download_files('ratthachat/writing-prompts', path=data_folder, unzip=True)
    else:
        print("Dataset already downloaded at", dataset_dir)

def load_writing(cache_dir=None):
    writing_path = 'data/writingPrompts'
    if not os.path.exists(writing_path):
        print(f"Writing dataset not found at {writing_path}. Initiating download...")
        download_writing_prompts()
    with open(f'{writing_path}/valid.wp_source', 'r') as f:
        prompts = f.readlines()
    with open(f'{writing_path}/valid.wp_target', 'r') as f:
        stories = f.readlines()

    prompts = [process_prompt(prompt) for prompt in prompts]
    joined = [process_spaces(prompt + " " + story) for prompt, story in zip(prompts, stories)]
    filtered = [story for story in joined if 'nsfw' not in story and 'NSFW' not in story]

    random.seed(0)
    random.shuffle(filtered)

    return filtered


def load_language(language, cache_dir):
    # load either the english or german portion of the wmt16 dataset
    assert language in ['en', 'de']
    d = datasets.load_dataset('wmt16', 'de-en', split='train', cache_dir=cache_dir)
    docs = d['translation']
    desired_language_docs = [d[language] for d in docs]
    lens = [len(d.split()) for d in desired_language_docs]
    sub = [d for d, l in zip(desired_language_docs, lens) if l > 100 and l < 150]
    return sub


def load_german(cache_dir):
    return load_language('de', cache_dir)


def load_english(cache_dir):
    return load_language('en', cache_dir)


def load(name, cache_dir, **kwargs):
    if name in DATASETS:
        load_fn = globals()[f'load_{name}']
        return load_fn(cache_dir=cache_dir, **kwargs)
    else:
        raise ValueError(f'Unknown dataset {name}')
