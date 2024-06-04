### Testy jednostkowe i kontaktowe plus raport:
coverage run -m unittest discover -s tests <br>
coverage report -m <br><br>

### Testy wydajnościowe (http://localhost:8089):
locust <br><br>

### Analiza wyników profilowania:
snakeviz profile_posts.prof <br>
snakeviz profile_post_detail.prof <br>
snakeviz profile_albums.prof <br>
snakeviz profile_album_detail.prof <br><br>

### Uruchomienie monitorowania pamięci: <br>
mprof run flask run <br>
mprof plot <br><br>

### Analiza profilowania i zużycia pamięci: <br>
python analyze_profiling.py <br><br>
