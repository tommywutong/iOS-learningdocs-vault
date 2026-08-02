---
title: echoTouch - Using the Voice Processing I/O audio unit
apple_id: TP40017575
resource_type: Sample Code
platform: iOS
topic: Audio, Video, & Visual Effects
technology: AudioToolbox
published: '2016-11-29'
source_url: https://developer.apple.com/library/archive/samplecode/echoTouch/Listings/MeteringViews_LevelMeter_h.html
archived_at: '2026-07-18T03:29:07.329225Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [echoTouch - Using the Voice Processing I/O audio unit](echoTouch%20-%20Using%20the%20Voice%20Processing%20I-O%20audio%20unit.md)


[Next](MeteringViews-AVLevelMeter.mm.md)[Previous](MeteringViews-AULevelMeter.h.md)

# MeteringViews/LevelMeter.h

```objc
/*
 </samplecode>
*/

#import <UIKit/UIKit.h>

#ifndef LEVELMETER_CLAMP
#define LEVELMETER_CLAMP(min,x,max) (x < min ? min : (x > max ? max : x))
#endif

// The LevelMeterColorThreshold struct is used to define the colors for the LevelMeter, 
// and at what values each of those colors begins.
typedef struct LevelMeterColorThreshold {
    CGFloat         maxValue; // A value from 0 - 1. The maximum value shown in this color
    UIColor         *color; // A UIColor to be used for this value range
} LevelMeterColorThreshold;

@interface LevelMeter : UIView {
    NSUInteger                  _numLights;
    CGFloat                     _level, _peakLevel;
    LevelMeterColorThreshold    *_colorThresholds;
    NSUInteger                  _numColorThresholds;
    BOOL                        _vertical;
    BOOL                        _variableLightIntensity;
    UIColor                     *_bgColor, *_borderColor;
    CGFloat                     _scaleFactor;
}

// The current level, from 0 - 1
@property                       CGFloat level;

// Optional peak level, will be drawn if > 0
@property                       CGFloat peakLevel;

// The number of lights to show, or 0 to show a continuous bar
@property                       NSUInteger numLights;

// Whether the view is oriented V or H. This is initially automatically set based on the 
// aspect ratio of the view.
@property(getter=isVertical)    BOOL vertical;

// Whether to use variable intensity lights. Has no effect if numLights == 0.
@property                       BOOL variableLightIntensity;

// The background color of the lights
@property(retain)               UIColor *bgColor;

// The border color of the lights
@property(retain)               UIColor *borderColor;

// Returns a pointer to the first LevelMeterColorThreshold struct. The number of color 
// thresholds is returned in count
- (LevelMeterColorThreshold *)colorThresholds:(NSUInteger *)count;

// Load <count> elements from <thresholds> and use these as our color threshold values.
- (void)setColorThresholds:(LevelMeterColorThreshold *)thresholds count:(NSUInteger)count;

@end
```

[Next](MeteringViews-AVLevelMeter.mm.md)[Previous](MeteringViews-AULevelMeter.h.md)

