upstream osher_back {
    server 127.0.0.1:8000;
}


server {
    listen 80;
    server_name tdregionsnab.ru;
    server_tokens off;

    location / {
        root   /usr/share/nginx/region;
        index  index.html index.htm;
        try_files $uri $uri/ /index.html;
    }

    location /api {
        try_files $uri @proxy_api;
    }
    location /admin {
        try_files $uri @proxy_api;
    }
    location /summernote {
        try_files $uri @proxy_api;
    }

    location @proxy_api {
        proxy_set_header X-Forwarded-Proto https;
        proxy_set_header X-Url-Scheme $scheme;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header Host $http_host;
        proxy_redirect off;
        proxy_pass   http://osher_back;
    }

    location /static/ {
        autoindex on;
        alias /static/;
    }

    location /media/ {
        autoindex on;
        alias /media/;
    }
}