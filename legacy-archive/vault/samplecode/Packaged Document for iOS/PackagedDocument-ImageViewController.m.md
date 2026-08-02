---
title: Packaged Document for iOS
apple_id: DTS40014139
resource_type: Sample Code
platform: iOS
topic: Data Management
technology: Foundation
published: '2016-02-04'
source_url: https://developer.apple.com/library/archive/samplecode/sc2281/Listings/PackagedDocument_ImageViewController_m.html
archived_at: '2026-07-26T19:54:13.657956Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Packaged Document for iOS](Packaged%20Document%20for%20iOS.md)


[Next](PackagedDocument-NotesDocument.m.md)[Previous](PackagedDocument-RootViewController.m.md)

# PackagedDocument/ImageViewController.m

```objc
/*
 Copyright (C) 2016 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 The view controller used for displaying the image portion of "NotesDocument".
 */

#import "ImageViewController.h"

@interface ImageViewController ()

@property (nonatomic, strong) IBOutlet UIImageView *imageView;

@end

#pragma mark -

@implementation ImageViewController

- (void)viewDidLoad
{
    [super viewDidLoad];
    self.imageView.image = self.image;
}

@end
```

[Next](PackagedDocument-NotesDocument.m.md)[Previous](PackagedDocument-RootViewController.m.md)

