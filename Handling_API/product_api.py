import requests

def Fetch_product_api():
    
    url= ("https://api.freeapi.app/api/v1/public/randomproducts")
    response=requests.get(url)
    data = response.json()
    
    if data.get("success"):
        # products = data["data"]["data"]   # list of products
        # first_product = products[0]        # pehla product
        # title = first_product["title"]
        # return title
        return data["data"]["data"]
    else:
        raise Exception ("Failed to fecth user data")
       
         
def main():
    try:
        products = Fetch_product_api()
        # print(f"title: {title}")
        for index, product in enumerate(products, start=1):
            print("-"*30)
            print(f"\nProduct {index}")
            print(f"ID :{product['id']}")
            print(f"Title :{product['title']}")
            print(f"Description :{product['description']}")
            print(f"Price :{product['price']}")
            print(f"Brand :{product['brand']}")
            
    
    except Exception as e:
        print(str(e))
    
if __name__ == '__main__':
    main()
    
        
    
    