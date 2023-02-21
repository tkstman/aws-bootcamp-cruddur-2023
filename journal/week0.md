# Week 0 — Billing and Architecture

Napkin: Produced in the live session. This is a high level conceptual design of the requirements given by the CTO, marketing and clients for the development of the Cruddur application.
[Lucid charts napkin direct link](https://lucid.app/lucidchart/91da6577-6e84-4570-89ab-c6d9e75de256/edit?viewport_loc=-377%2C-41%2C2219%2C1108%2C0_0&invitationId=inv_cb8b6048-9f6e-4783-8db9-61236c6adf0f)
![Napkin text](https://github.com/tkstman/aws-bootcamp-cruddur-2023/blob/main/_docs/assets/Napkin_Diagram_Week_0.PNG)


Architecture Diagram: A more detailed logical architectural output from the requirements given. Shows the different AWS services that we aim to use to develop the Cruddur application.
[Lucid charts architecture direct link](https://lucid.app/lucidchart/b3741afa-0b37-46a1-b041-9c1155c02095/edit?viewport_loc=-1878%2C-1140%2C1922%2C960%2C0_0&invitationId=inv_4ba04c27-093f-465a-9033-21e6eef7119c)
![Architecture text](https://github.com/tkstman/aws-bootcamp-cruddur-2023/blob/main/_docs/assets/Architecture_Recreated.PNG)

Opened a support ticket for pipeline limit increase after researchcing service limits of specific services:
![Support_Ticket text](https://github.com/tkstman/aws-bootcamp-cruddur-2023/blob/main/_docs/assets/pipeline_increase.PNG)

Generate Admin user and setup MFA for Root user:
![User_Cred text](https://github.com/tkstman/aws-bootcamp-cruddur-2023/blob/main/_docs/assets/setupMFA.PNG)
![Admin_User text](https://github.com/tkstman/aws-bootcamp-cruddur-2023/blob/main/_docs/assets/usercredentials.PNG)



Reference the below links for details on setting up billing alarm, aws budget, cloudshell and aws cli usage:
[Gitpod environment setup](https://github.com/tkstman/aws-bootcamp-cruddur-2023/commit/2d41280149e27f70db83edc00ffb82d2325632da#diff-370a022e48cb18faf98122794ffc5ce775b2606b09a9d1f80b71333425ec078e)

[Alarm Setup](https://github.com/tkstman/aws-bootcamp-cruddur-2023/blob/main/awsscript/json/alarm_config.json)

[Budget Setup](https://github.com/tkstman/aws-bootcamp-cruddur-2023/blob/main/awsscript/json/budget.json)

[Budget Notification Setup](https://github.com/tkstman/aws-bootcamp-cruddur-2023/blob/main/awsscript/json/budget-notifications-with-subscribers.json)

[EventBridge Setup](https://github.com/tkstman/aws-bootcamp-cruddur-2023/blob/main/_docs/assets/eventbridge.PNG)

Delivered SNS From EventBridge
![EventBridge SNS Delivery](https://github.com/tkstman/aws-bootcamp-cruddur-2023/blob/main/_docs/assets/eventbridge2.PNG)
