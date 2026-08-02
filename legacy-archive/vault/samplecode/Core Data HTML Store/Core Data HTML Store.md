---
title: Core Data HTML Store
apple_id: DTS10004009
resource_type: Sample Code
platform: macOS
topic: Data Management
technology: CoreData
published: '2007-06-01'
source_url: https://developer.apple.com/library/archive/samplecode/HTMLStore/Introduction/Intro.html
archived_at: '2026-07-18T03:11:39.423099Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](Application-ApplicationDelegate.h.md)

# Core Data HTML Store

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.1, 2007-06-01 Removed use of deprecated NSURL loading API. Removed use of deprecated NSString API. Updated to match current NSAtomicStore API. [(Full Revision History)](Document%20Revision%20History.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydimbqhewvezlwnfzws33ojbuxg5dpoj4s2rdpnz2ey2lonncwyzlnmvxhiskel4yq) |
| __Build Requirements:__ | Xcode 3.0 |
| __Runtime Requirements:__ | Mac OS X 10.5 |

This example illustrates how to create a custom atomic store and integrate it into any application. The format of the store is HTML and all data is stored as HTML tables. Each table maps to an entity. Each row in the table represents a managed object. Each table data element contains a property value. Relationships are represented as anchored links to other tables.

[Next](Application-ApplicationDelegate.h.md)

