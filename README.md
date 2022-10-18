# data-modeling-postgresql

Song data :
```
{"num_songs": 1, "artist_id": "ARD7TVE1187B99BFB1", "artist_latitude": null, "artist_longitude": null, "artist_location": "California - LA", "artist_name": "Casual", "song_id": "SOMZWCG12A8C13C480", "title": "I Didn't Mean To", "duration": 218.93179, "year": 0}
```

Log data (user activity):
```
{"artist":null,"auth":"Logged In","firstName":"Walter","gender":"M","itemInSession":0,"lastName":"Frye","length":null,"level":"free","location":"San Francisco-Oakland-Hayward, CA","method":"GET","page":"Home","registration":1540919166796.0,"sessionId":38,"song":null,"status":200,"ts":1541105830796,"userAgent":"\"Mozilla\/5.0 (Macintosh; Intel Mac OS X 10_9_4) AppleWebKit\/537.36 (KHTML, like Gecko) Chrome\/36.0.1985.143 Safari\/537.36\"","userId":"39"}
```

---

## Schema

### Fact table

__songplays__
```
songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent
```

### Dimension tables

__users__
```
uer_id, first_name, last_name, gender, level
```

__songs__
```
song_id, title, artist_id, year, duration
```

__artists__
```
artist_id, name, location, latitude, longitude
```

__time__
```
start_time, hour, day, week, month, year, weekday
```

---
