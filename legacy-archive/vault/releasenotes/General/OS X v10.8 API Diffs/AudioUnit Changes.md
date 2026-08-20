---
title: OS X v10.8 API Diffs
apple_id: TP40011748
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_8/AudioUnit.html
archived_at: '2026-07-18T02:53:56.754759Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.8 API Diffs](OS%20X%20v10.7%20to%20OS%20X%20v10.8%20API%20Differences.md)


# AudioUnit Changes

## AudioUnit

AUComponent.hRemoved kAudioUnitSubType_BoostClipRemoved kAudioUnitSubType_VolumeAdded [kAudioUnitSubType_AUiPodTimeOther](https://developer.apple.com/documentation/audiotoolbox/kaudiounitsubtype_auipodtimeother) (no architecture available)Added [kAudioUnitSubType_NBandEQ](https://developer.apple.com/documentation/audiotoolbox/1584154-effect_audio_unit_subtypes/kaudiounitsubtype_nbandeq) (no architecture available)Added [kAudioUnitSubType_Reverb2](https://developer.apple.com/documentation/audiotoolbox/kaudiounitsubtype_reverb2) (no architecture available)AudioCodec.hAdded [kAudioCodecDelayMode_Compatibility](https://developer.apple.com/documentation/audiotoolbox/1494050-anonymous/kaudiocodecdelaymode_compatibility)Added [kAudioCodecDelayMode_Minimum](https://developer.apple.com/documentation/audiotoolbox/kaudiocodecdelaymode_minimum)Added [kAudioCodecDelayMode_Optimal](https://developer.apple.com/documentation/audiotoolbox/1494050-anonymous/kaudiocodecdelaymode_optimal)Added [kAudioCodecPropertyDelayMode](https://developer.apple.com/documentation/audiotoolbox/kaudiocodecpropertydelaymode)AudioComponent.hAdded [AudioComponentCopyConfigurationInfo()](https://developer.apple.com/documentation/audiotoolbox/1410525-audiocomponentcopyconfigurationi)Added [kAudioComponentFlag_SandboxSafe](https://developer.apple.com/documentation/audiotoolbox/audiocomponentflags/kaudiocomponentflag_sandboxsafe)AudioUnitParameters.hAdded [kAUSamplerParam_CoarseTuning](https://developer.apple.com/documentation/audiotoolbox/kausamplerparam_coarsetuning)Added [kAUSamplerParam_FineTuning](https://developer.apple.com/documentation/audiotoolbox/1389769-anonymous/kausamplerparam_finetuning)Added [kAUSamplerParam_Gain](https://developer.apple.com/documentation/audiotoolbox/1389769-anonymous/kausamplerparam_gain)Added [kAUSamplerParam_Pan](https://developer.apple.com/documentation/audiotoolbox/kausamplerparam_pan)Added [kRoundTripAACParam_EncodingStrategy](https://developer.apple.com/documentation/audiotoolbox/1389808-anonymous/kroundtripaacparam_encodingstrategy)Added [kRoundTripAACParam_RateOrQuality](https://developer.apple.com/documentation/audiotoolbox/1389808-anonymous/kroundtripaacparam_rateorquality)AudioUnitProperties.hRemoved [kAUSamplerProperty_BankAndPreset](https://developer.apple.com/documentation/audiotoolbox/1534019-anonymous/kausamplerproperty_bankandpreset)Removed kAUVoiceIOProperty_DisableVPRemoved kAUVoiceIOProperty_MaximumMetadataByteSizeRemoved kAUVoiceIOProperty_MaximumNumberPacketsRemoved kAUVoiceIOProperty_MaximumOutputPacketByteSizeRemoved kAUVoiceIOProperty_MaximumRenderFrameSizeRemoved kAUVoiceIOProperty_RequestMetadataAdded [AUSamplerInstrumentData](https://developer.apple.com/documentation/audiotoolbox/ausamplerinstrumentdata)Added [kAUSamplerProperty_LoadAudioFiles](https://developer.apple.com/documentation/audiotoolbox/kausamplerproperty_loadaudiofiles)Added [kAUSamplerProperty_LoadInstrument](https://developer.apple.com/documentation/audiotoolbox/1533959-anonymous/kausamplerproperty_loadinstrument)Added [kAUSamplerProperty_LoadPresetFromBank](https://developer.apple.com/documentation/audiotoolbox/kausamplerproperty_loadpresetfrombank)Added [kAUVoiceIOErr_UnexpectedNumberOfInputChannels](https://developer.apple.com/documentation/audiotoolbox/kauvoiceioerr_unexpectednumberofinputchannels)Added [#def kAudioUnitConfigurationInfo_ChannelConfigurations](https://developer.apple.com/documentation/audiotoolbox/kaudiounitconfigurationinfo_channelconfigurations)Added [#def kAudioUnitConfigurationInfo_HasCustomView](https://developer.apple.com/documentation/audiotoolbox/kaudiounitconfigurationinfo_hascustomview)Added [#def kAudioUnitConfigurationInfo_InitialInputs](https://developer.apple.com/documentation/audiotoolbox/kaudiounitconfigurationinfo_initialinputs)Added [#def kAudioUnitConfigurationInfo_InitialOutputs](https://developer.apple.com/documentation/audiotoolbox/kaudiounitconfigurationinfo_initialoutputs)Added [kInstrumentType_AUPreset](https://developer.apple.com/documentation/audiotoolbox/kinstrumenttype_aupreset)Added [kInstrumentType_Audiofile](https://developer.apple.com/documentation/audiotoolbox/1534202-anonymous/kinstrumenttype_audiofile)Added [kInstrumentType_DLSPreset](https://developer.apple.com/documentation/audiotoolbox/1534202-anonymous/kinstrumenttype_dlspreset)Added [kInstrumentType_EXS24](https://developer.apple.com/documentation/audiotoolbox/1534202-anonymous/kinstrumenttype_exs24)Added [kInstrumentType_SF2Preset](https://developer.apple.com/documentation/audiotoolbox/1534202-anonymous/kinstrumenttype_sf2preset)

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
