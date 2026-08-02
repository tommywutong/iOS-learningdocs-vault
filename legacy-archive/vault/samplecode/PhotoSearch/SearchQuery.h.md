---
title: PhotoSearch
apple_id: DTS10003994
resource_type: Sample Code
platform: macOS
topic: Data Management
technology: AppKit
published: '2015-12-03'
source_url: https://developer.apple.com/library/archive/samplecode/PhotoSearch/Listings/SearchQuery_h.html
archived_at: '2026-07-18T03:18:55.114060Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [PhotoSearch](PhotoSearch.md)


[Next](ReadMe.md.md)[Previous](AppDelegate.m.md)

# SearchQuery.h

```objc
/*
 Copyright (C) 2015 Apple Inc. All Rights Reserved.
  See LICENSE.txt for this sample’s licensing information

  Abstract:
  Data model for a photo search query. 
 */

#import <Cocoa/Cocoa.h>

#import "SearchItem.h"

// SearchQuery is made up of a query string that will have individual SearchItems as children.

extern NSString *SearchQueryChildrenDidChangeNotification;

@interface SearchQuery : NSObject <NSMetadataQueryDelegate>

@property (strong) NSString *title;
@property (strong) NSURL *searchURL;

- (instancetype)initWithSearchPredicate:(NSPredicate *)searchPredicate title:(NSString *)title scopeURL:(NSURL *)url NS_DESIGNATED_INITIALIZER;

@end
```

[Next](ReadMe.md.md)[Previous](AppDelegate.m.md)

