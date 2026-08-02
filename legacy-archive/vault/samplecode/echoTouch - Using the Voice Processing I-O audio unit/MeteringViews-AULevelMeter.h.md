---
title: echoTouch - Using the Voice Processing I/O audio unit
apple_id: TP40017575
resource_type: Sample Code
platform: iOS
topic: Audio, Video, & Visual Effects
technology: AudioToolbox
published: '2016-11-29'
source_url: https://developer.apple.com/library/archive/samplecode/echoTouch/Listings/MeteringViews_AULevelMeter_h.html
archived_at: '2026-07-18T03:29:06.906571Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [echoTouch - Using the Voice Processing I/O audio unit](echoTouch%20-%20Using%20the%20Voice%20Processing%20I-O%20audio%20unit.md)


[Next](MeteringViews-LevelMeter.h.md)[Previous](MeteringViews-GLLevelMeter.m.md)

# MeteringViews/AULevelMeter.h

```objc
/*
 </samplecode>
*/

#import <UIKit/UIKit.h>

#import "MeterTable.h"
#import "PowerMeter.h"

#define kPeakFalloffPerSec      .7
#define kLevelFalloffPerSec     .8
#define kMinDBvalue             -80.0
#define kRefreshRate            60.
#define kDefaultSampleRate      44100.

// A LevelMeter subclass which is used specifically for AVAudioPlayer objects
@interface AULevelMeter : UIView {

    NSArray*            _channelNumbers;
    NSArray*            _subLevelMeters;
    MeterTable*         _meterTable;
    PowerMeter*         _powerMeters;
    NSTimer*            _updateTimer;
    CGFloat             _refreshHz;
    double              sampleRate;
    BOOL                _showsPeaks;
    BOOL                _vertical;
    BOOL                _useGL;
    BOOL                _running;
    CFAbsoluteTime      _peakFalloffLastFire;
    UIColor*            color;
}

@property (assign)      BOOL        running;        // Whether the unit is currently running
@property (assign)      CGFloat     refreshHz;      // How many times per second to redraw
@property (assign)      double      sampleRate;     // Sample rate of the audio unit
@property (retain)      NSArray*    channelNumbers; // Array of NSNumber objects: The indices of the channels to display in this meter
@property (retain)      UIColor*    color;
@property (assign)      BOOL        showsPeaks;     // Whether or not we show peak levels
@property (assign)      BOOL        vertical;       // Whether the view is oriented V or H
@property (assign)      BOOL        useGL;          // Whether or not to use OpenGL for drawing
@property (assign)      PowerMeter* powerMeters;
@end
```

[Next](MeteringViews-LevelMeter.h.md)[Previous](MeteringViews-GLLevelMeter.m.md)

