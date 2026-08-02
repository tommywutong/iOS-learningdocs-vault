---
title: URLCache
apple_id: DTS40008061
resource_type: Sample Code
platform: iOS
topic: Performance
technology: null
published: '2010-06-25'
source_url: https://developer.apple.com/library/archive/samplecode/URLCache/Introduction/Intro.html
archived_at: '2026-07-18T03:27:31.123556Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](ReadMe.txt.md)

# URLCache

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.1, 2010-06-25 Fixed several minor bugs. Upgraded project to build with iOS 4.0 SDK. [(Full Revision History)](Document%20Revision%20History.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydqmbwgewvezlwnfzws33ojbuxg5dpoj4s2rdpnz2ey2lonncwyzlnmvxhiskel4yq) |
| __Build Requirements:__ | iOS 4.0 SDK |
| __Runtime Requirements:__ | iOS 3.2 |

URLCache is a sample iPhone application that demonstrates how to download a resource off the web, store it in the application's data directory, and use the local copy of the resource. URLCache also demonstrates how to implement a couple of caching policies:

- The local copy of a web resource should remain valid for a period of time (for example, one day) during which the web is not re-checked.

- The HTTP header's Last-Modified date should be used to determine the last time a web resource changed before re-downloading it.

The audience for this sample is iPhone developers using resources such as images that are retrieved or updated from the web.

[Next](ReadMe.txt.md)

