---
title: OpenGL Queries
apple_id: TP40016611
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: OpenGL
published: '2015-12-10'
source_url: https://developer.apple.com/library/archive/samplecode/OpenGL_Queries/Listings/Sources_Frameworks_View_AppDelegate_h.html
archived_at: '2026-07-18T03:18:14.784470Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [OpenGL Queries](OpenGL%20Queries.md)


[Next](Sources-Frameworks-View-AppDelegate.mm.md)[Previous](Sources-Frameworks-Controller-OutlineViewController.mm.md)

# Sources/Frameworks/View/AppDelegate.h

```objc
/*
 Copyright (C) 2015 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 OpenGL Query View application delegate.
 */

#import <Cocoa/Cocoa.h>

#import "OutlineViewController.h"

@interface AppDelegate : NSObject <NSApplicationDelegate>

@property (nonatomic,assign) id<NSOutlineViewDelegate>    delegate;
@property (nonatomic,assign) id<NSOutlineViewDataSource>  dataSource;

- (IBAction) print:(id)sender;

@end
```

[Next](Sources-Frameworks-View-AppDelegate.mm.md)[Previous](Sources-Frameworks-Controller-OutlineViewController.mm.md)

