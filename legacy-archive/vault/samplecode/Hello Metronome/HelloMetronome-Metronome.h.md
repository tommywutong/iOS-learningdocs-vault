---
title: Hello Metronome
apple_id: TP40017587
resource_type: Sample Code
platform: watchOS|iOS|macOS
topic: Audio, Video, & Visual Effects
technology: AVFoundation
published: '2017-02-24'
source_url: https://developer.apple.com/library/archive/samplecode/HelloMetronome/Listings/HelloMetronome_Metronome_h.html
archived_at: '2026-07-18T03:11:51.052330Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Hello Metronome](Hello%20Metronome.md)


[Next](README.md.md)[Previous](HelloMetronome-HelloMetronome-Bridging-Header.h.md)

# HelloMetronome/Metronome.h

```objc
/*
 Copyright (C) 2017 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 Metronome class header file
*/

#import <AVFoundation/AVFoundation.h>

@protocol MetronomeDelegate;

@interface Metronome : NSObject {
}

- (nullable instancetype)init:(NSURL * _Nullable)fileURL NS_DESIGNATED_INITIALIZER;
- (BOOL)start;
- (void)stop;
- (void)setTempo:(Float32)tempo;

@property(weak, nullable) id<MetronomeDelegate> delegate;

@end

@protocol MetronomeDelegate <NSObject>
@optional 
- (void)metronomeTicking:(Metronome * _Nonnull)metronome bar:(SInt32)bar beat:(SInt32)beat;
@end
```

[Next](README.md.md)[Previous](HelloMetronome-HelloMetronome-Bridging-Header.h.md)

