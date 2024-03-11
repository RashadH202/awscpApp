import uuid

# Define the question bank data
question_bank = [
  
    {
        'id': str(uuid.uuid4()),
        'question': 'What is the primary benefit of using Amazon S3?',
        'choices': [
            'Storing and retrieving data over the internet',
            'Running virtual servers in the cloud',
            'Managing relational databases',
            'Building scalable web applications'
        ],
        'correct_answer': 'Storing and retrieving data over the internet - Amazon S3 is a scalable object storage service designed for storing and retrieving data over the internet securely and reliably.'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'Which AWS service is used to deploy and manage containers?',
        'choices': [
            'Amazon S3',
            'Amazon RDS',
            'Amazon ECS',
            'Amazon Redshift'
        ],
        'correct_answer': 'Amazon ECS - Amazon ECS (Elastic Container Service) is a fully-managed container orchestration service used to deploy, manage, and scale containerized applications.'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'What is AWS Lambda used for?',
        'choices': [
            'Managing virtual networks',
            'Storing data in a scalable manner',
            'Running code in response to events',
            'Provisioning virtual machines'
        ],
        'correct_answer': 'Running code in response to events - AWS Lambda is a serverless computing service that allows you to run code in response to events without provisioning or managing servers.'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'Which AWS service is used to distribute content globally with low latency?',
        'choices': [
            'Amazon Route 53',
            'Amazon CloudFront',
            'AWS Direct Connect',
            'Amazon VPC'
        ],
        'correct_answer': 'Amazon CloudFront - Amazon CloudFront is a fast content delivery network (CDN) service that securely delivers data, videos, applications, and APIs to customers globally with low latency, high transfer speeds, and no minimum commitments.'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'What is the primary benefit of using Amazon EC2?',
        'choices': [
            'Storing and retrieving data over the internet',
            'Running virtual servers in the cloud',
            'Managing relational databases',
            'Building scalable web applications'
        ],
        'correct_answer': 'Running virtual servers in the cloud - Amazon EC2 (Elastic Compute Cloud) allows users to rent virtual servers on which they can run their applications. It provides scalable computing capacity in the cloud and helps businesses deploy and manage their applications quickly and securely.'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'What AWS service provides a fully managed NoSQL database service?',
        'choices': [
            'Amazon S3',
            'Amazon RDS',
            'Amazon DynamoDB',
            'Amazon Redshift'
        ],
        'correct_answer': 'Amazon DynamoDB - Amazon DynamoDB is a fully managed NoSQL database service that provides fast and predictable performance with seamless scalability. It is designed to handle large amounts of data and traffic, making it suitable for various applications requiring low-latency access to data.'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'What is Amazon RDS primarily used for?',
        'choices': [
            'Storing and retrieving data over the internet',
            'Running virtual servers in the cloud',
            'Managing relational databases',
            'Building scalable web applications'
        ],
        'correct_answer': 'Managing relational databases - Amazon RDS (Relational Database Service) is a fully managed relational database service provided by AWS. It enables users to set up, operate, and scale relational databases in the cloud easily. RDS supports various database engines, including MySQL, PostgreSQL, SQL Server, and Oracle.'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'What AWS service is used for scalable object storage?',
        'choices': [
            'Amazon S3',
            'Amazon RDS',
            'Amazon EC2',
            'Amazon DynamoDB'
        ],
        'correct_answer': 'Amazon S3 - Amazon S3 (Simple Storage Service) is a scalable object storage service designed for storing and retrieving any amount of data from anywhere on the web. It offers high durability, availability, and performance, making it suitable for a wide range of use cases, including backup and restore, content distribution, and data archiving.'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'What is Amazon VPC used for in AWS?',
        'choices': [
            'Managing virtual networks',
            'Storing data in a scalable manner',
            'Running code in response to events',
            'Provisioning virtual machines'
        ],
        'correct_answer': 'Managing virtual networks - Amazon VPC (Virtual Private Cloud) allows users to provision a logically isolated section of the AWS Cloud where they can launch AWS resources in a virtual network. It provides control over the virtual networking environment, including selection of IP address ranges, creation of subnets, and configuration of route tables and network gateways.'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'Which AWS service is used for real-time messaging and communication?',
        'choices': [
            'Amazon SNS',
            'Amazon SQS',
            'Amazon SES',
            'Amazon Route 53'
        ],
        'correct_answer': 'Amazon SNS - Amazon SNS (Simple Notification Service) is a fully managed messaging service that allows users to send messages and notifications to a large number of subscribers through multiple communication protocols, including SMS, email, and push notifications. It supports pub/sub and push messaging models, making it suitable for various use cases, such as application notifications, automated alerts, and mobile app messaging.'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'What AWS service provides scalable, low-latency storage for frequently accessed data?',
        'choices': [
            'Amazon S3',
            'Amazon Glacier',
            'Amazon EFS',
            'Amazon EBS'
        ],
        'correct_answer': 'Amazon EBS - Amazon EBS (Elastic Block Store) provides scalable block storage volumes that can be attached to EC2 instances. It offers consistent and low-latency performance for frequently accessed data and supports various data persistence options, including snapshots and encryption. EBS volumes are suitable for use cases requiring high-performance storage, such as databases, file systems, and containerized applications.'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'Which AWS service provides a managed Kubernetes service?',
        'choices': [
            'Amazon EKS',
            'Amazon ECS',
            'Amazon EC2',
            'Amazon S3'
        ],
        'correct_answer': 'Amazon EKS - Amazon EKS (Elastic Kubernetes Service) is a fully managed Kubernetes service provided by AWS. It allows users to deploy, manage, and scale containerized applications using Kubernetes without needing to install or operate the Kubernetes control plane. EKS supports integrations with other AWS services and offers high availability, security, and scalability for containerized workloads.'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'What AWS service enables users to analyze and visualize data with dashboards and reports?',
        'choices': [
            'Amazon Athena',
            'Amazon Redshift',
            'Amazon QuickSight',
            'Amazon Elasticsearch Service'
        ],
        'correct_answer': 'Amazon QuickSight - Amazon QuickSight is a fast, cloud-powered business intelligence service provided by AWS. It allows users to easily create, publish, and share interactive dashboards and reports that visualize data from various sources. QuickSight supports ad-hoc analysis, predictive analytics, and machine learning insights, making it suitable for businesses of all sizes.'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'What AWS service provides a fully managed, highly available relational database?',
        'choices': [
            'Amazon RDS',
            'Amazon DynamoDB',
            'Amazon S3',
            'Amazon ElastiCache'
        ],
        'correct_answer': 'Amazon RDS - Amazon RDS (Relational Database Service) is a fully managed relational database service provided by AWS. It automates routine database tasks such as provisioning, patching, backup, recovery, and scaling, allowing users to focus on their applications. RDS supports popular database engines, including MySQL, PostgreSQL, SQL Server, MariaDB, and Oracle.'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'Which AWS service enables users to build, train, and deploy machine learning models at scale?',
        'choices': [
            'Amazon SageMaker',
            'Amazon Rekognition',
            'Amazon Polly',
            'Amazon Transcribe'
        ],
        'correct_answer': 'Amazon SageMaker - Amazon SageMaker is a fully managed machine learning service provided by AWS. It provides developers and data scientists with the tools to build, train, and deploy machine learning models at scale, without needing to manage the underlying infrastructure. SageMaker supports a wide range of machine learning frameworks and algorithms, making it suitable for various machine learning tasks.'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'What is the primary benefit of using Amazon CloudWatch?',
        'choices': [
            'Monitoring and observability',
            'Storing and retrieving data over the internet',
            'Running virtual servers in the cloud',
            'Managing relational databases'
        ],
        'correct_answer': 'Monitoring and observability - Amazon CloudWatch is a monitoring and observability service provided by AWS. It collects and tracks metrics, logs, and events from AWS resources and applications, providing insights into their operational health and performance. CloudWatch enables users to set alarms, create dashboards, and take automated actions based on predefined thresholds, helping them monitor, troubleshoot, and optimize their AWS environments.'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'What AWS service is used to migrate on-premises applications to the cloud?',
        'choices': [
            'AWS Snowball',
            'AWS Snowmobile',
            'AWS Snowcone',
            'AWS Server Migration Service'
        ],
        'correct_answer': 'AWS Server Migration Service - AWS Server Migration Service (SMS) is an agentless service that enables users to automate the migration of on-premises virtual machines (VMs) to the AWS Cloud. It simplifies the migration process by automatically replicating VMs and their associated data to AWS, allowing users to test, validate, and cut over their applications with minimal downtime.'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'What is Amazon Aurora?',
        'choices': [
            'A managed NoSQL database service',
            'A fully managed relational database engine',
            'A data warehousing solution',
            'An analytics service'
        ],
        'correct_answer': 'A fully managed relational database engine - Amazon Aurora is a fully managed relational database engine provided by AWS. It is compatible with MySQL and PostgreSQL databases and offers performance, scalability, and reliability enhancements over traditional database engines. Aurora provides features such as high availability, automatic failover, and continuous backup, making it suitable for mission-critical applications.'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'What AWS service is used for real-time streaming of data?',
        'choices': [
            'Amazon Kinesis',
            'Amazon Redshift',
            'Amazon EMR',
            'Amazon DynamoDB'
        ],
        'correct_answer': 'Amazon Kinesis - Amazon Kinesis is a platform for real-time streaming of data at scale. It enables users to collect, process, and analyze streaming data in real time, allowing them to derive insights and take immediate actions. Kinesis supports various use cases, including real-time analytics, log and event data processing, and machine learning model inference.'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'What is Amazon ElastiCache?',
        'choices': [
            'A managed NoSQL database service',
            'A fully managed relational database engine',
            'A caching service',
            'A data warehousing solution'
        ],
        'correct_answer': 'A caching service - Amazon ElastiCache is a fully managed caching service provided by AWS. It supports popular open-source in-memory caching engines such as Redis and Memcached, allowing users to deploy and operate caching clusters in the cloud. ElastiCache improves the performance and scalability of applications by caching frequently accessed data and reducing the load on backend databases.'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'What AWS service provides fully managed file storage for use with EC2 instances?',
        'choices': [
            'Amazon S3',
            'Amazon EBS',
            'Amazon EFS',
            'Amazon Glacier'
        ],
        'correct_answer': 'Amazon EFS - Amazon EFS (Elastic File System) is a fully managed file storage service provided by AWS. It offers scalable and highly available file storage that can be shared across multiple EC2 instances, enabling concurrent access to data. EFS supports various use cases, including content management, media processing, and web serving.'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'What is Amazon Neptune?',
        'choices': [
            'A managed NoSQL database service',
            'A fully managed relational database engine',
            'A data warehousing solution',
            'A graph database service'
        ],
        'correct_answer': 'A graph database service - Amazon Neptune is a fully managed graph database service provided by AWS. It is optimized for storing and querying highly connected data with complex relationships, such as social networks, recommendation engines, and fraud detection systems. Neptune supports popular graph query languages and provides high availability, durability, and security for graph data.'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'What is AWS Glue used for?',
        'choices': [
            'Data warehousing',
            'Extract, transform, and load (ETL) jobs',
            'Real-time streaming of data',
            'Object storage'
        ],
        'correct_answer': 'Extract, transform, and load (ETL) jobs - AWS Glue is a fully managed extract, transform, and load (ETL) service provided by AWS. It enables users to prepare and transform data for analytics and machine learning using a serverless and scalable architecture. Glue automates the discovery, cataloging, and cleaning of data, making it easier to analyze and derive insights from diverse datasets.'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'What is Amazon Redshift primarily used for?',
        'choices': [
            'Storing and retrieving data over the internet',
            'Running virtual servers in the cloud',
            'Managing relational databases',
            'Data warehousing and analytics'
        ],
        'correct_answer': 'Data warehousing and analytics - Amazon Redshift is a fully managed data warehousing service provided by AWS. It allows users to analyze large datasets using SQL queries and business intelligence tools. Redshift is optimized for high-performance, scalable analytics, making it suitable for data warehousing, business intelligence, and reporting applications.'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'What AWS service is used for batch processing of data?',
        'choices': [
            'Amazon Kinesis',
            'Amazon EMR',
            'Amazon DynamoDB',
            'Amazon Athena'
        ],
        'correct_answer': 'Amazon EMR - Amazon EMR (Elastic MapReduce) is a fully managed big data processing service provided by AWS. It enables users to run distributed frameworks such as Apache Hadoop, Apache Spark, and Presto for processing and analyzing large datasets. EMR is suitable for batch processing, data transformation, and data analysis tasks.'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'What is AWS Lambda?',
        'choices': [
            'A managed container service',
            'A message queuing service',
            'A serverless compute service',
            'A content delivery network'
        ],
        'correct_answer': 'A serverless compute service - AWS Lambda is a serverless compute service provided by AWS. It allows users to run code in response to events without provisioning or managing servers. Lambda supports various programming languages and can be used for building serverless applications, event-driven architectures, and backend services.'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'What AWS service is used for managed file transfers?',
        'choices': [
            'Amazon S3',
            'Amazon EFS',
            'Amazon Transfer Family',
            'Amazon Glacier'
        ],
        'correct_answer': 'Amazon Transfer Family - Amazon Transfer Family is a fully managed service provided by AWS for transferring files into and out of AWS storage services securely. It supports protocols such as FTP, FTPS, and SFTP, allowing users to seamlessly migrate file transfer workloads to the cloud.'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'What is Amazon Cognito used for?',
        'choices': [
            'Identity and access management',
            'Data warehousing',
            'Real-time messaging and communication',
            'Content delivery network'
        ],
        'correct_answer': 'Identity and access management - Amazon Cognito is a fully managed identity and access management service provided by AWS. It allows users to add authentication, authorization, and user management to their web and mobile applications easily. Cognito supports features such as user sign-up and sign-in, social identity providers, and multi-factor authentication.'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'What AWS service is used for content delivery and acceleration?',
        'choices': [
            'Amazon S3',
            'Amazon CloudFront',
            'Amazon Route 53',
            'Amazon CloudWatch'
        ],
        'correct_answer': 'Amazon CloudFront - Amazon CloudFront is a content delivery network (CDN) service provided by AWS. It delivers data, videos, applications, and APIs to viewers with low latency and high transfer speeds. CloudFront accelerates the delivery of content by caching it at edge locations worldwide, reducing the load on origin servers and improving user experience.'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'What AWS service provides a fully managed container orchestration service?',
        'choices': [
            'Amazon ECS',
            'Amazon EKS',
            'Amazon EC2',
            'Amazon ECR'
        ],
        'correct_answer': 'Amazon ECS - Amazon ECS (Elastic Container Service) is a fully managed container orchestration service provided by AWS. It allows users to run, stop, and manage Docker containers on a cluster of EC2 instances easily. ECS supports containerized applications at scale and integrates with other AWS services for seamless deployment and management.'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'What is Amazon SQS?',
        'choices': [
            'A managed message queuing service',
            'A serverless compute service',
            'A fully managed relational database engine',
            'A content delivery network'
        ],
        'correct_answer': 'A managed message queuing service - Amazon SQS (Simple Queue Service) is a fully managed message queuing service provided by AWS. It allows users to decouple and scale microservices, distributed systems, and serverless applications by transmitting messages between components asynchronously. SQS offers features such as message retention, dead-letter queues, and FIFO queues for reliable message delivery.'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'What is AWS Direct Connect?',
        'choices': [
            'A managed container service',
            'A serverless compute service',
            'A content delivery network',
            'A dedicated network connection to AWS'
        ],
        'correct_answer': 'A dedicated network connection to AWS - AWS Direct Connect is a network service provided by AWS that establishes a dedicated network connection between the user’s data center or co-location environment and AWS. It provides private, low-latency connectivity for accessing AWS resources, enabling users to extend their data center to the cloud securely.'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'What is Amazon RDS Aurora?',
        'choices': [
            'A managed NoSQL database service',
            'A fully managed relational database engine',
            'A data warehousing solution',
            'An analytics service'
        ],
        'correct_answer': 'A fully managed relational database engine - Amazon RDS Aurora is a fully managed relational database engine provided by AWS. It is compatible with MySQL and PostgreSQL databases and offers performance, scalability, and reliability enhancements over traditional database engines. Aurora provides features such as high availability, automatic failover, and continuous backup, making it suitable for mission-critical applications.'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'What is AWS CodeDeploy?',
        'choices': [
            'A managed container service',
            'A serverless compute service',
            'A content delivery network',
            'A deployment automation service'
        ],
        'correct_answer': 'A deployment automation service - AWS CodeDeploy is a deployment automation service provided by AWS. It automates the deployment of applications to Amazon EC2 instances, on-premises servers, and serverless Lambda functions. CodeDeploy simplifies the release process, minimizes downtime, and ensures consistent deployments across different environments.'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'What is Amazon SNS used for?',
        'choices': [
            'A managed message queuing service',
            'A serverless compute service',
            'A real-time messaging and communication service',
            'A content delivery network'
        ],
        'correct_answer': 'A real-time messaging and communication service - Amazon SNS (Simple Notification Service) is a fully managed messaging service provided by AWS. It enables users to send notifications and messages to a variety of endpoints, including email, SMS, mobile push, and HTTP endpoints. SNS supports pub/sub and push/pull messaging models, making it suitable for real-time communication and event-driven architectures.'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'What AWS service is used for real-time analytics?',
        'choices': [
            'Amazon Kinesis',
            'Amazon DynamoDB',
            'Amazon RDS',
            'Amazon Redshift'
        ],
        'correct_answer': 'Amazon Kinesis - Amazon Kinesis is a platform for real-time streaming of data at scale. It enables users to collect, process, and analyze streaming data in real time, allowing them to derive insights and take immediate actions. Kinesis supports various use cases, including real-time analytics, log and event data processing, and machine learning model inference.'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'What is AWS CloudFormation?',
        'choices': [
            'A managed container service',
            'A serverless compute service',
            'An infrastructure as code service',
            'A content delivery network'
        ],
        'correct_answer': 'An infrastructure as code service - AWS CloudFormation is an infrastructure as code (IaC) service provided by AWS. It allows users to define and provision AWS infrastructure using declarative templates. CloudFormation automates the deployment and management of resources in a repeatable and predictable manner, enabling infrastructure to be version-controlled and managed as code.'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'What is Amazon DynamoDB?',
        'choices': [
            'A managed NoSQL database service',
            'A fully managed relational database engine',
            'A data warehousing solution',
            'A serverless compute service'
        ],
        'correct_answer': 'A managed NoSQL database service - Amazon DynamoDB is a fully managed NoSQL database service provided by AWS. It offers low-latency, high-performance storage for applications requiring seamless scalability and high availability. DynamoDB supports key-value and document data models, automatic scaling, and built-in security features.'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'What AWS service provides scalable object storage?',
        'choices': [
            'Amazon S3',
            'Amazon EBS',
            'Amazon EFS',
            'Amazon Glacier'
        ],
        'correct_answer': 'Amazon S3 - Amazon S3 (Simple Storage Service) is a scalable object storage service provided by AWS. It allows users to store and retrieve any amount of data from anywhere on the web. S3 provides features such as high availability, durability, and security, making it suitable for a wide range of use cases, including data lakes, backup and archiving, and static website hosting.'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'What is AWS Elastic Beanstalk?',
        'choices': [
            'A managed container service',
            'A serverless compute service',
            'A platform as a service (PaaS)',
            'A content delivery network'
        ],
        'correct_answer': 'A platform as a service (PaaS) - AWS Elastic Beanstalk is a platform as a service (PaaS) provided by AWS. It allows users to deploy and manage web applications and services without worrying about infrastructure configuration. Elastic Beanstalk automatically handles the provisioning, scaling, and monitoring of application resources, enabling developers to focus on writing code.'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'What is AWS S3 Glacier used for?',
        'choices': [
            'Storing and retrieving data over the internet',
            'Data warehousing and analytics',
            'Long-term archival of data',
            'Running virtual servers in the cloud'
        ],
        'correct_answer': 'Long-term archival of data - AWS S3 Glacier is a low-cost storage service provided by AWS for long-term archival of data. It is designed for data that is infrequently accessed and requires long-term retention. Glacier offers features such as data durability, retrieval options, and lifecycle policies for managing data storage costs over time.'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'What is Amazon EC2?',
        'choices': [
            'A managed container service',
            'A serverless compute service',
            'A fully managed relational database engine',
            'A scalable virtual server in the cloud'
        ],
        'correct_answer': 'A scalable virtual server in the cloud - Amazon EC2 (Elastic Compute Cloud) is a scalable virtual server service provided by AWS. It allows users to deploy and manage virtual servers in the cloud, providing resizable compute capacity to meet changing workload demands. EC2 instances can be launched from a variety of pre-configured templates called Amazon Machine Images (AMIs).'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'What is Amazon Athena used for?',
        'choices': [
            'A managed NoSQL database service',
            'A fully managed relational database engine',
            'A serverless interactive query service',
            'An analytics service'
        ],
        'correct_answer': 'A serverless interactive query service - Amazon Athena is a serverless interactive query service provided by AWS. It allows users to analyze data stored in Amazon S3 using standard SQL queries without the need for complex ETL processes or data warehousing solutions. Athena supports ad-hoc querying and interactive analysis of large datasets, enabling users to derive insights quickly.'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'What is AWS Step Functions?',
        'choices': [
            'A managed container service',
            'A serverless compute service',
            'A serverless orchestration service',
            'A content delivery network'
        ],
        'correct_answer': 'A serverless orchestration service - AWS Step Functions is a serverless orchestration service provided by AWS. It allows users to coordinate and automate workflows using visual workflows called state machines. Step Functions enables developers to build resilient and scalable applications by orchestrating multiple AWS services and integrating with custom code.'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'What is Amazon RDS used for?',
        'choices': [
            'A managed NoSQL database service',
            'A fully managed relational database engine',
            'A data warehousing solution',
            'A content delivery network'
        ],
        'correct_answer': 'A fully managed relational database engine - Amazon RDS (Relational Database Service) is a fully managed relational database engine provided by AWS. It allows users to deploy, operate, and scale databases in the cloud without managing the underlying infrastructure. RDS supports popular database engines such as MySQL, PostgreSQL, SQL Server, Oracle, and MariaDB.'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'What is AWS Glue used for?',
        'choices': [
            'Data warehousing',
            'Extract, transform, and load (ETL) jobs',
            'Real-time streaming of data',
            'Object storage'
        ],
        'correct_answer': 'Extract, transform, and load (ETL) jobs - AWS Glue is a fully managed extract, transform, and load (ETL) service provided by AWS. It allows users to prepare and transform data for analytics and machine learning applications by discovering, cataloging, and cleaning datasets. Glue supports serverless ETL jobs, data cataloging, and integration with other AWS services.'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'What is AWS Secrets Manager?',
        'choices': [
            'A managed NoSQL database service',
            'A fully managed relational database engine',
            'A service for storing and managing secrets',
            'A serverless compute service'
        ],
        'correct_answer': 'A service for storing and managing secrets - AWS Secrets Manager is a fully managed service provided by AWS for storing and managing secrets such as API keys, passwords, and database credentials. It enables users to rotate, manage access, and retrieve secrets programmatically, helping secure sensitive information used by applications and services.'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'What is Amazon S3 Glacier Deep Archive?',
        'choices': [
            'A data warehousing solution',
            'Long-term archival storage at the lowest cost',
            'A managed NoSQL database service',
            'A scalable virtual server in the cloud'
        ],
        'correct_answer': 'Long-term archival storage at the lowest cost - Amazon S3 Glacier Deep Archive is an archival storage class provided by AWS for long-term data retention at the lowest cost. It is designed for data that is rarely accessed and requires long-term preservation, such as compliance archives and digital preservation. Glacier Deep Archive offers durability, low-cost storage, and flexible retrieval options.'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'What is AWS Fargate?',
        'choices': [
            'A managed container service',
            'A serverless compute service',
            'A platform as a service (PaaS)',
            'A content delivery network'
        ],
        'correct_answer': 'A serverless compute service - AWS Fargate is a serverless compute service provided by AWS for running containers without managing the underlying infrastructure. It allows users to deploy and manage containers as standalone tasks or services without provisioning or scaling servers. Fargate abstracts away the infrastructure management tasks, enabling developers to focus on building and running containerized applications.'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'What is Amazon DocumentDB?',
        'choices': [
            'A managed NoSQL database service',
            'A fully managed relational database engine',
            'A data warehousing solution',
            'A serverless compute service'
        ],
        'correct_answer': 'A managed NoSQL database service - Amazon DocumentDB is a fully managed NoSQL database service provided by AWS. It is compatible with MongoDB and offers the scalability, performance, and availability of a managed database service. DocumentDB is suitable for applications requiring a flexible, JSON-like document model and ACID transactions.'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'What is AWS IoT Core?',
        'choices': [
            'A managed NoSQL database service',
            'A fully managed relational database engine',
            'An Internet of Things (IoT) platform',
            'A data warehousing solution'
        ],
        'correct_answer': 'An Internet of Things (IoT) platform - AWS IoT Core is an Internet of Things (IoT) platform provided by AWS. It allows users to connect devices to the cloud securely, collect and analyze device data, and build IoT applications at scale. IoT Core provides features such as device management, message brokering, and secure communication protocols.'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'What is Amazon ElastiCache?',
        'choices': [
            'A managed NoSQL database service',
            'A fully managed relational database engine',
            'A caching service',
            'A serverless compute service'
        ],
        'correct_answer': 'A caching service - Amazon ElastiCache is a fully managed caching service provided by AWS. It enables users to deploy and manage in-memory caches in the cloud, improving the performance and scalability of applications. ElastiCache supports popular caching engines such as Redis and Memcached, providing low-latency access to frequently accessed data.'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'What is AWS DataSync?',
        'choices': [
            'A data warehousing solution',
            'A managed data transfer service',
            'A serverless compute service',
            'A content delivery network'
        ],
        'correct_answer': 'A managed data transfer service - AWS DataSync is a managed data transfer service provided by AWS for transferring data between on-premises storage and AWS services. It simplifies and automates data migration, replication, and synchronization tasks, allowing users to move large volumes of data quickly and securely to the cloud.'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'What is AWS Amplify?',
        'choices': [
            'A managed NoSQL database service',
            'A serverless compute service',
            'A platform for building scalable web applications',
            'A content delivery network'
        ],
        'correct_answer': 'A platform for building scalable web applications - AWS Amplify is a platform provided by AWS for building full-stack web and mobile applications. It offers a set of tools and services for frontend and backend development, including authentication, data storage, analytics, and hosting. Amplify simplifies the development process and accelerates time-to-market for modern applications.'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'What is Amazon Kendra?',
        'choices': [
            'A managed NoSQL database service',
            'A serverless compute service',
            'An intelligent search service',
            'A content delivery network'
        ],
        'correct_answer': 'An intelligent search service - Amazon Kendra is an intelligent search service provided by AWS. It enables users to easily search and retrieve information from multiple sources, including documents, databases, and websites. Kendra uses natural language understanding (NLU) and machine learning algorithms to deliver accurate and relevant search results.'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'What is AWS WAF?',
        'choices': [
            'A managed firewall service',
            'A managed NoSQL database service',
            'A fully managed relational database engine',
            'A data warehousing solution'
        ],
        'correct_answer': 'A managed firewall service - AWS WAF (Web Application Firewall) is a managed firewall service provided by AWS. It helps protect web applications from common web exploits and attacks by monitoring and filtering HTTP traffic. WAF allows users to create custom rules, block malicious requests, and mitigate security threats to their web applications.'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'What is Amazon Neptune?',
        'choices': [
            'A managed NoSQL database service',
            'A fully managed relational database engine',
            'A graph database service',
            'A serverless compute service'
        ],
        'correct_answer': 'A graph database service - Amazon Neptune is a fully managed graph database service provided by AWS. It is optimized for storing and querying highly connected datasets, such as social networks, recommendation engines, and fraud detection systems. Neptune supports popular graph models and query languages, making it suitable for building graph-based applications.'
    },

    {
        'id': str(uuid.uuid4()),
        'question': 'What is AWS CloudFormation?',
        'choices': [
            'A service for managing virtual servers in the cloud',
            'A service for automatically scaling web applications',
            'A service for provisioning and managing infrastructure as code',
            'A service for monitoring cloud resources'
        ],
        'correct_answer': 'A service for provisioning and managing infrastructure as code'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'What is Amazon RDS?',
        'choices': [
            'A service for running virtual servers in the cloud',
            'A fully managed relational database service',
            'A service for distributing content globally with low latency',
            'A service for building scalable web applications'
        ],
        'correct_answer': 'A fully managed relational database service'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'What is AWS Lambda?',
        'choices': [
            'A service for managing virtual networks',
            'A service for storing data in a scalable manner',
            'A service for running code in response to events',
            'A service for provisioning virtual machines'
        ],
        'correct_answer': 'A service for running code in response to events'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'What is Amazon ECS?',
        'choices': [
            'A service for storing and retrieving data over the internet',
            'A service for managing containers',
            'A service for distributing content globally with low latency',
            'A service for building scalable web applications'
        ],
        'correct_answer': 'A service for managing containers'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'What is Amazon SNS?',
        'choices': [
            'A service for managing virtual networks',
            'A service for running code in response to events',
            'A service for sending notifications',
            'A service for monitoring cloud resources'
        ],
        'correct_answer': 'A service for sending notifications'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'What is Amazon SQS?',
        'choices': [
            'A service for monitoring cloud resources',
            'A service for storing and retrieving data over the internet',
            'A service for sending notifications',
            'A fully managed message queuing service'
        ],
        'correct_answer': 'A fully managed message queuing service'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'What is Amazon DynamoDB?',
        'choices': [
            'A fully managed relational database service',
            'A service for running code in response to events',
            'A serverless compute service',
            'A fully managed NoSQL database service'
        ],
        'correct_answer': 'A fully managed NoSQL database service'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'What is Amazon Redshift?',
        'choices': [
            'A service for managing virtual servers in the cloud',
            'A service for running code in response to events',
            'A fully managed relational database service',
            'A service for distributing content globally with low latency'
        ],
        'correct_answer': 'A fully managed relational database service'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'What is Amazon Route 53?',
        'choices': [
            'A service for monitoring cloud resources',
            'A service for distributing content globally with low latency',
            'A service for sending notifications',
            'A scalable domain name system (DNS) web service'
        ],
        'correct_answer': 'A scalable domain name system (DNS) web service'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'What is AWS IAM?',
        'choices': [
            'A service for distributing content globally with low latency',
            'A service for managing virtual servers in the cloud',
            'A service for monitoring cloud resources',
            'A service for managing user permissions and access to AWS services'
        ],
        'correct_answer': 'A service for managing user permissions and access to AWS services'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'What is AWS S3?',
        'choices': [
            'A service for distributing content globally with low latency',
            'A service for monitoring cloud resources',
            'A service for storing and retrieving data over the internet',
            'A service for managing user permissions and access to AWS services'
        ],
        'correct_answer': 'A service for storing and retrieving data over the internet'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'What is AWS EBS?',
        'choices': [
            'A service for distributing content globally with low latency',
            'A service for managing user permissions and access to AWS services',
            'A service for monitoring cloud resources',
            'A service for block storage volumes'
        ],
        'correct_answer': 'A service for block storage volumes'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'What is AWS ELB?',
        'choices': [
            'A service for monitoring cloud resources',
            'A service for managing user permissions and access to AWS services',
            'A service for distributing content globally with low latency',
            'A service for automatically distributing incoming application traffic across multiple targets'
        ],
        'correct_answer': 'A service for automatically distributing incoming application traffic across multiple targets'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'What is Amazon Aurora?',
        'choices': [
            'A service for managing virtual servers in the cloud',
            'A service for running code in response to events',
            'A service for distributing content globally with low latency',
            'A MySQL and PostgreSQL-compatible relational database built for the cloud'
        ],
        'correct_answer': 'A MySQL and PostgreSQL-compatible relational database built for the cloud'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'What is Amazon Kinesis?',
        'choices': [
            'A service for monitoring cloud resources',
            'A service for distributing content globally with low latency',
            'A service for managing virtual servers in the cloud',
            'A service for collecting, processing, and analyzing real-time, streaming data'
        ],
        'correct_answer': 'A service for collecting, processing, and analyzing real-time, streaming data'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'What is AWS Glacier?',
        'choices': [
            'A service for managing virtual servers in the cloud',
            'A service for storing data in a scalable manner',
            'A service for archiving long-term data storage',
            'A service for running code in response to events'
        ],
        'correct_answer': 'A service for archiving long-term data storage'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'What is Amazon Cognito?',
        'choices': [
            'A service for managing virtual networks',
            'A service for monitoring cloud resources',
            'A service for sending notifications',
            'A service for securely managing user identities and authentication'
        ],
        'correct_answer': 'A service for securely managing user identities and authentication'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'What is Amazon VPC?',
        'choices': [
            'A service for distributing content globally with low latency',
            'A service for managing virtual servers in the cloud',
            'A service for monitoring cloud resources',
            'A service for provisioning isolated sections of the AWS Cloud'
        ],
        'correct_answer': 'A service for provisioning isolated sections of the AWS Cloud'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'What is AWS Direct Connect?',
        'choices': [
            'A service for monitoring cloud resources',
            'A service for distributing content globally with low latency',
            'A service for securely connecting the AWS cloud with on-premises infrastructure',
            'A service for sending notifications'
        ],
        'correct_answer': 'A service for securely connecting the AWS cloud with on-premises infrastructure'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'What is AWS Elastic Beanstalk?',
        'choices': [
            'A service for monitoring cloud resources',
            'A service for running code in response to events',
            'A service for deploying and scaling web applications',
            'A service for storing and retrieving data over the internet'
        ],
        'correct_answer': 'A service for deploying and scaling web applications'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'What is AWS OpsWorks?',
        'choices': [
            'A service for managing virtual servers in the cloud',
            'A service for provisioning and managing infrastructure as code',
            'A service for monitoring cloud resources',
            'A service for distributing content globally with low latency'
        ],
        'correct_answer': 'A service for provisioning and managing infrastructure as code'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'What is AWS CloudWatch?',
        'choices': [
            'A service for monitoring cloud resources',
            'A service for storing and retrieving data over the internet',
            'A service for managing virtual networks',
            'A service for sending notifications'
        ],
        'correct_answer': 'A service for monitoring cloud resources'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'What is Amazon EMR?',
        'choices': [
            'A service for running code in response to events',
            'A service for monitoring cloud resources',
            'A service for distributing content globally with low latency',
            'A service for processing and analyzing large datasets using open-source tools'
        ],
        'correct_answer': 'A service for processing and analyzing large datasets using open-source tools'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'What is AWS Glue?',
        'choices': [
            'A service for managing virtual networks',
            'A service for monitoring cloud resources',
            'A fully managed extract, transform, and load (ETL) service',
            'A service for sending notifications'
        ],
        'correct_answer': 'A fully managed extract, transform, and load (ETL) service'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'What is Amazon S3 Glacier?',
        'choices': [
            'A service for storing data in a scalable manner',
            'A service for running code in response to events',
            'A service for archiving long-term data storage',
            'A service for managing virtual servers in the cloud'
        ],
        'correct_answer': 'A service for archiving long-term data storage'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'What is AWS Snowball?',
        'choices': [
            'A service for securely connecting the AWS cloud with on-premises infrastructure',
            'A service for monitoring cloud resources',
            'A service for distributing content globally with low latency',
            'A service for transferring large amounts of data into and out of the AWS cloud'
        ],
        'correct_answer': 'A service for transferring large amounts of data into and out of the AWS cloud'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'What is Amazon CloudFront?',
        'choices': [
            'A service for managing virtual networks',
            'A service for sending notifications',
            'A service for distributing content globally with low latency',
            'A service for running code in response to events'
        ],
        'correct_answer': 'A service for distributing content globally with low latency'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'What is AWS Step Functions?',
        'choices': [
            'A service for managing virtual servers in the cloud',
            'A service for orchestrating multiple AWS services into serverless workflows',
            'A service for sending notifications',
            'A service for monitoring cloud resources'
        ],
        'correct_answer': 'A service for orchestrating multiple AWS services into serverless workflows'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'What is AWS CodeDeploy?',
        'choices': [
            'A service for distributing content globally with low latency',
            'A service for managing virtual servers in the cloud',
            'A service for deploying applications to a fleet of EC2 instances',
            'A service for managing user permissions and access to AWS services'
        ],
        'correct_answer': 'A service for deploying applications to a fleet of EC2 instances'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'What is AWS CodePipeline?',
        'choices': [
            'A service for running code in response to events',
            'A service for monitoring cloud resources',
            'A service for distributing content globally with low latency',
            'A service for orchestrating and automating the continuous integration and delivery pipeline'
        ],
        'correct_answer': 'A service for orchestrating and automating the continuous integration and delivery pipeline'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'What is AWS X-Ray?',
        'choices': [
            'A service for monitoring cloud resources',
            'A service for distributing content globally with low latency',
            'A service for analyzing and debugging distributed applications',
            'A service for running code in response to events'
        ],
        'correct_answer': 'A service for analyzing and debugging distributed applications'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'What is AWS IoT?',
        'choices': [
            'A service for managing virtual servers in the cloud',
            'A service for monitoring cloud resources',
            'A service for securely connecting devices to the AWS cloud',
            'A service for distributing content globally with low latency'
        ],
        'correct_answer': 'A service for securely connecting devices to the AWS cloud'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'What is AWS Certificate Manager?',
        'choices': [
            'A service for managing virtual networks',
            'A service for sending notifications',
            'A service for securely managing SSL/TLS certificates',
            'A service for distributing content globally with low latency'
        ],
        'correct_answer': 'A service for securely managing SSL/TLS certificates'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'What is AWS AppSync?',
        'choices': [
            'A service for managing virtual servers in the cloud',
            'A service for building scalable web applications',
            'A service for securely connecting devices to the AWS cloud',
            'A fully managed serverless GraphQL service'
        ],
        'correct_answer': 'A fully managed serverless GraphQL service'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'What is Amazon MQ?',
        'choices': [
            'A service for managing virtual networks',
            'A managed message broker service for Apache ActiveMQ',
            'A service for securely managing user identities and authentication',
            'A service for securely managing SSL/TLS certificates'
        ],
        'correct_answer': 'A managed message broker service for Apache ActiveMQ'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'What is AWS Secrets Manager?',
        'choices': [
            'A service for monitoring cloud resources',
            'A service for securely storing and managing sensitive information',
            'A service for orchestrating and automating the continuous integration and delivery pipeline',
            'A service for securely managing SSL/TLS certificates'
        ],
        'correct_answer': 'A service for securely storing and managing sensitive information'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'What is AWS DataSync?',
        'choices': [
            'A service for securely managing SSL/TLS certificates',
            'A service for securely connecting devices to the AWS cloud',
            'A service for migrating data between on-premises storage and AWS',
            'A service for distributing content globally with low latency'
        ],
        'correct_answer': 'A service for migrating data between on-premises storage and AWS'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'What is Amazon EFS?',
        'choices': [
            'A service for securely managing user identities and authentication',
            'A service for securely connecting devices to the AWS cloud',
            'A service for monitoring cloud resources',
            'A service for scalable file storage for use with Amazon EC2'
        ],
        'correct_answer': 'A service for scalable file storage for use with Amazon EC2'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'What is Amazon WorkSpaces?',
        'choices': [
            'A service for monitoring cloud resources',
            'A service for provisioning and managing cloud-based virtual desktops',
            'A service for securely managing user identities and authentication',
            'A service for securely connecting devices to the AWS cloud'
        ],
        'correct_answer': 'A service for provisioning and managing cloud-based virtual desktops'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'What is AWS Security Hub?',
        'choices': [
            'A service for securely managing user identities and authentication',
            'A service for securely connecting devices to the AWS cloud',
            'A service for monitoring and managing security alerts and compliance',
            'A service for orchestrating and automating the continuous integration and delivery pipeline'
        ],
        'correct_answer': 'A service for monitoring and managing security alerts and compliance'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'What is AWS Transfer Family?',
        'choices': [
            'A service for monitoring and managing security alerts and compliance',
            'A service for securely transferring files over the internet into and out of Amazon S3',
            'A service for securely connecting devices to the AWS cloud',
            'A service for provisioning and managing cloud-based virtual desktops'
        ],
        'correct_answer': 'A service for securely transferring files over the internet into and out of Amazon S3'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'What is AWS Elemental MediaLive?',
        'choices': [
            'A service for monitoring and managing security alerts and compliance',
            'A service for securely transferring files over the internet into and out of Amazon S3',
            'A service for encoding live video for broadcast and streaming to any device',
            'A service for orchestrating and automating the continuous integration and delivery pipeline'
        ],
        'correct_answer': 'A service for encoding live video for broadcast and streaming to any device'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'What is Amazon Kinesis Video Streams?',
        'choices': [
            'A service for securely connecting devices to the AWS cloud',
            'A service for encoding live video for broadcast and streaming to any device',
            'A service for monitoring and managing security alerts and compliance',
            'A service for securely transferring files over the internet into and out of Amazon S3'
        ],
        'correct_answer': 'A service for securely transferring files over the internet into and out of Amazon S3'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'What is AWS CloudTrail?',
        'choices': [
            'A service for monitoring and managing security alerts and compliance',
            'A service for securely transferring files over the internet into and out of Amazon S3',
            'A service for securely connecting devices to the AWS cloud',
            'A service for provisioning and managing cloud-based virtual desktops'
        ],
        'correct_answer': 'A service for monitoring and managing security alerts and compliance'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'What is AWS License Manager?',
        'choices': [
            'A service for monitoring and managing security alerts and compliance',
            'A service for securely transferring files over the internet into and out of Amazon S3',
            'A service for orchestrating and automating the continuous integration and delivery pipeline',
            'A service for managing software licenses and usage'
        ],
        'correct_answer': 'A service for managing software licenses and usage'
    },
       {
        'id': str(uuid.uuid4()),
        'question': 'What is AWS Glue used for?',
        'choices': [
            'A service for managing virtual networks',
            'A fully managed extract, transform, and load (ETL) service',
            'A service for securely connecting devices to the AWS cloud',
            'A service for distributing content globally with low latency'
        ],
        'correct_answer': 'A fully managed extract, transform, and load (ETL) service. AWS Glue is used for ETL processes, making it easy to prepare and load data for analysis.'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'What is Amazon Aurora?',
        'choices': [
            'A service for managing virtual servers in the cloud',
            'A managed relational database service compatible with MySQL and PostgreSQL',
            'A service for orchestrating and automating the continuous integration and delivery pipeline',
            'A service for securely managing user identities and authentication'
        ],
        'correct_answer': 'A managed relational database service compatible with MySQL and PostgreSQL. Amazon Aurora is known for its high performance and scalability.'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'What is AWS Elastic Beanstalk?',
        'choices': [
            'A service for securely transferring files over the internet into and out of Amazon S3',
            'A service for managing virtual servers in the cloud',
            'A fully managed service for deploying and scaling web applications',
            'A service for securely managing SSL/TLS certificates'
        ],
        'correct_answer': 'A fully managed service for deploying and scaling web applications. AWS Elastic Beanstalk abstracts the complexity of managing infrastructure.'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'What is AWS CloudFormation?',
        'choices': [
            'A service for monitoring and managing security alerts and compliance',
            'A service for orchestrating and automating the continuous integration and delivery pipeline',
            'A service for securely transferring files over the internet into and out of Amazon S3',
            'A service for provisioning and managing AWS resources using templates'
        ],
        'correct_answer': 'A service for provisioning and managing AWS resources using templates. AWS CloudFormation allows you to define your infrastructure as code.'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'What is Amazon DynamoDB?',
        'choices': [
            'A service for securely connecting devices to the AWS cloud',
            'A service for monitoring and managing security alerts and compliance',
            'A fully managed NoSQL database service',
            'A service for securely transferring files over the internet into and out of Amazon S3'
        ],
        'correct_answer': 'A fully managed NoSQL database service. Amazon DynamoDB is known for its low-latency and scalable performance.'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'What is AWS Direct Connect?',
        'choices': [
            'A service for monitoring and managing security alerts and compliance',
            'A service for securely transferring files over the internet into and out of Amazon S3',
            'A service for securely connecting the AWS cloud with on-premises infrastructure',
            'A service for orchestrating and automating the continuous integration and delivery pipeline'
        ],
        'correct_answer': 'A service for securely connecting the AWS cloud with on-premises infrastructure. AWS Direct Connect provides dedicated network connections.'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'What is Amazon Kinesis?',
        'choices': [
            'A service for securely transferring files over the internet into and out of Amazon S3',
            'A service for orchestrating and automating the continuous integration and delivery pipeline',
            'A service for monitoring and managing security alerts and compliance',
            'A service for real-time streaming and analytics of large data sets'
        ],
        'correct_answer': 'A service for real-time streaming and analytics of large data sets. Amazon Kinesis enables you to ingest and process real-time data.'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'What is AWS Key Management Service (KMS)?',
        'choices': [
            'A service for securely connecting devices to the AWS cloud',
            'A service for managing virtual servers in the cloud',
            'A service for securely managing user identities and authentication',
            'A service for creating and controlling encryption keys'
        ],
        'correct_answer': 'A service for creating and controlling encryption keys. AWS KMS helps you protect sensitive data by managing cryptographic keys.'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'What is Amazon Elastic Container Service (ECS)?',
        'choices': [
            'A service for securely managing user identities and authentication',
            'A service for securely transferring files over the internet into and out of Amazon S3',
            'A service for running code in response to events',
            'A fully managed container orchestration service'
        ],
        'correct_answer': 'A fully managed container orchestration service. Amazon ECS simplifies the deployment and management of containerized applications.'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'What is AWS Lambda?',
        'choices': [
            'A service for securely transferring files over the internet into and out of Amazon S3',
            'A service for managing virtual servers in the cloud',
            'A service for orchestrating and automating the continuous integration and delivery pipeline',
            'A serverless computing service for running code without provisioning or managing servers'
        ],
        'correct_answer': 'A serverless computing service for running code without provisioning or managing servers. AWS Lambda allows you to run code in response to events.'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'What is Amazon RDS?',
        'choices': [
            'A service for securely transferring files over the internet into and out of Amazon S3',
            'A service for monitoring and managing security alerts and compliance',
            'A service for managing virtual servers in the cloud',
            'A managed relational database service'
        ],
        'correct_answer': 'A managed relational database service. Amazon RDS makes it easy to set up, operate, and scale a relational database in the cloud.'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'What is AWS S3 Transfer Acceleration?',
        'choices': [
            'A service for securely transferring files over the internet into and out of Amazon S3 at lower latency',
            'A service for monitoring and managing security alerts and compliance',
            'A service for orchestrating and automating the continuous integration and delivery pipeline',
            'A service for securely managing user identities and authentication'
        ],
        'correct_answer': 'A service for securely transferring files over the internet into and out of Amazon S3 at lower latency. AWS S3 Transfer Acceleration uses optimized network paths to accelerate uploads and downloads.'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'What is Amazon CloudWatch?',
        'choices': [
            'A service for securely transferring files over the internet into and out of Amazon S3',
            'A service for monitoring and managing security alerts and compliance',
            'A service for managing virtual servers in the cloud',
            'A service for monitoring and managing AWS resources and applications'
        ],
        'correct_answer': 'A service for monitoring and managing AWS resources and applications. Amazon CloudWatch provides metrics, logs, and alarms for your AWS infrastructure.'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'What is AWS IAM?',
        'choices': [
            'A service for securely transferring files over the internet into and out of Amazon S3',
            'A service for managing virtual servers in the cloud',
            'A service for securely managing user identities and authentication',
            'A service for orchestrating and automating the continuous integration and delivery pipeline'
        ],
        'correct_answer': 'A service for securely managing user identities and authentication. AWS IAM enables you to control access to AWS services and resources securely.'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'What is Amazon VPC?',
        'choices': [
            'A service for securely transferring files over the internet into and out of Amazon S3',
            'A service for managing virtual servers in the cloud',
            'A service for securely connecting devices to the AWS cloud',
            'A service for provisioning and managing isolated sections of the AWS cloud'
        ],
        'correct_answer': 'A service for provisioning and managing isolated sections of the AWS cloud. Amazon VPC enables you to launch AWS resources into a virtual network.'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'What is AWS ECS Fargate?',
        'choices': [
            'A service for managing virtual servers in the cloud',
            'A serverless compute engine for containers',
            'A service for securely connecting devices to the AWS cloud',
            'A service for real-time streaming and analytics of large data sets'
        ],
        'correct_answer': 'A serverless compute engine for containers. AWS ECS Fargate allows you to run containers without managing the underlying infrastructure.'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'What is AWS SQS?',
        'choices': [
            'A service for securely transferring files over the internet into and out of Amazon S3',
            'A service for managing virtual servers in the cloud',
            'A fully managed message queuing service',
            'A service for orchestrating and automating the continuous integration and delivery pipeline'
        ],
        'correct_answer': 'A fully managed message queuing service. AWS SQS offers reliable, scalable, and fully managed queues for storing messages.'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'What is Amazon Neptune?',
        'choices': [
            'A service for monitoring and managing security alerts and compliance',
            'A fully managed graph database service',
            'A service for managing virtual servers in the cloud',
            'A service for securely transferring files over the internet into and out of Amazon S3'
        ],
        'correct_answer': 'A fully managed graph database service. Amazon Neptune is optimized for storing and querying highly connected data.'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'What is AWS DMS?',
        'choices': [
            'A service for securely connecting devices to the AWS cloud',
            'A service for managing virtual servers in the cloud',
            'A service for securely transferring files over the internet into and out of Amazon S3',
            'A service for database migration'
        ],
        'correct_answer': 'A service for database migration. AWS DMS helps you migrate databases to AWS quickly and securely.'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'What is Amazon RDS Multi-AZ?',
        'choices': [
            'A service for managing virtual servers in the cloud',
            'A service for securely connecting devices to the AWS cloud',
            'A service for securely transferring files over the internet into and out of Amazon S3',
            'A high-availability feature that provides failover support for RDS instances'
        ],
        'correct_answer': 'A high-availability feature that provides failover support for RDS instances. Amazon RDS Multi-AZ automatically replicates data across multiple Availability Zones.'
    },
        {
        'id': str(uuid.uuid4()),
        'question': 'What is Amazon Redshift?',
        'choices': [
            'A service for securely transferring files over the internet into and out of Amazon S3',
            'A service for managing virtual servers in the cloud',
            'A fully managed data warehouse service',
            'A service for orchestrating and automating the continuous integration and delivery pipeline'
        ],
        'correct_answer': 'A fully managed data warehouse service. Amazon Redshift is optimized for high-performance analysis of large datasets.'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'What is AWS CodePipeline?',
        'choices': [
            'A service for securely transferring files over the internet into and out of Amazon S3',
            'A service for managing virtual servers in the cloud',
            'A service for orchestrating and automating the continuous integration and delivery pipeline',
            'A service for securely managing user identities and authentication'
        ],
        'correct_answer': 'A service for orchestrating and automating the continuous integration and delivery pipeline. AWS CodePipeline helps you automate the build, test, and deployment phases of your release process.'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'What is AWS ECS?',
        'choices': [
            'A service for securely managing user identities and authentication',
            'A service for managing virtual servers in the cloud',
            'A service for securely transferring files over the internet into and out of Amazon S3',
            'A fully managed container orchestration service'
        ],
        'correct_answer': 'A fully managed container orchestration service. Amazon ECS makes it easy to run, stop, and manage Docker containers on a cluster.'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'What is Amazon Route 53?',
        'choices': [
            'A service for securely transferring files over the internet into and out of Amazon S3',
            'A service for managing virtual servers in the cloud',
            'A highly available and scalable domain name system (DNS) web service',
            'A service for orchestrating and automating the continuous integration and delivery pipeline'
        ],
        'correct_answer': 'A highly available and scalable domain name system (DNS) web service. Amazon Route 53 effectively connects user requests to infrastructure running in AWS.'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'What is AWS S3?',
        'choices': [
            'A service for securely transferring files over the internet into and out of Amazon S3',
            'A service for managing virtual servers in the cloud',
            'A highly scalable object storage service',
            'A service for securely managing user identities and authentication'
        ],
        'correct_answer': 'A highly scalable object storage service. Amazon S3 allows customers to store and retrieve any amount of data at any time.'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'What is Amazon EFS?',
        'choices': [
            'A service for securely transferring files over the internet into and out of Amazon S3',
            'A fully managed NoSQL database service',
            'A service for managing virtual servers in the cloud',
            'A fully managed file system for EC2 instances'
        ],
        'correct_answer': 'A fully managed file system for EC2 instances. Amazon EFS provides scalable file storage for use with Amazon EC2 instances in the AWS Cloud.'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'What is AWS CloudFront?',
        'choices': [
            'A service for securely transferring files over the internet into and out of Amazon S3',
            'A service for monitoring and managing security alerts and compliance',
            'A global content delivery network (CDN)',
            'A service for orchestrating and automating the continuous integration and delivery pipeline'
        ],
        'correct_answer': 'A global content delivery network (CDN). Amazon CloudFront accelerates the delivery of web content to users worldwide.'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'What is Amazon SES?',
        'choices': [
            'A service for securely transferring files over the internet into and out of Amazon S3',
            'A service for managing virtual servers in the cloud',
            'A service for securely managing user identities and authentication',
            'A scalable email service for sending and receiving email'
        ],
        'correct_answer': 'A scalable email service for sending and receiving email. Amazon SES simplifies the process of sending marketing, transactional, and notification emails.'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'What is AWS SNS?',
        'choices': [
            'A service for securely transferring files over the internet into and out of Amazon S3',
            'A service for managing virtual servers in the cloud',
            'A fully managed message queuing service',
            'A fully managed publish-subscribe messaging service'
        ],
        'correct_answer': 'A fully managed publish-subscribe messaging service. AWS SNS enables applications, end-users, and devices to instantly send and receive notifications.'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'What is AWS ECR?',
        'choices': [
            'A service for securely transferring files over the internet into and out of Amazon S3',
            'A fully managed container registry service',
            'A service for managing virtual servers in the cloud',
            'A service for orchestrating and automating the continuous integration and delivery pipeline'
        ],
        'correct_answer': 'A fully managed container registry service. Amazon ECR makes it easy to store, manage, and deploy Docker container images.'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'What is AWS Glue?',
        'choices': [
            'A service for securely transferring files over the internet into and out of Amazon S3',
            'A fully managed extract, transform, and load (ETL) service',
            'A service for managing virtual servers in the cloud',
            'A service for securely managing user identities and authentication'
        ],
        'correct_answer': 'A fully managed extract, transform, and load (ETL) service. AWS Glue simplifies and automates the process of preparing and loading data for analytics.'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'What is AWS CodeBuild?',
        'choices': [
            'A service for securely transferring files over the internet into and out of Amazon S3',
            'A fully managed build service for compiling source code and running tests',
            'A service for managing virtual servers in the cloud',
            'A service for orchestrating and automating the continuous integration and delivery pipeline'
        ],
        'correct_answer': 'A fully managed build service for compiling source code and running tests. AWS CodeBuild scales continuously and processes multiple builds concurrently.'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'What is AWS EKS?',
        'choices': [
            'A service for securely transferring files over the internet into and out of Amazon S3',
            'A fully managed Kubernetes service',
            'A service for managing virtual servers in the cloud',
            'A service for orchestrating and automating the continuous integration and delivery pipeline'
        ],
        'correct_answer': 'A fully managed Kubernetes service. AWS EKS makes it easy to deploy, manage, and scale containerized applications using Kubernetes.'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'What is Amazon Aurora?',
        'choices': [
            'A service for securely transferring files over the internet into and out of Amazon S3',
            'A fully managed relational database engine',
            'A service for managing virtual servers in the cloud',
            'A service for orchestrating and automating the continuous integration and delivery pipeline'
        ],
        'correct_answer': 'A fully managed relational database engine. Amazon Aurora is compatible with MySQL and PostgreSQL, offering the performance and availability of commercial databases at a fraction of the cost.'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'What is Amazon EMR?',
        'choices': [
            'A service for securely transferring files over the internet into and out of Amazon S3',
            'A fully managed Hadoop framework for processing big data',
            'A service for managing virtual servers in the cloud',
            'A service for orchestrating and automating the continuous integration and delivery pipeline'
        ],
        'correct_answer': 'A fully managed Hadoop framework for processing big data. Amazon EMR provides a managed cluster platform that simplifies running big data frameworks, such as Apache Hadoop and Apache Spark, on AWS.'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'What is AWS Lambda?',
        'choices': [
            'A service for securely transferring files over the internet into and out of Amazon S3',
            'A serverless compute service that runs your code in response to events',
            'A service for managing virtual servers in the cloud',
            'A service for orchestrating and automating the continuous integration and delivery pipeline'
        ],
        'correct_answer': 'A serverless compute service that runs your code in response to events. AWS Lambda automatically scales your application by running code in response to triggers and events without provisioning or managing servers.'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'What is AWS Step Functions?',
        'choices': [
            'A service for securely transferring files over the internet into and out of Amazon S3',
            'A service for managing virtual servers in the cloud',
            'A serverless orchestration service for coordinating distributed applications',
            'A service for orchestrating and automating the continuous integration and delivery pipeline'
        ],
        'correct_answer': 'A serverless orchestration service for coordinating distributed applications. AWS Step Functions lets you coordinate multiple AWS services into serverless workflows so you can build and update applications quickly.'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'What is Amazon DynamoDB?',
        'choices': [
            'A service for securely transferring files over the internet into and out of Amazon S3',
            'A fully managed NoSQL database service',
            'A service for managing virtual servers in the cloud',
            'A service for orchestrating and automating the continuous integration and delivery pipeline'
        ],
        'correct_answer': 'A fully managed NoSQL database service. Amazon DynamoDB delivers single-digit millisecond performance at any scale.'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'What is AWS Glue DataBrew?',
        'choices': [
            'A service for securely transferring files over the internet into and out of Amazon S3',
            'A visual data preparation tool',
            'A service for managing virtual servers in the cloud',
            'A service for orchestrating and automating the continuous integration and delivery pipeline'
        ],
        'correct_answer': 'A visual data preparation tool. AWS Glue DataBrew is a visual data preparation tool that enables you to clean and normalize data without writing code.'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'What is AWS Amplify?',
        'choices': [
            'A service for securely transferring files over the internet into and out of Amazon S3',
            'A service for building scalable web applications',
            'A service for managing virtual servers in the cloud',
            'A service for orchestrating and automating the continuous integration and delivery pipeline'
        ],
        'correct_answer': 'A service for building scalable web applications. AWS Amplify enables developers to build, deploy, and scale full-stack web applications with ease.'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'What is Amazon Managed Blockchain?',
        'choices': [
            'A service for securely transferring files over the internet into and out of Amazon S3',
            'A fully managed blockchain service',
            'A service for managing virtual servers in the cloud',
            'A service for orchestrating and automating the continuous integration and delivery pipeline'
        ],
        'correct_answer': 'A fully managed blockchain service. Amazon Managed Blockchain makes it easy to create and manage scalable blockchain networks using popular open-source frameworks.'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'What is Amazon ECS Anywhere?',
        'choices': [
            'A service for securely transferring files over the internet into and out of Amazon S3',
            'A service for running containers on-premises and in the cloud',
            'A service for managing virtual servers in the cloud',
            'A service for orchestrating and automating the continuous integration and delivery pipeline'
        ],
        'correct_answer': 'A service for running containers on-premises and in the cloud. Amazon ECS Anywhere allows you to run and manage containerized applications on-premises and in the cloud using the same APIs and tooling.'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'What is AWS Outposts?',
        'choices': [
            'A service for securely transferring files over the internet into and out of Amazon S3',
            'A fully managed database service',
            'A service for managing virtual servers in the cloud',
            'A service for extending AWS infrastructure to on-premises environments'
        ],
        'correct_answer': 'A service for extending AWS infrastructure to on-premises environments. AWS Outposts enables you to run AWS infrastructure on-premises for a truly consistent hybrid experience.'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'What is AWS IoT Core?',
        'choices': [
            'A service for securely transferring files over the internet into and out of Amazon S3',
            'A fully managed internet of things (IoT) service',
            'A service for managing virtual servers in the cloud',
            'A service for orchestrating and automating the continuous integration and delivery pipeline'
        ],
        'correct_answer': 'A fully managed internet of things (IoT) service. AWS IoT Core lets you connect IoT devices to the cloud securely and at scale.'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'What is Amazon ECS Exec?',
        'choices': [
            'A service for securely transferring files over the internet into and out of Amazon S3',
            'A service for securely connecting to containers running on Amazon ECS',
            'A service for managing virtual servers in the cloud',
            'A service for orchestrating and automating the continuous integration and delivery pipeline'
        ],
        'correct_answer': 'A service for securely connecting to containers running on Amazon ECS. Amazon ECS Exec provides interactive shell access to your containers for troubleshooting and debugging.'
    },
        {
        'id': str(uuid.uuid4()),
        'question': 'What is Amazon SageMaker?',
        'choices': [
            'A service for securely transferring files over the internet into and out of Amazon S3',
            'A fully managed machine learning service',
            'A service for managing virtual servers in the cloud',
            'A service for orchestrating and automating the continuous integration and delivery pipeline'
        ],
        'correct_answer': 'A fully managed machine learning service. Amazon SageMaker enables developers to build, train, and deploy machine learning models at scale.'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'What is Amazon Redshift?',
        'choices': [
            'A service for securely transferring files over the internet into and out of Amazon S3',
            'A fully managed relational database service',
            'A service for managing virtual servers in the cloud',
            'A service for orchestrating and automating the continuous integration and delivery pipeline'
        ],
        'correct_answer': 'A fully managed relational database service. Amazon Redshift is a fast, scalable data warehouse that makes it simple and cost-effective to analyze all your data across data warehouses.'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'What is Amazon ElastiCache?',
        'choices': [
            'A service for securely transferring files over the internet into and out of Amazon S3',
            'A fully managed in-memory data store service',
            'A service for managing virtual servers in the cloud',
            'A service for orchestrating and automating the continuous integration and delivery pipeline'
        ],
        'correct_answer': 'A fully managed in-memory data store service. Amazon ElastiCache makes it easy to deploy, operate, and scale in-memory data stores in the cloud.'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'What is Amazon Kinesis?',
        'choices': [
            'A service for securely transferring files over the internet into and out of Amazon S3',
            'A fully managed stream processing service',
            'A service for managing virtual servers in the cloud',
            'A service for orchestrating and automating the continuous integration and delivery pipeline'
        ],
        'correct_answer': 'A fully managed stream processing service. Amazon Kinesis enables you to collect, process, and analyze real-time, streaming data with ease.'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'What is AWS Snowball?',
        'choices': [
            'A service for securely transferring files over the internet into and out of Amazon S3',
            'A fully managed data transport solution',
            'A service for managing virtual servers in the cloud',
            'A service for orchestrating and automating the continuous integration and delivery pipeline'
        ],
        'correct_answer': 'A fully managed data transport solution. AWS Snowball is a petabyte-scale data transport solution that uses secure appliances to transfer large amounts of data into and out of the AWS Cloud.'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'What is AWS Data Pipeline?',
        'choices': [
            'A service for securely transferring files over the internet into and out of Amazon S3',
            'A service for securely connecting on-premises data centers to the cloud',
            'A service for orchestrating and automating the continuous integration and delivery pipeline',
            'A fully managed data integration service'
        ],
        'correct_answer': 'A fully managed data integration service. AWS Data Pipeline helps you reliably process and move data between different AWS services and on-premises data sources.'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'What is Amazon Route 53?',
        'choices': [
            'A service for securely transferring files over the internet into and out of Amazon S3',
            'A service for managing domain names and routing traffic to resources',
            'A service for managing virtual servers in the cloud',
            'A service for orchestrating and automating the continuous integration and delivery pipeline'
        ],
        'correct_answer': 'A service for managing domain names and routing traffic to resources. Amazon Route 53 is a highly available and scalable cloud Domain Name System (DNS) web service.'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'What is AWS CodePipeline?',
        'choices': [
            'A service for securely transferring files over the internet into and out of Amazon S3',
            'A service for managing domain names and routing traffic to resources',
            'A service for orchestrating and automating the continuous integration and delivery pipeline',
            'A fully managed machine learning service'
        ],
        'correct_answer': 'A service for orchestrating and automating the continuous integration and delivery pipeline. AWS CodePipeline is a fully managed continuous integration and continuous delivery (CI/CD) service that automates the build, test, and deploy phases of your release process.'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'What is Amazon CloudWatch?',
        'choices': [
            'A service for securely transferring files over the internet into and out of Amazon S3',
            'A service for managing domain names and routing traffic to resources',
            'A service for monitoring and managing your AWS resources and applications',
            'A fully managed machine learning service'
        ],
        'correct_answer': 'A service for monitoring and managing your AWS resources and applications. Amazon CloudWatch provides monitoring for AWS cloud resources and applications, enabling you to collect and track metrics, collect and monitor log files, set alarms, and automatically react to changes in your AWS resources.'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'What is AWS CloudFormation?',
        'choices': [
            'A service for securely transferring files over the internet into and out of Amazon S3',
            'A service for managing domain names and routing traffic to resources',
            'A service for monitoring and managing your AWS resources and applications',
            'A service for orchestrating and automating the continuous integration and delivery pipeline'
        ],
        'correct_answer': 'A service for managing domain names and routing traffic to resources. Amazon Route 53 is a highly available and scalable cloud Domain Name System (DNS) web service.'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'What is Amazon RDS?',
        'choices': [
            'A service for securely transferring files over the internet into and out of Amazon S3',
            'A fully managed relational database service',
            'A service for monitoring and managing your AWS resources and applications',
            'A service for orchestrating and automating the continuous integration and delivery pipeline'
        ],
        'correct_answer': 'A fully managed relational database service. Amazon RDS makes it easy to set up, operate, and scale a relational database in the cloud.'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'What is AWS Direct Connect?',
        'choices': [
            'A service for securely transferring files over the internet into and out of Amazon S3',
            'A service for securely connecting an on-premises data center to the AWS cloud',
            'A service for monitoring and managing your AWS resources and applications',
            'A service for orchestrating and automating the continuous integration and delivery pipeline'
        ],
        'correct_answer': 'A service for securely connecting an on-premises data center to the AWS cloud. AWS Direct Connect is a cloud service solution that makes it easy to establish a dedicated network connection from your premises to AWS.'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'What is Amazon VPC?',
        'choices': [
            'A service for securely transferring files over the internet into and out of Amazon S3',
            'A service for securely connecting an on-premises data center to the AWS cloud',
            'A service for monitoring and managing your AWS resources and applications',
            'A service for provisioning and managing virtual private networks'
        ],
        'correct_answer': 'A service for provisioning and managing virtual private networks. Amazon VPC lets you provision a logically isolated section of the AWS Cloud where you can launch AWS resources in a virtual network that you define.'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'What is AWS Lambda?',
        'choices': [
            'A service for securely transferring files over the internet into and out of Amazon S3',
            'A service for securely connecting an on-premises data center to the AWS cloud',
            'A service for running code in response to events',
            'A service for orchestrating and automating the continuous integration and delivery pipeline'
        ],
        'correct_answer': 'A service for running code in response to events. AWS Lambda lets you run code without provisioning or managing servers. You pay only for the compute time you consume.'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'What is Amazon ECS?',
        'choices': [
            'A service for securely transferring files over the internet into and out of Amazon S3',
            'A service for deploying and managing containers',
            'A service for managing your AWS resources and applications',
            'A service for orchestrating and automating the continuous integration and delivery pipeline'
        ],
        'correct_answer': 'A service for deploying and managing containers. Amazon ECS is a fully managed container orchestration service that makes it easy to run, stop, and manage containers on a cluster.'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'What is AWS CodeDeploy?',
        'choices': [
            'A service for securely transferring files over the internet into and out of Amazon S3',
            'A service for deploying and managing containers',
            'A service for managing your AWS resources and applications',
            'A service for automating code deployments to any instance, including Amazon EC2 instances and instances running on-premises'
        ],
        'correct_answer': 'A service for automating code deployments to any instance, including Amazon EC2 instances and instances running on-premises. AWS CodeDeploy makes it easier for you to rapidly release new features, helps you avoid downtime during application deployment, and handles the complexity of updating your applications.'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'What is AWS Glue?',
        'choices': [
            'A service for securely transferring files over the internet into and out of Amazon S3',
            'A service for deploying and managing containers',
            'A fully managed extract, transform, and load (ETL) service',
            'A service for automating code deployments to any instance'
        ],
        'correct_answer': 'A fully managed extract, transform, and load (ETL) service. AWS Glue is a fully managed extract, transform, and load (ETL) service that makes it easy to prepare and load your data for analytics.'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'What is AWS Storage Gateway?',
        'choices': [
            'A service for securely transferring files over the internet into and out of Amazon S3',
            'A service for deploying and managing containers',
            'A service for automating code deployments to any instance',
            'A hybrid cloud storage service that enables your on-premises applications to seamlessly use AWS cloud storage'
        ],
        'correct_answer': 'A hybrid cloud storage service that enables your on-premises applications to seamlessly use AWS cloud storage. AWS Storage Gateway is a hybrid cloud storage service that gives you on-premises access to virtually unlimited cloud storage.'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'What is Amazon S3?',
        'choices': [
            'A service for securely transferring files over the internet into and out of Amazon S3',
            'A service for deploying and managing containers',
            'A service for managing your AWS resources and applications',
            'A scalable object storage service'
        ],
        'correct_answer': 'A scalable object storage service. Amazon S3 is designed to store and retrieve any amount of data from anywhere on the web.'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'What is Amazon SQS?',
        'choices': [
            'A service for securely transferring files over the internet into and out of Amazon S3',
            'A service for deploying and managing containers',
            'A service for managing your AWS resources and applications',
            'A fully managed message queuing service'
        ],
        'correct_answer': 'A fully managed message queuing service. Amazon SQS offers a secure, durable, and available hosted queue that lets you integrate and decouple distributed software systems and components.'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'What is Amazon SNS?',
        'choices': [
            'A service for securely transferring files over the internet into and out of Amazon S3',
            'A service for deploying and managing containers',
            'A fully managed message queuing service',
            'A fully managed messaging service for both application-to-application (A2A) and application-to-person (A2P) communication'
        ],
        'correct_answer': 'A fully managed messaging service for both application-to-application (A2A) and application-to-person (A2P) communication. Amazon SNS is a fully managed messaging service for both application-to-application (A2A) and application-to-person (A2P) communication.'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'What is Amazon Aurora?',
        'choices': [
            'A service for securely transferring files over the internet into and out of Amazon S3',
            'A service for deploying and managing containers',
            'A fully managed relational database service',
            'A fully managed message queuing service'
        ],
        'correct_answer': 'A fully managed relational database service. Amazon Aurora is a MySQL and PostgreSQL-compatible relational database built for the cloud, that combines the performance and availability of high-end commercial databases with the simplicity and cost-effectiveness of open-source databases.'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'What is Amazon DynamoDB?',
        'choices': [
            'A service for securely transferring files over the internet into and out of Amazon S3',
            'A service for deploying and managing containers',
            'A fully managed NoSQL database service',
            'A fully managed relational database service'
        ],
        'correct_answer': 'A fully managed NoSQL database service. Amazon DynamoDB is a fast and flexible NoSQL database service for any scale.'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'What is Amazon EMR?',
        'choices': [
            'A service for securely transferring files over the internet into and out of Amazon S3',
            'A service for deploying and managing containers',
            'A fully managed NoSQL database service',
            'A fully managed big data platform'
        ],
        'correct_answer': 'A fully managed big data platform. Amazon EMR is a cloud big data platform for processing large amounts of data using open-source tools such as Apache Hadoop, Apache Spark, Apache HBase, Apache Flink, Apache Hudi, and Presto.'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'What is Amazon Elasticsearch Service?',
        'choices': [
            'A service for securely transferring files over the internet into and out of Amazon S3',
            'A service for deploying and managing containers',
            'A fully managed big data platform',
            'A fully managed service that makes it easy to deploy, operate, and scale Elasticsearch for log analytics, full text search, application monitoring, and more'
        ],
        'correct_answer': 'A fully managed service that makes it easy to deploy, operate, and scale Elasticsearch for log analytics, full text search, application monitoring, and more. Amazon Elasticsearch Service is a fully managed service that makes it easy to deploy, operate, and scale Elasticsearch for log analytics, full text search, application monitoring, and more.'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'What is Amazon Neptune?',
        'choices': [
            'A service for securely transferring files over the internet into and out of Amazon S3',
            'A service for deploying and managing containers',
            'A fully managed graph database service',
            'A fully managed big data platform'
        ],
        'correct_answer': 'A fully managed graph database service. Amazon Neptune is a fast, reliable, fully managed graph database service that makes it easy to build and run applications that work with highly connected datasets.'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'What is Amazon MQ?',
        'choices': [
            'A service for securely transferring files over the internet into and out of Amazon S3',
            'A service for deploying and managing containers',
            'A managed message broker service',
            'A fully managed big data platform'
        ],
        'correct_answer': 'A managed message broker service. Amazon MQ is a managed message broker service for Apache ActiveMQ and RabbitMQ that makes it easy to set up and operate message brokers in the cloud.'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'What is AWS IoT Core?',
        'choices': [
            'A service for securely transferring files over the internet into and out of Amazon S3',
            'A service for deploying and managing containers',
            'A managed message broker service',
            'A managed cloud platform that lets connected devices easily and securely interact with cloud applications and other devices'
        ],
        'correct_answer': 'A managed cloud platform that lets connected devices easily and securely interact with cloud applications and other devices. AWS IoT Core is a managed cloud platform that lets connected devices easily and securely interact with cloud applications and other devices.'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'What is AWS X-Ray?',
        'choices': [
            'A service for securely transferring files over the internet into and out of Amazon S3',
            'A service for deploying and managing containers',
            'A managed cloud platform that lets connected devices easily and securely interact with cloud applications and other devices',
            'A service for debugging, analyzing, and optimizing your applications'
        ],
        'correct_answer': 'A service for debugging, analyzing, and optimizing your applications. AWS X-Ray helps developers analyze and debug production, distributed applications, such as those built using a microservices architecture.'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'What is AWS CloudTrail?',
        'choices': [
            'A service for securely transferring files over the internet into and out of Amazon S3',
            'A service for deploying and managing containers',
            'A managed cloud platform that lets connected devices easily and securely interact with cloud applications and other devices',
            'A service for logging, monitoring, and auditing your AWS infrastructure and services'
        ],
        'correct_answer': 'A service for logging, monitoring, and auditing your AWS infrastructure and services. AWS CloudTrail is a service that enables governance, compliance, operational auditing, and risk auditing of your AWS account.'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'What is AWS Firewall Manager?',
        'choices': [
            'A service for securely transferring files over the internet into and out of Amazon S3',
            'A service for deploying and managing containers',
            'A managed cloud platform that lets connected devices easily and securely interact with cloud applications and other devices',
            'A service that makes it easy to centrally configure and manage AWS WAF rules across your accounts and applications'
        ],
        'correct_answer': 'A service that makes it easy to centrally configure and manage AWS WAF rules across your accounts and applications. AWS Firewall Manager is a security management service that makes it easier to centrally configure and manage AWS WAF rules across your accounts and applications.'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'What is AWS Shield?',
        'choices': [
            'A service for securely transferring files over the internet into and out of Amazon S3',
            'A service for deploying and managing containers',
            'A managed cloud platform that lets connected devices easily and securely interact with cloud applications and other devices',
            'A managed Distributed Denial of Service (DDoS) protection service'
        ],
        'correct_answer': 'A managed Distributed Denial of Service (DDoS) protection service. AWS Shield is a managed Distributed Denial of Service (DDoS) protection service that safeguards applications running on AWS.'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'What is AWS WAF?',
        'choices': [
            'A service for securely transferring files over the internet into and out of Amazon S3',
            'A service for deploying and managing containers',
            'A managed cloud platform that lets connected devices easily and securely interact with cloud applications and other devices',
            'A web application firewall that helps protect web applications from common web exploits'
        ],
        'correct_answer': 'A web application firewall that helps protect web applications from common web exploits. AWS WAF is a web application firewall that helps protect your web applications or APIs against common web exploits that may affect availability, compromise security, or consume excessive resources.'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'What is AWS Artifact?',
        'choices': [
            'A service for securely transferring files over the internet into and out of Amazon S3',
            'A service for deploying and managing containers',
            'A managed cloud platform that lets connected devices easily and securely interact with cloud applications and other devices',
            'A service that provides on-demand access to AWS security and compliance reports and select online agreements'
        ],
        'correct_answer': 'A service that provides on-demand access to AWS\' security and compliance reports and select online agreements. AWS Artifact is a service that provides on-demand access to AWS\' security and compliance reports and select online agreements.'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'What is AWS Organizations?',
        'choices': [
            'A service for securely transferring files over the internet into and out of Amazon S3',
            'A service for deploying and managing containers',
            'A managed cloud platform that lets connected devices easily and securely interact with cloud applications and other devices',
            'A service that enables you to centrally manage and govern your environment as you grow and scale your AWS resources'
        ],
        'correct_answer': 'A service that enables you to centrally manage and govern your environment as you grow and scale your AWS resources. AWS Organizations is a service that enables you to centrally manage and govern your environment as you grow and scale your AWS resources.'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'What is AWS Secrets Manager?',
        'choices': [
            'A service for securely transferring files over the internet into and out of Amazon S3',
            'A service for deploying and managing containers',
            'A managed service to help you protect access to your applications, services, and IT resources without the upfront investment and on-going maintenance costs of operating your own infrastructure',
            'A service for managing and deploying SSL/TLS certificates for use with AWS services'
        ],
        'correct_answer': 'A managed service to help you protect access to your applications, services, and IT resources without the upfront investment and on-going maintenance costs of operating your own infrastructure. AWS Secrets Manager helps you protect access to your applications, services, and IT resources without the upfront investment and on-going maintenance costs of operating your own infrastructure.'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'What is AWS Systems Manager?',
        'choices': [
            'A service for securely transferring files over the internet into and out of Amazon S3',
            'A service for deploying and managing containers',
            'A managed service to help you protect access to your applications, services, and IT resources without the upfront investment and on-going maintenance costs of operating your own infrastructure',
            'A service for gaining operational insights and taking action on AWS resources'
        ],
        'correct_answer': 'A service for gaining operational insights and taking action on AWS resources. AWS Systems Manager gives you visibility and control of your infrastructure on AWS. Systems Manager provides a unified user interface so you can view operational data from multiple AWS services and allows you to automate operational tasks across your AWS resources.'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'What is AWS Certificate Manager?',
        'choices': [
            'A service for securely transferring files over the internet into and out of Amazon S3',
            'A service for deploying and managing containers',
            'A managed service to help you protect access to your applications, services, and IT resources without the upfront investment and on-going maintenance costs of operating your own infrastructure',
            'A service for managing and deploying SSL/TLS certificates for use with AWS services'
        ],
        'correct_answer': 'A service for managing and deploying SSL/TLS certificates for use with AWS services. AWS Certificate Manager is a service that lets you easily provision, manage, and deploy public and private Secure Sockets Layer/Transport Layer Security (SSL/TLS) certificates for use with AWS services and your internal connected resources.'
    }
]


