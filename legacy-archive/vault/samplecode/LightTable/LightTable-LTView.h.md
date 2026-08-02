---
title: LightTable
apple_id: DTS40008927
resource_type: Sample Code
platform: macOS
topic: Data Management
technology: AppKit
published: '2017-08-17'
source_url: https://developer.apple.com/library/archive/samplecode/LightTable/Listings/LightTable_LTView_h.html
archived_at: '2026-07-18T03:13:31.361688Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [LightTable](LightTable.md)


[Next](LightTable-MyDocument.h.md)[Previous](LightTable-LTWindowController.m.md)

# LightTable/LTView.h

```objc
/*
 Copyright (C) 2017 Apple Inc. All Rights Reserved.
  See LICENSE.txt for this sample’s licensing information

  Abstract:
  This custom view uses CALayers to arange and draw slides. Drag and Drop images onto this view to add them as slides. Double-click a slide to edit the masking of the image to the slide. This view tracks both mouse and touch events to modify the slide. Using two fingers on the trackpad will adjust the position and size of the slide under the cursor. 
*/

@import Cocoa;

@class LTMaskLayer;

@interface LTView : NSView <CALayerDelegate> {

}

//@property (nonatomic, weak) NSArrayController *theNewObjectCreator;
@property (weak) IBOutlet NSArrayController *theNewObjectCreator;

@property (strong, nonatomic) NSIndexSet *selectionIndexes;
@end

#pragma mark Data Binding Properties
// The following are the properties that bound slide objects must have.

// @"slides" The content for an LTView is an array of slides.
extern NSString *kLTViewSlides;

// @"selectionIndexes" The indexes of th selected slides
extern NSString *kLTViewSelectionIndexes;

// @"frame" The frame (NSRect) of the slide
extern NSString *kLTViewSlidePropertyFrame;

//@"photoFrame" The frame (NSRect) of the image inside the slide.
extern NSString *kLTViewSlidePropertyPhotoFrame;

//@"photo" The slide image data (NSData).
extern NSString *kLTViewSlidePropertyPhoto;

//@"cornerRadius" The radius (float) of the slide corners
extern NSString *kLTViewSlidePropertyCornerRadius;

//@"frameThickness" The width (float) of the frame.
extern NSString *kLTViewSlidePropertyFrameThickness;
```

[Next](LightTable-MyDocument.h.md)[Previous](LightTable-LTWindowController.m.md)

