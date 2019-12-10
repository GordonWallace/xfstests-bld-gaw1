import git
from git import Repo
import time

repo = Repo("gce-xfstests-test-repo")
assert not repo.bare
g = git.cmd.Git("gce-xfstests-test-repo")

origin = repo.remotes.origin

while(1):
    local_commit = repo.commit()
    remote_commit = origin.fetch()[0].commit
    if local_commit.hexsha == remote_commit.hexsha:
        print "Repo is up to date with remote."
    else:
        print "Repo is behind remote. Now pulling updates."
        g.pull()
    time.sleep(5)
