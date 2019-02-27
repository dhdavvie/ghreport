ghreport - review your activity on GitHub 
![License info](https://img.shields.io/github/license/mashape/apistatus.svg?style=flat-square)
================================================

ghreport is a small CLI tool that shows your activity on GitHub. It works via GitHub API.

## How to use

### Install

`pip install -i https://test.pypi.org/simple/ ghreport`

### Setup
1. Go to your profile [settings](https://github.com/settings/tokens) and create [new access token](https://github.com/settings/tokens/new) with repo scope.

2. Then store this token into the configuration file. The configuration file will be created in your profile directory.
```bash
$ ghreport --store-token <token>
```

3. And then add repositories names, for which you will need reports, into the configuration file.
```bash
$ ghreport --store-repository <username/repository>
```

### Run
Show activity for today:
```bash
$ ghreport
```

Show activity for the specific date:
```
$ ghreport --date 2019-02-27
```

## How to contribute
Want to make a suggestion? This project is open source. Help to improve it.

Feel free to open a new [issues](https://github.com/digitalduke/ghreport/issues/) or send pull requests.

## How to support
Star this repository or [buy me a coffee](https://www.buymeacoffee.com/digitalduke) ;)
