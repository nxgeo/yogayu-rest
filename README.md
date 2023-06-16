# Yogayu REST API

The Yogayu REST API codebase is designed for the Yogayu mobile app. It provides endpoints for managing yoga levels, yoga poses, users, and user yoga histories.

## Getting Started

These guidelines will assist you in deploying the project on the Google Cloud Platform for production purposes. Follow the steps below to set up and run the project on a live system using Cloud Run.

### Prerequisites

- Python 3.11.3
- Cloud SQL with PostgreSQL 15 database engine (publicly accessible)
- Cloud Storage Bucket with Uniform access control (publicly accessible)

### Deploying

1. Clone the repository into Cloud Shell:

    ```
    git clone https://github.com/nxgeo/yogayu-rest.git
    cd yogayu-rest
    ```

2. Install the required dependencies:

    ```
    python -m pip install -r requirements.txt
    ```

3. Import the [backup object](https://storage.googleapis.com/yogayu/yogayu) to the Cloud SQL instance and assign it to the 'postgres' user.

4. Set all the required environment variables, referring to the `.env.template` file.

5. Perform `collectstatic` to store static files in the bucket:

    ```
    python manage.py collectstatic
    ```

6. Deploy to Cloud Run from source:

    ```
    gcloud run deploy
    ```

    Set the environment variables on Cloud Run either during deployment or after deployment.

## API Documentation

For API documentation, please visit: [https://api.yogayu.app](https://api.yogayu.app)

Please feel free to ask if you have any further questions or need additional assistance.
