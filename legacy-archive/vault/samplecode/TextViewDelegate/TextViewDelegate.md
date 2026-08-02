---
title: TextViewDelegate
apple_id: DTS10000411
resource_type: Sample Code
platform: macOS
topic: Data Management
technology: AppKit
published: '2011-08-23'
source_url: https://developer.apple.com/library/archive/samplecode/TextViewDelegate/Introduction/Intro.html
archived_at: '2026-07-18T03:26:42.968843Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](ReadMe.txt.md)

# TextViewDelegate

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.1, 2011-08-23 Project updated for Xcode 4. [(Full Revision History)](Document%20Revision%20History.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydanbrgewvezlwnfzws33ojbuxg5dpoj4s2rdpnz2ey2lonncwyzlnmvxhiskel4yq) |
| __Build Requirements:__ | Xcode 3.2, Mac OS X 10.6 Snow Leopard or later. |
| __Runtime Requirements:__ | Mac OS X 10.6 Snow Leopard or later. |

This application demonstrates the use of the text view's delegate to control selection and user input. We use an unmodified text view, except that as its delegate we make sure that whenever a return is entered, the text that has been typed up to that point is colored red, and is recorded as committed, so that no further changes are allowed to it.

[Next](ReadMe.txt.md)

