# simple-viz

## System requirements
[Installing git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
```
$ git --version
```

[Installing Python package manager](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)
```
python3 -m pip install --user --upgrade pip
```

Installing Virtual Environment
```
python3 -m pip install --user virtualenv
```

## Get the repository 
* Only the first time
```
git clone https://github.com/peiyongsim/simple-viz.git
```
* To get latest changes
```
cd simple-viz && git pull
```

## Running the Code
Go into the project directory
```
cd simple-viz
```

Creating and activating a virtual environment
```
python3 -m venv env && source env/bin/activate

```

Installing packages
```
pip3 install -r requirements.txt
```

Getting the visualization
```
python3 run_viz.py <full_path_containing_csv_file>

example:
python3 run_viz.py ~/Desktop/gender.csv 
```

## Results/Output
It should look like this
![alt text](https://github.com/peiyongsim/simple-viz/viz.png)

Click on the floppy disk (diskette) symbol to save it to your local drive








