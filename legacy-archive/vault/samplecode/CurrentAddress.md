---
title: CurrentAddress
apple_id: DTS40009469
resource_type: Sample Code
platform: iOS
topic: User Experience
technology: MapKit
published: '2016-01-28'
source_url: https://developer.apple.com/library/archive/samplecode/CurrentAddress/Introduction/Intro.html
archived_at: '2026-07-27T06:57:01.772463Z'
---
> 导航：[总目录](../README.md) · [samplecode](../_indexes/samplecode.md)



# CurrentAddress

|  |  |
| --- | --- |
| __Last Revision:__ | Version 5.1, 2016-01-28 Adopts iOS 8 location services authorization, adopts asset catalogs [(Full Revision History)](https://developer.apple.com/library/archive/samplecode/CurrentAddress/History/History.html#//apple_ref/doc/uid/DTS40009469-RevisionHistory-DontLinkElementID_1) |
| __Build Requirements:__ | iOS 8 SDK |
| __Runtime Requirements:__ | iOS 8.0 or later |

This sample makes use of the CLGeocoder class that provides services for converting your map coordinate (specified as a latitude/longitude pair) into information about that coordinate, such as the country, city, or street. A reverse geocoder object is a single-shot object that works with a network-based map service to look up placemark information for its specified coordinate value. To use placemark information is leverages the MKPlacemark class to store this information.
