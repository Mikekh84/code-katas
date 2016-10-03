from forbes_json import FORBES_LIST as flist

def get_oldest_youngest(lst):
    """Get oldest under 80 and youngest about zero."""
    current_oldest = {'age': 0}
    current_youngest = {'age': 80}
    
    for item in lst:
        if item['age'] > current_oldest['age'] and item['age'] < 80:
            current_oldest = item
        if item['age'] < current_youngest['age'] and item['age'] > 0:
            current_youngest = item
    return 'Oldest: {oname}, {oworth}, {oindust} || Youngest: {yname}, {yworth}, {yindust}'.format(
        oname=current_oldest['name'],
        oworth=current_oldest['net_worth (USD)'],
        oindust=current_oldest['source'],
        yname=current_youngest['name'],
        yworth=current_youngest['net_worth (USD)'],
        yindust=current_youngest['source'],
    )

if __name__ == '__main__':
    print(get_oldest_youngest(flist))