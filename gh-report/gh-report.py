import argparse
import json
import os
from datetime import date, datetime, timedelta

from dateutil.parser import parse
from github import Github, BadCredentialsException

CONFIGURATION_FILENAME = 'gh-report'

parser = argparse.ArgumentParser(
    description="Review your daily activity on GitHub.",
    epilog="More information at https://https://github.com/digitalduke/gh-report"
)
parser.add_argument(
    '--version',
    action='version',
    version='gh-report 1.0.0'
)
parser.add_argument(
    '--date',
    action='store',
    default='today',
    metavar="YYYY-MM-DD",
    type=str,
    dest='date',
    help='date in ISO 8601 format (for example: 2019-10-16), today if omitted'
)
parser.add_argument(
    '--store-token',
    action='store',
    default=None,
    metavar="TOKEN",
    type=str,
    dest='store_token',
    help='save GitHub access token into configuration file'
)
parser.add_argument(
    '--remove-token',
    action='store_true',
    dest='remove_token',
    help='remove GitHub access token from configuration file'
)
parser.add_argument(
    '--store-repository',
    action='store',
    default=None,
    metavar="REPOSITORY",
    type=str,
    dest='store_repository',
    help='save repository name into configuration file'
)
parser.add_argument(
    '--remove-repository',
    action='store',
    default=None,
    metavar="REPOSITORY",
    type=str,
    dest='remove_repository',
    help='remove repository name from configuration file'
)
parser.add_argument(
    '--list-repositories',
    action='store_true',
    dest='list_repositories',
    help='list repositories stored in configuration file'
)


def get_config_path():
    if os.environ.get('XDG_CONFIG_HOME') is not None:
        config_path = os.environ.get('XDG_CONFIG_HOME')
    else:
        config_path = os.path.join(
            os.environ.get('HOME', ''),
            '.config'
        )
    return config_path


def get_config_file_full_path():
    return os.path.join(get_config_path(), CONFIGURATION_FILENAME)


def get_options():
    options = {}
    try:
        with open(get_config_file_full_path()) as config_file:
            options = json.load(config_file)
    except FileNotFoundError:
        print("Error while reading configuration: file does not exist.")
    return options


def save_options(options):
    os.makedirs(get_config_path(), exist_ok=True)

    with open(get_config_file_full_path(), 'w') as config_file:
        json.dump(options, config_file)


def run():
    args = parser.parse_args()
    options = get_options()

    if args.store_token:
        options.update(token=args.store_token)
        save_options(options)
        print("Token successfully stored in configuration file.")
    elif args.remove_token:
        options.update(token="")
        save_options(options)
        print("Token successfully removed from configuration file.")
    elif args.store_repository:
        repositories = list(options.get('repositories', ''))
        new_repo = args.store_repository
        if new_repo not in repositories:
            repositories.append(new_repo)
            options.update(repositories=repositories)
            save_options(options)
            print("Repository %s successfully stored in configuration." % new_repo)
        else:
            print("Repository %s already in configuration." % new_repo)
    elif args.remove_repository:
        repositories = list(options.get('repositories', ''))
        repo = args.remove_repository
        if repo in repositories:
            repositories.remove(repo)
            options.update(repositories=repositories)
            save_options(options)
            print("Repository %s successfully removed from configuration." % repo)
        else:
            print("Repository %s not in configuration." % repo)
    elif args.list_repositories:
        repositories = list(options.get('repositories', ''))
        for repo in repositories:
            print(repo)
    else:
        if args.date == 'today':
            date_since = date.today()
        else:
            date_since = parse(args.date)
        date_since = datetime.combine(date_since, datetime.min.time())
        date_until = datetime.combine(date_since.date() + timedelta(days=1), datetime.min.time())

        github = Github(options.get('token', ''))
        user = github.get_user()
        repositories = list(options.get('repositories', ''))

        for repository in repositories:
            try:
                repo = github.get_repo(repository)
            except (Exception, BadCredentialsException) as error:
                print("Can't get repo %s" % repository)

            try:
                closed_issues = user.get_issues(state="closed", since=date_since)
                print("List of daily closed issues")
                for issue in closed_issues:
                    if date_since <= issue.closed_at <= date_until:
                        print(issue.number, issue.html_url, issue.title)
                print()
            except (Exception, BadCredentialsException) as error:
                print("Can't get list of closed issues.")

            try:
                commits = repo.get_commits(since=date_since, author=user)
                print("List of daily commits in repo \"%s\" in PR which already closed" % repository)
                for commit in commits:
                    print(commit.sha[:7], commit.html_url, commit.commit.message)
                print()
            except (Exception, BadCredentialsException) as error:
                print("Can't get list of commits in PR which already closed.")

            try:
                pulls = repo.get_pulls(state="open", base="master")
                if pulls:
                    print("List of daily commits in repo \"%s\" in PR which don't closed" % repository)

                for pr in pulls:
                    commits = pr.get_commits()
                    print_pr_number = True

                    for commit in commits:

                        if not commit.committer.login == user.login:
                            continue

                        if date_since <= commit.commit.author.date <= date_until:
                            if print_pr_number:
                                print("PR#%s %s %s" % (pr.number, pr.html_url, pr.title))
                                print_pr_number = False

                            print(commit.sha[:7], commit.html_url, commit.commit.message)

            except (Exception, BadCredentialsException) as error:
                print("Can't get list of commits in opened PR.")

        print("\r\nDone.")


if __name__ == "__main__":
    run()
