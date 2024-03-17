# Image_Classification_CNN_and_MLFlow

#Workflows

Update config.yaml
Update secrets.yaml [Optional]
Update params.yaml
Update the entity 
Update the configuration manager in src config
Update the components
Update the pipeline
Update the main.py
Update the dvc.yaml

Here we are using DagsHub to host of model remotely :


MLFLOW_TRACKING_URI=https://dagshub.com/tejaswini1999teju15/Image_Classification_CNN_and_MLFlow.mlflow \
MLFLOW_TRACKING_USERNAME=tejaswini1999teju15 \
MLFLOW_TRACKING_PASSWORD=XXXXXXXXXXXXXXXXXXXXXXXXXXXXX \
python script.py


``` bash
export MLFLOW_TRACKING_URI=https://dagshub.com/tejaswini1999teju15/Image_Classification_CNN_and_MLFlow.mlflow
export MLFLOW_TRACKING_USERNAME=tejaswini1999teju15
export MLFLOW_TRACKING_PASSWORD=XXXXXXXXXXXXXXXXXXXXXXXXXXXXX
```

AWS-CICD-Deployment-with-Github-Actions
1. Login to AWS console.
2. Create IAM user for deployment

#with specific access

1. EC2 access : It is virtual machine

2. ECR: Elastic Container registry to save your docker image in aws


#Description: About the deployment

1. Build docker image of the source code

2. Push your docker image to ECR

3. Launch Your EC2 

4. Pull Your image from ECR in EC2

5. Lauch your docker image in EC2

#Policy:

1. AmazonEC2ContainerRegistryFullAccess

2. AmazonEC2FullAccess
3. Create ECR repo to store/save docker image
- Save the URI: 566373416292.dkr.ecr.us-east-1.amazonaws.com/chicken
4. Create EC2 machine (Ubuntu)
5. Open EC2 and Install docker in EC2 Machine:

#optinal

``` bash
sudo apt-get update -y

sudo apt-get upgrade

#required

curl -fsSL https://get.docker.com -o get-docker.sh

sudo sh get-docker.sh

sudo usermod -aG docker ubuntu
```

newgrp docker
6. Configure EC2 as self-hosted runner:
setting>actions>runner>new self hosted runner> choose os> then run command one by one

7. Setup github secrets:
``` bash
AWS_ACCESS_KEY_ID=

AWS_SECRET_ACCESS_KEY=

AWS_REGION = us-east-1

AWS_ECR_LOGIN_URI = demo>>  566373416292.dkr.ecr.ap-south-1.amazonaws.com

ECR_REPOSITORY_NAME = simple-app
```
