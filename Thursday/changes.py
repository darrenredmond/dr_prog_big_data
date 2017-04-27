
# open the file - and read all of the lines.
changes_file = 'changes_python.txt'
# use strip to strip out spaces and trim the line.

#my_file = open(changes_file, 'r')
#data = my_file.readlines()

data = [line.strip() for line in open(changes_file, 'r')]

print len(data)

sep = 72*'-'

class Commit:

    def __init__(self, revision=None, author=None, date=None,
            comment_line_length=None, changes=None, comment=None):
        self.revision = revision
        self.author = author
        self.date = date
        self.comment_line_length = comment_line_length
        self.changes = changes
        self.comment = comment

a_commit = Commit('r1551925', 'Thomas', '2015/11/27', 1,
        comment='Renamed folder to the correct name')

print a_commit.author
print a_commit.comment
        
index = 0
current_commit = None
commits = []

while True:
    try:
        details = data[index + 1].split('|')
        current_commit = {}
        current_commit['revision'] = details[0].strip()
        current_commit['author'] = details[1].strip()
        current_commit['date'] = details[2].strip()
        current_commit['comment_line_length'] = int(details[3].strip().split(' ')[0])

        current_commit['changes'] = data[index+2:data.index('',index+1)]

        index = data.index(sep, index+1)

        current_commit['comment'] = data[index - current_commit['comment_line_length'] : index]
        print current_commit['comment']

        commits.append(current_commit)
    except IndexError:
        break

print len(commits)
        
commits.reverse()



        
        
        
        
        
        
        
