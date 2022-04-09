# OCR cloud deployment demo

Demo of OCR API application combined with cloud deployment.

Stack
- Flask, Flask-RESTFul for web serving
- Tesseract for OCR
- Docker for container management
- Kubernetes for cloud deployment

Hosted on AWS using:
- API Gateway for secure endpoint integration
- VPC Link to connect Gateway to private VPC
- ECR as a container registry
- EKS as kubernetes cluster provider
- S3 bucket for image & PDF storage

What can be improved & expanded further:
- Formalized cloud configuration using Terraform by hashicorp.