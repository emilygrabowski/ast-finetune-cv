from datasets import load_dataset

import os


dir_name = "../data/150-percent"

print("Checking that the path exists...:",os.path.exists(dir_name))

dataset=load_dataset(dir_name)