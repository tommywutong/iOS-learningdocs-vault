---
title: Packaged Document for iOS
apple_id: DTS40014139
resource_type: Sample Code
platform: iOS
topic: Data Management
technology: Foundation
published: '2016-02-04'
source_url: https://developer.apple.com/library/archive/samplecode/sc2281/Listings/PackagedDocument_Note_h.html
archived_at: '2026-07-26T19:54:13.669825Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Packaged Document for iOS](Packaged%20Document%20for%20iOS.md)


[Next](PackagedDocument-FileRepresentation.m.md)[Previous](PackagedDocument-NotesDocument.m.md)

# PackagedDocument/Note.h

```objc
/*
 Copyright (C) 2016 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 Class describing the "NotesDocument" format.
 */

@import Foundation;

@interface Note : NSObject

@property (strong, nonatomic) NSString *notes;
@property (strong, nonatomic) UIImage *image;

@end
```

[Next](PackagedDocument-FileRepresentation.m.md)[Previous](PackagedDocument-NotesDocument.m.md)

