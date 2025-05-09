# DetectGPT Revisited: Zero-Shot LLM-Generated Text Detection

## Princeton University COS484 Spring 25 Final Project. Team members: Rafael Moschopoulos, Tersoo Upaa Jr., Bryan Boateng

## Instructions

**The code in this repo is adapted directly from the original [DetectGPT codebase](https://github.com/eric-mitchell/detect-gpt)**

First, install the Python dependencies:

    python3 -m venv env
    source env/bin/activate
    pip install -r requirements.txt

The code we used to carry out experiments is in `experiment_code/`.

You will need to pre-download all the datasets and models you will use. To do so, set a persistent cache directory in both pre_down_data.py and pre_down_models.py.

Uncomment models you don't wish to use to save space/download time.

Get a HF API key and enter it in the appropriate field in the pre_down_models.py file.

Get a kaggle.json API key and put it in the same directory as pre_down_data.py. This is necessary for the WritingPrompts dataset.

Run `pre_down_models.py` and `pre_down_data.py`. This will take a while and use hundreds of GBs of storage.

The file `experiment_code/run.py` contains all code required to perform experiments with different models/hyperparameters, etc.

To exactly replicate our experiments, `cd experiment_code` and then `sh ./paper_scripts/<desired script>`. Those scripts invoke `run.py` with the exact parameters we used for our experiments. Change the --cache_dir argument to whatever you set in the `pre_down_*` files.

**Note: Intermediate results are saved in `tmp_results/`. If your experiment completes successfully, the results will be moved into the `results/` directory. These folders will be generated wherever `run.py` is located.**

## Plots/visuals

The directory `./paper_elements/plots` contains the Jupyter Notebook used to generate all graphs in our paper. The experimental results were copied directly from the output of `run.py` into the notebook.

`./paper_elements/tables` contains an spreadsheet with the DetectGPT vs. baseline comparison experiment results, also copied directly from the `run.py` output. `get_latex_formatted.py` converts the spreadsheet to ready-to-copy-paste Latex code.

