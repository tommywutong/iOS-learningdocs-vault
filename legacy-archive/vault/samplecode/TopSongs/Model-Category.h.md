---
title: TopSongs
apple_id: DTS40008925
resource_type: Sample Code
platform: iOS
topic: Performance
technology: CoreData
published: '2017-03-23'
source_url: https://developer.apple.com/library/archive/samplecode/TopSongs/Listings/Model_Category_h.html
archived_at: '2026-07-18T03:27:04.636178Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [TopSongs](TopSongs.md)


[Next](Model-Category.m.md)[Previous](Model-Song.m.md)

# Model/Category.h

```objc
/*
 Copyright (C) 2017 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 Managed object subclass for Category entity.
 */

@import Foundation;
@import CoreData;

@interface Category : NSManagedObject

@property (nonatomic, strong) NSString *name;
@property (nonatomic, strong) NSSet *songs;

@end
```

[Next](Model-Category.m.md)[Previous](Model-Song.m.md)

