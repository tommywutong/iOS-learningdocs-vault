---
title: Extended Audio File Conversion Test
apple_id: DTS40009222
resource_type: Sample Code
platform: iOS
topic: Audio, Video, & Visual Effects
technology: AudioToolbox
published: '2016-09-29'
source_url: https://developer.apple.com/library/archive/samplecode/iPhoneExtAudioFileConvertTest/Listings/ExtendedAudioFileConvertTest_ExtendedAudioFileConvertOperation_h.html
archived_at: '2026-07-18T03:29:40.125130Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Extended Audio File Conversion Test](Extended%20Audio%20File%20Conversion%20Test.md)


[Next](LICENSE.txt.md)[Previous](ExtendedAudioFileConvertTest-AppDelegate.h.md)

# ExtendedAudioFileConvertTest/ExtendedAudioFileConvertOperation.h

```objc
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    Demonstrates converting audio using ExtAudioFile.
 */

#import <Foundation/Foundation.h>
@import AudioToolbox;

@protocol ExtendedAudioFileConvertOperationDelegate;

@interface ExtendedAudioFileConvertOperation : NSOperation

- (instancetype)initWithSourceURL:(NSURL *)sourceURL destinationURL:(NSURL *)destinationURL sampleRate:(Float64)sampleRate outputFormat:(AudioFormatID)outputFormat;

@property (readonly, nonatomic, strong) NSURL *sourceURL;

@property (readonly, nonatomic, strong) NSURL *destinationURL;

@property (readonly, nonatomic, assign) Float64 sampleRate;

@property (readonly, nonatomic, assign) AudioFormatID outputFormat;

@property (nonatomic, weak) id<ExtendedAudioFileConvertOperationDelegate> delegate;

@end

@protocol ExtendedAudioFileConvertOperationDelegate <NSObject>

- (void)audioFileConvertOperation:(ExtendedAudioFileConvertOperation *)audioFileConvertOperation didEncounterError:(NSError *)error;

- (void)audioFileConvertOperation:(ExtendedAudioFileConvertOperation *)audioFileConvertOperation didCompleteWithURL:(NSURL *)destinationURL;

@end
```

[Next](LICENSE.txt.md)[Previous](ExtendedAudioFileConvertTest-AppDelegate.h.md)

