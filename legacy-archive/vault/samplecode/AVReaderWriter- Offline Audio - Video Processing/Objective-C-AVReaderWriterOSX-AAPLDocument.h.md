---
title: 'AVReaderWriter: Offline Audio / Video Processing'
apple_id: DTS40011124
resource_type: Sample Code
platform: iOS|macOS
topic: null
technology: AVFoundation
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/samplecode/ReaderWriter/Listings/Objective_C_AVReaderWriterOSX_AAPLDocument_h.html
archived_at: '2026-07-18T03:21:57.913713Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [AVReaderWriter: Offline Audio / Video Processing](AVReaderWriter-%20Offline%20Audio%20-%20Video%20Processing.md)


[Next](Objective-C-AVReaderWriterOSX-AAPLDocument.m.md)[Previous](Objective-C-AVReaderWriterOSX-main.m.md)

# Objective-C/AVReaderWriterOSX/AAPLDocument.h

```objc
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    Main class used to demonstrate reading/writing of assets.
 */

@import AppKit;
@import CoreMedia;
@import AVFoundation;

@class AAPLSampleBufferChannel;
@class AAPLProgressPanelController;

@interface AAPLDocument : NSDocument
{
@private
    IBOutlet NSView             *frameView;
    IBOutlet NSPopUpButton      *filterPopUpButton;

    AVAsset                     *asset;
    AVAssetImageGenerator       *imageGenerator;
    CMTimeRange                 timeRange;
    NSInteger                   filterTag;
    dispatch_queue_t            serializationQueue;

    // Only accessed on the main thread
    NSURL                       *outputURL;
    BOOL                        writingSamples;
    AAPLProgressPanelController *progressPanelController;

    // All of these are createed, accessed, and torn down exclusively on the serializaton queue
    AVAssetReader               *assetReader;
    AVAssetWriter               *assetWriter;
    AAPLSampleBufferChannel     *audioSampleBufferChannel;
    AAPLSampleBufferChannel     *videoSampleBufferChannel;
    BOOL                        cancelled;  
}

@property (nonatomic, retain) AVAsset *asset;
@property (nonatomic) CMTimeRange timeRange;
@property (nonatomic, copy) NSURL *outputURL;

@property (nonatomic, retain) IBOutlet NSView *frameView;
@property (nonatomic, retain) IBOutlet NSPopUpButton *filterPopUpButton;

- (IBAction)start:(id)sender;
- (IBAction)cancel:(id)sender;
@property (nonatomic, getter=isWritingSamples) BOOL writingSamples;

@end
```

[Next](Objective-C-AVReaderWriterOSX-AAPLDocument.m.md)[Previous](Objective-C-AVReaderWriterOSX-main.m.md)

