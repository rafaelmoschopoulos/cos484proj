#!/bin/bash
#SBATCH --job-name=cos484proj-main_tab_1_part4
#SBATCH --partition=gpu-short         # GPU jobs up to 24h
#SBATCH --gres=gpu:1                  # Request 1 GPU (A100 40GB)
#SBATCH --cpus-per-task=1            # Number of CPU cores
#SBATCH --mem=32G                    # System memory
#SBATCH --time=23:59:59              # Job time limit
#SBATCH --output=/home/tu8435/Documents/COS484/Final_Project/slurm-%x-%j.out
#SBATCH --error=/home/tu8435/Documents/COS484/Final_Project/slurm-%x-%j.err
#SBATCH --mail-type=BEGIN,END,FAIL
#SBATCH --mail-user=tu8435@princeton.edu

# Trap signals for cleanup (optional if you're checkpointing mid-job)
trap "echo 'Job interrupted. Saving outputs...'; cp -r tmp_results/ /home/tu8435/Documents/COS484/Final_Project/; exit" SIGTERM SIGINT

# Load Anaconda and activate environment
module purge
module load anaconda3/2024.10
eval "$(conda shell.bash hook)"
conda activate /scratch/gpfs/tu8435/COS484/cos484proj/.env/cos484proj-env

# Redirect Hugging Face cache to scratch --> setting environment variables for duration of the run
export TRANSFORMERS_CACHE=/scratch/gpfs/tu8435/model_cache/
export HF_HOME=/scratch/gpfs/tu8435/model_cache/

# Create permanent storage dir (in case run.py doesn't)
mkdir -p /home/tu8435/Documents/COS484/Final_Project

# Create per-run output subdir in scratch (optional but useful)
SCRATCH_RUN_DIR="/scratch/gpfs/tu8435/runs/slurm_$SLURM_JOB_ID"
mkdir -p "$SCRATCH_RUN_DIR"

# Run the paper script (main_tab_1_part4.sh) and redirect output to your home dir
srun bash paper_scripts/main_tab_1_part4.sh > "$SCRATCH_RUN_DIR/output.log" 2>&1 & TRAIN_PID=$!

# Wait for the training job to finish
wait $TRAIN_PID

# Copy outputs back to home for permanence
cp -r "$SCRATCH_RUN_DIR" /home/tu8435/Documents/COS484/Final_Project/