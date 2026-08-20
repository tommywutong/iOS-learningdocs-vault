---
title: 'DragNDropOutlineView: implementing drag and drop in an NSOutlineView'
apple_id: DTS40008831
resource_type: Sample Code
platform: macOS
topic: User Experience
technology: AppKit
published: '2015-02-09'
source_url: https://developer.apple.com/library/archive/samplecode/DragNDropOutlineView/Listings/DragNDropOutlineView_AAPLImageAndTextCell_h.html
archived_at: '2026-07-18T03:07:10.978971Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [DragNDropOutlineView: implementing drag and drop in an NSOutlineView](DragNDropOutlineView-%20implementing%20drag%20and%20drop%20in%20an%20NSOutlineView.md)


[Next](DragNDropOutlineView-AAPLSimpleNodeData.m.md)[Previous](DragNDropOutlineView-AAPLSimpleNodeData.h.md)

# DragNDropOutlineView/AAPLImageAndTextCell.h

```objc
/*
 Copyright (C) 2015 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 Subclass of NSTextFieldCell which can display text and an image simultaneously.
 */

@import Cocoa;

@interface AAPLImageAndTextCell : NSTextFieldCell
@property (readwrite, strong) NSImage *myImage;
@end
```

[Next](DragNDropOutlineView-AAPLSimpleNodeData.m.md)[Previous](DragNDropOutlineView-AAPLSimpleNodeData.h.md)

