---
title: XMLPerformance
apple_id: DTS40008094
resource_type: Sample Code
platform: iOS
topic: Performance
technology: Foundation
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/samplecode/XMLPerformance/Introduction/Intro.html
archived_at: '2026-07-18T03:28:29.250405Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](main.m.md)

# XMLPerformance

|  |  |
| --- | --- |
| __Last Revision:__ | Version 5.0, 2015-09-16 Replaced NSURLConnection with NSURLSession, updated xib files to storyboard, added launch screen, changed super class of ParserChoiceController and StatsViewController to UITableViewController. [(Full Revision History)](Document%20Revision%20History.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydqmbzgqwvezlwnfzws33ojbuxg5dpoj4s2rdpnz2ey2lonncwyzlnmvxhiskel4yq) |
| __Build Requirements:__ | Xcode 7, iOS 9.0 SDK |
| __Runtime Requirements:__ | iOS 8.0 or later |

This sample explores two approaches to parsing XML, focusing on performance with respect to speed, memory footprint, and user experience. The XML data used is the current "Top 300" songs from the iTunes store. The data itself is not particularly important to the sample - it was chosen because of its simplicity, availability, and because the size (approximately 850KB) is sufficient to demonstrate the performance issues central to the sample.

[Next](main.m.md)

