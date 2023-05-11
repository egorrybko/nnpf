docker system prune -af || docker build --pull --no-cache --rm -f "Dockerfile" -t nnpf:latest "." 
docker compose -f "docker-compose.yml" up -d --build 