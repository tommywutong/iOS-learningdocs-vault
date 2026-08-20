---
title: Packaged Document for OS X
apple_id: DTS40012955
resource_type: Sample Code
platform: macOS
topic: Data Management
technology: AppKit
published: '2017-03-09'
source_url: https://developer.apple.com/library/archive/samplecode/PackagedDocument/Listings/PackagedDocument_ImageView_m.html
archived_at: '2026-07-18T03:18:44.817182Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Packaged Document for OS X](Packaged%20Document%20for%20OS%20X.md)


[Next](PackagedDocument-MyAppDelegate.h.md)[Previous](PackagedDocument-ImageView.h.md)

# PackagedDocument/ImageView.m

```objc
/*
 Copyright (C) 2017 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 Custom NSImageView for intercepting delete/cut/paste operations.
 */

#import "ImageView.h"

@implementation ImageView

- (void)copy:(id)sender
{
    if ([self allowsCutCopyPaste])
    {
        NSImage *anImage = [self image];
        if (anImage != nil)
        {
            // copy to pasteboard
            NSPasteboard *pboard = [NSPasteboard generalPasteboard];
            [pboard declareTypes: [NSArray arrayWithObject:NSTIFFPboardType] owner:self];
            [pboard setData: [anImage TIFFRepresentation] forType: NSTIFFPboardType];
        }
    }
}

- (void)paste:(id)sender {

    NSPasteboard *pasteboard = [NSPasteboard generalPasteboard];
    NSArray *classArray = [NSArray arrayWithObject:[NSImage class]];
    NSDictionary *options = [NSDictionary dictionary];
    if ([pasteboard canReadObjectForClasses:classArray options:options])
    {
        NSArray *objectsToPaste = [pasteboard readObjectsForClasses:classArray options:options];
        NSImage *image = [objectsToPaste objectAtIndex:0];
        [self setImage:image];
    }

    // Notify our delegate of the image change.
    [self.delegate imageView:self didChangeImage:self.image];
}

- (void)delete:(id)sender
{
    if ([self allowsCutCopyPaste])
    {
        [self setImage: nil];
    }

    // Notify our delegate of the image change.
    [self.delegate imageView:self didChangeImage:self.image];
}

- (void)cut:(id)sender
{
    if ([self allowsCutCopyPaste])
    {
        [self copy: sender];
        [self setImage: nil];
    }

    // Notify our delegate of the image change.
    [self.delegate imageView:self didChangeImage:self.image];
}

@end
```

[Next](PackagedDocument-MyAppDelegate.h.md)[Previous](PackagedDocument-ImageView.h.md)

