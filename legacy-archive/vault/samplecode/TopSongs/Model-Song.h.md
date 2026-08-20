---
title: TopSongs
apple_id: DTS40008925
resource_type: Sample Code
platform: iOS
topic: Performance
technology: CoreData
published: '2017-03-23'
source_url: https://developer.apple.com/library/archive/samplecode/TopSongs/Listings/Model_Song_h.html
archived_at: '2026-07-18T03:27:04.707164Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [TopSongs](TopSongs.md)


[Next](LICENSE.txt.md)[Previous](Model-Category.m.md)

# Model/Song.h

```objc
/*
 Copyright (C) 2017 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 Managed object subclass for Song entity.
 */

@import UIKit;
@import CoreData;

@class Category;

@interface Song : NSManagedObject

@property (nonatomic, strong) NSString *title;
@property (nonatomic, strong) Category *category;
@property (nonatomic, strong) NSNumber *rank;
@property (nonatomic, strong) NSString *album;
@property (nonatomic, strong) NSDate *releaseDate;
@property (nonatomic, strong) NSString *artist;

@end
```

[Next](LICENSE.txt.md)[Previous](Model-Category.m.md)

