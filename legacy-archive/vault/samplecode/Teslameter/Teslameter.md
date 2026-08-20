---
title: Teslameter
apple_id: DTS40008931
resource_type: Sample Code
platform: iOS
topic: null
technology: CoreLocation
published: '2014-08-25'
source_url: https://developer.apple.com/library/archive/samplecode/Teslameter/Introduction/Intro.html
archived_at: '2026-07-18T03:26:24.804503Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](ReadMe.txt.md)

# Teslameter

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.3, 2014-08-25 Upgraded for the iOS 7 SDK, adopts current best practices for Objective-C (including use of properties, autosynthesis, and literals), now uses Storyboards and ARC (Automatic Reference Counting). [(Full Revision History)](Document%20Revision%20History.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydqojtgewvezlwnfzws33ojbuxg5dpoj4s2rdpnz2ey2lonncwyzlnmvxhiskel4yq) |
| __Build Requirements:__ | iOS 7.0 SDK or later |
| __Runtime Requirements:__ | iOS 6.0 or later, requires a device with a magnetometer. This sample will run in the Simulator but only one magnetic measurement will be received. |

This application implements a Teslameter, a magnetic field detector. It displays the raw x, y, and z magnetometer values, a plotted history of those values, and a computed magnitude (size or strength) of the magnetic field.

The use of the Core Location API for getting "heading" data is contained in the TeslameterViewController class. It creates a CLLocationManager object and uses it to get heading by invoking -[CLLocationManager startUpdatingHeading]. It implements the CLLocationManagerDelegate APIs for receiving heading and updates its user interface accordingly.

[Next](ReadMe.txt.md)

