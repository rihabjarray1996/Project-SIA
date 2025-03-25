def fetch_data(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad status codes
        return response.text  # Return the content as a string
    except requests.exceptions.RequestException as e:
        print(f"Failed to fetch data: {e}")
        return None
