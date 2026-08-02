---
title: Audio Unit Examples (AudioUnit Effect, Generator, Instrument, MIDI Processor
  and Offline)
apple_id: DTS40013969
resource_type: Sample Code
platform: macOS
topic: Audio, Video, & Visual Effects
technology: AudioUnit
published: '2016-02-19'
source_url: https://developer.apple.com/library/archive/samplecode/sc2195/Listings/AudioUnitEffectExample_Source_CocoaUI_AppleDemoFilter_UIView_h.html
archived_at: '2026-07-26T19:54:12.963199Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Audio Unit Examples (AudioUnit Effect, Generator, Instrument, MIDI Processor and Offline)](Audio%20Unit%20Examples%20%28AudioUnit%20Effect%2C%20Generator%2C%20Instrument%2C%20MIDI%20Processor%20and.md)


[Next](AudioUnitEffectExample-ReadMe.md.md)[Previous](AudioUnitEffectExample-Source-CocoaUI-AppleDemoFilterGraphView.h.md)

# AudioUnitEffectExample/Source/CocoaUI/AppleDemoFilter_UIView.h

```objc
/*
Copyright (C) 2016 Apple Inc. All Rights Reserved.
See LICENSE.txt for this sample’s licensing information

*/

#import <Cocoa/Cocoa.h>
#import <AudioUnit/AudioUnit.h>
#import <AudioToolbox/AudioToolbox.h>

#import "AppleDemoFilter_GraphView.h"
#import "Filter.h"

/************************************************************************************************************/
/* NOTE: It is important to rename ALL ui classes when using the XCode Audio Unit with Cocoa View template  */
/*       Cocoa has a flat namespace, and if you use the default filenames, it is possible that you will     */
/*       get a namespace collision with classes from the cocoa view of a previously loaded audio unit.      */
/*       We recommend that you use a unique prefix that includes the manufacturer name and unit name on     */
/*       all objective-C source files. You may use an underscore in your name, but please refrain from      */
/*       starting your class name with an undescore as these names are reserved for Apple.                  */
/************************************************************************************************************/

@interface AppleDemoFilter_UIView : NSView
{
    IBOutlet AppleDemoFilter_GraphView  *graphView;
    IBOutlet NSTextField                *cutoffFrequencyField;
    IBOutlet NSTextField                *resonanceField;

    // Other Members
    AudioUnit               mAU;
    AUEventListenerRef      mAUEventListener;

    FrequencyResponse      *mData;              // the data used to draw the filter curve
    NSColor                *mBackgroundColor;   // the background color (pattern) of the view
}

#pragma mark ____ PUBLIC FUNCTIONS ____
- (void)setAU:(AudioUnit)inAU;

#pragma mark ____ INTERFACE ACTIONS ____
- (IBAction) cutoffFrequencyChanged:(id)sender;
- (IBAction) resonanceChanged:(id)sender;

#pragma mark ____ PRIVATE FUNCTIONS
- (void)priv_synchronizeUIWithParameterValues;
- (void)priv_addListeners;
- (void)priv_removeListeners;

#pragma mark ____ LISTENER CALLBACK DISPATCHEE ____
- (void)priv_eventListener:(void *) inObject event:(const AudioUnitEvent *)inEvent value:(Float32)inValue;
@end
```

[Next](AudioUnitEffectExample-ReadMe.md.md)[Previous](AudioUnitEffectExample-Source-CocoaUI-AppleDemoFilterGraphView.h.md)

