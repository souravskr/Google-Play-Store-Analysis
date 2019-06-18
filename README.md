# Introduction to data 

While many public datasets (on Kaggle and the like) provide Apple App Store data, there are not many counterpart datasets available for Google Play Store apps anywhere on the web.On digging deeper, it can be found out that iTunes App Store page deploys a nicely indexed appendix-like structure to allow for simple and easy web scraping. On the other hand, Google Play Store uses sophisticated modern-day techniques (like dynamic page load) using JQuery making scraping more challenging.

The Play Store apps data has enormous potential to drive app-making businesses to success. Actionable insights can be drawn for developers to work on and capture the Android market!

Each app (row) has values for catergory, rating, reviews, size, installs, price, rated, last updated, and version.

Source :[link](https://www.kaggle.com/lava18/google-play-store-apps)

# Google-Play Store Analysis

This project focuses on the analysis of the Play Store data set in Kaggle.

We want to use the data to analyze consumer trends and determine which type of apps are the most popular and profitable. 

# Important Pre-requisites

1. Python 3.7
2. Pip (usually installed by default with Python 3)
3. A Kaggle account ([More Information can be found here](https://www.kaggle.com/), and details about the configuration of the Kaggle certificates can be found in the _Kaggle Notes_ section contained within this README.md file ) 


# Installation 

There are 2 recommended ways to set up your environment to run the scripts, both of which will be described here.
We are also assuming that you have already downloaded, or cloned, the repository, and have moved into the _Project_ directory.

## Installation Method 1

1. Download the project(and uncompress the file if you downloaded a zip version of it), and move into the Project folder. Here is a quick example of what this might look like:
```bash
git clone https://gitlab.com/cmsc6950/team1/google-play-store-analysis.git
cd Project
```
2. Install virtualenv to be able to create separate working python environments. This is to prevent damaging any other projects that you may have on your computer
```bash 
pip install virtualenv 
```
3. Create and initiate a new virtual environment
```bash 
virtualenv -p python3 .
source ./bin/activate
```
4. Install the required libraries
```bash
pip install -r requirements.txt
```
5. At this point, you are ready to start enjoying the scripts. To deactivate the virtual environment, you just need to run the command `deactivate` from the terminal

## Installation Method 2 (With the makefile)

1. Download the project(and uncompress the file if you downloaded a zip version of it), and move into the Project folder. Here is a quick example of what this might look like:
```bash
git clone https://gitlab.com/cmsc6950/team1/google-play-store-analysis.git
cd Project
```
2. Create a virtual environment with anaconda and activate the new environment
```bash
conda create -n NewEnv python=3.7
conda activate NewEnv
```
3. Run the make command. This should be the last step, but if this command generates an error due to download problems, skip to the next step
```
make
```
4. OPTIONAL if step 3 fails, the make file includes an option to use our back-up version of the kaggle dataset (OrigData) 
```bash
make bashrun
```

# Short Description

All the scripts are inside the Project folder. Within the Folder, you will find an empty _Data_ folder, which is where the processed data will be stored. 
The _OrigData_ contains the data found in the Kaggle repository as a backup, should you not be able to directly download the repository from Kaggle, or should the data itself be removed from the Kaggle servers. 
The following is a list of the scripts included in this project with a brief description about their functionality. It is also recommended that you ran the scripts in the order in which they are listed the first you work with this repository.

1. download.py - This script downloads the necessary data. Please read the  *”Important Notes”* section to find out more about certain pre-requisites
2. cleandata.py - After the data has been downloaded, and unzipped, this script will get rid of unnecessary fields, filter out erronous data points, and fill empty cells with the ‘NA’ keyword
3. histograms.py - This script provides a preview of the data. It graphs each of the attributes against the number of apps. 

All of the scripts have a _-h_ or _—-help_ option, which provides more details about their syntax, and additional options.


# Kaggle Notes
To be able to download the datasets from Kaggle, it is recommended to use the Kaggle API, which can be found [link](https://github.com/Kaggle/kaggle-api)
Installing the Kaggle API is as simple as
`pip install kaggle`
Or you can download the source code directly from the aboved mentioned link. 

After the kaggle module has been downloaded, you need to set up a kaggle account, and download your credentials to be able to download datasets.  The steps required to download the credentials can be found in the [Kaggle's API github](https://github.com/Kaggle/kaggle-api). However, we have copied the instructions in further sections of this readme file. 

The command to download our data set after you configure your credentials is `kaggle datasets download lava18/google-play-store-apps`, which will download the zip file. 

The following sections were copied directly from the Kaggle's API README.md file.

#### API credentials

To use the Kaggle API, sign up for a Kaggle account at https://www.kaggle.com. Then go to the 'Account' tab of your user profile (`https://www.kaggle.com/<username>/account`) and select 'Create API Token'. This will trigger the download of `kaggle.json`, a file containing your API credentials. Place this file in the location `~/.kaggle/kaggle.json` (on Windows in the location `C:\Users\<Windows-username>\.kaggle\kaggle.json` - you can check the exact location, sans drive, with `echo %HOMEPATH%`). You can define a shell environment variable `KAGGLE_CONFIG_DIR` to change this location to `$KAGGLE_CONFIG_DIR/kaggle.json` (on Windows it will be `%KAGGLE_CONFIG_DIR%\kaggle.json`).

For your security, ensure that other users of your computer do not have read access to your credentials. On Unix-based systems you can do this with the following command: 

`chmod 600 ~/.kaggle/kaggle.json`

You can also choose to export your Kaggle username and token to the environment:

```bash
export KAGGLE_USERNAME=datadinosaur
export KAGGLE_KEY=xxxxxxxxxxxxxx
```
In addition, you can export any other configuration value that normally would be in
the `$HOME/.kaggle/kaggle.json` in the format 'KAGGLE_<VARIABLE>' (note uppercase).  
For example, if the file had the variable "proxy" you would export `KAGGLE_PROXY`
and it would be discovered by the client.


#### Commands

The command line tool supports the following commands:

``` 
kaggle competitions {list, files, download, submit, submissions, leaderboard}
kaggle datasets {list, files, download, create, version, init}
kaggle kernels {list, init, push, pull, output, status}
kaggle config {view, set, unset}
```

See more details below for using each of these commands.

##### Download dataset files

```
usage: kaggle datasets download [-h] [-f FILE_NAME] [-p PATH] [-w] [--unzip]
                                [-o] [-q]
                                [dataset]

optional arguments:
  -h, --help            show this help message and exit
  dataset               Dataset URL suffix in format <owner>/<dataset-name> (use "kaggle datasets list" to show options)
  -f FILE_NAME, --file FILE_NAME
                        File name, all files downloaded if not provided
                        (use "kaggle datasets files -d <dataset>" to show options)
  -p PATH, --path PATH  Folder where file(s) will be downloaded, defaults to current working directory
  -w, --wp              Download files to current working path
  --unzip               Unzip the downloaded file. Will delete the zip file when completed.
  -o, --force           Skip check whether local version of file is up to date, force file download
  -q, --quiet           Suppress printing information about the upload/download progress
```


Examples:

`kaggle datasets download zillow/zecon`

`kaggle datasets download zillow/zecon -f State\_time\_series.csv`

Please note that BigQuery datasets cannot be downloaded.

