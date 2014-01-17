from  pygit2 import Repository
from pygit2 import GIT_SORT_TIME
import sys
def main():
   #processGitDiff(2)
   processGitDiff(sys.maxsize)
def processGitDiff(commitsNum):
  counter = commitsNum;
  repositoryName = "../git-repos/postgres"
  repo = Repository(repositoryName +"/"+ ".git")
  childCommitNumber = ""
  for commit in repo.walk(repo.head.target, GIT_SORT_TIME):
    counter-=1;
    if counter<0:
      break
    currentCommitNumber = commit.oid.hex
    if(childCommitNumber!=""):
        diff = repo.diff(currentCommitNumber, childCommitNumber)
        fileChanges = 0;
        for p in diff:
          print(p.old_file_path)
              #print(p.old_oid)
          print(p.new_file_path)
              #print(p.new_oid)
          #print(p.additions)
          addLines = 0;
          deleteLines = 0;
          for hunk in p.hunks:
                  #print(hunk.old_start)
                  #print(hunk.old_lines)
                  #print(hunk.new_start)
                  #print(hunk.new_lines)
            for line in hunk.lines:
              if line[0] == "+":
                addLines+=1;
              if line[0] == "-":
                deleteLines+=1;
          print("lines added" + str(addLines));
          print("lines deleted" + str(deleteLines));
        fileChanges+=1
        print("file changed" + str(fileChanges));
    childCommitNumber = commit.oid.hex;
    #print(currentCommitNumber)
    #print(commit.message)
    #print(commit.author.name)

if __name__=="__main__":
    main()