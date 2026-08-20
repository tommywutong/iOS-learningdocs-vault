---
title: Packaged Document for iOS
apple_id: DTS40014139
resource_type: Sample Code
platform: iOS
topic: Data Management
technology: Foundation
published: '2016-02-04'
source_url: https://developer.apple.com/library/archive/samplecode/sc2281/Listings/PackagedDocument_NotesDocument_h.html
archived_at: '2026-07-26T19:54:13.621203Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Packaged Document for iOS](Packaged%20Document%20for%20iOS.md)


[Next](PackagedDocument-RootViewController.h.md)[Previous](PackagedDocument-main.m.md)

# PackagedDocument/NotesDocument.h

```objc
/*
 Copyright (C) 2016 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 Class representing our document format.
 */

@import Foundation;

extern NSString *kFileExtension;

@class Note;

@interface NotesDocument : UIDocument

@property (strong) Note *note;

@end
```

[Next](PackagedDocument-RootViewController.h.md)[Previous](PackagedDocument-main.m.md)

