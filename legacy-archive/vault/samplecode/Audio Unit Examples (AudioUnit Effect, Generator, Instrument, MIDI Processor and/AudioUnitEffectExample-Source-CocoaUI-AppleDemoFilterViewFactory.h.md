---
title: Audio Unit Examples (AudioUnit Effect, Generator, Instrument, MIDI Processor
  and Offline)
apple_id: DTS40013969
resource_type: Sample Code
platform: macOS
topic: Audio, Video, & Visual Effects
technology: AudioUnit
published: '2016-02-19'
source_url: https://developer.apple.com/library/archive/samplecode/sc2195/Listings/AudioUnitEffectExample_Source_CocoaUI_AppleDemoFilter_ViewFactory_h.html
archived_at: '2026-07-26T19:54:12.892417Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Audio Unit Examples (AudioUnit Effect, Generator, Instrument, MIDI Processor and Offline)](Audio%20Unit%20Examples%20%28AudioUnit%20Effect%2C%20Generator%2C%20Instrument%2C%20MIDI%20Processor%20and.md)


[Next](AudioUnitEffectExample-Source-CocoaUI-AppleDemoFilterViewFactory.m.md)[Previous](AudioUnitEffectExample-Source-AUSource-Filter.cpp.md)

# AudioUnitEffectExample/Source/CocoaUI/AppleDemoFilter_ViewFactory.h

```objc
/*
Copyright (C) 2016 Apple Inc. All Rights Reserved.
See LICENSE.txt for this sample’s licensing information

Abstract:
View Factory Class
*/

#import <Cocoa/Cocoa.h>
#import <AudioUnit/AUCocoaUIView.h>

/************************************************************************************************************/
/* NOTE: It is important to rename ALL ui classes when using the XCode Audio Unit with Cocoa View template  */
/*       Cocoa has a flat namespace, and if you use the default filenames, it is possible that you will     */
/*       get a namespace collision with classes from the cocoa view of a previously loaded audio unit.      */
/*       We recommend that you use a unique prefix that includes the manufacturer name and unit name on     */
/*       all objective-C source files. You may use an underscore in your name, but please refrain from      */
/*       starting your class name with an undescore as these names are reserved for Apple.                  */
/************************************************************************************************************/

@class AppleDemoFilter_UIView;

@interface AppleDemoFilter_ViewFactory : NSObject <AUCocoaUIBase>
{
    IBOutlet AppleDemoFilter_UIView *uiFreshlyLoadedView;   // This class is the File's Owner of the CocoaView nib
}                                                           // This data member needs to be the same class as the view class the factory will return

- (NSString *) description; // string description of the view

@end
```

[Next](AudioUnitEffectExample-Source-CocoaUI-AppleDemoFilterViewFactory.m.md)[Previous](AudioUnitEffectExample-Source-AUSource-Filter.cpp.md)

