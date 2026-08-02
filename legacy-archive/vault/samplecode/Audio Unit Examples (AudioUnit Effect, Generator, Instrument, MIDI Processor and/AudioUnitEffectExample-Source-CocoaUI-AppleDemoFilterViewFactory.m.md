---
title: Audio Unit Examples (AudioUnit Effect, Generator, Instrument, MIDI Processor
  and Offline)
apple_id: DTS40013969
resource_type: Sample Code
platform: macOS
topic: Audio, Video, & Visual Effects
technology: AudioUnit
published: '2016-02-19'
source_url: https://developer.apple.com/library/archive/samplecode/sc2195/Listings/AudioUnitEffectExample_Source_CocoaUI_AppleDemoFilter_ViewFactory_m.html
archived_at: '2026-07-26T19:54:12.897948Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Audio Unit Examples (AudioUnit Effect, Generator, Instrument, MIDI Processor and Offline)](Audio%20Unit%20Examples%20%28AudioUnit%20Effect%2C%20Generator%2C%20Instrument%2C%20MIDI%20Processor%20and.md)


[Next](AudioUnitEffectExample-Source-CocoaUI-AppleDemoFilterGraphView.m.md)[Previous](AudioUnitEffectExample-Source-CocoaUI-AppleDemoFilterViewFactory.h.md)

# AudioUnitEffectExample/Source/CocoaUI/AppleDemoFilter_ViewFactory.m

```objc
/*
Copyright (C) 2016 Apple Inc. All Rights Reserved.
See LICENSE.txt for this sample’s licensing information

Abstract:
View Factory Class
*/

#import "AppleDemoFilter_ViewFactory.h"
#import "AppleDemoFilter_UIView.h"

@implementation AppleDemoFilter_ViewFactory

// version 0
- (unsigned) interfaceVersion {
    return 0;
}

// string description of the Cocoa UI
- (NSString *) description {
    return @"Apple Demo: Filter";
}

// N.B.: this class is simply a view-factory,
// returning a new autoreleased view each time it's called.
- (NSView *)uiViewForAudioUnit:(AudioUnit)inAU withSize:(NSSize)inPreferredSize {
    if (! [NSBundle loadNibNamed: @"CocoaView" owner:self]) {
        NSLog (@"Unable to load nib for view.");
        return nil;
    }

    // This particular nib has a fixed size, so we don't do anything with the inPreferredSize argument.
    // It's up to the host application to handle.
    [uiFreshlyLoadedView setAU:inAU];

    NSView *returnView = uiFreshlyLoadedView;
    uiFreshlyLoadedView = nil;  // zero out pointer.  This is a view factory.  Once a view's been created
                                // and handed off, the factory keeps no record of it.

    return [returnView autorelease];
}

@end
```

[Next](AudioUnitEffectExample-Source-CocoaUI-AppleDemoFilterGraphView.m.md)[Previous](AudioUnitEffectExample-Source-CocoaUI-AppleDemoFilterViewFactory.h.md)

