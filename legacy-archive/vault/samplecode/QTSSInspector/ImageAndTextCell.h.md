---
title: QTSSInspector
apple_id: DTS10001050
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/QTSSInspector/Listings/ImageAndTextCell_h.html
archived_at: '2026-07-18T03:21:19.383287Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [QTSSInspector](QTSSInspector.md)


[Next](ImageAndTextCell.m.md)[Previous](base64.h.md)

# ImageAndTextCell.h

```objc
//
//  ImageAndTextCell.h
//
//  Copyright (c) 2001 Apple. All rights reserved.
//

#import <Cocoa/Cocoa.h>

@interface ImageAndTextCell : NSTextFieldCell {
@private
    NSImage *image;
}

- (void)setImage:(NSImage *)anImage;
- (NSImage *)image;

- (void)drawWithFrame:(NSRect)cellFrame inView:(NSView *)controlView;
- (NSSize)cellSize;

@end
```

[Next](ImageAndTextCell.m.md)[Previous](base64.h.md)

