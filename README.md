# CogVideoDemo

Code that builds out a demo using several Azure technologies including: 

1)  Azure Databricks
2)  Azure Cognitive Services Containerized 
3)  Azure Blob Storage  

The demo builds a pipeline that analyzes videos (without the video indexer) by using the Azure Cognitive Services Face API to mark facial landmarks and evaluate emotion over a time frame.   It uses a pre-built model using Torch (link here), to evaluate and compare the results over time in the analysis section.   

It also emplyos the Speech Service to correlate transcribed speech to emotion over time.   

This demo is to illustrate potential uses of Databricks with cogntive services and custom modeling algorithms.  

Directions on building the demo are held in a private teams site, this repository is only for code artifacts
