---
title: 'ImageBrowserViewAppearance: Customizing IKImageBrowserView'
apple_id: DTS40009013
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: Quartz
published: '2018-05-03'
source_url: https://developer.apple.com/library/archive/samplecode/ImageBrowserViewAppearance/Listings/ImageBrowserAppearance_ImageBrowserBackgroundLayer_h.html
archived_at: '2026-07-18T03:12:22.744765Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [ImageBrowserViewAppearance: Customizing IKImageBrowserView](ImageBrowserViewAppearance-%20Customizing%20IKImageBrowserView.md)


[Next](ImageBrowserAppearance-ImageBrowserView.h.md)[Previous](ReadMe.md.md)

# ImageBrowserAppearance/ImageBrowserBackgroundLayer.h

```objc
/*
 Copyright (C) 2018 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 IKImageBrowserView's background CALayer subclass for drawing a custom background image.
 */

@import Quartz;
@import Cocoa;

@interface ImageBrowserBackgroundLayer : CALayer

@property (weak) IKImageBrowserView *owner;

@end
```

[Next](ImageBrowserAppearance-ImageBrowserView.h.md)[Previous](ReadMe.md.md)

