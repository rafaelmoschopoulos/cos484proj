import os
import datasets
import custom_datasets

cache_dir = ""

def pre_download_datasets(cache_dir):
    if not os.path.exists(cache_dir):
        os.makedirs(cache_dir)

    datasets_to_download = ['xsum', 'squad', 'pubmed', 'english', 'german', 'writing']

    key_map = {
        "xsum": "document",
        "squad": "context"
    }

    for ds in datasets_to_download:
        print(f"Pre-downloading dataset: {ds}")
        try:
            if ds in custom_datasets.DATASETS:
                # covers pubmed, english, german
                data = custom_datasets.load(ds, cache_dir)
                print(f"Custom dataset '{ds}' loaded.")
            else:
                # For datasets not handled by custom_datasets
                key = key_map.get(ds, None)
                dset = datasets.load_dataset(ds, split='train', trust_remote_code=True, cache_dir=cache_dir)

                if key is not None:
                    data = dset[key]
                else:
                    data = dset
                print(f"Dataset '{ds}' pre-downloaded. Number of examples: {len(data)}")
        except Exception as e:
            print(f"Error pre-downloading dataset '{ds}': {e}")

if __name__ == "__main__":
    pre_download_datasets(cache_dir)
