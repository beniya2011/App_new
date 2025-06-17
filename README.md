diff --git a//dev/null b/README.md
index 0000000000000000000000000000000000000000..cc174c286ab8f14d27124657881e914a00bb1181 100644
--- a//dev/null
+++ b/README.md
@@ -0,0 +1,23 @@
+# Full Stack Caching App
+
+This repository contains a small Flask backend with Redis caching and a React frontend. Docker is used to run both services along with a Redis container.
+
+## Prerequisites
+- [Docker](https://docs.docker.com/get-docker/)
+- [Docker Compose](https://docs.docker.com/compose/)
+
+## Running the application
+1. Clone the repository.
+2. Navigate to the project directory.
+3. Build and start the containers:
+   ```bash
+   docker-compose up --build
+   ```
+4. Open your browser at [http://localhost:3000](http://localhost:3000) to access the frontend. The backend API will be available at [http://localhost:5000](http://localhost:5000).
+
+## Stopping the application
+To stop all containers, run:
+```bash
+docker-compose down
+```
+
