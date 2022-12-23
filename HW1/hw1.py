# Kate Radford 11537868 CptS 315 HW 1
import itertools
import numpy as np

# line.split() for line in file
def openFile():
    file = open("browsing-data.txt", "r")
    # file = open("browsingdata_50baskets.txt", "r")
    array = np.array([line.split() for line in file])
    print("reading from file...")
    file.close()
    return array

def firstScan(arr):
    C1 = dict()
    support = 100
    global L1
    L1 = dict()
    print("executing first apriori scan...")

    # count frequencies
    for line in arr:
        for element in line:
            if element in C1.keys():
                C1[element] += 1
            else:
                C1[element] = 1

    for key, value in C1.items():
        if value >= support:
            L1[key] = value

    # for x in C1:
    #     print(x, ":", C1[x])
    #
    # for x in L1:
    #     print(x, ":", L1[x])

    # print("L1 size: ", len(L1))

def confidencePairs(pairs):
    global confidence_pairs
    confidence_pairs = dict()
    print("calculating confidence for pairs...")

    for pair in pairs:
        xAlone = 0
        xWithY = 0
        yAlone = 0
        yWithX = 0
        for line in dataArray:
            # X -> Y
            if pair[0] in line:
                if pair[1] in line:
                    xWithY += 1
                else:
                    xAlone += 1
            # Y -> X
            if pair[1] in line:
                if pair[0] in line:
                    yWithX += 1
                else:
                    yAlone += 1
        confidence_pairs[pair] = xWithY/xAlone
        confidence_pairs[(pair[1],pair[0])] = yWithX/yAlone

    return sorted(confidence_pairs.items(), key = lambda x: x[1], reverse = True)


def confidenceTriples(triples):
    global confidence_triples
    confidence_triples = dict()
    print("calculating confidence for triples...")

    for triple in triples:
        xyAlone = 0
        xyWithZ = 0
        xzAlone = 0
        xzWithY = 0
        yzAlone = 0
        yzWithX = 0
        for line in dataArray:
            #{X,Y}-> Z
            if (triple[0] in line) and (triple[1] in line):
                if triple[2] in line:
                    xyWithZ += 1
                else:
                    xyAlone += 1
            #{X,Z}-> Y
            if (triple[0] in line) and (triple[2] in line):
                if triple[1] in line:
                    xzWithY += 1
                else:
                    xzAlone += 1
            #{Y,Z}-> X
            if (triple[1] in line) and (triple[2] in line):
                if triple[0] in line:
                    yzWithX += 1
                else:
                    yzAlone += 1

        if xyAlone != 0:
            confidence_triples[triple] = xyWithZ/xyAlone
        else:
            confidence_triples[triple] = 0
        if xzAlone != 0:
            confidence_triples[(triple[0], triple[2], triple[1])] = xzWithY/xzAlone
        else:
            confidence_triples[(triple[0], triple[2], triple[1])] = 0
        if yzAlone != 0:
            confidence_triples[(triple[1], triple[2], triple[0])] = yzWithX/yzAlone
        else:
            confidence_triples[(triple[1], triple[2], triple[0])] = 0
        print(confidence_triples)

    return sorted(confidence_triples.items(), key = lambda x: x[1], reverse = True)


def secondScan():
    support = 100
    global C2p
    C2p = dict()
    global C2t
    C2t = dict()

    itemList = [key for key in L1.keys()]

    itemPairs = itertools.combinations(itemList, 2)
    confidencePairs(itemPairs)

    for line in dataArray:
        #print("Line: ", line)
        for pair in itemPairs:
            if (pair[0] in line) and (pair[1] in line):
                # print(pair, "is in ", line)
                if pair in C2p.keys():
                    x = C2p[pair]
                    C2p[pair] = x + 1
                else:
                    C2p[pair] = 1

    print("C2 Pairs")
    for x in C2p:
        print(x, ":", C2p[x])

    itemTriples = itertools.combinations(itemList, 3)
    for line in dataArray:
        for triple in itemTriples:
            if (triple[0] in line) and (triple[1] in line) and (triple[2] in line):
                # print(triple, " in ", line)
                if triple in C2t.keys():
                    x = C2t[triple]
                    C2t[triple] = x + 1
                else:
                    C2t[triple] = 1

    print("C2 Triples")
    for x in C2t:
        print(x, ":", C2t[x])

def writeFile(cp, ct):
    pairsOutput = cp[:5]
    triplesOutput = ct[:5]
    print("printing results to output.txt...")

    outfile = open("output.txt", "w")
    outfile.write("OUTPUT A\n")
    for pair in pairsOutput:
        line = ' '.join(str(x) for x in pair)
        outfile.write(line + '\n')
    outfile.write("OUTPUT B\n")
    for triple in triplesOutput:
        line = ' '.join(str(x) for x in triple)
        outfile.write(line + '\n')
    outfile.close()

if __name__ == "__main__":
    global dataArray
    dataArray = openFile()
    firstScan(dataArray)
    itemList = [key for key in L1.keys()]
    itemPairs = itertools.combinations(itemList, 2)
    itemTriples = itertools.combinations(itemList, 3)
    sortedCPairs = confidencePairs(itemPairs)
    sortedTPairs = confidenceTriples(itemTriples)
    writeFile(sortedCPairs, sortedTPairs)
    #secondScan()
