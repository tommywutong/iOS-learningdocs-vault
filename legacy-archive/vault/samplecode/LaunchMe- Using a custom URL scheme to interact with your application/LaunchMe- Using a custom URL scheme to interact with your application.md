---
title: 'LaunchMe: Using a custom URL scheme to interact with your application'
apple_id: DTS40007417
resource_type: Sample Code
platform: iOS
topic: Data Management
technology: null
published: '2017-02-11'
source_url: https://developer.apple.com/library/archive/samplecode/LaunchMe/Introduction/Intro.html
archived_at: '2026-07-18T03:13:27.311690Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](LaunchMe-main.m.md)

# LaunchMe: Using a custom URL scheme to interact with your application

|  |  |
| --- | --- |
| __Last Revision:__ | Version 5.0, 2017-02-11 Upgraded to iOS 10.0 SDK, expanded URL scheme, improved user interface. [(Full Revision History)](Document%20Revision%20History.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydonbrg4wvezlwnfzws33ojbuxg5dpoj4s2rdpnz2ey2lonncwyzlnmvxhiskel4yq) |
| __Build Requirements:__ | iOS 10.0 SDK or later |
| __Runtime Requirements:__ | iOS 10.0 or later |

The LaunchMe sample application demonstrates how to implement a custom URL scheme to allow other applications to interact with your application. It registers the "launchme" URL scheme, of which the URL contains an HTML color code (for example, #FF0000 or #F00) and text data. The sample shows how to handle an incoming URL request by overriding -application:openURL:sourceApplication:annotation: to properly parse and extract information from the requested URL before updating the user interface.

[Next](LaunchMe-main.m.md)

