---
title: MatrixMixerTest
apple_id: DTS40008645
resource_type: Sample Code
platform: macOS
topic: Audio, Video, & Visual Effects
technology: AudioUnit
published: '2016-02-11'
source_url: https://developer.apple.com/library/archive/samplecode/MatrixMixerTest/Listings/MeteringView_h.html
archived_at: '2026-07-18T03:14:31.787363Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [MatrixMixerTest](MatrixMixerTest.md)


[Next](LICENSE.txt.md)[Previous](ReadMe.md.md)

# MeteringView.h

```objc
/*
Copyright (C) 2016 Apple Inc. All Rights Reserved.
See LICENSE.txt for this sample’s licensing information

Abstract:
The Metering View
*/

#import <Cocoa/Cocoa.h>

@interface MeteringView : NSView {
    int     mNumChannels;
    double  mMinDB;
    double  mMaxDB;
    double  mMinValue;
    double  mMaxValue; 

    float   *mMeterValues;
    float   *mOldMeterValues;

    int     *mClipValues;

    float   firstTrackOffset;

    BOOL drawsMetersOnly;
    BOOL mHasClip;
}

- (void) setNumChannels: (int) num;
- (void) setMinValue: (double) num; // min value (usually 0)
- (void) setMaxValue: (double) num; // max value (usually 1 to √2)

- (void) setMinDB: (double) num; // min db value (usually -INF)
- (void) setMaxDB: (double) num; // max db value (usually 0 to +6)

- (void) setHasClipIndicator: (BOOL) hasClip;

- (void) updateMeters: (float *) meterValues;   // takes an array of floats
                                                // meterValue[0]: db value for channel 0
                                                // meterValue[1]: db peak for channel 0
                                                // meterValue[2]: db value for channel 1
                                                // meterValue[3]: db peak for channel 1 ...etc

@end
```

[Next](LICENSE.txt.md)[Previous](ReadMe.md.md)

