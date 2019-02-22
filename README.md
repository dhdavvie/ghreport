gh-report — review your daily activity on GitHub 
![License info](https://img.shields.io/github/license/mashape/apistatus.svg?style=flat-square)
================================================

gh-report is a small command line tools that shows your daily activity on GitHub. It Works via GitHub API.

## How to use

### Install

Package(s) will be later, sorry. For now, you may follow this steps:
1. Clone repository and change dir `git clone https://github.com/digitalduke/gh-report.git && cd gh-report`
1. Install Python3 `sudo apt install python3 python3-pip`
1. Create and activate environment `virtualenv -p python3 env && source env/bin/activate`
1. Install dependencies `pip -r requirements.txt`

### Setup
1. Go to your profile [settings](https://github.com/settings/tokens) and create [new access token](https://github.com/settings/tokens/new) with repo scope.

2. Then store this token into the configuration file. The configuration file will be created in your profile directory.
```bash
$ python3 gh-report.py --store-token <token>
```

3. And then add repositories names, for which you will need reports, into the configuration file.
```bash
$ python3 gh-report.py --store-repository <username/repository>
```

### Run
Show daily activity for today:
```bash
$ python3 gh-report.py
```

Show activity for the specific date:
```
$ python3 gh-report.py --date 2018-11-25
```

## How to contribute
Want to make a suggestion? This project is open source. Help to improve it.

Feel free to open a new [issues](https://github.com/digitalduke/gh-report/issues/) or send pull requests.

## How to support
Star this repository or [buy me a coffee](https://www.buymeacoffee.com/digitalduke) ;)
