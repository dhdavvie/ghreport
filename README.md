<h1 align="center">
  gh-report
</h1>

<h4 align="center">
  Review your daily activity on GitHub.
</h4>

<p align="center">
  <img alt="License MIT" src="https://img.shields.io/github/license/mashape/apistatus.svg?style=flat-square">
  <img alt="OS independent" src="https://img.shields.io/badge/platform-independent-yellow.svg?style=flat-square">
</p>

### What is it?

This is a small script that shows your daily activity on GitHub. Works via GitHub API.

### How to use

#### Install

Packages will be coming soon, sorry. For now, you may just clone this repository. 

#### Setup
1. Go to your profile [settings](https://github.com/settings/tokens) and create [new access token](https://github.com/settings/tokens/new) with repo scope.

2. Then store this token into the configuration file. The configuration file will be created in your profile directory.
```bash
$ python3 gh-report.py --store-token <token>
```

3. And then add repositories names, for which you will need reports, into the configuration file.
```bash
$ python3 gh-report.py --store-repository <username/repository>
```

#### Run
Show daily activity for today:
```bash
$ python3 gh-report.py
```

Show activity for the specific date:
```
$ python3 gh-report.py --date 2018-11-25
```

### How to contribute
Want to make a suggestion? This project is open source. Help to improve it.

Feel free to open a new [issues](https://github.com/digitalduke/gh-report/issues/) or send pull requests.

### How to support
