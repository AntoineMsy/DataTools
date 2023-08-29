#!/bin/bash
#SBATCH --account=rpp-blairt2k
#SBATCH --time=0-05:30:00
#SBATCH --mem=200G  
#SBATCH --cpus-per-task=3
source /home/amisery/DataTools/cedar_scripts/sourceme.sh
python /home/amisery/DataTools/root_utils/convert_softmax.py "/home/amisery/scratch/softmaxes/softmax_cl/"