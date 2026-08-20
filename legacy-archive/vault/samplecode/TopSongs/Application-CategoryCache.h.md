---
title: TopSongs
apple_id: DTS40008925
resource_type: Sample Code
platform: iOS
topic: Performance
technology: CoreData
published: '2017-03-23'
source_url: https://developer.apple.com/library/archive/samplecode/TopSongs/Listings/Application_CategoryCache_h.html
archived_at: '2026-07-18T03:27:04.020328Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [TopSongs](TopSongs.md)


[Next](Application-AppDelegate.h.md)[Previous](Application-iTunesRSSImporter.m.md)

# Application/CategoryCache.h

```objc
/*
 Copyright (C) 2017 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 Simple LRU (least recently used) cache for Category objects to reduce fetching.
 */

@import Foundation;
@import CoreData;
@import UIKit;

@class Category;

/*
 About the LRU implementation in this class:

 There are many different ways to implement an LRU cache. This class takes a very minimal approach using an integer "access counter". This counter is incremented each time an item is retrieved from the cache, and the item retrieved has a counter that is set to match the counter for the cache as a whole. This is similar to using a timestamp - the access counter for a given cache node indicates at what point it was last used. The counter does not reflect the number of times the node has been used.

 With the access counter, it is easy to iterate over the items in the cache and find the item with the lowest access value. This item is the "least recently used" item. 
 */

@interface CategoryCache : NSObject

@property (nonatomic, strong) NSManagedObjectContext *managedObjectContext;

- (Category *)categoryWithName:(NSString *)name;

@end
```

[Next](Application-AppDelegate.h.md)[Previous](Application-iTunesRSSImporter.m.md)

