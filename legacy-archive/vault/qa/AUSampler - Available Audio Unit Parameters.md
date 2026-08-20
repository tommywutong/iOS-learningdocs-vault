---
title: AUSampler - Available Audio Unit Parameters
apple_id: DTS40013145
resource_type: QA
platform: iOS|macOS
topic: Audio, Video, & Visual Effects
technology: AudioUnit
published: '2013-02-21'
source_url: https://developer.apple.com/library/archive/qa/qa1632/_index.html
archived_at: '2026-07-18T02:33:02.609434Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1632

# AUSampler - Available Audio Unit Parameters

## Q:  What are the available parameters for the AUSampler Audio Unit Instrument?

A: `AudioUnitParameters.h` defines the following parameters for the AUSampler:


```swift
// Music Device
// Parameters for the AUSampler unit
enum {
        // Global, dB, -90->12, 0
    kAUSamplerParam_Gain			= 900,

        // Global, Semitones, -24->24, 0
    kAUSamplerParam_CoarseTuning		= 901,

        // Global, Cents, -99->99, 0
    kAUSamplerParam_FineTuning			= 902,

        // Global, -1.0->1.0, 0
    kAUSamplerParam_Pan				= 903
};
```

These four parameters affect the Global Gain, Course Tuning, Fine Tuning, and Stereo Pan of the Sampler's output.

The Sampler Audio Unit additionally supports a set of eight "Performance Parameters" that can be queried via the `kAudioUnitProperty_ParameterList` property:


```
Parameter: 1000 - Performance Parameter 01
Parameter: 1001 - Performance Parameter 02
Parameter: 1002 - Performance Parameter 03
Parameter: 1003 - Performance Parameter 04
Parameter: 1004 - Performance Parameter 05
Parameter: 1005 - Performance Parameter 06
Parameter: 1006 - Performance Parameter 07
Parameter: 1007 - Performance Parameter 08
```

When designing a preset for the Sampler Audio Unit via its custom view in the AU Lab application, each of these eight Performance Parameters can be mapped to modify (in real time) some aspect of the Sampler instrument's state. For example, you can set Performance Parameter 01 to modify the attack time of the first envelope generator, Performance Parameter 02 to modify the filter cutoff frequency, Performance Parameter 03 to modify the LFO rate, and so on. There is a lot of flexibility available with these eight parameters. Once these parameter mappings are set up in the Performance Parameter Editor, they can be stored into the preset. These parameters have the advantage that they can be [automated](https://developer.apple.com/library/mac/#documentation/MusicAudio/Conceptual/AudioUnitProgrammingGuide/AudioUnitDevelopmentFundamentals/AudioUnitDevelopmentFundamentals.html#//apple_ref/doc/uid/TP40003278-CH7-SW13) using Parameter Events.

Using AU Lab's Connection Editor, you can also map any available MIDI controller to modify the same aspects of the instrument's state. For example, controller 67 could be configured to adjust the LFO's delay time. These have the advantages that there are a large number of available controllers, and that the controller data (and therefor the automation) can be stored directory into the MIDI data.

AU Lab can be found on of the "Audio Tools for Xcode" disk image available [here](https://developer.apple.com/downloads/index.action).

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2013-02-21 | New document that describes the available Audio Unit Parameters when using the AUSampler. |

