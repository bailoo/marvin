# last.fm
[last.fm](https://www.last.fm/) is a online website for `music` services. 
Users can join and listen to the latest tracks from around the globe.<br>
`last.fm` builds a detailed profile for each user on their music taste by recording what the user is listening to, 
for how long the user is listening, count of the number of times a track gets played by the user and many other factors.

`last.fm` also provides [API]() for Developers.<br>
The [API](https://www.last.fm/api) allows anyone to build their own programs using `last.fm` data, 
whether they're on the web, the desktop or mobile devices.<br>

Using API we can <i>search</i> for Artists, Albums or Tracks. <i>GET</i> Top Artists or Tracks and <i>GET</i> Similar Tracks and Similar Artists.

---

## Artist.getSimilar

How to get API key from last .fm?

   1. [Create an account at last.fm](https://www.last.fm/join) or [log in to an existing account](https://secure.last.fm/login).
   2. [Create API account](https://www.last.fm/api/account/create).
      - Add a name & description for your application & SUBMIT
   3. DONE.
   4. Read the [documentation](https://www.last.fm/api/intro) for references.
   
To Get Similar Artists.<br>
 ```http://ws.audioscrobbler.com/2.0/?method=artist.getsimilar&artist=artist-name&api_key=YOUR_API_KEY&format=json```
