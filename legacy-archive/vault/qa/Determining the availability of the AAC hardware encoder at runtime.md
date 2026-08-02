---
title: Determining the availability of the AAC hardware encoder at runtime
apple_id: DTS40009213
resource_type: QA
platform: iOS
topic: Audio, Video, & Visual Effects
technology: AudioToolbox
published: '2010-12-23'
source_url: https://developer.apple.com/library/archive/qa/qa1663/_index.html
archived_at: '2026-07-18T02:33:22.481119Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1663

# Determining the availability of the AAC hardware encoder at runtime

## Q:  How can I determine the availability of the AAC hardware encoder at runtime?

A: How can I determine the availability of the AAC hardware encoder at runtime?

iOS 4.0 and later supports hardware-assisted offline encoding using Extended Audio File and Audio Converter APIs.

To check for the availablility of the AAC hardware encoder, get the Audio Format `kAudioFormatProperty_Encoders` property using `kAudioFormatMPEG4AAC` as the encoder specifier, then compare the  `mSubType`  and `mManufacturer` fields of returned `AudioClassDescription` structures for `kAudioFormatMPEG4AAC` and `kAppleHardwareAudioCodecManufacturer`, as shown in Listing 1.

__Listing 1__  Using AudioFormat to check the availability of the AAC hardware encoder.

```
Boolean IsAACHardwareEncoderAvailable(void) {     Boolean isAvailable = false;     OSStatus error;      // get an array of AudioClassDescriptions for all installed encoders for the given format      // the specifier is the format that we are interested in - this is 'aac ' in our case     UInt32 encoderSpecifier = kAudioFormatMPEG4AAC;     UInt32 size;      error = AudioFormatGetPropertyInfo(kAudioFormatProperty_Encoders, sizeof(encoderSpecifier),                                          &encoderSpecifier, &size);     if (error) { printf("AudioFormatGetPropertyInfo kAudioFormatProperty_Encoders                           error %lu %4.4s\n", error, (char*)&error); return false; }      UInt32 numEncoders = size / sizeof(AudioClassDescription);     AudioClassDescription encoderDescriptions[numEncoders];      error = AudioFormatGetProperty(kAudioFormatProperty_Encoders, sizeof(encoderSpecifier),                                      &encoderSpecifier, &size, encoderDescriptions);     if (error) { printf("AudioFormatGetProperty kAudioFormatProperty_Encoders error %lu %4.4s\n",                           error, (char*)&error); return false; }      for (UInt32 i=0; i < numEncoders; ++i) {         if (encoderDescriptions[i].mSubType == kAudioFormatMPEG4AAC &&             encoderDescriptions[i].mManufacturer == kAppleHardwareAudioCodecManufacturer) isAvailable = true;     }      return isAvailable; }
```

The check demonstrated above is only one of a number of steps that must be followed when performing hardware-assisted offline encoding. For details concerning Audio Session configuration and Interruption Handling during an encoding operation, refer to the Audio Session Programming Guide, iPhoneExtAudioFileConvertTest and iPhoneACFileConvertTest samples available in the [iOS Reference Library](https://developer.apple.com/devcenter/ios/).

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2010-12-23 | Updated for 4.1 |
| 2009-09-08 | New document that describes how to find out if the AAC hardware encoder is available at runtime. |

