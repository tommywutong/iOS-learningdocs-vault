---
title: PhotoSearch
apple_id: DTS10003994
resource_type: Sample Code
platform: macOS
topic: Data Management
technology: AppKit
published: '2015-12-03'
source_url: https://developer.apple.com/library/archive/samplecode/PhotoSearch/Listings/SearchItem_h.html
archived_at: '2026-07-18T03:18:54.995430Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [PhotoSearch](PhotoSearch.md)


[Next](AppDelegate.m.md)[Previous](main.m.md)

# SearchItem.h

```objc
/*
 Copyright (C) 2015 Apple Inc. All Rights Reserved.
  See LICENSE.txt for this sample’s licensing information

  Abstract:
  Data model for a search result item. 
 */

#import <Cocoa/Cocoa.h>

extern NSString *SearchItemDidChangeNotification;

@interface SearchItem : NSObject

- (instancetype)initWithItem:(NSMetadataItem *)item NS_DESIGNATED_INITIALIZER;

@property (readonly) NSMetadataItem *item;
@property (assign) NSInteger state;

@property (copy) NSString *title;

@property (readonly, strong) NSMetadataItem *metadataItem;

@property (readonly) NSSize imageSize;

@property (readonly, copy) NSURL *filePathURL;

@property (readonly, copy) NSDate *modifiedDate;
@property (readonly, copy) NSString *cameraModel;

// the thumbnail image may return nil if it isn't loaded. The first access of it will request it to load
@property (readonly, copy) NSImage *thumbnailImage;

@end
```

[Next](AppDelegate.m.md)[Previous](main.m.md)

