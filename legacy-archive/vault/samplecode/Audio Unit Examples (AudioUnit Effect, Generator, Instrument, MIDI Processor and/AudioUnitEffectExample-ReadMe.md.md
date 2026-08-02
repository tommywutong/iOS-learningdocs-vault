---
title: Audio Unit Examples (AudioUnit Effect, Generator, Instrument, MIDI Processor
  and Offline)
apple_id: DTS40013969
resource_type: Sample Code
platform: macOS
topic: Audio, Video, & Visual Effects
technology: AudioUnit
published: '2016-02-19'
source_url: https://developer.apple.com/library/archive/samplecode/sc2195/Listings/AudioUnitEffectExample_ReadMe_md.html
archived_at: '2026-07-26T19:54:12.967003Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Audio Unit Examples (AudioUnit Effect, Generator, Instrument, MIDI Processor and Offline)](Audio%20Unit%20Examples%20%28AudioUnit%20Effect%2C%20Generator%2C%20Instrument%2C%20MIDI%20Processor%20and.md)


[Next](ReadMe.md.md)[Previous](AudioUnitEffectExample-Source-CocoaUI-AppleDemoFilterUIView.h.md)

# AudioUnitEffectExample/ReadMe.md

```
ReadMe for FilterDemo
---------------------

FilterDemo project will build a simple Effect Audio Unit with a Cocoa Custom View (UI). The effect is a simple resonant low-pass filter which has two parameters: cutoff frequency and resonance. It demonstrates how to implement a custom property for communicating information between the Audio Unit and its view.
Also, it shows how to publish factory presets. The Cocoa view features a resizable real-time display of the frequency-response curve which can be directly manipulated through a control point.

There are two targets in the FilterDemo project:
FilterDemo - builds both the Audio Unit component and the CocoaUI bundle
CocoaUI    - builds just the CocoaUI bundle

Note:
The implementation subclasses the AUEffectBase class which assumes that the effect processes
the same number of input channels as output channels (n->n). Furthermore, AUEffectBase assumes that the processing will occur independently on each of these channels.  This may not be appropriate for some kinds of effects which require access to all channels at the same time (stereo-locked compressors, cross-coupling reverbs).  For these types of effects it is better to subclass AUBase, and override the Render() method.
```

[Next](ReadMe.md.md)[Previous](AudioUnitEffectExample-Source-CocoaUI-AppleDemoFilterUIView.h.md)

