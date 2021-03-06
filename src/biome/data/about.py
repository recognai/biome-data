from datetime import datetime

# See https://www.python.org/dev/peps/pep-0440/ for version numbering
__version__ = "0.2.0"


def package_version(version: str):
    """Generates a proper package version from git repository info"""

    def get_commit_hash(repository: git.Git) -> str:
        """
        Fetch current commit hash from configured git repository. The working folder should
        be part of a already git repository

        """
        return repository.log("--pretty=format:'%h'", "-n 1").replace("'", "")

    def get_first_tag_for_commit(repository: git.Git, commit_hash: str) -> str:
        """ Return tags related to current commit """

        tags = (
            repository.tag("--contains", commit_hash)
            if commit_hash
            else repository.tag("--contains")
        ).split("\n")
        return tags[0]

    try:
        repo = git.Git()
    except Exception:  # pylint: disable=broad-except
        return version

    commit = get_commit_hash(repo)
    repo_tag = get_first_tag_for_commit(repo, commit)
    today = datetime.today().strftime("%Y%m%d%H%M%S")

    return repo_tag if repo_tag else f"{version}.{today}+{commit}"


try:
    import git  # pylint: disable=import-error
except ImportError:
    pass
else:
    __version__ = package_version(__version__)
