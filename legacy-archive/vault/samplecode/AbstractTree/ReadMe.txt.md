---
title: AbstractTree
apple_id: DTS10004546
resource_type: Sample Code
platform: macOS
topic: Data Management
technology: CoreData
published: '2009-07-24'
source_url: https://developer.apple.com/library/archive/samplecode/AbstractTree/Listings/ReadMe_txt.html
archived_at: '2026-07-18T03:00:32.662541Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [AbstractTree](AbstractTree.md)


[Next](AbstractTree-AbstractTreeAppDelegate.h.md)[Previous](AbstractTree.md)

# ReadMe.txt

```
;AbstractTree
November 28, 2007


"AbstractTree" is a Cocoa sample application that demonstrates how to use Core Data and Bindings with NSTreeController. The data model is intentionally simple and abstract - you can extend it to any hierarchical model suitable for your problem domain. Likewise, the user interface is minimal - just an outline view and buttons for creating and removing nodes in the tree. In addition, the project shows how to implement drag and drop for managing parent-child relationships of the Core Data content.

A detailed description in html format is included in the Tutorial directory.

Sample Requirements
The supplied Xcode project was created using Xcode v3.0 running under Mac OS X 10.5.x or later. The project will create a Universal Binary.

Notes
1) This sample leverages Leopard APIs and improvements to NSTreeController. For this reason, the sample will only run on Mac OS X 10.5 and higher.
2) For simplicity, the sample uses the Xcode template generated for Core Data Applications with minimal modifications. 

Changes from Previous Versions
Version 2 - Fixed crash that occurs when node is dragged to a descendent by adding logic to outlineView:validateDrop:proposedItem:proposedChildIndex:.


Copyright © 2007 Apple Inc. All rights reserved.
```

[Next](AbstractTree-AbstractTreeAppDelegate.h.md)[Previous](AbstractTree.md)

