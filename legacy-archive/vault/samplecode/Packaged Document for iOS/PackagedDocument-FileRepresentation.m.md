---
title: Packaged Document for iOS
apple_id: DTS40014139
resource_type: Sample Code
platform: iOS
topic: Data Management
technology: Foundation
published: '2016-02-04'
source_url: https://developer.apple.com/library/archive/samplecode/sc2281/Listings/PackagedDocument_FileRepresentation_m.html
archived_at: '2026-07-26T19:54:13.674977Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Packaged Document for iOS](Packaged%20Document%20for%20iOS.md)


[Next](PackagedDocument-FileRepresentation.h.md)[Previous](PackagedDocument-Note.h.md)

# PackagedDocument/FileRepresentation.m

```objc
/*
 Copyright (C) 2016 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 Class representing each item in our table view controller.
 */

#import "FileRepresentation.h"

@implementation FileRepresentation

- (instancetype)init
{
    self = [self initWithURL:nil];
    return self;
}

- (instancetype)initWithURL:(NSURL *)URL
{
    self = [super init];
    if (self != nil)
    {
        _URL = URL;
    }
    return self;
}

@end
```

[Next](PackagedDocument-FileRepresentation.h.md)[Previous](PackagedDocument-Note.h.md)

