#!/bin/bash
#SBATCH --account=rpp-blairt2k
#SBATCH --time=0-05:30 
#SBATCH --mem=200G  
#SBATCH --cpus-per-task=3
source /home/amisery/39env/bin/activate

file_path="/home/amisery/DataTools/npz_splits/npz_split_$1.txt"

files=()

# Read the file line by line
while IFS= read -r line; do
  files+=("$line") # Append each line to the list
done < "$file_path"

out_fpath="/home/amisery/scratch/outputs_h5/wcsim_kmtsui_mdt_good_$1.h5"

python /home/amisery/DataTools/root_utils/np_to_digihit_array_hdf5.py "${files[@]}" -o $out_fpath