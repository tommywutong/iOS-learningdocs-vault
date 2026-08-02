---
title: Controlling The Location Services Status Bar (Blue Bar) From Your App
apple_id: DTS40017676
resource_type: QA
platform: iOS
topic: null
technology: CoreLocation
published: '2017-09-05'
source_url: https://developer.apple.com/library/archive/qa/qa1965/_index.html
archived_at: '2026-07-18T02:38:00.890133Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1965

# Controlling The Location Services Status Bar (Blue Bar) From Your App

## Q:  How do I turn on or off the Location Services Status Bar (Blue Bar) for my app while it is in the background.

A: The Location Services Status Bar (Blue Bar) will be displayed for apps using Continuous Location Updates in the background.

Once an app starts the Continuous Location Updates in the foreground, and then is sent to the background, if the app is configured to continue receiving Continuous Background Location Updates, iOS may show the Blue Bar, indicating the app is receiving location updates in the background.

Starting with iOS 11, apps have more control over the appearance of the Location Services Status Bar (Blue Bar) for their apps.

Apps which are given __When-in-use authorization__ by the users (regardless of the authorization asked for), will automatically get the Blue Bar displayed. Apps cannot opt out of the Blue Bar if they are only given __When-in-use authorization__ by the users.

Apps which are given __Always authorization__, on the other hand, will get the Blue Bar displayed based on a new property of the CLLocationManager object.

`@property(assign, nonatomic) BOOL showsBackgroundLocationIndicator;`

Apps which have their Continuous Background Location session active, and have obtained __Always authorization__ the Blue Bar will be shown only when the `showsBackgroundLocationIndicator` property is __YES__.

An app can toggle the `showsBackgroundLocationIndicator` property to change the visibility of the blue bar at any time.

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2017-09-05 | New document that explains how apps can control the Location Services Status Bar (Blue Bar) to be displayed or hidden when using Continuous Background Location Updates |

