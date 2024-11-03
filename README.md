# Student Management System

This project is a web application that allows users to manage student data, specifically student IDs, names, subjects, and ages, using various AWS services.

<p align="center">
  <img width="600" src="https://github.com/user-attachments/assets/d44e6ad8-df8c-4543-8ac3-0b57b59665e1">
</p>

## AWS Services Used

- **AWS Amplify**: A development platform for building secure, scalable mobile and web applications, which hosts the frontend of the application.
- **AWS Lambda**: A serverless compute service that runs the backend code for handling requests and interfacing with the database.
- **AWS API Gateway**: A fully managed service that enables the creation, deployment, and management of secure APIs for the Lambda functions.
- **DynamoDB**: A NoSQL database service that stores student data with high availability and scalability.

## Steps to Implement the Project

1. **Create a DynamoDB Table**: 
   - Create a table named `students` with `studentid` as the partition key. 
   - Copy the ARN (Amazon Resource Name) of the table for later use.
     <p align="center">
      <img width="900" src="https://github.com/user-attachments/assets/20d65eea-7ff4-4e86-97a3-a0181f3a5d20">
     </p>

2. **Create Lambda Functions**: 
   - Create two Lambda functions: one for retrieving student data and another for creating new student records. 
   - When creating the Lambda functions, create a new role using the provided `role_policy.txt`, ensuring to include your DynamoDB table ARN in the role's permissions.
     <p align="center">
      <img width="900" src="https://github.com/user-attachments/assets/cfc0ba64-36b0-478a-a906-f7ea22949502">
     </p>

3. **Set Up API Gateway**: 
   - Create a REST API in API Gateway.
   - Add two methods: 
     - **GET** method: Choose the Lambda function for retrieving students.
     - **POST** method: Choose the Lambda function for creating new students.
   - Enable CORS (Cross-Origin Resource Sharing) for both methods and deploy the API. 
   - Copy the Invoke URL provided after deployment.
     <p align="center">
      <img width="900" src="https://github.com/user-attachments/assets/2516ad23-b9ee-4768-945d-4b3a7842c105">
     </p>

4. **Develop Frontend Code**: 
   - Write your HTML, CSS, and JavaScript code for the application.
   - In the JavaScript code, make sure to include the API Invoke URL where appropriate.
   - Zip all your code files into one file named `index.zip`.

5. **Deploy Using AWS Amplify**: 
   - Go to AWS Amplify and deploy your zipped file (`index.zip`).
   - Once the deployment is complete, you should be able to access your application through the provided link.
     <p align="center">
      <img width="900" src="https://github.com/user-attachments/assets/2c48535d-9684-49b3-b7ef-15ed25f06a21">
     </p>

## Project Demo

https://github.com/user-attachments/assets/2e377c75-26c2-45ca-b293-41d701d927e1

