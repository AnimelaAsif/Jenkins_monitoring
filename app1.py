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

def save_to_file(console_output, filename):
    try:
        with open(filename, 'w') as file:
            file.write(console_output)
        print(f"Console output saved to {filename}")
    except IOError as e:
        print(f"Failed to write to file: {str(e)}")

# Example usage:
if __name__ == "__main__":
    job_name = 'monitoring'
    build_number = '1'
    # output_file = 'f"{build_number}.log'

    console_output = fetch_console_output(job_name, build_number)
    if console_output:
        save_to_file(console_output, f"{build_number}.log)
