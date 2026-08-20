---
title: AirDrop Examples
apple_id: DTS40013842
resource_type: Sample Code
platform: iOS
topic: null
technology: null
published: '2013-10-17'
source_url: https://developer.apple.com/library/archive/samplecode/sc2273/Introduction/Intro.html
archived_at: '2026-07-26T19:54:10.840899Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](ReadMe.txt.md)

# AirDrop Examples

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.0, 2013-10-17 "AirDropSample" illustrates three scenarios for incorporating AirDrop into an app. |
| __Build Requirements:__ | Xcode 5.0, iOS SDK 7.0 |
| __Runtime Requirements:__ | iOS 7.0 |

"AirDropSample" demonstrates three use cases for incorporating AirDrop into an app.

1) Sending/receiving a URL with a custom scheme via AirDrop

URLs can be used as a simple way to transfer information between devices. Apps can easily parse a received URL to determine what action to take. After an app registers a URL scheme (including custom schemes), the system will know to launch that app when a URL of that type is received.

2) Sending/receiving an instance of a custom class as data via AirDrop

Often an app will want to send some data it has, for instance a serialized object, to another device. Apps can easily do this by attaching a UTI to that data, and then registering to accept that UTI on the receiving side.

3) Asynchronously preprocessing content after the user decides to send via AirDrop

There are certain circumstances when a piece of content needs to be preprocessed before a send. The APIs allow for this preprocessing to happen asynchronously.

[Next](ReadMe.txt.md)

