from api_handler import APIHandler

def main():
    api_handler = APIHandler("http://localhost:3002/api")
    output = api_handler.call_specific_api()
    print(output)

if __name__ == "__main__":
    main()
