
from match import Match

def get_criteria(match: Match, criteria: str):
    if criteria == 'kda':
        return match.calculate_kda()
    elif criteria == 'champion':
        return match.champion
    return match.date  

def _merge(left: list[Match], right: list[Match], criteria: str) -> list[Match]:
    result = []
    i_left, i_right = 0, 0
    while i_left < len(left) and i_right < len(right):
        left_value = get_criteria(left[i_left], criteria)
        right_value = get_criteria(right[i_right], criteria)
        
        if criteria in ('kda', 'date'):
            if left_value >= right_value:
                result.append(left[i_left])
                i_left += 1
            else:
                result.append(right[i_right])
                i_right += 1
        else:
            if left_value <= right_value:
                result.append(left[i_left])
                i_left += 1
            else:
                result.append(right[i_right])
                i_right += 1
                
    result.extend(left[i_left:])
    result.extend(right[i_right:])
    return result

def merge_sort(match_list: list[Match], criteria='date') -> list[Match]:
    if len(match_list) <= 1:
        return match_list

    middle = len(match_list) // 2
    left_half = merge_sort(match_list[:middle], criteria)
    right_half = merge_sort(match_list[middle:], criteria)
    return _merge(left_half, right_half, criteria)