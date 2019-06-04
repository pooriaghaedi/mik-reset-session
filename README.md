# Remove Mikrotik Hotspot Session 

Sometimes users forget to logout from their hotspot session, they go to different Locations and they want to use Wireless again. With this app users can remove their hotspot session. Here I used Active directory as Authentication. After user is being Authenticated their session would be removed.


## Dockerfile
There are some environment variables in the Dockerfile You need to set, most of them are credentials. after thet you can build the dockerfile using this command.
```
docker build -t mikresetsession .
docker run -d -p 80:5000 mikresetsession 
```
