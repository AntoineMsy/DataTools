#!/bin/bash
#SBATCH --account=rpp-blairt2k
#SBATCH --cpus-per-task=5
#SBATCH --time=0-23:00:00 
#SBATCH --mem=200GB
module load StdEnv/2016
module load python/3.6.3

SCRIPTDIR=$(dirname "$0")
BASEDIR=$(dirname "$SCRIPTDIR")

source "$SCRIPTDIR/sourceme.sh"

for ((i=1; i<=10; i++))
do
lb=$((1000*i + 1))  # Calculate the lower bound
hb=$((1000*(i+1)))  # Calculate the upper bound
# sbatch /home/amisery/DataTools/process_raw_batch.sh -l "$lb" -h "$hb" -o /home/amisery/scratch/outputs_npz/
sbatch <<EOF
#!/bin/bash
#SBATCH --account=rpp-blairt2k
#SBATCH --cpus-per-task=5
#SBATCH --time=0-23:00:00 
#SBATCH --mem=200GB

python "$BASEDIR/root_utils/npz_batch_prod.py" -l "$lb" -h "$hb" -o /home/amisery/scratch/outputs_npz/
EOF
done
# source /home/amisery/39env/bin/activate

#python np_to_digihit_array_hdf5.py /home/amisery/scratch/outputs_npz/ -o /home/amisery/scratch/outputs_h5/