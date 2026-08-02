---
title: Audio Unit Examples (AudioUnit Effect, Generator, Instrument, MIDI Processor
  and Offline)
apple_id: DTS40013969
resource_type: Sample Code
platform: macOS
topic: Audio, Video, & Visual Effects
technology: AudioUnit
published: '2016-02-19'
source_url: https://developer.apple.com/library/archive/samplecode/sc2195/Listings/AudioUnitEffectExample_Source_CocoaUI_AppleDemoFilter_GraphView_h.html
archived_at: '2026-07-26T19:54:12.957024Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Audio Unit Examples (AudioUnit Effect, Generator, Instrument, MIDI Processor and Offline)](Audio%20Unit%20Examples%20%28AudioUnit%20Effect%2C%20Generator%2C%20Instrument%2C%20MIDI%20Processor%20and.md)


[Next](AudioUnitEffectExample-Source-CocoaUI-AppleDemoFilterUIView.h.md)[Previous](AudioUnitEffectExample-Source-CocoaUI-AppleDemoFilterUIView.m.md)

# AudioUnitEffectExample/Source/CocoaUI/AppleDemoFilter_GraphView.h

```objc
/*
Copyright (C) 2016 Apple Inc. All Rights Reserved.
See LICENSE.txt for this sample’s licensing information

Abstract:
AU Filter Graph View
*/

#import <Cocoa/Cocoa.h>
#import "Filter.h"

/************************************************************************************************************/
/* NOTE: It is important to rename ALL ui classes when using the XCode Audio Unit with Cocoa View template  */
/*       Cocoa has a flat namespace, and if you use the default filenames, it is possible that you will     */
/*       get a namespace collision with classes from the cocoa view of a previously loaded audio unit.      */
/*       We recommend that you use a unique prefix that includes the manufacturer name and unit name on     */
/*       all objective-C source files. You may use an underscore in your name, but please refrain from      */
/*       starting your class name with an undescore as these names are reserved for Apple.                  */
/************************************************************************************************************/

@interface AppleDemoFilter_GraphView : NSView
{
    NSRect  mGraphFrame;        // This is the frame of the drawing area of the view
    float   mActiveWidth;       // The usable portion of the graph
    NSPoint mEditPoint;         // This is the current location in the drawing area that is active
    BOOL    mMouseDown;         // True if the mouse is currently down

    NSColor *curveColor;        // the current color of the graph curve

    NSImage *mBackgroundCache;  // An image cache of the background so that we don't have to re-draw the grid lines and labels all the time

    float mRes;                 // internal copy of the resonance value
    float mFreq;                // internal copy of the frequency value

    NSBezierPath *mCurvePath;   // The bezier path that is used to draw the curve.

    NSDictionary *mDBAxisStringAttributes;      // Text attributes used to draw the strings on the db axis
    NSDictionary *mFreqAxisStringAttributes;    // Text attributes used to draw the strings on the frequency axis
}

-(void) setRes: (float) res;    // sets the graph's internal resonance value (to match the au)
-(void) setFreq: (float) freq;  // sets the graphs' internal frequency value (to match the au

-(float)getRes;                 // gets the graph's internal resonance value (so the au can match the graph)
-(float)getFreq;                // gets the graph's internal frequency value (so the au can match the graph)

-(double) locationForFrequencyValue: (double) value;    // converts a frequency value to the pixel coordinate in the graph
-(double) locationForDBValue: (double) value;           // converts a db value to the pixel coordinate in the graph

-(FrequencyResponse *) prepareDataForDrawing: (FrequencyResponse *) data;   // prepares the data for drawing by initializing frequency fields based on values on pixel boundaries
-(void) plotData: (FrequencyResponse *) data;                               // draws the curve data
-(void) disableGraphCurve;                                                  // update the view, but don't draw the curve (used when the AU is not initialized and the curve can not be retrieved)

-(void) handleBeginGesture;     // called when parameter automation started
-(void) handleEndGesture;       // called when parameter automation finished

@end
```

[Next](AudioUnitEffectExample-Source-CocoaUI-AppleDemoFilterUIView.h.md)[Previous](AudioUnitEffectExample-Source-CocoaUI-AppleDemoFilterUIView.m.md)

