import requests

def fetch_console_output(job_name, build_number):
    base_url = 'http://65.2.74.65:8080/'
    api_url = f'{base_url}job/{job_name}/{build_number}/consoleText'

    try:
        response = requests.get(api_url, auth=('mohammedasif', 'Rmn@73383271'))

        if response.status_code == 200:
            return response.text
        else:
            print(f"Failed to fetch console output. Status code: {response.status_code}")
            return None

    except requests.exceptions.RequestException as e:
        print(f"Failed to fetch console output: {str(e)}")
        return None

# Example usage:
if __name__ == "__main__":
    job_name = 'monitoring'
    build_number = '1'

    console_output = fetch_console_output(job_name, build_number)
    if console_output:
        print(f"Console output for job '{job_name}' build #{build_number}:")
        print(console_output)
