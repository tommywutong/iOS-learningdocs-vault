---
title: Packaged Document for OS X
apple_id: DTS40012955
resource_type: Sample Code
platform: macOS
topic: Data Management
technology: AppKit
published: '2017-03-09'
source_url: https://developer.apple.com/library/archive/samplecode/PackagedDocument/Listings/PackagedDocument_WindowController_m.html
archived_at: '2026-07-18T03:18:45.231690Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Packaged Document for OS X](Packaged%20Document%20for%20OS%20X.md)


[Next](PackagedDocument-AttachmentView.m.md)[Previous](PackagedDocument-MyTextPictDocument.m.md)

# PackagedDocument/WindowController.m

```objc
/*
 Copyright (C) 2017 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 NSWindowController controlling the behavior of our primary document window.
  It is the subclass for managing the "TextPictDocument" class
 */

#import "WindowController.h"

@implementation WindowController

- (void)windowDidLoad
{
    [super windowDidLoad];

    self.shouldCascadeWindows = YES;
}

@end
```

[Next](PackagedDocument-AttachmentView.m.md)[Previous](PackagedDocument-MyTextPictDocument.m.md)

