---
title: AbstractTree
apple_id: DTS10004546
resource_type: Sample Code
platform: macOS
topic: Data Management
technology: CoreData
published: '2009-07-24'
source_url: https://developer.apple.com/library/archive/samplecode/AbstractTree/Introduction/Intro.html
archived_at: '2026-07-18T03:00:32.458639Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](ReadMe.txt.md)

# AbstractTree

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.2, 2009-07-24 Fixed crash that occurs when node is dragged to a descendent by adding logic to outlineView:validateDrop:proposedItem:proposedChildIndex:. [(Full Revision History)](Document%20Revision%20History.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydinjugywvezlwnfzws33ojbuxg5dpoj4s2rdpnz2ey2lonncwyzlnmvxhiskel4yq) |
| __Build Requirements:__ | Xcode 3.0, Mac OS X 10.5 |
| __Runtime Requirements:__ | Mac OS X 10.5 |

AbstractTree is a Cocoa sample application that demonstrates how to use Core Data and Bindings with NSTreeController. The data model is intentionally simple and abstract - you can extend it to any hierarchical model suitable for your problem domain. Likewise, the user interface is minimal - just an outline view and buttons for creating and removing nodes in the tree. In addition, the project shows how to implement drag and drop for managing parent-child relationships of the Core Data content.

[Next](ReadMe.txt.md)

