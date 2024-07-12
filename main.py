import requests

def read_queries(file_path):
    queries = []
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            query, title = line.strip().split(' - ')
            queries.append((query, title))
    return queries

def send_request(query):
    url = f"http://62.84.112.172:5003/items/search?title={query}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def find_service_index(data, title):
    if data and 'content' in data:
        for index, service in enumerate(data['content'], start=1):
            if repr(service['title']).strip().replace('\'', '') == title.strip():
                return index
    return 0

def main(file_path):
    queries = read_queries(file_path)
    for query, title in queries:
        data = send_request(query)
        index = find_service_index(data, title)
        print(f"{index} - ({title}) {query}")

if __name__ == "__main__":
    file_path = "queries.txt"
    main(file_path)