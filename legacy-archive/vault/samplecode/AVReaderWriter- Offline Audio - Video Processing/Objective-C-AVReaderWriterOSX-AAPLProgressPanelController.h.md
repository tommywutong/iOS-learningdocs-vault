---
title: 'AVReaderWriter: Offline Audio / Video Processing'
apple_id: DTS40011124
resource_type: Sample Code
platform: iOS|macOS
topic: null
technology: AVFoundation
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/samplecode/ReaderWriter/Listings/Objective_C_AVReaderWriterOSX_AAPLProgressPanelController_h.html
archived_at: '2026-07-18T03:21:58.182721Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [AVReaderWriter: Offline Audio / Video Processing](AVReaderWriter-%20Offline%20Audio%20-%20Video%20Processing.md)


[Next](Objective-C-AVReaderWriterOSX-AAPLProgressPanelController.m.md)[Previous](Objective-C-AVReaderWriterOSX-AAPLDocument.m.md)

# Objective-C/AVReaderWriterOSX/AAPLProgressPanelController.h

```objc
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    Main window controller for the sample app.
 */

@import AppKit;
@import CoreMedia;

@protocol AAPLProgressPanelControllerDelegate;

@interface AAPLProgressPanelController : NSWindowController
{
@private
    id <AAPLProgressPanelControllerDelegate> delegate;

    IBOutlet NSView                         *frameView;
    IBOutlet NSProgressIndicator            *progressIndicator;
    CALayer                                 *frameLayer;

    NSMutableArray                          *interestingProgressValues;
}

@property (nonatomic, retain) IBOutlet NSView *frameView;
@property (nonatomic, retain) IBOutlet NSProgressIndicator *progressIndicator;
@property (nonatomic, assign) id <AAPLProgressPanelControllerDelegate> delegate;

- (void)setPixelBuffer:(CVPixelBufferRef)pixelBuffer forProgress:(double)progress; // progress should be in the range 0.0 to 1.0
- (IBAction)cancel:(id)sender;

@end


@protocol AAPLProgressPanelControllerDelegate <NSObject>
@optional
- (void)progressPanelControllerDidCancel:(AAPLProgressPanelController *)progressPanelController;
@end
```

[Next](Objective-C-AVReaderWriterOSX-AAPLProgressPanelController.m.md)[Previous](Objective-C-AVReaderWriterOSX-AAPLDocument.m.md)

