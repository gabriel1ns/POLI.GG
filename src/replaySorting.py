# decider of the criteria used in sort
def get_sort_value(match, criterion):
    if criterion == 'kda':
        return match.calculate_kda()
    elif criterion == 'champion':
        return match.champion
    else:
        return match.date

# method to sort within the category
def merge(left, right, criterion):
    result = []
    i = 0
    j = 0
    
    while i < len(left) and j < len(right):
        left_val = get_sort_value(left[i], criterion)
        right_val = get_sort_value(right[j], criterion)
        
        if criterion in ('kda', 'date'):
            if left_val >= right_val:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        else:
            if left_val <= right_val:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
    
    while i < len(left):
        result.append(left[i])
        i += 1
    
    while j < len(right):
        result.append(right[j])
        j += 1
    
    return result

def merge_sort(matches, criterion='date'):
    if len(matches) <= 1:
        return matches

    mid = len(matches) // 2
    left = merge_sort(matches[:mid], criterion)
    right = merge_sort(matches[mid:], criterion)

    return merge(left, right, criterion)