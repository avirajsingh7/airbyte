# Avni

This page contains the setup guide and reference information for the Awtomic source connector.

## Prerequisites

- Your own Awtomic Account

## Setup guide

### Step 1: Set up an Awtomic account

1. Signup on [Awtomic](https://www.awtomic.com/) to create an account.

### Step 2: Set up the Avni connector in Airbyte

**For Airbyte Open Source:**

1. Go to local Airbyte page.
2. In the left navigation bar, click **Sources**. In the top-right corner, click **+ New Source**.
3. On the source setup page, select **Awtomic** from the Source type dropdown and enter a name for this connector.
4. Enter the **ApiKey**s of your Awtomic account
5. Click **Set up source**.

## Supported sync modes

The Awtomic source connector supports the following[ sync modes](https://docs.airbyte.com/cloud/core-concepts#connection-sync-modes):
​

- [Full Refresh - Overwrite](https://docs.airbyte.com/understanding-airbyte/connections/full-refresh-overwrite)
- [Full Refresh - Append](https://docs.airbyte.com/understanding-airbyte/connections/full-refresh-append)

## Supported Streams

Awtomic Source connector Support Following Streams:

- **Subscriptions Stream** : This stream retrieve all the subscriptions for the shop.
- **Subscription Contract Stream** : This stream help in getting a subscription contract, the lines will be returned in the response.

## Changelog

| Version | Date | Pull Request | Subject |
| 0.1.0   | 2024-04-16 | []()   |  Amtomic Source Connector |