def histogram(points, bins):
    """
    points: a sorted Python list of n numbers, in order from smallest to largest
    
    bins: a Python list of k tuples, each of the form (a,b), where a and b are the 
    start and end of a bin, respectively. You can assume that the bins are also sorted
    from left to right, and the endpoint of one bin is the start of the next. For example, 
    the list [(0,4), (4,8), (8,12)] denotes the bins [0,4), [4,8), [8,12). Each bin 
    includes its start, but not its end.

    returns: a Python list which contains the histogram's density within each bin. So if
    bins has k elements, your function should return a list of k numbers.
    """

    # density = number of points in bin / number of points * bin width
    # aim for O(n) time complexity

    densities = []
    for bin in bins:
        densities.append(0)

    n = len(points)

    bin_idx = 0
    point_idx = 0
    while point_idx < n:
        if points[point_idx] < bins[bin_idx][0]:
            point_idx += 1
        else:
            densities[bin_idx] += 1 / (n * (bins[bin_idx][1] - bins[bin_idx][0])) 
            point_idx += 1
    return densities    # O(n) time complexity