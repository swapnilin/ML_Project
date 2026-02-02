### Steps to follow:
Create a virtual environment
```bash
conda create -n project python=3.10 -y
```
-y automatically answers “yes” to confirmation prompts and -n is for the name of the environment.

After the env is created, switch to the new environment
``bash
conda activate project
```
Remember to delete environements after projects are completed. They take up lot of space in your drive.

Next, install all the modules required for this project using the requirements.txt file
```bash
pip install -r requirements.txt
```
When you start your project you may not know all the modules required upfront, you create this list just before the final commit using
```bash
pip freeze > requirements.txt
```
This captures exact versions and ensures anyone can reproduce your environment.
