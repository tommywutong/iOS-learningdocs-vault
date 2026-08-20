---
title: AudioDevice Sample Rates
apple_id: DTS10002385
resource_type: QA
platform: macOS
topic: Audio, Video, & Visual Effects
technology: CoreAudio
published: '2011-07-22'
source_url: https://developer.apple.com/library/archive/qa/qa1196/_index.html
archived_at: '2026-07-18T02:30:12.362653Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1196

# AudioDevice Sample Rates

## Q:  How do I get and set the sample rate for an AudioDevice? What if my input audio device has a different sample rate than the output device, how can I handle conversions between the two?

A: The code below is taken from the CoreAudio Public Utility Sources (/Developer/Extras/CoreAudio/PublicUtility/CAHALAudioDevice.\*) and can be used to get and set available sample rate ranges for a given HAL Audio Device.

__Listing 1__  How to get and set the available sample rate ranges.

```
Float64	CAHALAudioDevice::GetNominalSampleRate() const {     Float64 theAnswer = 0;     CAPropertyAddress theAddress(kAudioDevicePropertyNominalSampleRate);     UInt32 theSize = sizeof(Float64);     GetPropertyData(theAddress, 0, NULL, theSize, &theAnswer);     return theAnswer; }  void	CAHALAudioDevice::SetNominalSampleRate(Float64 inSampleRate) {     CAPropertyAddress theAddress(kAudioDevicePropertyNominalSampleRate);     SetPropertyData(theAddress, 0, NULL, sizeof(Float64), &inSampleRate); }  UInt32	CAHALAudioDevice::GetNumberAvailableNominalSampleRateRanges() const {     UInt32 theAnswer = 0;     CAPropertyAddress theAddress(kAudioDevicePropertyAvailableNominalSampleRates);     if(HasProperty(theAddress))     {         UInt32 theSize = GetPropertyDataSize(theAddress, 0, NULL);         theAnswer = theSize / sizeof(AudioValueRange);     }     return theAnswer; }  void	CAHALAudioDevice::GetAvailableNominalSampleRateRanges(UInt32& ioNumberRanges, AudioValueRange* outRanges) const {     CAPropertyAddress theAddress(kAudioDevicePropertyAvailableNominalSampleRates);     if(HasProperty(theAddress))     {         UInt32 theSize = ioNumberRanges * sizeof(AudioValueRange);         GetPropertyData(theAddress, 0, NULL, theSize, outRanges);         ioNumberRanges = theSize / sizeof(AudioValueRange);     }     else     {         ioNumberRanges = 0;     } }
```

There are two ways to meet your goals when the input has a different sample rate than the output:

1. You can use an AudioConverter to handle the sample rate conversions between the devices. An AudioConverter can be created with the input and output stream formats. Then you must use AudioConverterFillBuffer to convert a buffer of data.
2. Use the DefaultOutputUnit. This audio unit will handle sample rate converstion between your input device and the default output device automatically. See [DefaultOutputUnit sample code.](https://developer.apple.com/library/mac/#samplecode/DefaultOutputUnit/Introduction/Intro.html)

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2011-07-22 | Editorial |
| 2003-12-09 | New document that getting, setting and converting sample rates with Audio Devices. |

