# maxp_emp

A paper focused on computational techniques for identifying regional employment centers

## Setup

1. clone this repository
2. run `make environment` to build the conda environment with necessary dependencies
   - run `conda activate lodeshoods` each time you work on the project
   - run `make environment-update` to rebuild the conda environment if you add new dependencies or they change upstream

## Use

The current version of the manuscript lives at `paper/draft.md` and generated versions will be placed in `paper/compiled/`. Do not edit anything in that directory directly, as it will be overwritten in the build process. The makefile handles all the heavy lifting. Use `make` in the root of this directory to see all available commands.

- use `make paper` to build the draft
- use `make notebooks` to re-run the analysis - **note it takes about a day for all everything to execute**
