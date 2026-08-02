---
title: BonjourWeb
apple_id: DTS40007415
resource_type: Sample Code
platform: iOS
topic: Networking, Internet, & Web
technology: Foundation
published: '2010-06-16'
source_url: https://developer.apple.com/library/archive/samplecode/BonjourWeb/Introduction/Intro.html
archived_at: '2026-07-18T03:02:10.724804Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](ReadMe.txt.md)

# BonjourWeb

|  |  |
| --- | --- |
| __Last Revision:__ | Version 2.9, 2010-06-16 Updated to work with iOS SDK 4.0. [(Full Revision History)](Document%20Revision%20History.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydonbrguwvezlwnfzws33ojbuxg5dpoj4s2rdpnz2ey2lonncwyzlnmvxhiskel4yq) |
| __Build Requirements:__ | iOS SDK 4.0 |
| __Runtime Requirements:__ | iOS 4.0 |

This application illustrates the fundamentals of browsing for network services using Bonjour. The BonjourBrowser hierarchically displays Bonjour domains and services as table views in a navigation controller. The contents of the table views are discovered and updated dynamically using NSNetServiceBrowser objects. Tapping an item in the services table causes the corresponding NSNetService object to be resolved asynchronously. When that resolution completes, a delegate method is called which constructs a URL and opens it in Safari.

[Next](ReadMe.txt.md)

