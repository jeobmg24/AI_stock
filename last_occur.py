def find_peak_date(prices, dates, left, right):
    # Base case
    if left == right:
        return dates[left]
    
    if right - left == 1:
        if prices[left] > prices[right]:
            return dates[left]
        return dates[right]
    
    mid = (left + right) // 2
    
    if prices[mid] > prices[mid-1] and prices[mid] > prices[mid+1]:
        return dates[mid]
    
    if prices[mid] < prices[mid-1]:
        return find_peak_date(prices, dates, left, mid-1)

    return find_peak_date(prices, dates, mid+1, right)

def find_highest_price_date(prices, dates):
    if len(prices) < 2:
        return dates[0] if prices else None
    return find_peak_date(prices, dates, 0, len(prices)-1)