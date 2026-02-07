# import pymongo;
from pymongo import MongoClient

client = MongoClient("mongodb+srv://youtubepy:youtubepy@cluster0.4djvwx5.mongodb.net/",tlsAllowInvalidCertificates=True);

# Not a good idea to include id and password in code files.

db = client ["ytmanager"]
video_collection = db["videos"]

print(video_collection)



def list_videos():
    for video in video_collection.find():
        print(f"ID: {video['_id']}, Name: {video['name']}, Time: {video['time']}")
def add_videos(name,time):
    video_collection.insert_one({"name": name, "time": time})
def update_videos(video_id, new_name, new_time):
    video_collection.update_one(
        {'_id': (video_id)},
        {"$set": {"name": new_name,"time":new_time}}
        )
def delete_video(video_id):
    video_collection.delete_one({"_id": video_id})
def main():
    while True:
        print("Youtube Manager App\n")
        print("List all videos")
        print("Add Videos")
        print("update a Videos")
        print("Delete a video")
        print("Exist the App")
        
        choice= input("Enter Your choice: ")
        
        if choice=='1':
            list_videos()
        elif choice=='2':
            name = input("Enter the video name: ")
            time = input("Enter the video time: ")
            add_videos(name, time)
        elif choice=='3':
            video_id = int(input("Enter the video Id to Update: "))
            name = input("Enter the video name: ")
            time = input("Enter the video time: ")
            update_videos(video_id, name, time)
        elif choice == '4':
            video_id = int(input("Enter the video Id delete: "))
            delete_video(video_id)
            print("Delete Successfully!")
        elif choice == '5':
            break
        
        else:
            print("Invalid Choice. Try again! ")
        

if __name__ == '__main__':
        main()
        
    
    
 