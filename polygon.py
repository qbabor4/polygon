def get_area(listOfPeaks):
    area = 0.
    numOfPeaks = len(listOfPeaks)
    for i in xrange(numOfPeaks):
        area += listOfPeaks[i][0] * (listOfPeaks[(i-1)%numOfPeaks][1] - listOfPeaks[(i+1)%numOfPeaks][1])
    area = abs(area)*(1./2.)

    return area
