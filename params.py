from pathlib import Path
import socket

hostname = socket.gethostname()
# name of the machine you are running on:
# laptop: "apc", workstation: "P620"
assert hostname in ["apc", "P620"]

PROJECT_NAME = "ijc-histology"
PATH_PROJECT = Path("/home/anton/Projects/PythonProjects") / PROJECT_NAME
assert PATH_PROJECT.exists()

PATH_DATA = Path("/mnt/data/ijc-histology-data/") if hostname == "apc" else Path("/mnt/disk4/")

PATH_PATCHES = PATH_DATA / "TCGA-COAD-patches-5-percent"
assert PATH_PATCHES.exists()

WANDB_PROJECT = "ijc-histology-wandb"
ENTITY = None
RAW_DATA_AT = "TCGA-COAD"
PROCESSED_DATA_AT = "TCGA-COAD-split"