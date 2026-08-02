---
title: Revenue Reporting API for News Publishers
apple_id: TP40016970
resource_type: Guide
platform: iAd System JS|iAd Producer|iOS
topic: General
technology: null
published: '2016-08-12'
source_url: https://developer.apple.com/library/archive/documentation/General/Conceptual/iAd_News_Revenue_API/Document/Revenue_Ch4_RevenueMethods.html
archived_at: '2026-07-15T07:34:29.616343Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Revenue Reporting API for News Publishers](Revenue%20API%20for%20News%20Publishers%20%E2%80%94%20Overview.md)


[Next](Document%20Revision%20History.md)[Previous](Authentication.md)

# Revenue Methods

The Revenue API for News Publishers methods described in this document provides programmatic access to the iAd ad server to do the same kinds of tasks as you would do with the iAd [Workbench for News Publishers](https://iadworkbench.apple.com/):

- `GetChannelMetrics` — Obtain revenue performance metrics by channel.
- `GetChannelMetricsByCreativeType` — Obtain revenue performance metrics by creative (ad) type.

When requesting data, be aware of the following:

- You can request data for the following intervals within past 12 months:

  - Hourly: one day only.
  - Daily: up to 7 consecutive days.

This method allows you to get Revenue, Supply, Fill Rate, Impressions, and Taps by:

- Channel
- Date
- Country
- Device type

| Parameter | Type | Required / Optional | Comments |
| --- | --- | --- | --- |
| `SessionID` | String (Alphanumeric) | Required | Session ID obtained from InitSession call. |
| `ChannelIds` | List of Strings | Required | List of full UUIDs (not minified) of up to 10 channels. These are the UUIDs returned by the News Campaign API method `GetTargetingDetails` in the `TargetingDimensons: DimentionsName: Channels` output. |
| `StartTime` | String (date) | Required | Start date of report period, formatted as yyyy-mm-dd. |
| `EndTime` | String (date) | Required | End date of report period, formatted as yyyy-mm-dd. |
| `Timezone` | String | Optional | Must be either `UTC` (Coordinated Universal Time, GMT) or `ATZ` (Account Time Zone, determined from your account settings). Default is `UTC`. |
| `Interval` | String | Required | Must be either `Hourly` or `Daily`. |

__Listing 4-1__  GetChannelMetrics Sample Input

```
{
  "method":"GetChannelMetrics",
  "id":"1001",
  "params":{
    "SessionId":"04df16280af800092be3d638c28db00666164f36",
    "ChannelIds":[
      "9ae04346-233b-445f-8466-26d708a16ec1],
    "StartTime":"2015-12-08",
    "EndTime":"2015-12-09",
    "Interval":"Daily"
  },
  "jsonrpc":"2.0"
}
```


| Parameter | Type | Comments |
| --- | --- | --- |
| `Metrics` | Collection | Collection of revenue metrics parameters and values. |
| `Metrics: ChannelId` | String | Full channel UUID for each channel output returned. |
| `Metrics: ChannelName` | String | Channel name for each channel output returned. |
| `Metrics: Country` | String | Two-character country code, “AU”, “GB”, or “US”. |
| `Metrics: AdPosition` | String | All potential Ad positions. |
| `Metrics: DeviceClass` | String | Type of device. The only device types are `iPhone` and `iPad`. |
| `Metrics: DateTime` | String | For `Hourly`, the value will be the date and hour: yyyy-mm-dd hh:mm  For `Daily`, the value is the date: yyyy-mm-dd hh:mm |
| `Metrics: TimeZone` | String | Will be either `UTC` (Coordinated Universal Time, GMT) or `ATZ` (Account Time Zone, determined from your account settings). Default is `UTC`. |
| `Metrics: Taps` | String | Number of times users have tapped on ads. |
| `Metrics: iAdBackfillCPM` | String | Estimated revenue per thousand clicks. |
| `Metrics: iAdBackfillImpressions` | String | Number of times that iAd backfill ads appeared in your channels. |
| `Metrics: DirectSoldImpressions` | String | Number of times that direct-sold ads appeared in your channels. |
| `Metrics: HouseImpressions` | String | Number of times that in-house ads appeared in your channels. |
| `Metrics: TTR` | String | Tap-through rate. |
| `Metrics: iAdBackfillRevenue` | String | Revenue from iAd backfill ads displayed. |
| `Metrics: Supply` | String | The number of ad requests that are eligible for ads. Some ad requests might be ineligible for a variety of reasons. Supply is an indication of the maximum number of ad impressions that could have been delivered during the reporting time period.. |
| `Metrics: FillRate` | String | The ratio of total impressions to the total supply, in percent. |
| `Success` | Boolean | `true` or `false`, depending on whether the call succeeded or not. |

__Listing 4-2__  GetChannelMetrics Sample Output

```json
{
  "id": "1001",
  "jsonrpc": "2.0",
  "result":
  {
    "Metrics":
    [
      {
        "ChannelId": "9ae04346-233b-445f-8466-26d708a16ec1",
        "ChannelName": "GQ",
        "Country": "US",
        "DeviceClass": "iPhone",
        "DateTime": "2015-12-08 00:00:00",
        "Taps": "1",
        "eCPM": "0.00",
        "iAdImpressions": "0",
        "TTR": "1429.00",
        "Revenue": "0.00",
        "Supply": "7",
        "FillRate": "100.00",
        "DirectSoldImpressions": "0",
        "HouseImpressions": "0",
        "AdPosition": "In Feed"
      }
    ],
    "Success": true
  }
}
```


This method allows you to get Revenue, Impressions, and Taps by:

- Channel
- Date
- Creative type

Note that the input parameters are the same as `GetChannelMetrics`. The difference in the method name provides a different set of output.

| Parameter | Type | Required / Optional | Comments |
| --- | --- | --- | --- |
| `SessionID` | String (Alphanumeric) | Required | Session ID obtained from InitSession call. |
| `ChannelIds` | List of Strings | Required | List of full UUIDs (not minified) of up to 10 channels. These are the UUIDs returned by the News Campaign API method `GetTargetingDetails` in the `TargetingDimensons: DimentionsName: Channels` output. |
| `StartTime` | String (date) | Required | Start date of report period, formatted as yyyy-mm-dd. |
| `EndTime` | String (date) | Required | End date of report period, formatted as yyyy-mm-dd. |
| `Timezone` | String | Optional | Must be either `UTC` (Coordinated Universal Time, GMT) or `ATZ` (Account Time Zone, determined from your account settings). Default is `UTC`. |
| `Interval` | String | Required | Must be either `Hourly` or `Daily`. |

__Listing 4-3__  GetChannelMetricsByCreativeType Sample Input

```json
{
  "method":"GetChannelMetricsByCreativeType",
  "id":"1001",
  "params":{
    "SessionId":"faffb41b6ab628ea8998a77af1d9b8ae694f107a",
    "ChannelIds":[
      "9ae04346-233b-445f-8466-26d708a16ec1"
    ],
    "StartTime":"2015-12-09",
    "EndTime":"2015-12-0",
    "Interval":"Daily"
  },
  "jsonrpc":"2.0"
}
```


| Parameter | Type | Comments |
| --- | --- | --- |
| `Metrics` | Collection | Collection of revenue metrics parameters and values. |
| `Metrics: ChannelId` | String | Full channel UUID for each channel output returned. |
| `Metrics: ChannelName` | String | Channel name for each channel output returned. |
| `Metrics: Country` | String | Two-character country code, “AU”, “GB”, or “US”. |
| `Metrics: AdPosition` | String | All potential ad positions. |
| `Metrics: DeviceClass` | String | Type of device. The only device types are `iPhone` and `iPad`. |
| `Metrics: CreativeType` | String | A different `CreativeType` value will be provided to identify each `Dim` structure returned. |
| `Metrics: DateTime` | String | For hourly, the value will be the date and hour: yyyy-mm-dd hh:mm  For daily, the value is the date: yyyy-mm-dd hh:mm |
| `Metrics: TimeZone` | String | Will be either `UTC` (Coordinated Universal Time, GMT) or `ATZ` (Account Time Zone, determined from your account settings). Default is `UTC`. |
| `Metrics: Taps` | String | Number of times users have tapped on ads. |
| `Metrics: iAdBackfillCPM` | String | Estimated revenue per thousand clicks. |
| `Metrics: iAdBackfillImpressions` | String | Number of times that iAd backfill ads appeared in your channels. |
| `Metrics: DirectSoldImpressions` | String | Number of times that direct-sold ads appeared in your channels. |
| `Metrics: HouseImpressions` | String | Number of times that in-house ads appeared in your channels. |
| `Metrics: TTR` | String | Tap-through rate. |
| `Metrics: iAdBackfillRevenue` | String | Revenue from iAd backfill ads displayed. |
| `Success` | Boolean | `true` or `false` depending on whether the call succeeded or not. |

__Listing 4-4__  GetChannelMetricsByCreativeType Sample Output

```json
{
  "id": "1001",
  "jsonrpc": "2.0",
  "result":
  {
    "Metrics":
    [
      {
        "ChannelId": "9ae04346-233b-445f-8466-26d708a16ec1",
        "ChannelName": "GQ",
        "Country": "US",
        "CreativeType": "Double Banner",
        "DeviceClass": "iPad",
        "DateTime": "2015-12-09 00:00:00",
        "Taps": "1",
        "eCPM": "0.00",
        "iAdImpressions": "0",
        "TTR": "10000.00",
        "Revenue": "0.00",
        "DirectSoldImpressions": "1",
        "HouseImpressions": "0",
        "AdPosition": "In Feed"
      }
    ],
    "Success": true
  }
}
```

[Next](Document%20Revision%20History.md)[Previous](Authentication.md)

