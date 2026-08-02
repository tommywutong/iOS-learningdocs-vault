---
title: OS X v10.9 API Diffs
apple_id: TP40013007
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2013-10-22'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_9/AudioUnit.html
archived_at: '2026-07-18T02:54:10.866374Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.9 API Diffs](OS%20X%20v10.8%20to%20OS%20X%20v10.9%20API%20Differences.md)


# AudioUnit Changes

## AudioUnit

AUComponent.hAdded [kAudioUnitSubType_AUiPodTimeOther](https://developer.apple.com/documentation/audiotoolbox/kaudiounitsubtype_auipodtimeother)Added [kAudioUnitSubType_NBandEQ](https://developer.apple.com/documentation/audiotoolbox/1584154-effect_audio_unit_subtypes/kaudiounitsubtype_nbandeq)Added [kAudioUnitType_MIDIProcessor](https://developer.apple.com/documentation/audiotoolbox/1584142-audio_unit_types/kaudiounittype_midiprocessor)AudioCodec.hAdded [kAudioCodecPropertyAdjustLocalQuality](https://developer.apple.com/documentation/audiotoolbox/1494111-instance_codec_properties/kaudiocodecpropertyadjustlocalquality)Added [kAudioCodecPropertyDynamicRangeControlMode](https://developer.apple.com/documentation/audiotoolbox/kaudiocodecpropertydynamicrangecontrolmode)Added [kAudioCodecPropertyPacketSizeLimitForVBR](https://developer.apple.com/documentation/audiotoolbox/1494111-instance_codec_properties/kaudiocodecpropertypacketsizelimitforvbr)Added [kAudioCodecPropertyProgramTargetLevel](https://developer.apple.com/documentation/audiotoolbox/kaudiocodecpropertyprogramtargetlevel)Added [kAudioCodecPropertyProgramTargetLevelConstant](https://developer.apple.com/documentation/audiotoolbox/kaudiocodecpropertyprogramtargetlevelconstant)Added [kAudioCodecPropertyRecommendedBitRateRange](https://developer.apple.com/documentation/audiotoolbox/1494111-instance_codec_properties/kaudiocodecpropertyrecommendedbitraterange)Added [kDynamicRangeControlMode_Heavy](https://developer.apple.com/documentation/audiotoolbox/kdynamicrangecontrolmode_heavy)Added [kDynamicRangeControlMode_Light](https://developer.apple.com/documentation/audiotoolbox/kdynamicrangecontrolmode_light)Added [kDynamicRangeControlMode_None](https://developer.apple.com/documentation/audiotoolbox/kdynamicrangecontrolmode_none)Added [kProgramTargetLevel_Minus20dB](https://developer.apple.com/documentation/audiotoolbox/1494116-anonymous/kprogramtargetlevel_minus20db)Added [kProgramTargetLevel_Minus23dB](https://developer.apple.com/documentation/audiotoolbox/kprogramtargetlevel_minus23db)Added [kProgramTargetLevel_Minus31dB](https://developer.apple.com/documentation/audiotoolbox/kprogramtargetlevel_minus31db)Added [kProgramTargetLevel_None](https://developer.apple.com/documentation/audiotoolbox/kprogramtargetlevel_none)AudioUnitParameters.hAdded [kAUNBandEQFilterType_2ndOrderButterworthHighPass](https://developer.apple.com/documentation/audiotoolbox/kaunbandeqfiltertype_2ndorderbutterworthhighpass)Added [kAUNBandEQFilterType_2ndOrderButterworthLowPass](https://developer.apple.com/documentation/audiotoolbox/kaunbandeqfiltertype_2ndorderbutterworthlowpass)Added [kAUNBandEQFilterType_BandPass](https://developer.apple.com/documentation/audiotoolbox/1389965-mutitype_eq_unit_filter_types/kaunbandeqfiltertype_bandpass)Added [kAUNBandEQFilterType_BandStop](https://developer.apple.com/documentation/audiotoolbox/kaunbandeqfiltertype_bandstop)Added [kAUNBandEQFilterType_HighShelf](https://developer.apple.com/documentation/audiotoolbox/kaunbandeqfiltertype_highshelf)Added [kAUNBandEQFilterType_LowShelf](https://developer.apple.com/documentation/audiotoolbox/kaunbandeqfiltertype_lowshelf)Added [kAUNBandEQFilterType_Parametric](https://developer.apple.com/documentation/audiotoolbox/1389965-mutitype_eq_unit_filter_types/kaunbandeqfiltertype_parametric)Added [kAUNBandEQFilterType_ResonantHighPass](https://developer.apple.com/documentation/audiotoolbox/1389965-mutitype_eq_unit_filter_types/kaunbandeqfiltertype_resonanthighpass)Added [kAUNBandEQFilterType_ResonantHighShelf](https://developer.apple.com/documentation/audiotoolbox/kaunbandeqfiltertype_resonanthighshelf)Added [kAUNBandEQFilterType_ResonantLowPass](https://developer.apple.com/documentation/audiotoolbox/1389965-mutitype_eq_unit_filter_types/kaunbandeqfiltertype_resonantlowpass)Added [kAUNBandEQFilterType_ResonantLowShelf](https://developer.apple.com/documentation/audiotoolbox/1389965-mutitype_eq_unit_filter_types/kaunbandeqfiltertype_resonantlowshelf)Added [kAUNBandEQParam_Bandwidth](https://developer.apple.com/documentation/audiotoolbox/1389745-anonymous/kaunbandeqparam_bandwidth)Added [kAUNBandEQParam_BypassBand](https://developer.apple.com/documentation/audiotoolbox/kaunbandeqparam_bypassband)Added [kAUNBandEQParam_FilterType](https://developer.apple.com/documentation/audiotoolbox/kaunbandeqparam_filtertype)Added [kAUNBandEQParam_Frequency](https://developer.apple.com/documentation/audiotoolbox/kaunbandeqparam_frequency)Added [kAUNBandEQParam_Gain](https://developer.apple.com/documentation/audiotoolbox/kaunbandeqparam_gain)Added [kAUNBandEQParam_GlobalGain](https://developer.apple.com/documentation/audiotoolbox/kaunbandeqparam_globalgain)Added [kNumAUNBandEQFilterTypes](https://developer.apple.com/documentation/audiotoolbox/knumaunbandeqfiltertypes)Added [kRandomParam_BoundA](https://developer.apple.com/documentation/audiotoolbox/1389639-anonymous/krandomparam_bounda)Added [kRandomParam_BoundB](https://developer.apple.com/documentation/audiotoolbox/krandomparam_boundb)Added [kRandomParam_Curve](https://developer.apple.com/documentation/audiotoolbox/1389639-anonymous/krandomparam_curve)AudioUnitProperties.hAdded [HostCallback_GetTransportState2](https://developer.apple.com/documentation/audiotoolbox/hostcallback_gettransportstate2)Added [kAUNBandEQProperty_BiquadCoefficients](https://developer.apple.com/documentation/audiotoolbox/kaunbandeqproperty_biquadcoefficients)Added [kAUNBandEQProperty_MaxNumberOfBands](https://developer.apple.com/documentation/audiotoolbox/1534022-anonymous/kaunbandeqproperty_maxnumberofbands)Added [kAUNBandEQProperty_NumberOfBands](https://developer.apple.com/documentation/audiotoolbox/1534022-anonymous/kaunbandeqproperty_numberofbands)Added [kAUSamplerProperty_BankAndPreset](https://developer.apple.com/documentation/audiotoolbox/1534019-anonymous/kausamplerproperty_bankandpreset)Added [kAudioUnitProperty_NickName](https://developer.apple.com/documentation/audiotoolbox/1534199-generic_audio_unit_properties/kaudiounitproperty_nickname)

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
