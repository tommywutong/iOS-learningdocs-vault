---
title: MatrixMixerTest
apple_id: DTS40008645
resource_type: Sample Code
platform: macOS
topic: Audio, Video, & Visual Effects
technology: AudioUnit
published: '2016-02-11'
source_url: https://developer.apple.com/library/archive/samplecode/MatrixMixerTest/Listings/MeteringView_mm.html
archived_at: '2026-07-18T03:14:31.845812Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [MatrixMixerTest](MatrixMixerTest.md)


[Next](PublicUtility-CAComponentDescription.h.md)[Previous](main.mm.md)

# MeteringView.mm

```objc
/*
Copyright (C) 2016 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 The Metering View 
*/

#import "MeteringView.h"
#include <math.h>

double dbamp(double db) { return pow(10., 0.05 * db); }
double ampdb(double amp) { return 20. * log10(amp); }

#define kMinBarGap          3
#define kBarWidth           11
#define kBarInteriorWidth   9
#define kClipBoxHeight      6

@implementation MeteringView

- (id)initWithFrame:(NSRect)frame {
    self = [super initWithFrame:frame];
    if (self) {
        // initialization code here
        mMeterValues = nil;
        mOldMeterValues = nil;
        mNumChannels = 0;  // must set with setNumChannels:

        drawsMetersOnly = NO;
        mHasClip = NO;
        mMinValue = 0.;
        mMinDB = ampdb(0.);
        mMaxValue = 1.;
        mMaxDB = ampdb(1.);
    }
    return self;
}

- (void) dealloc {
    if (mMeterValues)
        free(mMeterValues);
    if (mOldMeterValues)
        free(mOldMeterValues);
    if (mClipValues)
        free(mClipValues);
    [super dealloc];
}

- (void)drawRect:(NSRect)rect {
    // Drawing code here.
    NSRect bounds = [self bounds];

    float xOffset = firstTrackOffset + .5;
    float yOffset = 0;
    float topGap  = mHasClip ? kClipBoxHeight + 2: 0;

    // draw the frame
    for (int i = 0; i < mNumChannels; i++) {
        NSRect  barRect = NSMakeRect(xOffset + .5, .5, kBarWidth-2, bounds.size.height-1.5 - topGap);

        if (!drawsMetersOnly) {
            NSPoint pt1 = NSMakePoint(xOffset, yOffset);
            NSPoint pt2 = NSMakePoint(xOffset, bounds.size.height-.5 - topGap);
            NSPoint pt3 = NSMakePoint(xOffset + kBarWidth-1, pt2.y);
            NSPoint pt4 = NSMakePoint(pt3.x, yOffset);

            [[NSColor colorWithCalibratedWhite: .37 alpha: 1] set]; // light color
            [NSBezierPath strokeLineFromPoint: pt1 toPoint: pt2];
            [NSBezierPath strokeLineFromPoint: pt2 toPoint: pt3];

            [[NSColor colorWithCalibratedWhite: .53 alpha: 1] set]; // shadow color
            [NSBezierPath strokeLineFromPoint: pt3 toPoint: pt4];
            [NSBezierPath strokeLineFromPoint: pt4 toPoint: pt1];

            if (mHasClip) {
                NSPoint pt5 = NSMakePoint(xOffset, bounds.size.height + 2.5 - topGap);
                NSPoint pt6 = NSMakePoint(xOffset, bounds.size.height-.5);
                NSPoint pt7 = NSMakePoint(xOffset + kBarWidth-1, pt6.y);
                NSPoint pt8 = NSMakePoint(pt7.x, pt5.y);

                [NSBezierPath strokeLineFromPoint: pt7 toPoint: pt8];
                [NSBezierPath strokeLineFromPoint: pt8 toPoint: pt5];

                [[NSColor colorWithCalibratedWhite: .37 alpha: 1] set]; // light color
                [NSBezierPath strokeLineFromPoint: pt5 toPoint: pt6];
                [NSBezierPath strokeLineFromPoint: pt6 toPoint: pt7];
            }

            // now draw the background above and including the current value
            [[NSColor colorWithCalibratedWhite: .4 alpha: 1] set];
            float value = roundf(mMeterValues[i * 2]);
            barRect.origin.y = value + 1;
            barRect.size.height   = bounds.size.height-2 - value - topGap;
            [NSBezierPath fillRect: barRect];

            if (mHasClip) {
                NSRect clipRect = NSMakeRect(barRect.origin.x, bounds.size.height + 3 - topGap, barRect.size.width, kClipBoxHeight -1.5);
                int clipVal = mClipValues[i];
                if (clipVal == 0) 
                    [[NSColor colorWithCalibratedWhite: .4 alpha: 1] set];
                else if (clipVal >= 1 && clipVal < 10) {
                    [[NSColor redColor] set];
                    clipVal++;
                } else 
                    [[NSColor colorWithCalibratedRed: 0.75 green: .18 blue: .18 alpha: 1] set];

                [NSBezierPath fillRect: clipRect];
            }

            [[NSColor greenColor] set];
            barRect.size.height   = barRect.origin.y;
            barRect.origin.y = 1;
            [NSBezierPath fillRect: barRect]; 
        } else {
            // only draw the difference area
            float old = roundf(mOldMeterValues[i * 2]);
            float curr= roundf(mMeterValues[i * 2]);

            // erase previous peak if it is different from the current
            float oldPeak = roundf(mOldMeterValues[(i*2) + 1]) + .5;
            float newPeak = roundf(mMeterValues[(i*2) + 1]) + .5;

            if (oldPeak != newPeak) {
                [[NSColor colorWithCalibratedWhite: .4 alpha: 1] set];
                [NSBezierPath strokeLineFromPoint: NSMakePoint(barRect.origin.x, oldPeak) toPoint: NSMakePoint(barRect.origin.x+barRect.size.width, oldPeak)];
            }

            if (curr > old) {   // draw only green difference
                [[NSColor greenColor] set];
                barRect.origin.y = (old < 1)? 1 : old;
                barRect.size.height = curr - old;
                [NSBezierPath fillRect: barRect];           
            } else if (curr < old) {    // draw only gray difference
                [[NSColor colorWithCalibratedWhite: .4 alpha: 1] set];
                barRect.origin.y = curr + 1;
                barRect.size.height = old - curr;
                [NSBezierPath fillRect: barRect]; 
            } 

            // draw the peak
            if (oldPeak != newPeak || mClipValues[i] == 1) {
                if (mClipValues[i] == 1)
                    [[NSColor redColor] set];
                else
                    [[NSColor colorWithCalibratedWhite: .8 alpha: 1] set];
                [NSBezierPath strokeLineFromPoint: NSMakePoint(barRect.origin.x, newPeak) toPoint: NSMakePoint(barRect.origin.x+barRect.size.width, newPeak)];
            }

            if (mHasClip) {
                NSRect clipRect = NSMakeRect(barRect.origin.x, bounds.size.height + 3 - topGap, barRect.size.width, kClipBoxHeight -1.5);
                int clipVal = mClipValues[i];
                if (clipVal == 1) {
                    [[NSColor redColor] set];
                    [NSBezierPath fillRect: clipRect];
                    clipVal++;
                } 
                else if (clipVal > 1 && clipVal < 10)
                    clipVal++;
                else if (clipVal == 10) {
                    [[NSColor colorWithCalibratedRed: 0.75 green: .18 blue: .18 alpha: 1] set];
                    [NSBezierPath fillRect: clipRect];

                    clipVal++;
                }
                mClipValues[i] = clipVal;
            }
        }

        xOffset += kMinBarGap + kBarWidth;
    }
    drawsMetersOnly = NO;
}

- (void) setNumChannels: (int) num {
    if (0 == num) { NSLog(@"Can't set 0 number of channles!!!!\n"); return; }

    if (mNumChannels != num) {
        mNumChannels = num;
        if (mMeterValues != nil)
            free(mMeterValues);
        if (mOldMeterValues != nil)
            free(mOldMeterValues);
        if (mClipValues != nil)
            free(mClipValues);

        mMeterValues = (float *) calloc (2 * mNumChannels, sizeof(float));
        mOldMeterValues = (float *) calloc (2 * mNumChannels, sizeof(float));
        mClipValues = (int *) calloc (num, sizeof(int));

        drawsMetersOnly = NO;

        firstTrackOffset = floorf(([self bounds].size.width - (mNumChannels * kBarWidth + (mNumChannels-1) * kMinBarGap))/2);
        [self setNeedsDisplay: YES];
    }
}

- (void) setMinValue: (double) num { // lowest value possible slider (should be divisible by 2)
    if (num != mMinValue) {
        mMinValue = num;
        mMinDB = ampdb(num);
        drawsMetersOnly = NO;
        [self setNeedsDisplay: YES];
    }
}

- (void) setMaxValue: (double) num { // highest possible slider value (should be divisible by 2)
    if (num != mMaxValue) {
        mMaxValue = num;
        mMaxDB = ampdb(num);
        drawsMetersOnly = NO;
        [self setNeedsDisplay: YES];
    }
}

- (void) setMinDB: (double) num { 
    if (num != mMinDB) {
        mMinDB = num;
        mMinValue = dbamp(num);
        drawsMetersOnly = NO;
        [self setNeedsDisplay: YES];
    }
}

- (void) setMaxDB: (double) num { 
    if (num != mMaxDB) {
        mMaxDB = num;
        mMaxValue = dbamp(num);
        drawsMetersOnly = NO;
        [self setNeedsDisplay: YES];
    }
}

- (void) setHasClipIndicator: (BOOL) hasClip {
    if (hasClip != mHasClip) {
        mHasClip = hasClip;
        drawsMetersOnly = NO;
        [self setNeedsDisplay: YES];
    }
}

- (float)  pixelForValue: (double) value inSize: (int) size {
    return size * ((value - mMinValue) / (mMaxValue - mMinValue));      // figure out what percentage the value is of the entire range
}

- (void) updateMeters: (float *)meterValues {

    if (![self inLiveResize]) {
        int numItems = 2 * mNumChannels;
        for (int i = 0, j = 0; i < numItems; i++) {
            float tempValue = dbamp(meterValues[i]);
            mOldMeterValues[i] = mMeterValues[i];
            float pixelValue = [self pixelForValue: tempValue inSize: (int) [self bounds].size.height];
            float top = [self bounds].size.height - (mHasClip ? kClipBoxHeight + 4: 2);
            if (pixelValue < 0)
                pixelValue = 0;
            else if (pixelValue > top)
                pixelValue = top;

            mMeterValues[i] = pixelValue;

            if (mHasClip) {
                if ((i & 1) == 0) {
                    if (tempValue > mMaxValue)
                        mClipValues[j] = 1;
                    ++j;
                }
            }       
        }
        drawsMetersOnly = YES;
        [self setNeedsDisplay: YES];
    }
}

- (void)mouseDown:(NSEvent *)theEvent
{
    if (mHasClip) {
        float xOffset = .5 + firstTrackOffset;
        float topGap  = mHasClip ? kClipBoxHeight + 3: 0;

        NSRect clipRect = NSMakeRect(0, [self bounds].size.height - topGap, kBarWidth-2, kClipBoxHeight);
        NSPoint mouseLoc = [self convertPoint:[theEvent locationInWindow] fromView:nil];

        for (int i = 0; i < mNumChannels; i++) {
            clipRect.origin.x = xOffset + .5;
            if ([self mouse:mouseLoc inRect: clipRect]) {
                mClipValues[i] = 0;
                break;
            }
            xOffset += kMinBarGap + kBarWidth;
        }
    }
    drawsMetersOnly = NO;
    [self setNeedsDisplay: YES];
}

- (BOOL) acceptsFirstMouse: (NSEvent *) event {
    return YES;
}

- (BOOL) isOpaque {
    return YES;
}

@end
```

[Next](PublicUtility-CAComponentDescription.h.md)[Previous](main.mm.md)

