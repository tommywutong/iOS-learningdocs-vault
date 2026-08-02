---
title: Hello Metronome
apple_id: TP40017587
resource_type: Sample Code
platform: watchOS|iOS|macOS
topic: Audio, Video, & Visual Effects
technology: AVFoundation
published: '2017-02-24'
source_url: https://developer.apple.com/library/archive/samplecode/HelloMetronome/Listings/iOSHelloMetronome_watchOSMetronome_Extension_Metronome_h.html
archived_at: '2026-07-18T03:11:52.300118Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Hello Metronome](Hello%20Metronome.md)


[Next](iOSHelloMetronome-watchOSMetronome%20Extension-ExtensionDelegate.h.md)[Previous](iOSHelloMetronome-watchOSMetronome%20Extension-InterfaceController.h.md)

# iOSHelloMetronome/watchOSMetronome Extension/Metronome.h

```objc
/*
 Copyright (C) 2017 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 Metronome class header file
*/

#import <Foundation/Foundation.h>
#import <AVFoundation/AVFoundation.h>

@protocol MetronomeDelegate <NSObject>
@optional
- (void)metronomeTick:(NSInteger)currentTick;
@end

@interface Metronome : NSObject

+ (nullable instancetype)sharedInstance;

- (BOOL)startClock;
- (void)stopClock;
- (void)reset;

- (void)incrementTempo:(NSInteger)increment;
- (void)incrementMeter:(NSInteger)increment;
- (void)incrementDivisionIndex:(NSInteger)increment;

@property (nonatomic, readonly) NSInteger   tempo;
@property (nonatomic, readonly) NSUInteger  meter;
@property (nonatomic, readonly) NSInteger   division;
@property (nonatomic, readonly) NSInteger   currentTick;
@property (nonatomic, readonly) BOOL        isRunning;
@property (nonatomic, weak, nullable) id<MetronomeDelegate> delegate;

@end
```

[Next](iOSHelloMetronome-watchOSMetronome%20Extension-ExtensionDelegate.h.md)[Previous](iOSHelloMetronome-watchOSMetronome%20Extension-InterfaceController.h.md)

