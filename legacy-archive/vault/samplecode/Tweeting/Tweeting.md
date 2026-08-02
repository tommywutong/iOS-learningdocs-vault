---
title: Tweeting
apple_id: DTS40011191
resource_type: Sample Code
platform: iOS
topic: General
technology: Twitter
published: '2011-10-12'
source_url: https://developer.apple.com/library/archive/samplecode/Tweeting/Introduction/Intro.html
archived_at: '2026-07-18T03:27:23.877128Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](ReadMe.txt.md)

# Tweeting

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.0, 2011-10-12 This sample demonstrates the built-in Twitter composition sheet, creating a POST request, and parsing returned data. |
| __Build Requirements:__ | Xcode 4.1 or later on OS X Snow Leopard or Xcode 4.2 or later on OS X Lion |
| __Runtime Requirements:__ | iOS 5.0 or later |

By using the Twitter framework, Accounts framework, and the NSJSONSerialization class, this sample demonstrates using the built-in Twitter composition sheet, creating a custom POST request, and downloading the public timeline from Twitter.

The "Send Easy Tweet" button checks if a Twitter account is present on the device and creates a pre-populated TWTweetComposeViewController. This also handles the "cancel" and "send" actions from the TWTweetComposeViewController.

The "Send Custom Tweet" button utilizes the Accounts framework to create an instance of the account store on the device and then find all Twitter accounts present. In this example, the first Twitter ACAccount object found is used to pre-populate a tweet and uses a TWRequest to post the tweet using the Twitter API. This example also handles the returned response data and http response.

The "Get Public Timeline" button creates a TWRequest to get the current public timeline using the Twitter API. The response data is then converted from JSON data to an NSDictionary, using the NSJSONSerialization class.

[Next](ReadMe.txt.md)

