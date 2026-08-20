---
title: OS X v10.7 API Diffs
apple_id: TP40010630
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2011-06-06'
source_url: https://developer.apple.com/library/archive/releasenotes/General/MacOSXLionAPIDiffs/CoreAudio.html
archived_at: '2026-07-18T02:54:26.491476Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.7 API Diffs](OS%20X%20v10.6%20to%20v10.7%20API%20Diffs.md)


# CoreAudio Changes

## CoreAudio

|  | Framework Architectures |
| --- | --- |
| From | i386,ppc,x86_64 |
| To | i386,x86_64 |

AudioHardware.hAdded [AudioDeviceCreateIOProcIDWithBlock()](https://developer.apple.com/documentation/coreaudio/1422986-audiodevicecreateioprocidwithblo)Added [AudioDeviceIOBlock](https://developer.apple.com/documentation/coreaudio/audiodeviceioblock)Added [AudioObjectAddPropertyListenerBlock()](https://developer.apple.com/documentation/coreaudio/1422686-audioobjectaddpropertylistenerbl)Added [AudioObjectPropertyListenerBlock](https://developer.apple.com/documentation/coreaudio/audioobjectpropertylistenerblock)Added [AudioObjectRemovePropertyListenerBlock()](https://developer.apple.com/documentation/coreaudio/1421640-audioobjectremovepropertylistene)Added [#def kAudioAggregateDeviceIsStackedKey](https://developer.apple.com/documentation/coreaudio/kaudioaggregatedeviceisstackedkey)Added [kAudioDevicePropertyDataSourceKindForID](https://developer.apple.com/documentation/coreaudio/1545881-anonymous/kaudiodevicepropertydatasourcekindforid)Added [kAudioDevicePropertyHighPassFilterSetting](https://developer.apple.com/documentation/coreaudio/kaudiodevicepropertyhighpassfiltersetting)Added [kAudioDevicePropertyHighPassFilterSettingNameForID](https://developer.apple.com/documentation/coreaudio/kaudiodevicepropertyhighpassfiltersettingnameforid)Added [kAudioDevicePropertyHighPassFilterSettingNameForIDCFString](https://developer.apple.com/documentation/coreaudio/1545881-anonymous/kaudiodevicepropertyhighpassfiltersettingnameforidcfstring)Added [kAudioDevicePropertyHighPassFilterSettings](https://developer.apple.com/documentation/coreaudio/1545881-anonymous/kaudiodevicepropertyhighpassfiltersettings)Added [kAudioDevicePropertyPhantomPower](https://developer.apple.com/documentation/coreaudio/kaudiodevicepropertyphantompower)Added [kAudioDevicePropertyPhaseInvert](https://developer.apple.com/documentation/coreaudio/kaudiodevicepropertyphaseinvert)Added [kAudioDeviceTransportTypeDisplayPort](https://developer.apple.com/documentation/coreaudio/kaudiodevicetransporttypedisplayport)Added [kAudioDeviceTransportTypeHDMI](https://developer.apple.com/documentation/coreaudio/1494580-anonymous/kaudiodevicetransporttypehdmi)Added [kAudioHighPassFilterControlClassID](https://developer.apple.com/documentation/coreaudio/kaudiohighpassfiltercontrolclassid)Added [kAudioObjectPropertyBaseClass](https://developer.apple.com/documentation/coreaudio/1494449-anonymous/kaudioobjectpropertybaseclass)Added [kAudioPhantomPowerControlClassID](https://developer.apple.com/documentation/coreaudio/1494512-anonymous/kaudiophantompowercontrolclassid)Added [kAudioPhaseInvertControlClassID](https://developer.apple.com/documentation/coreaudio/1494512-anonymous/kaudiophaseinvertcontrolclassid)Added [kAudioSelectorControlItemKindSpacer](https://developer.apple.com/documentation/coreaudio/1494470-anonymous/kaudioselectorcontrolitemkindspacer)Added [kAudioSelectorControlPropertyItemKind](https://developer.apple.com/documentation/coreaudio/kaudioselectorcontrolpropertyitemkind)Added [kAudioSliderControlClassID](https://developer.apple.com/documentation/coreaudio/kaudioslidercontrolclassid)Added [kAudioSliderControlPropertyRange](https://developer.apple.com/documentation/coreaudio/1494510-anonymous/kaudioslidercontrolpropertyrange)Added [kAudioSliderControlPropertyValue](https://developer.apple.com/documentation/coreaudio/1494510-anonymous/kaudioslidercontrolpropertyvalue)Added [kAudioStreamPropertyIsActive](https://developer.apple.com/documentation/coreaudio/1494541-anonymous/kaudiostreampropertyisactive)Added [kAudioStreamTerminalTypeDisplayPort](https://developer.apple.com/documentation/coreaudio/1494543-anonymous/kaudiostreamterminaltypedisplayport)Added [kAudioStreamTerminalTypeHDMI](https://developer.apple.com/documentation/coreaudio/kaudiostreamterminaltypehdmi)Modified [AudioHardwareRemoveRunLoopSource()](https://developer.apple.com/documentation/coreaudio/1580717-audiohardwareremoverunloopsource)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified [AudioHardwareAddRunLoopSource()](https://developer.apple.com/documentation/coreaudio/1580725-audiohardwareaddrunloopsource)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

AudioHardwarePlugIn.hAdded #def kAudioHardwarePlugInInterface5IDCoreAudioTypes.hAdded [kAudioChannelLayoutTag_DTS_3_1](https://developer.apple.com/documentation/coreaudio/1572101-audio_channel_layout_tags/kaudiochannellayouttag_dts_3_1)Added [kAudioChannelLayoutTag_DTS_4_1](https://developer.apple.com/documentation/coreaudio/1572101-audio_channel_layout_tags/kaudiochannellayouttag_dts_4_1)Added [kAudioChannelLayoutTag_DTS_6_0_A](https://developer.apple.com/documentation/coreaudio/1572101-audio_channel_layout_tags/kaudiochannellayouttag_dts_6_0_a)Added [kAudioChannelLayoutTag_DTS_6_0_B](https://developer.apple.com/documentation/coreaudio/1572101-audio_channel_layout_tags/kaudiochannellayouttag_dts_6_0_b)Added [kAudioChannelLayoutTag_DTS_6_0_C](https://developer.apple.com/documentation/coreaudio/kaudiochannellayouttag_dts_6_0_c)Added [kAudioChannelLayoutTag_DTS_6_1_A](https://developer.apple.com/documentation/coreaudio/kaudiochannellayouttag_dts_6_1_a)Added [kAudioChannelLayoutTag_DTS_6_1_B](https://developer.apple.com/documentation/coreaudio/1572101-audio_channel_layout_tags/kaudiochannellayouttag_dts_6_1_b)Added [kAudioChannelLayoutTag_DTS_6_1_C](https://developer.apple.com/documentation/coreaudio/kaudiochannellayouttag_dts_6_1_c)Added [kAudioChannelLayoutTag_DTS_6_1_D](https://developer.apple.com/documentation/coreaudio/1572101-audio_channel_layout_tags/kaudiochannellayouttag_dts_6_1_d)Added [kAudioChannelLayoutTag_DTS_7_0](https://developer.apple.com/documentation/coreaudio/1572101-audio_channel_layout_tags/kaudiochannellayouttag_dts_7_0)Added [kAudioChannelLayoutTag_DTS_7_1](https://developer.apple.com/documentation/coreaudio/1572101-audio_channel_layout_tags/kaudiochannellayouttag_dts_7_1)Added [kAudioChannelLayoutTag_DTS_8_0_A](https://developer.apple.com/documentation/coreaudio/kaudiochannellayouttag_dts_8_0_a)Added [kAudioChannelLayoutTag_DTS_8_0_B](https://developer.apple.com/documentation/coreaudio/kaudiochannellayouttag_dts_8_0_b)Added [kAudioChannelLayoutTag_DTS_8_1_A](https://developer.apple.com/documentation/coreaudio/1572101-audio_channel_layout_tags/kaudiochannellayouttag_dts_8_1_a)Added [kAudioChannelLayoutTag_DTS_8_1_B](https://developer.apple.com/documentation/coreaudio/kaudiochannellayouttag_dts_8_1_b)Added [kAudioChannelLayoutTag_EAC3_6_1_A](https://developer.apple.com/documentation/coreaudio/kaudiochannellayouttag_eac3_6_1_a)Added [kAudioChannelLayoutTag_EAC3_6_1_B](https://developer.apple.com/documentation/coreaudio/1572101-audio_channel_layout_tags/kaudiochannellayouttag_eac3_6_1_b)Added [kAudioChannelLayoutTag_EAC3_6_1_C](https://developer.apple.com/documentation/coreaudio/kaudiochannellayouttag_eac3_6_1_c)Added [kAudioChannelLayoutTag_EAC3_7_1_A](https://developer.apple.com/documentation/coreaudio/1572101-audio_channel_layout_tags/kaudiochannellayouttag_eac3_7_1_a)Added [kAudioChannelLayoutTag_EAC3_7_1_B](https://developer.apple.com/documentation/coreaudio/1572101-audio_channel_layout_tags/kaudiochannellayouttag_eac3_7_1_b)Added [kAudioChannelLayoutTag_EAC3_7_1_C](https://developer.apple.com/documentation/coreaudio/1572101-audio_channel_layout_tags/kaudiochannellayouttag_eac3_7_1_c)Added [kAudioChannelLayoutTag_EAC3_7_1_D](https://developer.apple.com/documentation/coreaudio/kaudiochannellayouttag_eac3_7_1_d)Added [kAudioChannelLayoutTag_EAC3_7_1_E](https://developer.apple.com/documentation/coreaudio/kaudiochannellayouttag_eac3_7_1_e)Added [kAudioChannelLayoutTag_EAC3_7_1_F](https://developer.apple.com/documentation/coreaudio/1572101-audio_channel_layout_tags/kaudiochannellayouttag_eac3_7_1_f)Added [kAudioChannelLayoutTag_EAC3_7_1_G](https://developer.apple.com/documentation/coreaudio/1572101-audio_channel_layout_tags/kaudiochannellayouttag_eac3_7_1_g)Added [kAudioChannelLayoutTag_EAC3_7_1_H](https://developer.apple.com/documentation/coreaudio/1572101-audio_channel_layout_tags/kaudiochannellayouttag_eac3_7_1_h)Added [kAudioChannelLayoutTag_EAC_6_0_A](https://developer.apple.com/documentation/coreaudio/kaudiochannellayouttag_eac_6_0_a)Added [kAudioChannelLayoutTag_EAC_7_0_A](https://developer.apple.com/documentation/coreaudio/1572101-audio_channel_layout_tags/kaudiochannellayouttag_eac_7_0_a)Added [kAudioFormatMPEG4AAC_ELD](https://developer.apple.com/documentation/coreaudio/kaudioformatmpeg4aac_eld)Added [kAudioFormatMPEG4AAC_ELD_SBR](https://developer.apple.com/documentation/coreaudio/kaudioformatmpeg4aac_eld_sbr)Added [kAudio_FileNotFoundError](https://developer.apple.com/documentation/coreaudio/1572099-anonymous/kaudio_filenotfounderror)Added [kAudio_MemFullError](https://developer.apple.com/documentation/coreaudio/1572099-anonymous/kaudio_memfullerror)Added [kAudio_ParamError](https://developer.apple.com/documentation/coreaudio/1572099-anonymous/kaudio_paramerror)Added [kAudio_UnimplementedError](https://developer.apple.com/documentation/coreaudio/kaudio_unimplementederror)

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
