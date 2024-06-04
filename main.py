from flask import Flask, render_template, request
import requests
import logging
import cProfile
import pstats
import io

app = Flask(__name__)

logging.basicConfig(filename='error.log', level=logging.ERROR)

BASE_URL = 'https://jsonplaceholder.typicode.com'


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/posts', methods=['GET', 'POST'])
def posts():
    if request.method == 'POST':
        pr = cProfile.Profile()
        pr.enable()
        try:
            num_posts = int(request.form['num_posts'])
            num_comments = int(request.form['num_comments'])
            max_chars = int(request.form['max_chars'])
            response = requests.get(f'{BASE_URL}/posts')
            response.raise_for_status()
            posts = response.json()[:num_posts]

            for post in posts:
                post['body'] = (post['body'][:max_chars] + '...') if len(post['body']) > max_chars else post['body']
                response_comments = requests.get(f'{BASE_URL}/posts/{post["id"]}/comments')
                response_comments.raise_for_status()
                post['comments'] = response_comments.json()[:num_comments]

            pr.disable()
            pr.dump_stats("profile_posts.prof")

            return render_template('posts.html', posts=posts)
        except Exception as e:
            logging.error(f'Error fetching posts: {e}')
            return render_template('posts.html', posts=[], error=str(e))
    return render_template('posts.html', posts=[])


@app.route('/posts/<int:post_id>')
def post_detail(post_id):
    pr = cProfile.Profile()
    pr.enable()
    try:
        post = requests.get(f'{BASE_URL}/posts/{post_id}').json()
        comments = requests.get(f'{BASE_URL}/posts/{post_id}/comments').json()

        pr.disable()
        pr.dump_stats("profile_post_detail.prof")

        return render_template('post_detail.html', post=post, comments=comments)
    except Exception as e:
        logging.error(f'Error fetching post detail: {e}')
        return render_template('post_detail.html', post={}, comments=[], error=str(e))


@app.route('/albums', methods=['GET', 'POST'])
def albums():
    if request.method == 'POST':
        pr = cProfile.Profile()
        pr.enable()
        try:
            num_albums = int(request.form['num_albums'])
            num_photos = int(request.form['num_photos'])
            response = requests.get(f'{BASE_URL}/albums')
            response.raise_for_status()
            albums = response.json()[:num_albums]

            for album in albums:
                response_photos = requests.get(f'{BASE_URL}/albums/{album["id"]}/photos')
                response_photos.raise_for_status()
                album['photos'] = response_photos.json()[:num_photos]

            pr.disable()
            pr.dump_stats("profile_albums.prof")

            return render_template('albums.html', albums=albums)
        except Exception as e:
            logging.error(f'Error fetching albums: {e}')
            return render_template('albums.html', albums=[], error=str(e))
    return render_template('albums.html', albums=[])


@app.route('/albums/<int:album_id>')
def album_detail(album_id):
    pr = cProfile.Profile()
    pr.enable()
    try:
        album = requests.get(f'{BASE_URL}/albums/{album_id}').json()
        photos = requests.get(f'{BASE_URL}/albums/{album_id}/photos').json()

        pr.disable()
        pr.dump_stats("profile_album_detail.prof")

        return render_template('album_detail.html', album=album, photos=photos)
    except Exception as e:
        logging.error(f'Error fetching album detail: {e}')
        return render_template('album_detail.html', album={}, photos=[], error=str(e))


if __name__ == '__main__':
    app.run(debug=True)
