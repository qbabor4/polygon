#-*- coding: utf-8 -*-

def _get_data():
    peaks = []
    i = 0
    numOfPeaks = int(input("Number of peaks\n>"))
    while True:
        if numOfPeaks < 0:
            print "Wrong number of peaks"
            numOfPeaks = int(input("Number of peaks\n>"))
        else:
            break
        
    print "Type x coordinate of the peak. Click enter. \nThen in the next input type y coordinate of the peak and click enter."
    while i < numOfPeaks:
        print "Type coordinates of {:d} peak".format(i+1)
        try:
            x = float(input("x > "))
            y = float(input("y > "))
            peaks.append( [x,y] )
            i += 1
        except:
            print "Wrong type of input"
            
    return peaks
    
def get_area(listOfPeaks):
    area = 0.
    numOfPeaks = len(listOfPeaks)
    for i in xrange(numOfPeaks):
        area += listOfPeaks[i][0] * (listOfPeaks[(i-1)%numOfPeaks][1] - listOfPeaks[(i+1)%numOfPeaks][1])
    area = abs(area)*(1./2.)

    return area

if __name__ == "__main__":
    peaks = _get_data()
    print "Area: ",get_area(peaks)
