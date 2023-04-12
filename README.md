# SocialScape

It contains RESTful APIs for social media platform. It allows users to authenticate, create and manage posts, follow / unfollow other user, like / unlike posts, add comments to posts, and retrieve user profiles, posts and their own post details.

## Installation:
#### 1. Clone the repository
`git clone https://github.com/sonaljain067/SocialScape.git
`

#### 2. Create a virtual environment
`cd SocialScape` <br/>
`python3 -m venv env` or `virtualenv env` 
to create virtual environment named `env`

#### 3. Activate the virtual environment
In Ubuntu: `source env/bin/activate` <br/>
In Windows: `.\env\Scripts\activate`

#### 4. Install dependencies
`pip install -r requirements.txt`

#### 5. Setup database 
`python manage.py migrate`

#### 6. Run the server
`python manage.py runserver`

## Authentication 
Authentication of APIs is done using JSON Web Token(JWT). To obtain token for active & valid user, send a post request ot `/api/authenticate` with valid username and password. The access and refresh token will be returned in the response.
To authenticate & use the APIs, add the token to the `Authorization` header as:

`Authorization: Bearer <access_token>`

## API Endpoints:
`POST /api/follow/{id}` - Authenticated user would follow user with {id} <br/>
`POST /api/unfollow/{id}` - Authenticated user would unfollow a user with {id}  <br/>
`GET /api/user` - Authenticate the request and return the respective user profile  <br/>
`POST api/posts/` - Add a new post created by the authenticated user <br/>
`DELETE api/posts/{id} ` - Delete post with {id} created by the authenticated user <br/>
`POST /api/like/{id}` - Like the post with {id} by the authenticated user <br/>
`POST /api/unlike/{id}` - Unlike the post with {id} by the authenticated user <br/>
`POST /api/comment/{id}` - Add comment for post with {id} by the authenticated user <br/>
`GET api/posts/{id}/` - Return a single post with {id} populated with its number of likes and comments <br/>
`GET /api/all_posts` - Return all posts created by authenticated user sorted by post time. <br/>

## API Documentation
The SocialScape API is documented using Postman. You can import the [Postman Collection](https://elements.getpostman.com/redirect?entityId=17433654-27ef72cb-abcd-4ba2-a3dc-e0c291b52a4e&entityType=collection) to get started.
