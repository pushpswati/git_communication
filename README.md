# git_communication 
## Ubuntu 16.04

## Git Communication API:
### API signature:
```
http://0.0.0.0:8000/pullrequest/metadata?username=pushpswati&repo_name=git_communication
```
#### Request Type-  GET
#### Request Response:
```
{
    "pull_request": [
        {
            "status": "REVIEWER_PENDING",
            "state": "open",
            "id": 199141947,
            "merge_status": "MERGE_PENDING"
        }
    ]
}
```


## Setup and installation


### Run following cammand
```
sudo apt-get update
sudo apt-get install python-pip python-dev libpq-dev nginx
```
### Install python package
```
sudo pip install -r requirement.txt
```

## Gunicorn setup [Edit following file]

sudo nano /etc/systemd/system/gunicorn.service

```
[Unit]
Description=gunicorn daemon
After=network.target

[Service]
User=sss
Group=www-data
WorkingDirectory=/home/sss/Documents/pythontask/project
ExecStart=/usr/bin/gunicorn --access-logfile - --workers 3 --bind unix:/home/sss/Documents/pythontask/project/project.sock project.wsgi:application

[Install]
WantedBy=multi-user.target
```
## Nginx set up
sudo nano /etc/nginx/sites-available/myproject

```
server {
    listen 8000;
    server_name server_domain_or_IP;

    location = /favicon.ico { access_log off; log_not_found off; }
    location /static/ {
        root /home/sss/Documents/pythontask/project;
    }

    location / {
        include proxy_params;
        proxy_pass http://unix:/home/sss/Documents/pythontask/project/project.sock;
    }
}
```


### Run following cammand
```
sudo systemctl start gunicorn
sudo systemctl enable gunicorn
sudo systemctl daemon-reload
sudo systemctl restart nginx
```

