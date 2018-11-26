# 2dv515-a2

#### Run

To run the project, download docker:
* [Docker för Mac](https://docs.docker.com/docker-for-mac/install/#download-docker-for-mac)  
* [Docker för Windows](https://docs.docker.com/toolbox/toolbox_install_windows/)  
* [Docker för Ubuntu](https://www.docker.com/docker-ubuntu) samt [docker-compose](https://docs.docker.com/compose/install/)

Start the project with `docker-compose up -d --build`.
Visit `localhost:80`.

#### API
`http://localhost/api`

```
{
    "_links": {
        "self": {
            "href": "http://localhost:8080/api"
        },
        "user-based": {
            "href": "http://localhost:8080/api/ub",
            "title": "Get user-based recommendations"
        },
        "item-based": {
            "href": "http://localhost:8080/api/ib",
            "title": "Get item-based recommendations"
        }
    }
}
```

#### Get k-cluster based clusters
`http://localhost/api/kcluster/<number_of_clusters>`

```
{
    "clusters": [<result>]
}
```

#### Generate Hierarchical cluster image
`http://localhost:8080/api/generate`

```
{
    "success": true/false
}
```

#### Get Hierarchical cluster image
`http://localhost:8080/api/tree.jpg`

```
<JPEG>
```