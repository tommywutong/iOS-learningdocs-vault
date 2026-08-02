---
title: 'Regions: region monitoring, significant location changes, background location
  service, location service authorization'
apple_id: DTS40010726
resource_type: Sample Code
platform: iOS
topic: User Experience
technology: null
published: '2016-02-11'
source_url: https://developer.apple.com/library/archive/samplecode/Regions/Introduction/Intro.html
archived_at: '2026-07-18T03:22:05.092452Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](Regions-main.m.md)

# Regions: region monitoring, significant location changes, background location service, location service authorization

|  |  |
| --- | --- |
| __Last Revision:__ | Version 3.1, 2016-02-11 Updated for iOS 8.0. [(Full Revision History)](Document%20Revision%20History.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytanzsgywvezlwnfzws33ojbuxg5dpoj4s2rdpnz2ey2lonncwyzlnmvxhiskel4yq) |
| __Build Requirements:__ | iOS 8.0 SDK or later |
| __Runtime Requirements:__ | iOS 8.0 or later |

This sample demonstrates proper use of region monitoring, significant location changes, and handling location events in the background on iOS.

The sample uses an MKMapView that allows the user to add and remove regions to monitor, as well as a UITableView to display the region enter/exit/fail events that occur.

When the application goes into the background, location updates are stopped and significant location changes are started. Likewise, when the application enters the foreground, location updates are started again and significant location changes are stopped.

When location updates occur in the background, a badge is added to the homescreen icon displaying the number of region enter/exit/fail events logged.

[Next](Regions-main.m.md)

