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

    n = len(points)
    res = []
    i = 0                    # pointer into points

    for a, b in bins:
        # move i to the first point >= a
        while i < n and points[i] < a:
            i += 1

        j = i                # j will advance to first point >= b
        while j < n and points[j] < b:
            j += 1

        count = j - i
        width = b - a
        # guard against empty dataset or zero-width bins (shouldn't happen per spec)
        density = (count / (n * width)) if (n > 0 and width > 0) else 0.0
        res.append(density)

        i = j  # next bin starts at b; reuse work already done

    return res