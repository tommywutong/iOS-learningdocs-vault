---
title: TopSongs
apple_id: DTS40008925
resource_type: Sample Code
platform: iOS
topic: Performance
technology: CoreData
published: '2017-03-23'
source_url: https://developer.apple.com/library/archive/samplecode/TopSongs/Listings/Model_Song_m.html
archived_at: '2026-07-18T03:27:04.745186Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [TopSongs](TopSongs.md)


[Next](Model-Category.h.md)[Previous](Application-CategoryCache.m.md)

# Model/Song.m

```objc
/*
 Copyright (C) 2017 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 Managed object subclass for Song entity.
 */

#import "Song.h"
#import "Category.h"

@implementation Song

@dynamic title, artist, rank, album, releaseDate, category;

@end
```

[Next](Model-Category.h.md)[Previous](Application-CategoryCache.m.md)

