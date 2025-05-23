#!/bin/bash
#SBATCH --job-name=cos484proj-figure7
#SBATCH --partition=gpu-test         # GPU jobs up to 24h
#SBATCH --gres=gpu:1                  # Request 1 GPU (A100 40GB)
#SBATCH --cpus-per-task=4            # Number of CPU cores
#SBATCH --mem=16G                    # System memory
#SBATCH --time=01:00:00              # Job time limit
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

# Run the paper script (scale.sh) and redirect output to your home dir
srun bash paper_scripts/scale.sh > "$SCRATCH_RUN_DIR/output.log" 2>&1 & TRAIN_PID=$!

# Wait for the training job to finish
wait $TRAIN_PID

# Copy outputs back to home for permanence
cp -r "$SCRATCH_RUN_DIR" /home/tu8435/Documents/COS484/Final_Project/
