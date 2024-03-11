---
layout: post
title: "dynamo and lock"
author: "Ray"
header-style: text
tags:
  - dynamo
date: 2022-05-10
---
* Lock
** Optimistic Locking
*** With Optimistic Locking, there is always one attribute in your DynamoDB table that will act as a "/version number./" It can be a nano-id, an integer, or a timestamp. The version number associated with the record must also be sent when clients request data.
*** When client modifies the data. The version number present on the client side must be the same as the item's version number present in the table item. If it is the same, it means that no other user has changed the record, allowing the write to go through. However, if the version numbers are different, it's likely that another user has already updated the record, causing DynamoDB to reject your write by throwing the exception - ~ConditionalCheckFailedException~. You can retrieve the item again (with newly updated data) and retry your update when this happens.
** Pessimistic Locking
*** Pessimistic Locking is another strategy used by DynamoDB to prevent concurrent updates to a particular row. It use DynamoDB Transactions API
*** typescript
#+BEGIN_SRC typescript
const AWS = require("aws-sdk");
const dynamoDB = new AWS.DynamoDB.DocumentClient({ region:'us-east-1' });

await dynamoDB.transactWrite({
  TransactItems: [
    {
      Put: { // Write an item to the Cart table
        Item: { // Actual Item
          id: '777',
          count: '1',
          description: 'Lorem ipsum...'
        }
        TableName: "Cart",
      },
    },
    {
      Update: { // Decrement count of items available to buy only if the count is greater than zero
        ConditionExpression: "#count > 0",
        ExpressionAttributeNames: { "#count": "count" },
        ExpressionAttributeValues: {
         ":value": 1,
        },
        Key: {
         id: '777-000',
        }
        TableName: "Items",
        UpdateExpression: "SET #count = :count - :value",
        },
      },
    ],
  }).promise();

#+END_SRC
* Benefits of Optimistic Locking
**
