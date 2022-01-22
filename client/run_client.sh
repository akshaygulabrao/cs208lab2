docker build -t client .
docker run -network=host --name ipc_server_dns_name server
docker run --network=host client
