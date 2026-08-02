---
title: Revenue Reporting API for News Publishers
apple_id: TP40016970
resource_type: Guide
platform: iAd System JS|iAd Producer|iOS
topic: General
technology: null
published: '2016-08-12'
source_url: https://developer.apple.com/library/archive/documentation/General/Conceptual/iAd_News_Revenue_API/Document/Revenue_Ch2_SummaryOfMethods.html
archived_at: '2026-07-15T07:34:29.580304Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Revenue Reporting API for News Publishers](Revenue%20API%20for%20News%20Publishers%20%E2%80%94%20Overview.md)


[Next](Authentication.md)[Previous](Revenue%20API%20for%20News%20Publishers%20%E2%80%94%20Overview.md)

# Summary of Revenue API for News Publishers Methods

The iAd News Publishers API methods are presented here by the workflow phase in which they are used. The following chapters of this document provide details of these methods, specifying input and output parameters and providing sample code.

The `InitSession` method must be used before every API interaction session to obtain a session ID that will be used with all subsequent calls during the session.

| Method Name | Description |
| --- | --- |
| `InitSession` | Use the `InitSession` procedure to initiate access and get a session ID. |

| Method Name | Description |
| --- | --- |
| `GetChannelMetrics` | This method allows you to get Revenue, Supply, Fill Rate, Impressions, and Taps by:   - Channel - Date - Country - Device type |
| `GetChannelMetricsByCreativeType` | This method allows you to get Revenue, Impressions, and Taps by:   - Channel - Date - Creative type |

[Next](Authentication.md)[Previous](Revenue%20API%20for%20News%20Publishers%20%E2%80%94%20Overview.md)

