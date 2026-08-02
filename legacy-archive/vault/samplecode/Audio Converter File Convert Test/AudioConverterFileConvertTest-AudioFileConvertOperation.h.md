---
title: Audio Converter File Convert Test
apple_id: DTS40010581
resource_type: Sample Code
platform: iOS
topic: Audio, Video, & Visual Effects
technology: AudioToolbox
published: '2016-09-29'
source_url: https://developer.apple.com/library/archive/samplecode/iPhoneACFileConvertTest/Listings/AudioConverterFileConvertTest_AudioFileConvertOperation_h.html
archived_at: '2026-07-18T03:29:37.422715Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Audio Converter File Convert Test](Audio%20Converter%20File%20Convert%20Test.md)


[Next](AudioConverterFileConvertTest-AudioFileConvertOperation.m.md)[Previous](AudioConverterFileConvertTest-AppDelegate.h.md)

# AudioConverterFileConvertTest/AudioFileConvertOperation.h

```objc
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    Demonstrates converting audio using AudioConverterFillComplexBuffer.
 */

@import Foundation;
@import AudioToolbox;

@protocol AudioFileConvertOperationDelegate;

@interface AudioFileConvertOperation : NSOperation

- (instancetype)initWithSourceURL:(NSURL *)sourceURL destinationURL:(NSURL *)destinationURL sampleRate:(Float64)sampleRate outputFormat:(AudioFormatID)outputFormat;

@property (readonly, nonatomic, strong) NSURL *sourceURL;

@property (readonly, nonatomic, strong) NSURL *destinationURL;

@property (readonly, nonatomic, assign) Float64 sampleRate;

@property (readonly, nonatomic, assign) AudioFormatID outputFormat;

@property (nonatomic, weak) id<AudioFileConvertOperationDelegate> delegate;

@end

@protocol AudioFileConvertOperationDelegate <NSObject>

- (void)audioFileConvertOperation:(AudioFileConvertOperation *)audioFileConvertOperation didEncounterError:(NSError *)error;

- (void)audioFileConvertOperation:(AudioFileConvertOperation *)audioFileConvertOperation didCompleteWithURL:(NSURL *)destinationURL;

@end
```

[Next](AudioConverterFileConvertTest-AudioFileConvertOperation.m.md)[Previous](AudioConverterFileConvertTest-AppDelegate.h.md)

