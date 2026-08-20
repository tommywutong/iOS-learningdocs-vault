---
title: avTouch
apple_id: DTS40008636
resource_type: Sample Code
platform: iOS
topic: Audio, Video, & Visual Effects
technology: AVFoundation
published: '2014-02-12'
source_url: https://developer.apple.com/library/archive/samplecode/avTouch/Listings/Classes_CALevelMeter_h.html
archived_at: '2026-07-18T03:28:55.744365Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [avTouch](avTouch.md)


[Next](Classes-CALevelMeter.mm.md)[Previous](Classes-avTouchViewController.m.md)

# Classes/CALevelMeter.h

```objc
/*

<codex>

*/

#import <UIKit/UIKit.h>
#import <AudioToolbox/AudioQueue.h>
#import <AVFoundation/AVFoundation.h>

#include "MeterTable.h"

#define kPeakFalloffPerSec  .7
#define kLevelFalloffPerSec .8
#define kMinDBvalue -80.0

// A LevelMeter subclass which is used specifically for AVAudioPlayer objects
@interface CALevelMeter : UIView {
    AVAudioPlayer               *_player;
    NSArray                     *_channelNumbers;
    NSArray                     *_subLevelMeters;
    MeterTable                  *_meterTable;
    CADisplayLink               *_updateTimer;
    BOOL                        _showsPeaks;
    BOOL                        _vertical;
    BOOL                        _useGL;

    CFAbsoluteTime              _peakFalloffLastFire;;
}

- (void)setPlayer:(AVAudioPlayer*)v;

@property (readonly)    AVAudioPlayer *player; // The AVAudioPlayer object
@property (retain)      NSArray *channelNumbers; // Array of NSNumber objects: The indices of the channels to display in this meter
@property               BOOL showsPeaks; // Whether or not we show peak levels
@property               BOOL vertical; // Whether the view is oriented V or H
@property               BOOL useGL; // Whether or not to use OpenGL for drawing
@end
```

[Next](Classes-CALevelMeter.mm.md)[Previous](Classes-avTouchViewController.m.md)

