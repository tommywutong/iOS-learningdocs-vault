---
title: echoTouch - Using the Voice Processing I/O audio unit
apple_id: TP40017575
resource_type: Sample Code
platform: iOS
topic: Audio, Video, & Visual Effects
technology: AudioToolbox
published: '2016-11-29'
source_url: https://developer.apple.com/library/archive/samplecode/echoTouch/Listings/MeteringViews_AVLevelMeter_h.html
archived_at: '2026-07-18T03:29:07.059732Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [echoTouch - Using the Voice Processing I/O audio unit](echoTouch%20-%20Using%20the%20Voice%20Processing%20I-O%20audio%20unit.md)


[Next](MeteringViews-LevelMeter.m.md)[Previous](MeteringViews-MeterTable.cpp.md)

# MeteringViews/AVLevelMeter.h

```objc
/*
 </samplecode>
*/

#import <UIKit/UIKit.h>
#import <AudioToolbox/AudioQueue.h>
#import <AVFoundation/AVFoundation.h>

#include "MeterTable.h"

#define kPeakFalloffPerSec  .7
#define kLevelFalloffPerSec .8
#define kMinDBvalue -80.0

// A LevelMeter subclass which is used specifically for AVAudioPlayer objects
@interface AVLevelMeter : UIView {
    AVAudioPlayer               *_player;
    NSArray                     *_channelNumbers;
    NSArray                     *_subLevelMeters;
    MeterTable                  *_meterTable;
    NSTimer                     *_updateTimer;
    CGFloat                     _refreshHz;
    BOOL                        _showsPeaks;
    BOOL                        _vertical;
    BOOL                        _useGL;

    CFAbsoluteTime              _peakFalloffLastFire;
    UIColor*                    color;
}

- (void)setPlayer:(AVAudioPlayer*)v;

@property (readonly)    AVAudioPlayer*  player; // The AVAudioPlayer object
@property               CGFloat         refreshHz; // How many times per second to redraw
@property (retain)      NSArray*        channelNumbers; // Array of NSNumber objects: The indices of the channels to display in this meter
@property (retain)      UIColor*        color;
@property               BOOL            showsPeaks; // Whether or not we show peak levels
@property               BOOL            vertical; // Whether the view is oriented V or H
@property               BOOL            useGL; // Whether or not to use OpenGL for drawing

@end
```

[Next](MeteringViews-LevelMeter.m.md)[Previous](MeteringViews-MeterTable.cpp.md)

