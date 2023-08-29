from root_utils.event_dump import dump_file
file = "/home/amisery/projects/rpp-blairt2k/rakutsu/iwcd/mc/MassProNov2020/files/wcsim_root/NuMode/2p39/iwcd_p320ka_w750m_1e17pot_2p39_wcsim.00001.root"
km_file = "/project/rpp-blairt2k/rakutsu/iwcd/mc/MassProNov2020/files/wcsim_root/NuMode/2p39_MDT_kmtsui/mdt_iwcd_p320ka_w750m_1e17pot_2p39_wcsim.00001.root"
#dump_file(file, "out_test.npz")
#dump_file(km_file, "out_test_km.npz")
start = 1
stop = 2
home_path = "/project/rpp-blairt2k/rakutsu/iwcd/mc/MassProNov2020/files/wcsim_root/NuMode/2p39_MDT_kmtsui/mdt_iwcd_p320ka_w750m_1e17pot_2p39_wcsim."
out_folder = '/home/amisery/scratch/outputs_npz/'
i=1
out_fpath = out_folder + "wcsim_2p39_MDT_kmtsui_%s.npz"%(str(i).zfill(5))
#dump_file(file, "out_test_km.npz")
list_to_convert = [1000*i for i in range(1,10)]
for i in list_to_convert:
    in_fpath = home_path +"%s.root"%(str(i).zfill(5))
    print(in_fpath)
    out_fpath = out_folder + "wcsim_2p39_MDT_kmtsui_%s.npz"%(str(i).zfill(5))
    dump_file(in_fpath, out_fpath)
for i in range(start, stop):
        in_fpath = home_path +"%s.root"%(str(i).zfill(5))
        print(in_fpath)
        out_fpath = out_folder + "wcsim_2p39_MDT_kmtsui_%s.npz"%(str(i).zfill(5))
        dump_file(km_file, out_fpath)
####### Converting softmaxes from numpy to root with pyroot
import ROOT
import numpy as np
from root_utils.root_file_utils import convert
dir_inpath = '/home/amisery/scratch/likelihoods/wcml/likelihoods'
dir_outpath = '/home/amisery/scratch/likelihoods/wcml_root/likelihoods'
files_to_skip = np.load("/home/amisery/Analysis/files_to_skip.npy")

for i in range(9992,10001):
    if not np.isin(i, files_to_skip):
        fpath = dir_inpath + '%s.npy'%(str(i).zfill(5))
        outpath = dir_outpath + '%s.root'%(str(i).zfill(5))
        convert(fpath, outpath)
#######

python root_utils/np_to_digihit_array_hdf5_mod.py out_test.npz -o out_test.h5
python root_utils/np_to_digihit_array_hdf5_mod.py out_test_km.npz -o out_test_km.h5
#######
from root_utils.root_file_utils import *
import ROOT
import numpy as np
orig_files = ["/home/amisery/projects/rpp-blairt2k/machine_learning/data/IWCD_mPMT_Short/WCSim/%s/E0to1000MeV/unif-pos-R400-y300cm/4pi-dir/IWCD_mPMT_Short_%s_E0to1000MeV_unif-pos-R400-y300cm_4pi-dir_3000evts_0.root"%(s,s) for s in ["e-", "gamma", "mu-", "pi0"]]
n_files = 1000
files_list = ["/home/amisery/projects/rpp-blairt2k/rakutsu/iwcd/mc/MassProNov2020/files/wcsim_root/NuMode/2p39/iwcd_p320ka_w750m_1e17pot_2p39_wcsim.%s.root"%(str(i).zfill(5)) for i in range(n_files)
]
file = "/home/amisery/projects/rpp-blairt2k/rakutsu/iwcd/mc/MassProNov2020/files/wcsim_root/NuMode/2p39/iwcd_p320ka_w750m_1e17pot_2p39_wcsim.00000.root"
km_file = "/project/rpp-blairt2k/rakutsu/iwcd/mc/MassProNov2020/files/wcsim_root/NuMode/2p39_MDT_kmtsui/mdt_iwcd_p320ka_w750m_1e17pot_2p39_wcsim.00001.root"
wcsimfile = WCSimFile(file)
km_wcsimfile = WCSimFile(km_file)
file = "/home/amisery/projects/rpp-blairt2k/rakutsu/iwcd/mc/MassProNov2020/files/wcsim_root/NuMode/2p39/iwcd_p320ka_w750m_1e17pot_2p39_wcsim.00000.root"
wcsimfile = ROOT.TFile(file, "read")
ntracker = wcsimfile.Get("fRooTrackerOutputTree")
ntrackervtx = ntracker.GetBranch("NRooTrackerVtx")
ntrackervtx.GetEntry(0)
for branch in ntracker.GetListOfBranches():
    print(branch.GetName())
for key in wcsimfile.GetListOfKeys():
        print(key)
        tree = wcsimfile.Get(key)
        print(tree)
        # if isinstance(tree, ROOT.TTree):
        #     for branch in tree.GetListOfBranch():
        #         print(branch.GetName())

for ev in range(wcsimfile.nevent):
    wcsimfile.get_event(ev)
    km_wcsimfile.get_event(ev)
    wcsimfile.get_event_info()
    km_wcsimfile.get_event_info()

wcsimfile.get_tracks()
km_wcsimfile.get_tracks()

pid_list = []
mode_list = []

for f in files_list :
    wcsimfile = WCSimFile(f)
    for ev in range(wcsimfile.nevent):
        wcsimfile.get_event(ev)
        wcsimfile.get_event_info()
        mode = wcsimfile.trigger.GetMode()
        if mode != -1:
            print(mode)
            print(ev)
            print(f)
        # out_dict = wcsimfile.get_event_info()
        # mode_list.append(wcsimfile.trigger.GetMode())
        #pid_list = pid_list + out_dict["mode"]
    break

unique, counts = np.unique(np.array(mode_list), return_counts = True)

print(unique, counts)

##############
import ROOT
path_list = []
with open("np_files.txt") as f:
    for line in f:
        path = line.strip()
        path_list.append(path)
for file in path_list:
    f = WCSimFile(file, "read")
    key_list = []
    for key in f.GetListOfKeys():
        print(key)
        tree = f.Get(key)
        print(tree)
        if isinstance(tree, ROOT.TTree):
            for branch in tree.GetListOfBranches():
                print(branch.GetName())
        

for leaf in ntracker.GetListOfLeaves():
    print(leaf.GetName())

#########
import numpy as np
import os
files_to_skip = np.load("/home/amisery/Analysis_mod/files_to_skip.npy")
for i in range(1,10000):
    file = "/home/amisery/scratch/outputs_npz/wcsim_2p39_MDT_kmtsui_%s.npz"%(str(i).zfill(5))
    if np.isin(i,files_to_skip):
        os.rename(file, "/home/amisery/scratch/outputs_npz_bad_fitqun/wcsim_2p39_MDT_kmtsui_%s.npz"%(str(i).zfill(5)))
########
import numpy as np
import os
files_to_skip = np.load("/home/amisery/Analysis_mod/files_to_skip.npy")
for i in range(1,10000):
    file = "/home/amisery/scratch/outputs_npz/wcsim_2p39_MDT_kmtsui_%s.npz"%(str(i).zfill(5))
    if np.isin(i,files_to_skip):
        os.rename(file, "/home/amisery/scratch/outputs_npz_bad_fitqun/wcsim_2p39_MDT_kmtsui_%s.npz"%(str(i).zfill(5)))

########
import numpy as np
import os
files_to_skip = np.load("/home/amisery/Analysis_mod/files_to_skip.npy")
for i in range(1,101):
    file = "/home/amisery/scratch/softmaxes/softmax%s.root"%(str(i).zfill(5))
    if np.isin(i,files_to_skip):
        os.rename(file, "/home/amisery/scratch/bad_softmaxes/softmax%s.root"%(str(i).zfill(5)))

#####
b = [i*1000 for i in range(1,11)]
import numpy as np
import os
files_to_skip = np.load("/home/amisery/Analysis/files_to_skip.npy")
for j in range(1, len(b)) :
    out_folder = "/home/amisery/scratch/outputs_npz_%i_%i/"%(b[j-1],b[j])
    os.mkdir(out_folder) 
    for i in range(b[j-1],b[j]):
        file = "/home/amisery/scratch/outputs_npz/wcsim_2p39_MDT_kmtsui_%s.npz"%(str(i).zfill(5))
        out_fpath = out_folder + "wcsim_2p39_MDT_kmtsui_%s.npz"%(str(i).zfill(5))
        if not np.isin(i,files_to_skip):
            os.rename(file, out_fpath)

#####
#generate the good list of fitqun files
import numpy as np

files_to_skip = np.load("/home/amisery/Analysis/files_to_skip.npy")

with open("fitqun_files_whole.txt", "w") as f:
    for i in range(1,10000):
        if not np.isin(i, files_to_skip):
            f_path = "/home/amisery/rakutsu_iwcd/mc/MassProNov2020/files/fq_root/NuMode/2p39/iwcd_p320ka_w750m_1e17pot_2p39_fitqun.%s.root"%(str(i).zfill(5))
            f.write(f_path + "\n")

#####
import numpy as np
files_to_skip = np.load("/home/amisery/Analysis/files_to_skip.npy")
delim = [1] + [1000*i for i in range(1,11)]

for i in range(1,len(delim)):
    with open("npz_split_%i.txt"%(i), "w") as f:
        for i in range(delim[i-1],delim[i]):
            if not np.isin(i, files_to_skip):
                f_path = "/home/amisery/scratch/outputs_npz/wcsim_2p39_MDT_kmtsui_%s.npz"%(str(i).zfill(5))
                f.write(f_path + "\n")

#####
import numpy as np
import os
def make_split_paths(dir_path, chunks, split_type = "softmax"):
    files_to_skip = np.load("/home/amisery/Analysis/files_to_skip.npy")
    delim = [1] + [10000//chunks*i for i in range(1,chunks+1)]
    out_dirpath = "/home/amisery/Analysis/RecoAnalysis/" + split_type + "_split"
    if not os.path.exists(out_dirpath):
        os.mkdir(out_dirpath)
    for i in range(1,len(delim)):
        with open(out_dirpath + "/%s_split_%i.txt"%(split_type, i), "w") as f:
            for j in range(delim[i-1],delim[i]):
                if not np.isin(j, files_to_skip):
                    f_path = "%s%s.root"%(dir_path,str(j).zfill(5))
                    if j==delim[i]-1:
                        f.write(f_path)
                    else :
                        f.write(f_path + "\n")

#make_split_paths("/home/amisery/scratch/likelihoods/wcml_root/likelihoods", 100, "likelihoods")
#make_split_paths("/home/amisery/rakutsu_iwcd/mc/MassProNov2020/files/fq_root/NuMode/2p39/iwcd_p320ka_w750m_1e17pot_2p39_fitqun.", 100, "fitqun")
make_split_paths("/home/amisery/scratch/softmaxes/softmax_cl_root/softmax", 100, "softmax")

