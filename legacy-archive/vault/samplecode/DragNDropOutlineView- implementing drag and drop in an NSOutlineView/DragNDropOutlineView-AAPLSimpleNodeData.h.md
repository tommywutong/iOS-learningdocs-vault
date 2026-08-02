---
title: 'DragNDropOutlineView: implementing drag and drop in an NSOutlineView'
apple_id: DTS40008831
resource_type: Sample Code
platform: macOS
topic: User Experience
technology: AppKit
published: '2015-02-09'
source_url: https://developer.apple.com/library/archive/samplecode/DragNDropOutlineView/Listings/DragNDropOutlineView_AAPLSimpleNodeData_h.html
archived_at: '2026-07-18T03:07:11.079510Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [DragNDropOutlineView: implementing drag and drop in an NSOutlineView](DragNDropOutlineView-%20implementing%20drag%20and%20drop%20in%20an%20NSOutlineView.md)


[Next](DragNDropOutlineView-AAPLImageAndTextCell.h.md)[Previous](DragNDropOutlineView-main.m.md)

# DragNDropOutlineView/AAPLSimpleNodeData.h

```objc
/*
 Copyright (C) 2015 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 Represents the model object. Implements NSPasteboardWriting and NSPasteboardReading for easier pasteboard support.
 */

@import Foundation;
@import Cocoa;

@interface AAPLSimpleNodeData : NSObject<NSPasteboardWriting, NSPasteboardReading>

- (instancetype)initWithName:(NSString *)name;
+ (AAPLSimpleNodeData *)nodeDataWithName:(NSString *)name;

@property(readwrite, copy) NSString *name;
@property(readwrite, strong) NSImage *image;
@property(readwrite, getter=isContainer) BOOL container;
@property(readwrite, getter=isExpandable) BOOL expandable;
@property(readwrite, getter=isSelectable) BOOL selectable;

@end
```

[Next](DragNDropOutlineView-AAPLImageAndTextCell.h.md)[Previous](DragNDropOutlineView-main.m.md)

