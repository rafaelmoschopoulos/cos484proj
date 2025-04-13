import os
import datasets
import custom_datasets

def pre_download_datasets(cache_dir):
    # Create the cache directory if it doesn't exist
    if not os.path.exists(cache_dir):
        os.makedirs(cache_dir)

    # List of datasets you need
    # For custom datasets (pubmed, english, german), the custom_datasets module handles loading.
    # For others (xsum, squad), we use datasets.load_dataset.
    datasets_to_download = ['xsum', 'squad', 'pubmed', 'english', 'german', 'writing']

    # For non-custom datasets, define the key used to index the dataset items.
    # (According to your run.py, xsum uses key "document"; squad might use "context" or another field.)
    key_map = {
        "xsum": "document",
        "squad": "context"
    }

    for ds in datasets_to_download:
        print(f"Pre-downloading dataset: {ds}")
        try:
            if ds in custom_datasets.DATASETS:
                # This covers pubmed, english, german as defined in your module.
                data = custom_datasets.load(ds, cache_dir)
                # Here you might simply print the number of loaded examples if applicable.
                if isinstance(data, list):
                    print(f"Custom dataset '{ds}' loaded with {len(data)} examples.")
                else:
                    print(f"Custom dataset '{ds}' loaded.")
            else:
                # For datasets not handled by custom_datasets (here: xsum and squad)
                key = key_map.get(ds, None)
                dset = datasets.load_dataset(ds, split='train', trust_remote_code=True, cache_dir=cache_dir)

                if key is not None:
                    # Access the specific field to force tokenization/caching.
                    data = dset[key]
                else:
                    data = dset
                # Force retrieval (you could take a small subset if you wish)
                print(f"Dataset '{ds}' pre-downloaded. Number of examples: {len(data)}")
        except Exception as e:
            print(f"Error pre-downloading dataset '{ds}': {e}")

if __name__ == "__main__":
    # Replace with your desired cache directory path. This should be the same value used in run.py.
    cache_dir = "/scratch/gpfs/tu8435/data_cache/"
    pre_download_datasets(cache_dir)
