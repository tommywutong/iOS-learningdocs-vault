---
title: DemoMonkey
apple_id: DTS40008848
resource_type: Sample Code
platform: macOS
topic: User Experience
technology: AppKit
published: '2010-08-31'
source_url: https://developer.apple.com/library/archive/samplecode/DemoMonkey/Introduction/Intro.html
archived_at: '2026-07-18T03:06:22.937687Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](ReadMe.txt.md)

# DemoMonkey

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.1, 2010-08-31 Removed extraneous comments and log statements. Updated implementation of initializer methods. [(Full Revision History)](Document%20Revision%20History.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydqobuhawvezlwnfzws33ojbuxg5dpoj4s2rdpnz2ey2lonncwyzlnmvxhiskel4yq) |
| __Build Requirements:__ | Xcode 3.2 or later, Mac OS X v10.6 or later. |
| __Runtime Requirements:__ | Mac OS X v10.6 or later. |

This example shows how to use pasteboard and services APIs for Mac OS X v10.6 and later.

The example is a document-based application which serves as a "typing assistant". Each document contains a collection of text snippets which you can insert in turn into another application using a service. When creating a document, you can import text snippets also using a service.

The application uses the pasteboard to support copy and paste and drag and drop. Drag and drop is illustrated using a subclass of NSArrayController in conjunction with Cocoa bindings.

[Next](ReadMe.txt.md)

