# AWS Cloud Assignment

## Project Overview
This project demonstrates a cloud-based file upload and metadata retrieval system using AWS services.

## AWS Services Used
- Amazon EC2
- Amazon S3
- AWS Lambda
- Amazon DynamoDB
- IAM
- Nginx

## Technologies
- Node.js
- Express.js
- HTML
- JavaScript

## Project Architecture
S3 Upload → Lambda Trigger → DynamoDB Storage → Node.js API → Hosted Website

## Hosted Website
http://13.232.95.99

## API Endpoint
http://13.232.95.99:3000/api/files

## Features
- Static website hosted on EC2 using Nginx
- Backend REST API using Node.js and Express
- File metadata stored in Amazon DynamoDB
- API returns uploaded file details in JSON format
- IAM role used for secure AWS service access

## Repository
Source code for the AWS Cloud Assignment project.
