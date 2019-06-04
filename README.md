# Google-Play Store Analysis

This project focuses on the analysis of the Play Store data set in Kaggle obtained from the following [link](https://www.kaggle.com/lava18/google-play-store-apps)

We want to use the data to analyze consumer trends and determine which apps are the most popular and profitable. 



# Important Notes
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

