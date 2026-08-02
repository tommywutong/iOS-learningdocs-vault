---
title: OS X v10.9 API Diffs
apple_id: TP40013007
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2013-10-22'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_9/CoreAudio.html
archived_at: '2026-07-18T02:54:11.139135Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.9 API Diffs](OS%20X%20v10.8%20to%20OS%20X%20v10.9%20API%20Differences.md)


# CoreAudio Changes

## CoreAudio

AudioHardware.hAdded [kAudioDevicePropertyIOStoppedAbnormally](https://developer.apple.com/documentation/coreaudio/1545866-anonymous/kaudiodevicepropertyiostoppedabnormally)Added [kAudioHardwarePowerHintFavorSavingPower](https://developer.apple.com/documentation/coreaudio/audiohardwarepowerhint/kaudiohardwarepowerhintfavorsavingpower)Added [kAudioHardwarePowerHintNone](https://developer.apple.com/documentation/coreaudio/audiohardwarepowerhint/kaudiohardwarepowerhintnone)Added [kAudioHardwarePropertyBoxList](https://developer.apple.com/documentation/coreaudio/1545886-anonymous/kaudiohardwarepropertyboxlist)Added [kAudioHardwarePropertyPlugInList](https://developer.apple.com/documentation/coreaudio/kaudiohardwarepropertypluginlist)Added [kAudioHardwarePropertyPowerHint](https://developer.apple.com/documentation/coreaudio/kaudiohardwarepropertypowerhint)Added [kAudioHardwarePropertyTranslateBundleIDToPlugIn](https://developer.apple.com/documentation/coreaudio/kaudiohardwarepropertytranslatebundleidtoplugin)Added [kAudioHardwarePropertyTranslateUIDToBox](https://developer.apple.com/documentation/coreaudio/kaudiohardwarepropertytranslateuidtobox)Modified [kAudioHardwarePropertyPlugInForBundleID](https://developer.apple.com/documentation/coreaudio/kaudiohardwarepropertypluginforbundleid)

|  | Header |
| --- | --- |
| From | CoreAudio/AudioHardware.h |
| To | CoreAudio/AudioHardwareDeprecated.h |

AudioHardwareBase.hAdded [kAudioBoxClassID](https://developer.apple.com/documentation/coreaudio/kaudioboxclassid)Added [kAudioBoxPropertyAcquired](https://developer.apple.com/documentation/coreaudio/1494522-anonymous/kaudioboxpropertyacquired)Added [kAudioBoxPropertyAcquisitionFailed](https://developer.apple.com/documentation/coreaudio/kaudioboxpropertyacquisitionfailed)Added [kAudioBoxPropertyBoxUID](https://developer.apple.com/documentation/coreaudio/kaudioboxpropertyboxuid)Added [kAudioBoxPropertyDeviceList](https://developer.apple.com/documentation/coreaudio/1494522-anonymous/kaudioboxpropertydevicelist)Added [kAudioBoxPropertyHasAudio](https://developer.apple.com/documentation/coreaudio/kaudioboxpropertyhasaudio)Added [kAudioBoxPropertyHasMIDI](https://developer.apple.com/documentation/coreaudio/1494522-anonymous/kaudioboxpropertyhasmidi)Added [kAudioBoxPropertyHasVideo](https://developer.apple.com/documentation/coreaudio/1494522-anonymous/kaudioboxpropertyhasvideo)Added [kAudioBoxPropertyIsProtected](https://developer.apple.com/documentation/coreaudio/1494522-anonymous/kaudioboxpropertyisprotected)Added [kAudioBoxPropertyTransportType](https://developer.apple.com/documentation/coreaudio/1494522-anonymous/kaudioboxpropertytransporttype)Added [kAudioObjectPropertyFirmwareVersion](https://developer.apple.com/documentation/coreaudio/1494449-anonymous/kaudioobjectpropertyfirmwareversion)Added [kAudioObjectPropertyIdentify](https://developer.apple.com/documentation/coreaudio/1494449-anonymous/kaudioobjectpropertyidentify)Added [kAudioObjectPropertySerialNumber](https://developer.apple.com/documentation/coreaudio/1494449-anonymous/kaudioobjectpropertyserialnumber)Added [kAudioPlugInPropertyBoxList](https://developer.apple.com/documentation/coreaudio/kaudiopluginpropertyboxlist)Added [kAudioPlugInPropertyTranslateUIDToBox](https://developer.apple.com/documentation/coreaudio/1494489-anonymous/kaudiopluginpropertytranslateuidtobox)AudioHardwareDeprecated.hModified [kAudioHardwarePropertyPlugInForBundleID](https://developer.apple.com/documentation/coreaudio/kaudiohardwarepropertypluginforbundleid)

|  | Header |
| --- | --- |
| From | CoreAudio/AudioHardware.h |
| To | CoreAudio/AudioHardwareDeprecated.h |

AudioServerPlugIn.hRemoved kAudioDeviceClockAlgorithmUnclockedAdded [kAudioDevicePropertyClockIsStable](https://developer.apple.com/documentation/coreaudio/1583996-anonymous/kaudiodevicepropertyclockisstable)CoreAudioTypes.hAdded [kAudioChannelLayoutTag_AAC_7_1_C](https://developer.apple.com/documentation/coreaudio/1572101-audio_channel_layout_tags/kaudiochannellayouttag_aac_7_1_c)Added [kAudio_BadFilePathError](https://developer.apple.com/documentation/coreaudio/kaudio_badfilepatherror)Added [kAudio_FilePermissionError](https://developer.apple.com/documentation/coreaudio/1572099-anonymous/kaudio_filepermissionerror)Added [kAudio_TooManyFilesOpenError](https://developer.apple.com/documentation/coreaudio/1572099-anonymous/kaudio_toomanyfilesopenerror)

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
