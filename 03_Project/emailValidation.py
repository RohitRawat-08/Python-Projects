import requests

def emailValidate():

    key = "ema_live_CiDbIZBOPYEmyzpzrvwonS7PRYo9bqGKavYMQmXu"
    email = input("\nEnter Email to validate :")
    url = f"https://api.emailvalidation.io/v1/info?apikey={key}&email={email}"

    response = requests.get(url)
    data=response.json()
   
    return data

def main():
    try:
        result = emailValidate()
        print()
        for i in result :
            if result[i] not in (None,"",False,True):
                print(f"{i}:{result[i]}")
            print()

    except BaseException as e:
        print(e)


if __name__ == "__main__":
    main()
















