---
title: TopSongs
apple_id: DTS40008925
resource_type: Sample Code
platform: iOS
topic: Performance
technology: CoreData
published: '2017-03-23'
source_url: https://developer.apple.com/library/archive/samplecode/TopSongs/Listings/Controllers_SongsViewController_h.html
archived_at: '2026-07-18T03:27:04.480614Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [TopSongs](TopSongs.md)


[Next](Application-iTunesRSSImporter.h.md)[Previous](Controllers-SongDetailsController.h.md)

# Controllers/SongsViewController.h

```objc
/*
 Copyright (C) 2017 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 Lists all songs in a table view. Also allows sorting and grouping via bottom segmented control.
 */

@import UIKit;

@interface SongsViewController : UITableViewController

@property (nonatomic, strong) NSManagedObjectContext *managedObjectContext;

- (void)fetch;

@end
```

[Next](Application-iTunesRSSImporter.h.md)[Previous](Controllers-SongDetailsController.h.md)

