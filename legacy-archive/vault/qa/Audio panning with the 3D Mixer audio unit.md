---
title: Audio panning with the 3D Mixer audio unit
apple_id: DTS40009995
resource_type: QA
platform: iOS
topic: Audio, Video, & Visual Effects
technology: AudioUnit
published: '2010-05-22'
source_url: https://developer.apple.com/library/archive/qa/qa1695/_index.html
archived_at: '2026-07-18T02:34:12.144997Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1695

# Audio panning with the 3D Mixer audio unit

## Q:  How do I implement audio panning with the 3D Mixer on iPhone OS devices?

A: How do I implement audio panning with the 3D Mixer on iPhone OS devices?

The 3D Mixer audio unit, of subtype `kAudioUnitSubType_AU3DMixerEmbedded`, allows you to mix multiple mono audio streams and specify stereo output panning. You can change the spatial location of each input source by varying its azimuth (angle) and distance relative to the listener, using the `k3DMixerParam_Azimuth` and `k3DMixerParam_Distance` audio unit parameters.

The 3D Mixer audio unit only supports mono LPCM input streams. In other words, it can only accept single-channel input streams. To use a stereo source, you may treat its left and right channels as two independent single-channel sources, and then feed each side of the stereo stream to its own input bus. You should setup a mono stream format for each input bus of the 3D Mixer audio unit.

Make sure you set a non-zero positive distance value, for example 1.0, so that changes to azimuth of the audio unit take effect. The following describes in detail how to do this using the `k3DMixerParam_Distance` and `k3DMixerParam_Azimuth` parameters.

__Listing 1__  Setting a non-zero positive distance

```
Float32 distance = 1.0;  for (int i = 0; i < numbuses; i++) {     AudioUnitSetParameter(mMixer, k3DMixerParam_Distance, kAudioUnitScope_Input, i, distance, 0); }
```


__Listing 2__  Panning from left to right by adjusting azimuth

```
// pan ranges from -1 to +1 Float32 azimuth = 90.0 * pan;  for (int i = 0; i < numbuses; i++) {     AudioUnitSetParameter(mMixer, k3DMixerParam_Azimuth, kAudioUnitScope_Input, i, azimuth, 0); }
```

For more information on how to use the 3D Mixer audio unit, see [Using the 3D Mixer audio unit](https://developer.apple.com/mac/library/technotes/tn2004/tn2112.html). While this document discusses the non-embedded version of this audio unit, they are very similar especially in general setup.

For reference information on the `k3DMixerParam_Distance` and `k3DMixerParam_Azimuth` audio unit parameters, see [Audio Unit Parameters Reference](https://developer.apple.com/mac/library/documentation/AudioUnit/Reference/AudioUnitParametersReference/Reference/reference.html).

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2010-05-22 | New document that discusses how to implement stereo panning using the 3D Mixer audio unit. |

