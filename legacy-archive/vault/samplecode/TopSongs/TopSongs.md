---
title: TopSongs
apple_id: DTS40008925
resource_type: Sample Code
platform: iOS
topic: Performance
technology: CoreData
published: '2017-03-23'
source_url: https://developer.apple.com/library/archive/samplecode/TopSongs/Introduction/Intro.html
archived_at: '2026-07-18T03:27:03.827614Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](Application-main.m.md)

# TopSongs

|  |  |
| --- | --- |
| __Last Revision:__ | Version 5.2, 2017-03-23 Upgrade to iOS 10.2 SDK, replaced deprecated APIs, updated the NSAppTransportSecurity key value server domain. [(Full Revision History)](Document%20Revision%20History.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydqojsguwvezlwnfzws33ojbuxg5dpoj4s2rdpnz2ey2lonncwyzlnmvxhiskel4yq) |
| __Build Requirements:__ | iOS 10.2 SDK or later |
| __Runtime Requirements:__ | iOS 10.10 or later |

This sample code demonstrates efficiently parsing and importing data from an XML RSS feed into Core Data. The XML parsing is done using libxml. The feed is from iTunes Top Songs and contains data about songs, artists, and categories. The application's data model has an entity for Song and for Category. Managed objects are inserted into a managed object context on a background thread, so the application remains responsive to the user while the import is taking place.

[Next](Application-main.m.md)

