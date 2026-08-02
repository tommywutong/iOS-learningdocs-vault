---
title: Canonicalized String Searching Using a Core Data Derived Property
apple_id: DTS40007750
resource_type: Sample Code
platform: macOS
topic: Data Management
technology: CoreData
published: '2013-05-20'
source_url: https://developer.apple.com/library/archive/samplecode/DerivedProperty/Introduction/Intro.html
archived_at: '2026-07-18T03:06:40.254563Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](ReadMe.txt.md)

# Canonicalized String Searching Using a Core Data Derived Property

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.3, 2013-05-20 Updated project format, and to use ARC. [(Full Revision History)](Document%20Revision%20History.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydonzvgawvezlwnfzws33ojbuxg5dpoj4s2rdpnz2ey2lonncwyzlnmvxhiskel4yq) |
| __Build Requirements:__ | Xcode 4.5, OS X 10.7 or later. |
| __Runtime Requirements:__ | OS X 10.7 or later. |

Searching against Unicode text is a potentially expensive operation. "DerivedProperty" shows how you can use a derived property in Core Data to maintain a canonicalized version of string data to make searching more efficient. In addition, a value transformer overrides the predicate in a search field so that the search string is also normalized.

[Next](ReadMe.txt.md)

