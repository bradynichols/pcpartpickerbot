import nltk
def find_nearest(input, datalist):
    indices = []
    for string in datalist:
        indices.append(nltk.edit_distance(input, string))
    cindex = indices.index(min(indices)) #lowest index
    closest = datalist[cindex]
    return closest
