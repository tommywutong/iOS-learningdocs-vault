---
title: Using NSTokenField
apple_id: DTS40013108
resource_type: Sample Code
platform: macOS
topic: User Experience
technology: AppKit
published: '2016-06-03'
source_url: https://developer.apple.com/library/archive/samplecode/Tokens/Listings/Tokens_MyToken_m.html
archived_at: '2026-07-18T03:26:59.388978Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Using NSTokenField](Using%20NSTokenField.md)


[Next](Tokens-AppDelegate.h.md)[Previous](Tokens-ViewController.m.md)

# Tokens/MyToken.m

```objc
/*
 Copyright (C) 2016 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 Custom token class.
 */

#import "MyToken.h"

@implementation MyToken

// NSCoder routines necessary for token drag and drop

- (void)encodeWithCoder:(NSCoder *)encoder
{
    [encoder encodeObject:self.name];
}

- (instancetype)initWithCoder:(NSCoder *)decoder
{
    _name = [decoder decodeObject];
    return self;
}

@end
```

[Next](Tokens-AppDelegate.h.md)[Previous](Tokens-ViewController.m.md)

