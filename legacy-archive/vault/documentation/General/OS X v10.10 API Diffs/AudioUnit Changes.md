---
title: OS X v10.10 API Diffs
apple_id: TP40014444
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2014-10-16'
source_url: https://developer.apple.com/library/archive/documentation/General/Reference/APIDiffsMacOSX10_10SeedDiff/frameworks/AudioUnit.html
archived_at: '2026-07-15T07:34:44.812928Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [OS X v10.10 API Diffs](OS%20X%20v10.9%20to%20OS%20X%20v10.10%20API%20Differences.md)


# AudioUnit Changes

## AudioUnit

AUComponent.hAdded [kAudioUnitSubType_MIDISynth](https://developer.apple.com/documentation/audiotoolbox/1584149-music_instrument_audio_unit_subt/kaudiounitsubtype_midisynth)Added [kAudioUnitSubType_SpatialMixer](https://developer.apple.com/documentation/audiotoolbox/1584150-mixer_audio_unit_subtypes/kaudiounitsubtype_spatialmixer)AudioUnitParameters.hAdded [kReverbParam_FilterEnable](https://developer.apple.com/documentation/audiotoolbox/kreverbparam_filterenable)Added [kReverbParam_FilterType](https://developer.apple.com/documentation/audiotoolbox/1390119-additional_reverb_parameters/kreverbparam_filtertype)Added [kSpatialMixerParam_Azimuth](https://developer.apple.com/documentation/audiotoolbox/kspatialmixerparam_azimuth)Added [kSpatialMixerParam_Distance](https://developer.apple.com/documentation/audiotoolbox/kspatialmixerparam_distance)Added [kSpatialMixerParam_Elevation](https://developer.apple.com/documentation/audiotoolbox/1390073-anonymous/kspatialmixerparam_elevation)Added [kSpatialMixerParam_Enable](https://developer.apple.com/documentation/audiotoolbox/kspatialmixerparam_enable)Added [kSpatialMixerParam_Gain](https://developer.apple.com/documentation/audiotoolbox/1390073-anonymous/kspatialmixerparam_gain)Added [kSpatialMixerParam_GlobalReverbGain](https://developer.apple.com/documentation/audiotoolbox/kspatialmixerparam_globalreverbgain)Added [kSpatialMixerParam_MaxGain](https://developer.apple.com/documentation/audiotoolbox/kspatialmixerparam_maxgain)Added [kSpatialMixerParam_MinGain](https://developer.apple.com/documentation/audiotoolbox/kspatialmixerparam_mingain)Added [kSpatialMixerParam_ObstructionAttenuation](https://developer.apple.com/documentation/audiotoolbox/1390073-anonymous/kspatialmixerparam_obstructionattenuation)Added [kSpatialMixerParam_OcclusionAttenuation](https://developer.apple.com/documentation/audiotoolbox/1390073-anonymous/kspatialmixerparam_occlusionattenuation)Added [kSpatialMixerParam_PlaybackRate](https://developer.apple.com/documentation/audiotoolbox/1390073-anonymous/kspatialmixerparam_playbackrate)Added [kSpatialMixerParam_ReverbBlend](https://developer.apple.com/documentation/audiotoolbox/kspatialmixerparam_reverbblend)AudioUnitProperties.hAdded [kAUMIDISynthProperty_EnablePreload](https://developer.apple.com/documentation/audiotoolbox/kaumidisynthproperty_enablepreload)Added [#def kAudioUnitConfigurationInfo_IconURL](https://developer.apple.com/documentation/audiotoolbox/kaudiounitconfigurationinfo_iconurl)Added [kAudioUnitParameterFlag_OmitFromPresets](https://developer.apple.com/documentation/audiotoolbox/audiounitparameteroptions/1439594-flag_omitfrompresets)Added [kAudioUnitProperty_SpatialMixerAttenuationCurve](https://developer.apple.com/documentation/audiotoolbox/kaudiounitproperty_spatialmixerattenuationcurve)Added [kAudioUnitProperty_SpatialMixerDistanceParams](https://developer.apple.com/documentation/audiotoolbox/kaudiounitproperty_spatialmixerdistanceparams)Added [kAudioUnitProperty_SpatialMixerRenderingFlags](https://developer.apple.com/documentation/audiotoolbox/1534150-anonymous/kaudiounitproperty_spatialmixerrenderingflags)Added [kScheduledAudioSliceFlag_Interrupt](https://developer.apple.com/documentation/audiotoolbox/auscheduledaudiosliceflags/1440972-scheduledaudiosliceflag_interrup)Added [kScheduledAudioSliceFlag_InterruptAtLoop](https://developer.apple.com/documentation/audiotoolbox/auscheduledaudiosliceflags/kscheduledaudiosliceflag_interruptatloop)Added [kScheduledAudioSliceFlag_Loop](https://developer.apple.com/documentation/audiotoolbox/auscheduledaudiosliceflags/1439505-scheduledaudiosliceflag_loop)Added [kSpatialMixerAttenuationCurve_Exponential](https://developer.apple.com/documentation/audiotoolbox/auspatialmixerattenuationcurve/kspatialmixerattenuationcurve_exponential)Added [kSpatialMixerAttenuationCurve_Inverse](https://developer.apple.com/documentation/audiotoolbox/auspatialmixerattenuationcurve/spatialmixerattenuationcurve_inverse)Added [kSpatialMixerAttenuationCurve_Linear](https://developer.apple.com/documentation/audiotoolbox/auspatialmixerattenuationcurve/kspatialmixerattenuationcurve_linear)Added [kSpatialMixerAttenuationCurve_Power](https://developer.apple.com/documentation/audiotoolbox/auspatialmixerattenuationcurve/kspatialmixerattenuationcurve_power)Added [kSpatialMixerRenderingFlags_DistanceAttenuation](https://developer.apple.com/documentation/audiotoolbox/auspatialmixerrenderingflags/kspatialmixerrenderingflags_distanceattenuation)Added [kSpatialMixerRenderingFlags_InterAuralDelay](https://developer.apple.com/documentation/audiotoolbox/auspatialmixerrenderingflags/kspatialmixerrenderingflags_interauraldelay)LogicAUProperties.h (Removed)Removed LogicAUNodePropertyDescriptionRemoved kLogicAUNodeOperationMode_EndianSwapRemoved kLogicAUNodeOperationMode_FullSupportRemoved kLogicAUNodeOperationMode_NodeEnabledRemoved kLogicAUNodeOperationMode_RemoteUIRemoved kLogicAUNodePropertyEndianMode_All32BitsRemoved kLogicAUNodePropertyEndianMode_All64BitsRemoved kLogicAUNodePropertyEndianMode_DontTouchRemoved kLogicAUNodePropertyEndianMode_SerializableCFTypeRemoved kLogicAUNodePropertyFlag_FullRoundTripRemoved kLogicAUNodePropertyFlag_NeedsInitializationRemoved kLogicAUNodePropertyFlag_SynchronousRemoved kLogicAUProperty_NodeOperationModeRemoved kLogicAUProperty_NodePropertyDescriptions

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
