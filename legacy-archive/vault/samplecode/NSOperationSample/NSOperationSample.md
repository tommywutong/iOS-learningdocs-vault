---
title: NSOperationSample
apple_id: DTS10004184
resource_type: Sample Code
platform: macOS
topic: Data Management
technology: Foundation
published: '2012-03-27'
source_url: https://developer.apple.com/library/archive/samplecode/NSOperationSample/Introduction/Intro.html
archived_at: '2026-07-18T03:16:48.539999Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](ReadMe.txt.md)

# NSOperationSample

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.3, 2012-03-27 Upgraded to Xcode 4.3 and Mac OS X 10.7, replaced one deprecated API use, adopted NSURL APIs, now uses ARC (Objective-C Automatic Reference Counting). [(Full Revision History)](Document%20Revision%20History.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydimjygqwvezlwnfzws33ojbuxg5dpoj4s2rdpnz2ey2lonncwyzlnmvxhiskel4yq) |
| __Build Requirements:__ | Xcode 4.2 - Mac OS X 10.7 |
| __Runtime Requirements:__ | Mac OS X 10.6.x or later |

"NSOperationSample" is a Cocoa application that demonstrates how to use NSOperation and NSOperationQueue classes. It encapsulates specific tasks like searching the file system for certain image files. One NSOperation is created for recursively searching a given directory, other NSOperation instances are then created for each image file found. It uses NSOperationQueue to manage these operations so users can stop the search and give the primary search operation more time to execute.

[Next](ReadMe.txt.md)

