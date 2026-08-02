---
title: OS X v10.10 API Diffs
apple_id: TP40014444
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2014-10-16'
source_url: https://developer.apple.com/library/archive/documentation/General/Reference/APIDiffsMacOSX10_10SeedDiff/frameworks/CoreAudio.html
archived_at: '2026-07-15T07:34:45.002043Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [OS X v10.10 API Diffs](OS%20X%20v10.9%20to%20OS%20X%20v10.10%20API%20Differences.md)


# CoreAudio Changes

## CoreAudio

AudioHardware.hAdded [AudioHardwareCreateAggregateDevice()](https://developer.apple.com/documentation/coreaudio/1422096-audiohardwarecreateaggregatedevi)Added [AudioHardwareDestroyAggregateDevice()](https://developer.apple.com/documentation/coreaudio/1422062-audiohardwaredestroyaggregatedev)AudioHardwareBase.hAdded [kAudioDeviceTransportTypeBluetoothLE](https://developer.apple.com/documentation/coreaudio/kaudiodevicetransporttypebluetoothle)AudioHardwareDeprecated.hModified [kAudioDeviceTransportTypeAutoAggregate](https://developer.apple.com/documentation/coreaudio/kaudiodevicetransporttypeautoaggregate)

|  | Header |
| --- | --- |
| From | CoreAudio/AudioHardwareBase.h |
| To | CoreAudio/AudioHardwareDeprecated.h |

CoreAudioTypes.hRemoved [CalculateLPCMFlags()](https://developer.apple.com/documentation/coreaudio/core_audio_data_types/1804841-calculatelpcmflags)Removed [FillOutASBDForLPCM()](https://developer.apple.com/documentation/coreaudio/core_audio_data_types/1804847-filloutasbdforlpcm)Removed [FillOutAudioTimeStampWithHostTime()](https://developer.apple.com/documentation/coreaudio/core_audio_data_types/1804854-filloutaudiotimestampwithhosttim)Removed [FillOutAudioTimeStampWithSampleAndHostTime()](https://developer.apple.com/documentation/coreaudio/core_audio_data_types/1804865-filloutaudiotimestampwithsamplea)Removed [FillOutAudioTimeStampWithSampleTime()](https://developer.apple.com/documentation/coreaudio/core_audio_data_types/1804859-filloutaudiotimestampwithsamplet)Removed [IsAudioFormatNativeEndian()](https://developer.apple.com/documentation/coreaudio/core_audio_data_types/1804821-isaudioformatnativeendian)Added [AudioFormatFlags](https://developer.apple.com/documentation/coreaudio/audioformatflags)Added [AudioFormatID](https://developer.apple.com/documentation/coreaudio/audioformatid)Added #def CA_CANONICAL_DEPRECATEDAdded [kAudioFormatAMR_WB](https://developer.apple.com/documentation/coreaudio/1572096-audio_data_format_identifiers/kaudioformatamr_wb)Modified [AudioSampleType](https://developer.apple.com/documentation/coreaudio/audiosampletype)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [AudioUnitSampleType](https://developer.apple.com/documentation/coreaudio/audiounitsampletype)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [kAudioFormatFlagsAudioUnitCanonical](https://developer.apple.com/documentation/coreaudio/kaudioformatflagsaudiounitcanonical)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [kAudioFormatFlagsCanonical](https://developer.apple.com/documentation/coreaudio/kaudioformatflagscanonical)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

## Sending feedback…

## We’re sorry, an error has occurred.

Please try submitting your feedback later.

## Thank you for providing feedback!

Your input helps improve our developer documentation.

## How helpful is this document?

\*

Very helpful

Somewhat helpful

Not helpful

## How can we improve this document?

Fix typos or links

Fix incorrect information

Add or update code samples

Add or update illustrations

Add information about...

\*

_\* Required information_

To submit a product bug or enhancement request, please visit the
[Bug Reporter](https://developer.apple.com/bugreporter/)
page.

Please read [Apple's Unsolicited Idea Submission Policy](http://www.apple.com/legal/policies/ideas.html)
before you send us your feedback.

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
