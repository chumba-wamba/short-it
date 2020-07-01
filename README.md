# Short-It

[![](https://img.shields.io/badge/BUILT%20FOR-WEB-blue?style=for-the-badge&logo=android&labelColor=000000&color=3DDC84&logoColor=3DDC84)](https://flask.palletsprojects.com/en/1.1.x/) [![](https://img.shields.io/badge/MADE%20USING-FLASK-blue?style=for-the-badge&logo=flask&labelColor=000000&color=blue&logoColor=ffffff)](https://flask.palletsprojects.com/en/1.1.x/) [![](https://img.shields.io/badge/IDE-VISUAL%20STUDIO%20CODE-blue?style=for-the-badge&logo=visual-studio-code&labelColor=000000&color=007ACC&logoColor=ffffff)](https://code.visualstudio.com/)


A web-app for shortening URLs developed with Python (Flask), MongoDB, HTML, CSS, JavaScript, and BootStrap. The web-app also offers a variety of statistics regarding the shortened URL through a custom dashboard.

To do:

* Draw sequence, architecture, and/or use-case diagrams. 
* Code the models for MongoDB in MongoEngine. ✔
* Code the routing logic to interact with the database. ✔
* Design and code the front-end (probably requires AJAX). ✔
* Add logic to integrate dashboard for registered users. ✔

## Features

* Responsive UI.
* Shorten URLs to custom or automatically generated strings.
* View analytics for your shortened URL (only for registered users).
* Shorten URLs without registering as a user.
* Share the details of a shortened URL with other users. 
* Edit basic account details and your password.

## Installation

Follow the steps to run the web-app on your local machine:

1. Clone the repository

    ```shell
    git clone https://github.com/chumba-wamba/Short-It.git
    ```
2. Install the Dependencies

    ```shell
    cd Short-It
    pip install -r requirements.txt
    ```
3. Install MongoDB on your local machine

4. Run the app on a browser

    ```shell
    cd Short-It
    python run.py
    ```

6. Open localhost in your browser @http://localhost:5000

## Screenshots

#### Home Page
![Home Page](https://github.com/chumba-wamba/Short-It/blob/master/assets/images/home.PNG?raw=true)

#### Login Page
![Login Page](https://github.com/chumba-wamba/Short-It/blob/master/assets/images/login.PNG?raw=true)

#### Register Page
![Register Page](https://github.com/chumba-wamba/Short-It/blob/master/assets/images/register.PNG?raw=true)

#### Shorten Page
![Shorten Page](https://github.com/chumba-wamba/Short-It/blob/master/assets/images/shorten.PNG?raw=true)

#### Dashboard Page
![Dashboard Page](https://github.com/chumba-wamba/Short-It/blob/master/assets/images/dashboard.PNG?raw=true)

#### Account Page
![Home Page](https://github.com/chumba-wamba/Short-It/blob/master/assets/images/account.PNG?raw=true)
