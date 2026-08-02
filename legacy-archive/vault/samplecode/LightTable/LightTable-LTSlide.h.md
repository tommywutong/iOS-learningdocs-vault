---
title: LightTable
apple_id: DTS40008927
resource_type: Sample Code
platform: macOS
topic: Data Management
technology: AppKit
published: '2017-08-17'
source_url: https://developer.apple.com/library/archive/samplecode/LightTable/Listings/LightTable_LTSlide_h.html
archived_at: '2026-07-18T03:13:31.137527Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [LightTable](LightTable.md)


[Next](LightTable-LTSlide.m.md)[Previous](LightTable-AppDelegate.m.md)

# LightTable/LTSlide.h

```objc
/*
 Copyright (C) 2017 Apple Inc. All Rights Reserved.
  See LICENSE.txt for this sample’s licensing information

  Abstract:
  This is the completion of the slide entity from our Core Data model. We needed to create a class in order for our entity to return CGRect data. We accomplish this by using the methods in "Core Data Programming Guide: Non-Standard Persistent Attributes" 
*/

@import Cocoa;
@import CoreData;

@interface LTSlide : NSManagedObject {

}

@property(assign, nonatomic) CGRect frame;
@property(assign, nonatomic) CGRect photoFrame;

@end
```

[Next](LightTable-LTSlide.m.md)[Previous](LightTable-AppDelegate.m.md)

