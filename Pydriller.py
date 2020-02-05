from pydriller import RepositoryMining
for commit in RepositoryMining('https://github.com/jovotech/jovo-framework.git').traverse_commits(): print('Hash {}, author {}'.format(commit.hash, commit.author.name))


