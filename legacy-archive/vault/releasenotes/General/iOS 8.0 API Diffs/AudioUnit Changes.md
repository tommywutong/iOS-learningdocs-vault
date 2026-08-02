---
title: iOS 8.0 API Diffs
apple_id: TP40014455
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2014-09-17'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS80APIDiffs/frameworks/AudioUnit.html
archived_at: '2026-07-18T02:55:55.598977Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 8.0 API Diffs](iOS%207.1%20to%20iOS%208.0%20API%20Differences.md)


# AudioUnit Changes

## AudioUnit

AUComponent.hAdded [kAudioUnitSubType_MIDISynth](https://developer.apple.com/documentation/audiotoolbox/1584149-music_instrument_audio_unit_subt/kaudiounitsubtype_midisynth)Added [kAudioUnitSubType_RoundTripAAC](https://developer.apple.com/documentation/audiotoolbox/1584145-converter_audio_unit_subtypes/kaudiounitsubtype_roundtripaac)Added [kAudioUnitSubType_SampleDelay](https://developer.apple.com/documentation/audiotoolbox/1584154-effect_audio_unit_subtypes/kaudiounitsubtype_sampledelay)Added [kAudioUnitSubType_SpatialMixer](https://developer.apple.com/documentation/audiotoolbox/1584150-mixer_audio_unit_subtypes/kaudiounitsubtype_spatialmixer)AudioUnitParameters.hAdded [kReverbParam_FilterEnable](https://developer.apple.com/documentation/audiotoolbox/kreverbparam_filterenable)Added [kReverbParam_FilterType](https://developer.apple.com/documentation/audiotoolbox/1390119-additional_reverb_parameters/kreverbparam_filtertype)Added [kRoundTripAACParam_EncodingStrategy](https://developer.apple.com/documentation/audiotoolbox/1389808-anonymous/kroundtripaacparam_encodingstrategy)Added [kRoundTripAACParam_Format](https://developer.apple.com/documentation/audiotoolbox/kroundtripaacparam_format)Added [kRoundTripAACParam_RateOrQuality](https://developer.apple.com/documentation/audiotoolbox/1389808-anonymous/kroundtripaacparam_rateorquality)Added [kSpatialMixerParam_Azimuth](https://developer.apple.com/documentation/audiotoolbox/kspatialmixerparam_azimuth)Added [kSpatialMixerParam_Distance](https://developer.apple.com/documentation/audiotoolbox/kspatialmixerparam_distance)Added [kSpatialMixerParam_Elevation](https://developer.apple.com/documentation/audiotoolbox/1390073-anonymous/kspatialmixerparam_elevation)Added [kSpatialMixerParam_Enable](https://developer.apple.com/documentation/audiotoolbox/kspatialmixerparam_enable)Added [kSpatialMixerParam_Gain](https://developer.apple.com/documentation/audiotoolbox/1390073-anonymous/kspatialmixerparam_gain)Added [kSpatialMixerParam_GlobalReverbGain](https://developer.apple.com/documentation/audiotoolbox/kspatialmixerparam_globalreverbgain)Added [kSpatialMixerParam_MaxGain](https://developer.apple.com/documentation/audiotoolbox/kspatialmixerparam_maxgain)Added [kSpatialMixerParam_MinGain](https://developer.apple.com/documentation/audiotoolbox/kspatialmixerparam_mingain)Added [kSpatialMixerParam_ObstructionAttenuation](https://developer.apple.com/documentation/audiotoolbox/1390073-anonymous/kspatialmixerparam_obstructionattenuation)Added [kSpatialMixerParam_OcclusionAttenuation](https://developer.apple.com/documentation/audiotoolbox/1390073-anonymous/kspatialmixerparam_occlusionattenuation)Added [kSpatialMixerParam_PlaybackRate](https://developer.apple.com/documentation/audiotoolbox/1390073-anonymous/kspatialmixerparam_playbackrate)Added [kSpatialMixerParam_ReverbBlend](https://developer.apple.com/documentation/audiotoolbox/kspatialmixerparam_reverbblend)AudioUnitProperties.hAdded [AudioUnitParameterIDName](https://developer.apple.com/documentation/audiotoolbox/audiounitparameteridname)Added [AudioUnitParameterStringFromValue](https://developer.apple.com/documentation/audiotoolbox/audiounitparameterstringfromvalue)Added [AudioUnitParameterValueFromString](https://developer.apple.com/documentation/audiotoolbox/audiounitparametervaluefromstring)Added [kAUMIDISynthProperty_EnablePreload](https://developer.apple.com/documentation/audiotoolbox/kaumidisynthproperty_enablepreload)Added [#def kAudioUnitConfigurationInfo_IconURL](https://developer.apple.com/documentation/audiotoolbox/kaudiounitconfigurationinfo_iconurl)Added [kAudioUnitParameterFlag_OmitFromPresets](https://developer.apple.com/documentation/audiotoolbox/audiounitparameteroptions/1439594-flag_omitfrompresets)Added [kAudioUnitParameterName_Full](https://developer.apple.com/documentation/audiotoolbox/1534055-anonymous/kaudiounitparametername_full)Added [kAudioUnitProperty_ParameterIDName](https://developer.apple.com/documentation/audiotoolbox/kaudiounitproperty_parameteridname)Added [kAudioUnitProperty_ParameterStringFromValue](https://developer.apple.com/documentation/audiotoolbox/kaudiounitproperty_parameterstringfromvalue)Added [kAudioUnitProperty_ParameterValueFromString](https://developer.apple.com/documentation/audiotoolbox/1534199-generic_audio_unit_properties/kaudiounitproperty_parametervaluefromstring)Added [kAudioUnitProperty_SpatialMixerAttenuationCurve](https://developer.apple.com/documentation/audiotoolbox/kaudiounitproperty_spatialmixerattenuationcurve)Added [kAudioUnitProperty_SpatialMixerDistanceParams](https://developer.apple.com/documentation/audiotoolbox/kaudiounitproperty_spatialmixerdistanceparams)Added [kAudioUnitProperty_SpatialMixerRenderingFlags](https://developer.apple.com/documentation/audiotoolbox/1534150-anonymous/kaudiounitproperty_spatialmixerrenderingflags)Added [kMusicDeviceProperty_BankName](https://developer.apple.com/documentation/audiotoolbox/kmusicdeviceproperty_bankname)Added [kMusicDeviceProperty_InstrumentCount](https://developer.apple.com/documentation/audiotoolbox/1533930-anonymous/kmusicdeviceproperty_instrumentcount)Added [kMusicDeviceProperty_InstrumentName](https://developer.apple.com/documentation/audiotoolbox/kmusicdeviceproperty_instrumentname)Added [kMusicDeviceProperty_InstrumentNumber](https://developer.apple.com/documentation/audiotoolbox/kmusicdeviceproperty_instrumentnumber)Added [kMusicDeviceProperty_SoundBankURL](https://developer.apple.com/documentation/audiotoolbox/kmusicdeviceproperty_soundbankurl)Added [kScheduledAudioSliceFlag_Interrupt](https://developer.apple.com/documentation/audiotoolbox/auscheduledaudiosliceflags/1440972-scheduledaudiosliceflag_interrup)Added [kScheduledAudioSliceFlag_InterruptAtLoop](https://developer.apple.com/documentation/audiotoolbox/auscheduledaudiosliceflags/kscheduledaudiosliceflag_interruptatloop)Added [kScheduledAudioSliceFlag_Loop](https://developer.apple.com/documentation/audiotoolbox/auscheduledaudiosliceflags/1439505-scheduledaudiosliceflag_loop)Added [kSpatialMixerAttenuationCurve_Exponential](https://developer.apple.com/documentation/audiotoolbox/auspatialmixerattenuationcurve/kspatialmixerattenuationcurve_exponential)Added [kSpatialMixerAttenuationCurve_Inverse](https://developer.apple.com/documentation/audiotoolbox/auspatialmixerattenuationcurve/spatialmixerattenuationcurve_inverse)Added [kSpatialMixerAttenuationCurve_Linear](https://developer.apple.com/documentation/audiotoolbox/auspatialmixerattenuationcurve/kspatialmixerattenuationcurve_linear)Added [kSpatialMixerAttenuationCurve_Power](https://developer.apple.com/documentation/audiotoolbox/auspatialmixerattenuationcurve/kspatialmixerattenuationcurve_power)Added [kSpatialMixerRenderingFlags_DistanceAttenuation](https://developer.apple.com/documentation/audiotoolbox/auspatialmixerrenderingflags/kspatialmixerrenderingflags_distanceattenuation)Added [kSpatialMixerRenderingFlags_InterAuralDelay](https://developer.apple.com/documentation/audiotoolbox/auspatialmixerrenderingflags/kspatialmixerrenderingflags_interauraldelay)

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
