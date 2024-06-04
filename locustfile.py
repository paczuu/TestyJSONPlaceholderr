from locust import HttpUser, TaskSet, task, between

class MyTaskSet(TaskSet):

    @task
    def index(self):
        self.client.get("/")

    @task
    def posts(self):
        self.client.post("/posts", {
            "num_posts": 5,
            "num_comments": 3,
            "max_chars": 100
        })

    @task
    def post_detail(self):
        self.client.get("/posts/1")

    @task
    def albums(self):
        self.client.post("/albums", {
            "num_albums": 3,
            "num_photos": 2
        })

    @task
    def album_detail(self):
        self.client.get("/albums/1")


class WebsiteUser(HttpUser):
    tasks = [MyTaskSet]
    wait_time = between(1, 5)
