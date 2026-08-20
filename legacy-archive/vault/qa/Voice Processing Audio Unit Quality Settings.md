---
title: Voice Processing Audio Unit Quality Settings
apple_id: DTS40010211
resource_type: QA
platform: iOS
topic: Audio, Video, & Visual Effects
technology: AudioUnit
published: '2010-07-27'
source_url: https://developer.apple.com/library/archive/qa/qa1683/_index.html
archived_at: '2026-07-18T02:33:47.528258Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1683

# Voice Processing Audio Unit Quality Settings

## Q:  What are the differences between the quality values set with the `kAUVoiceIOProperty_VoiceProcessingQuality` property?

A: iOS 4 includes a new Voice Processing Audio Unit which provides significantly better audio quality and is specially designed for high-quality voice chatting. Two algorithms are now available allowing developers to fine tune the quality versus complexity (CPU usage) tradeoff.

The values between `0 - 63` use the standard suppression algorithm from iPhone OS 3 for lower CPU usage, while values between `64 - 127` use the high-quality echo canceler for superior echo rejection. The default value for this property is `127`.

__Listing 1__  Setting the Voice Processor Quality.

```
OSStatus SetVoiceAUQuality(AudioUnit inVoiceUnit, UInt32 inQuality)
{
    if ((inVoiceUnit == NULL) || (inQuality > 127)) return paramErr;

    OSStatus result = AudioUnitSetProperty(inVoiceUnit, kAUVoiceIOProperty_VoiceProcessingQuality, kAudioUnitScope_Global, 1, &inQuality, sizeof(inQuality));
    if (result) NSLog(@"Error setting voice unit quality: %ld\n", result);
    return result;
}
```

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2010-07-27 | New document that describes the differences between the quality values which can be set with the kAUVoiceIOProperty_VoiceProcessingQuality property. |

