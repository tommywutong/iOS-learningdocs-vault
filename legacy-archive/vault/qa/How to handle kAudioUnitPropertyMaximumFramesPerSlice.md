---
title: How to handle kAudioUnitProperty_MaximumFramesPerSlice
apple_id: DTS10004404
resource_type: QA
platform: macOS
topic: Audio, Video, & Visual Effects
technology: AudioUnit
published: '2015-05-28'
source_url: https://developer.apple.com/library/archive/qa/qa1533/_index.html
archived_at: '2026-07-18T02:32:15.099316Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1533

# How to handle kAudioUnitProperty_MaximumFramesPerSlice

## Q:  What is the `kAudioUnitProperty_MaximumFramesPerSlice` and how do I use it appropriately?

A: The `kAudioUnitProperty_MaximumFramesPerSlice` is used by Audio Units to determine what the maximum number of frames the Audio Unit will be asked to render for any given render call. If you ask an Audio Unit to render for more frames than the value specified by this property, the Audio Unit will return an error and not render any data. Therefore, you need to ensure that value specified by the `kAudioUnitProperty_MaximumFramesPerSlice` property is always as big as the largest number of frames you would ask to render.

__Listing 1__  Configuring maximum frames

```
// get the output device's frame count and set any Audio Units to match
UInt32 numFrames;
UInt32 dataSize = sizeof(numFrames);

AudioObjectPropertyAddress theAddress = { kAudioDevicePropertyBufferFrameSize,
                                          kAudioObjectPropertyScopeGlobal,
                                          kAudioObjectPropertyElementMaster };

result = AudioObjectGetPropertyData(myDeviceID, theAddress, 0, NULL, &dataSize, &numFrames);

if (result == noErr)
{
    result = AudioUnitSetProperty(myOutputAU, kAudioUnitProperty_MaximumFramesPerSlice,
        kAudioUnitScope_Global, 0, &numFrames, sizeof(numFrames));

    result = AudioUnitSetProperty(myMixerAU, kAudioUnitProperty_MaximumFramesPerSlice,
        kAudioUnitScope_Global, 0, &numFrames, sizeof(numFrames));
}
```

If you utilize any sample rate conversions in your Audio Unit chain or graph it is important to take this into account. For example, if the output sample rate of your AUConverter is 44.1kHz and the input is 22.0kHz the AUConverter will scale up its maximum frames by 2X to ensure it will be able to pull the data through correctly.

__Listing 2__  AUConverter scaling

```
// input sample rate = 22kHz
// output sample rate = 44.1kHz

UInt32 numFrames = 1500;
UInt32 dataSize = sizeof(numFrames);

AudioUnitSetProperty(myAU, kAudioUnitProperty_MaximumFramesPerSlice,
    kAudioUnitScope_Global, 0, &numFrames, sizeof(numFrames));

// the AUConverter will scale up
AudioUnitGetProperty(myAU, kAudioUnitProperty_MaximumFramesPerSlice,
    kAudioUnitScope_Global, 0, &numFrames, &dataSize);

// numFrames is now 3000
```

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2015-05-28 | Updated Listing 1 to use AudioObjectGetPropertyData |
| 2012-03-06 | Editorial |
| 2007-07-16 | New document that illustrates how to use the kAudioUnitProperty_MaximumFramesPerSlice property |

