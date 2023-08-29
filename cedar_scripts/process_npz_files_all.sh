#!/bin/bash
#SBATCH --account=rpp-blairt2k
#SBATCH --time=0-01:30 
#SBATCH --mem=200G  
#SBATCH --cpus-per-task=3
source /home/amisery/39env/bin/activate

SCRIPTDIR=$(dirname "$0")

for ((i=0; i<=10; i++))
do
lb=$((1000*i + 1))  # Calculate the lower bound
hb=$((1000*(i)))  # Calculate the upper bound
# sbatch /home/amisery/DataTools/cedar_scripts/process_npz_files_batch.sh "$lb" "$hb"
sbatch "$SCRIPTDIR/process_npz_files_batch.sh" $i
# sbatch <<EOF
# #!/bin/bash
# #SBATCH --account=rpp-blairt2k
# #SBATCH --cpus-per-task=5
# #SBATCH --time=0-3:00:00 
# #SBATCH --mem=200GB

# in_fpath="/home/amisery/scratch/outputs_npz_$lb_$hb"
# # Create an array to store the file names
# files=()

# # Loop through each file in the directory
# for file in "$in_fpath"/*; do
#   # Check if the file is a regular file (not a directory)
#   if [ -f "$file" ]; then
#     # Add the file name to the array
#     files+=("$file")
#   fi
# done
# out_fpath="/home/amisery/scratch/outputs_h5/wcsim_kmtsui_mdt_good_$lb_$hb.h5"
# python /home/amisery/DataTools/root_utils/np_to_digihit_array_hdf5.py "${files[@]}" -o $out_fpath
# EOF
done