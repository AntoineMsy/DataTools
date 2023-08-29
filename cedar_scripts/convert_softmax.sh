#!/bin/bash
#SBATCH --account=rpp-blairt2k
#SBATCH --time=0-05:30:00
#SBATCH --mem=200G  
#SBATCH --cpus-per-task=3
SCRIPTDIR=$(dirname "$0")
BASEDIR=$(dirname "$SCRIPTDIR")
echo "$BASEDIR"
source "$SCRIPTDIR/sourceme.sh"

source "$SCRIPTDIR/sourceme.sh"
python "$BASEDIR/root_utils/convert_softmax.py" "/home/amisery/scratch/softmaxes/softmax_cl/"