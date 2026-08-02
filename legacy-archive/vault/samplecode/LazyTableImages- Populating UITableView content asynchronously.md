---
title: 'LazyTableImages: Populating UITableView content asynchronously'
apple_id: DTS40009394
resource_type: Sample Code
platform: iOS
topic: null
technology: UIKit
published: '2017-11-30'
source_url: https://developer.apple.com/library/archive/samplecode/LazyTableImages/Introduction/Intro.html
archived_at: '2026-07-27T06:57:01.768557Z'
---
> 导航：[总目录](../README.md) · [samplecode](../_indexes/samplecode.md)



# LazyTableImages: Populating UITableView content asynchronously

|  |  |
| --- | --- |
| __Last Revision:__ | Version 7.0, 2017-11-30 Upgraded to iOS 11.0 SDK. [(Full Revision History)](https://developer.apple.com/library/archive/samplecode/LazyTableImages/History/History.html#//apple_ref/doc/uid/DTS40009394-RevisionHistory-DontLinkElementID_1) |
| __Build Requirements:__ | iOS 11.0 SDK or later |
| __Runtime Requirements:__ | iOS 10.0 or later |

This sample demonstrates a multi-stage approach to loading and displaying a UITableView. It displays the top paid iOS apps on Apple's App Store.

It begins by loading the relevant text from the RSS feed so the table can load as quickly as possible, then downloads the app icons for each row asynchronously so the user interface is more responsive.
