---
title: UIKit Printing with UIPrintInteractionController and UIViewPrintFormatter
apple_id: DTS40010311
resource_type: Sample Code
platform: iOS
topic: Graphics & Animation
technology: null
published: '2012-12-05'
source_url: https://developer.apple.com/library/archive/samplecode/PrintWebView/Introduction/Intro.html
archived_at: '2026-07-18T03:19:32.807649Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](ReadMe.txt.md)

# UIKit Printing with UIPrintInteractionController and UIViewPrintFormatter

|  |  |
| --- | --- |
| __Last Revision:__ | Version 2.0, 2012-12-05 Updated to use storyboards and autolayout. [(Full Revision History)](Document%20Revision%20History.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytamzrgewvezlwnfzws33ojbuxg5dpoj4s2rdpnz2ey2lonncwyzlnmvxhiskel4yq) |
| __Build Requirements:__ | Xcode 4.5 or later, iOS 5.0 or later. |
| __Runtime Requirements:__ | iOS 5.0 or later. |

PrintWebView demonstrates how to print the content displayed by a UIWebView object using the UIViewPrintFormatter class. This sample application is a primitive web browser with printing capability.

PrintWebView shows how to: \* Obtain and use the shared UIPrintInteractionController object. \* Use a UIViewPrintFormatter object to handle formatting and rendering of content in a web view. \* Use a custom UIPrintPageRenderer object to add a header and footer to each page along with the web view content, positioned relative to the imageable area of the paper. \* Position the printed content of a web view independently of the imageable area of the paper; for example, inset by 1/2 inch from each edge.

[Next](ReadMe.txt.md)

