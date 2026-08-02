---
title: 'CocoaSlideCollection: Using NSCollectionView on OS X 10.11'
apple_id: TP40016149
resource_type: Sample Code
platform: macOS
topic: User Experience
technology: AppKit
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/samplecode/CocoaSlideCollection/Listings/CocoaSlideCollection_View_AAPLSlide_h.html
archived_at: '2026-07-18T03:03:44.463161Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [CocoaSlideCollection: Using NSCollectionView on OS X 10.11](CocoaSlideCollection-%20Using%20NSCollectionView%20on%20OS%20X%2010.11.md)


[Next](CocoaSlideCollection-View-AAPLHeaderView.m.md)[Previous](CocoaSlideCollection-View-AAPLSlideCarrierView.m.md)

# CocoaSlideCollection/View/AAPLSlide.h

```objc
/*
    Copyright (C) 2015 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    This is the "Slide" NSCollectionViewItem subclass declaration.
*/

#import <Cocoa/Cocoa.h>

/*
    An NSCollectionViewItem that visually represents an AAPLImageFile in an
    NSCollectionView.  A Slide's "representedObject" property points to its
    AAPLImageFile.
*/
@interface AAPLSlide : NSCollectionViewItem

#pragma mark Outlets

// From NSCollectionViewItem, we also inherit an "imageView" outlet (which we wire up to the AAPLSlideImageView that shows our ImageFile's previewImage) and a "textField" outlet (which we wire up to the NSTextField that shows the ImageFile's filenameWithoutExtension).

// An NSTextField that shows a description of the ImageFile's kind (e.g. "JPEG image", "PNG image")
@property(weak) IBOutlet NSTextField *kindTextField;

// An NSTextField that shows the pixel dimensions of the ImageFile's main image (e.g. "5120 x 2880")
@property(weak) IBOutlet NSTextField *dimensionsTextField;


#pragma mark Actions

- (IBAction)openImageFile:(id)sender;
- (IBAction)setCollectionViewBackground:(id)sender;
- (IBAction)clearCollectionViewBackground:(id)sender;

@end
```

[Next](CocoaSlideCollection-View-AAPLHeaderView.m.md)[Previous](CocoaSlideCollection-View-AAPLSlideCarrierView.m.md)

