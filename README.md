# :green_book: Home Assigment (Data Engineering case study :beginner:)

This repository contains a soluton for **some** company `Assignment - Enterprise-Ready Data Platform`. I have a next task description, limitantions, and requirements.

---
### Design a cloud-based data platform that provides data to the following:
- Decision Services that provide risk assessment during the customer journey to checkout
- Data Scientists that need to understand and discover attributes to train the models for fraud model
- Analysts that need current and historical data for reporting and dashboard to respond to historical fraud cases
Since the decision services are a critical part of the customer journey, the provision of data must be considered mission-critical.
An additional consideration is that, by expanding in different markets, Billie’s business logic and data are subject to changes that must be faced in the least time possible. Consider such a scenario and describe/design a solution to mitigate potential issues
### Boundaries:
- The solution must consider budget/capacity constraints
- You can choose any cloud vendor/solution given the above considerations
- Chose a technology which you would be confident to code on
- The design can be presented in any format as long as it clearly exposes the solution
- We want a real-time solution
### Requirements:
- Data for the decision Service must be free from duplicates and irregular values
- Data for the decision Services have to be enriched with data from slow-changing dimensions sources
- No data shall be lost in case of disaster
---

### My opinion and Solution
Since I work mostly with historical data using `Python`, `Spark`, and `Azure` and `Kafka`,`HDFS` I will try to use it. (I will check first if I can use Spark-Stream with Azurem if not i will switch to Flink)
So after analysing the given requirements I have create next plan to implement it till 23.09.2024 :warning:

-  First sttep would be: Use Kafka to store all incomming data I will assume that i have incomming transacation data that is stored in json.
-  Use Kafka as input source to Azure Data Factory and write there cleaning logic (remove duplicates, replace/delete irregular values).
-  As for storage I will store in some db or warehouse with slow-change dimension with mix of SCD Type 1 and Type 2).
