from api_handler import APIHandler

def main():
    api_handler = APIHandler("http://localhost:3002/api")
    output = api_handler.call_course_info_api()
    print(output)

if __name__ == "__main__":
    main()
