---
title: 'ImageBrowserViewAppearance: Customizing IKImageBrowserView'
apple_id: DTS40009013
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: Quartz
published: '2018-05-03'
source_url: https://developer.apple.com/library/archive/samplecode/ImageBrowserViewAppearance/Listings/ReadMe_md.html
archived_at: '2026-07-18T03:12:23.743115Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [ImageBrowserViewAppearance: Customizing IKImageBrowserView](ImageBrowserViewAppearance-%20Customizing%20IKImageBrowserView.md)


[Next](ImageBrowserAppearance-ImageBrowserBackgroundLayer.h.md)[Previous](ImageBrowserAppearance-main.m.md)

# ReadMe.md

```objc
# ImageBrowserAppearance

## Description

This sample demonstrates and customizes the ImageKit’s `IKImageBrowserView` in a basic Cocoa application

Usual steps to customize the appearance of the image browser :

1) configure the view
    The `IKImageBrowserView` class allows you to:

    - set the font of the titles / subtitles
    - set the inter cell spacing
    - set the size of the cells
    - set the background color
    - set the selection color
    - set a background layer
    - set a foreground layer

2) implement your own cell
   Subclass the `IKImageBrowserView` and implement `newCellForRepresentedItem:`.
   In this method, return an instance of your own subclass of `IKImageBrowserCell`.
   In you subclass of `IKImageBrowserCell`, override some of the following methods to modify the layout:

    - (NSRect) imageContainerFrame;
    - (NSRect) imageFrame; 
    - (NSRect) selectionFrame;
    - (NSRect) titleFrame;
    - (NSRect) subtitleFrame;   
    - (NSImageAlignment) imageAlignment;

  In you subclass of `IKImageBrowserCell`, override some of the following methods to modify the appearance:

    - (CGFloat) opacity;
    - (CALayer *) layerForType:(NSString *) type;

## Requirements

### Build

macOS 10.13 SDK or later

### Runtime

OS X 10.10 or later


Copyright (C) 2008-2018 Apple Inc. All rights reserved.
```

[Next](ImageBrowserAppearance-ImageBrowserBackgroundLayer.h.md)[Previous](ImageBrowserAppearance-main.m.md)

