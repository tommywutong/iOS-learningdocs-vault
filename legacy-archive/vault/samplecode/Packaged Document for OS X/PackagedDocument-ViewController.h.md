---
title: Packaged Document for OS X
apple_id: DTS40012955
resource_type: Sample Code
platform: macOS
topic: Data Management
technology: AppKit
published: '2017-03-09'
source_url: https://developer.apple.com/library/archive/samplecode/PackagedDocument/Listings/PackagedDocument_ViewController_h.html
archived_at: '2026-07-18T03:18:45.053279Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Packaged Document for OS X](Packaged%20Document%20for%20OS%20X.md)


[Next](PackagedDocument-ViewController.m.md)[Previous](PackagedDocument-AttachmentView.h.md)

# PackagedDocument/ViewController.h

```objc
/*
 Copyright (C) 2017 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 Primary NSViewController content for our document window.
 */

#import <Cocoa/Cocoa.h>

@protocol ViewControllerDelegate;

@interface ViewController : NSViewController <NSTextDelegate>

@property (assign) IBOutlet NSTextView *textView;
@property (assign) BOOL disclosed;
@property (weak) id<ViewControllerDelegate> delegate;

- (void)updateImage:(NSImage *)image;

@end

@protocol ViewControllerDelegate <NSObject>

@required
- (void)viewController:(ViewController *)viewController didDiscloseImage:(BOOL)disclosedImage;

@end
```

[Next](PackagedDocument-ViewController.m.md)[Previous](PackagedDocument-AttachmentView.h.md)

