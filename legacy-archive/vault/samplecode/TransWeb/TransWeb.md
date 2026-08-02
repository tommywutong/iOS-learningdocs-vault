---
title: TransWeb
apple_id: DTS40008614
resource_type: Sample Code
platform: iOS
topic: User Experience
technology: null
published: '2010-06-25'
source_url: https://developer.apple.com/library/archive/samplecode/TransWeb/Introduction/Intro.html
archived_at: '2026-07-18T03:27:10.250509Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](ReadMe.txt.md)

# TransWeb

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.4, 2010-06-25 Updated iTunesArtwork. [(Full Revision History)](Document%20Revision%20History.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydqnrrgqwvezlwnfzws33ojbuxg5dpoj4s2rdpnz2ey2lonncwyzlnmvxhiskel4yq) |
| __Build Requirements:__ | iOS 4.0 SDK or later |
| __Runtime Requirements:__ | iPhone OS 3.2 or later |

Demonstrates how to implement UIWebView with a transparent background.

To achieve this you need to make the HTML body's background color transparent by doing the following -

1) set the UIWebView's backgroundColor property to [UIColor clearColor]

2) use the UIWebView's content in the html: <body style="background-color: transparent">

3) the UIWebView's opaque property set to NO

[Next](ReadMe.txt.md)

