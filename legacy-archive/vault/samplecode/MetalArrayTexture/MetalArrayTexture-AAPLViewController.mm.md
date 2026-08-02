---
title: MetalArrayTexture
apple_id: TP40016608
resource_type: Sample Code
platform: iOS|macOS
topic: null
technology: null
published: '2016-03-21'
source_url: https://developer.apple.com/library/archive/samplecode/MetalArrayTexture/Listings/MetalArrayTexture_AAPLViewController_mm.html
archived_at: '2026-07-18T03:14:46.793226Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [MetalArrayTexture](MetalArrayTexture.md)


[Next](MetalArrayTexture-GeoUtils.h.md)[Previous](MetalArrayTexture-AAPLArrayTexture.mm.md)

# MetalArrayTexture/AAPLViewController.mm

```objc
/*
 Copyright (C) 2015 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 View Controller for Metal Sample Code. Manages a MTKView and a AAPLRenderer object.
 */

#import "AAPLViewController.h"
#import "AAPLRenderer.h"
#import "AAPLMtkView.h"

#import <QuartzCore/CAMetalLayer.h>

@implementation AAPLViewController
{
@private

    // our renderer instance
    AAPLRenderer *_renderer;
}

- (void)initCommon
{
    _renderer = [AAPLRenderer new];
}

- (id)init
{
    self = [super init];

    if(self)
    {
        [self initCommon];
    }
    return self;
}

// called when loaded from nib
- (id)initWithNibName:(NSString *)nibNameOrNil
               bundle:(NSBundle *)nibBundleOrNil
{
    self = [super initWithNibName:nibNameOrNil
                           bundle:nibBundleOrNil];

    if(self)
    {
        [self initCommon];
    }

    return self;
}

// called when loaded from storyboard
- (id)initWithCoder:(NSCoder *)coder
{
    self = [super initWithCoder:coder];

    if(self)
    {
        [self initCommon];
    }

    return self;
}

- (void)viewDidLoad
{
    [super viewDidLoad];

    AAPLMtkView *renderView = (AAPLMtkView *)self.view;
    renderView.device = MTLCreateSystemDefaultDevice();
    renderView.renderer = _renderer;

    // load all renderer assets before starting game loop
    [_renderer configure:renderView];
}

@end
```

[Next](MetalArrayTexture-GeoUtils.h.md)[Previous](MetalArrayTexture-AAPLArrayTexture.mm.md)

