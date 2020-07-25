#
#  Discover the structure of a file format by splitting a set of examples into sets at points where they vary
#
#  Expect a list of dicts with a key of filename and a value of the content of the file
#

def split_decision(contents={}, index=0):
    #
    # drop any files that only have 1 character left, they've finished
    lastchoice = index
    finalists = dict([(f,v) for (f,v) in contents.items() if len(v[index:]) <= 1])
    if len(finalists)>0: print(f"ending at {index}: {len(finalists)}")
    #
    candidates = dict([(f,v) for (f,v) in contents.items() if len(v[index:])>1])
    if len(candidates) == 0: return
    #
    index = index + 1
    nextchars = set(v[index:index+1] for (f,v) in candidates.items())
    choices = len(nextchars)
    while choices ==1:
        index = index + 1
        nextchars = set(v[index:index + 1] for (f, v) in candidates.items())
        choices = len(nextchars)
    print(f"index: {index}, choices: {len(nextchars)}")
    split_decision(contents=candidates, index=index)