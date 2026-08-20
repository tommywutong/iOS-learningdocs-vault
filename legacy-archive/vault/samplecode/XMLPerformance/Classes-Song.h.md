---
title: XMLPerformance
apple_id: DTS40008094
resource_type: Sample Code
platform: iOS
topic: Performance
technology: Foundation
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/samplecode/XMLPerformance/Listings/Classes_Song_h.html
archived_at: '2026-07-18T03:28:29.811131Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [XMLPerformance](XMLPerformance.md)


[Next](Classes-DetailController.h.md)[Previous](Classes-AppDelegate.h.md)

# Classes/Song.h

```objc
/*
 Copyright (C) 2015 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 Contains the parsed information about a song.
*/


@import UIKit;

@interface Song : NSObject

@property (nonatomic, copy) NSString *title;
@property (nonatomic, copy) NSString *artist;
@property (nonatomic, copy) NSString *album;
@property (nonatomic, copy) NSDate *releaseDate;
@property (nonatomic, copy) NSString *category;

@end
```

[Next](Classes-DetailController.h.md)[Previous](Classes-AppDelegate.h.md)

