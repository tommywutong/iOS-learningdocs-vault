---
title: DisplayURL
apple_id: DTS10003783
resource_type: Sample Code
platform: macOS
topic: Data Management
technology: CoreFoundation
published: '2011-04-18'
source_url: https://developer.apple.com/library/archive/samplecode/DisplayURL/Introduction/Intro.html
archived_at: '2026-07-18T03:07:04.437192Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](main.c.md)

# DisplayURL

|  |  |
| --- | --- |
| __Last Revision:__ | Version 2.1, 2011-04-18 Set SDK to Latest and deployment target to 10.6. Fixed a couple of minor static analyzer complaints. [(Full Revision History)](Document%20Revision%20History.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgnzygmwvezlwnfzws33ojbuxg5dpoj4s2rdpnz2ey2lonncwyzlnmvxhiskel4yq) |
| __Build Requirements:__ | Mac OS X 10.6.x or later |
| __Runtime Requirements:__ | Mac OS X 10.5.x or later |

DisplayURL creates a CFURL and then uses CFURL functions to parse the CFURL and display its components. This is very useful for determining the exact behavior of the CFURL functions. DisplayURL accepts either a URL or path (from which a URL is created). DisplayURL allows you to create relative CFURLs and leave them relative, or make them absolute before parsing. And DisplayURL allows you to use the delete/append component and extension functions.

[Next](main.c.md)

