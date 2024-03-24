import re

def compute_importance(pages_file, N):
    
    pages = {}
    links = {}
    with open(pages_file, 'r') as f:
        for line in f:
            match = re.match(r'(URL\d+), (0\.\d+): (.*)', line)
            url = match.group(1)
            init_importance = float(match.group(2))
            text = match.group(3)
            pages[url] = (init_importance, text)
            links[url] = set(re.findall(r'URL\d+', text))

    
    overall_importance = {url: 0 for url in pages.keys()}

    
    for url, referencing_pages in links.items():
        for referenced_page in referencing_pages:
            overall_importance[referenced_page] += pages[url][0] / len(referencing_pages)

    
    sorted_pages = sorted(overall_importance.items(), key=lambda x: x[1], reverse=True)
    return sorted_pages[:N]

pages_file = 'pages.txt'
N = int(input())

result = compute_importance(pages_file, N)
print(result)

for i, (url, importance) in enumerate(result):
    print(f'{i+1}. {url}: {importance}')






