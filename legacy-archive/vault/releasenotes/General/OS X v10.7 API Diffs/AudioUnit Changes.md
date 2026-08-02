---
title: OS X v10.7 API Diffs
apple_id: TP40010630
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2011-06-06'
source_url: https://developer.apple.com/library/archive/releasenotes/General/MacOSXLionAPIDiffs/AudioUnit.html
archived_at: '2026-07-18T02:54:26.227862Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.7 API Diffs](OS%20X%20v10.6%20to%20v10.7%20API%20Diffs.md)


# AudioUnit Changes

## AudioUnit

|  | Framework Architectures |
| --- | --- |
| From | i386,ppc,x86_64 |
| To | i386,x86_64 |

AUComponent.hAdded [AudioUnitAddPropertyListenerProc](https://developer.apple.com/documentation/audiotoolbox/audiounitaddpropertylistenerproc)Added [AudioUnitAddRenderNotifyProc](https://developer.apple.com/documentation/audiotoolbox/audiounitaddrendernotifyproc)Added [AudioUnitComplexRenderProc](https://developer.apple.com/documentation/audiotoolbox/audiounitcomplexrenderproc)Added [AudioUnitGetPropertyInfoProc](https://developer.apple.com/documentation/audiotoolbox/audiounitgetpropertyinfoproc)Added [AudioUnitGetPropertyProc](https://developer.apple.com/documentation/audiotoolbox/audiounitgetpropertyproc)Added [AudioUnitInitializeProc](https://developer.apple.com/documentation/audiotoolbox/audiounitinitializeproc)Added [AudioUnitProcess()](https://developer.apple.com/documentation/audiotoolbox/1439630-audiounitprocess)Added [AudioUnitProcessMultiple()](https://developer.apple.com/documentation/audiotoolbox/1440334-audiounitprocessmultiple)Added [AudioUnitProcessMultipleProc](https://developer.apple.com/documentation/audiotoolbox/audiounitprocessmultipleproc)Added [AudioUnitProcessProc](https://developer.apple.com/documentation/audiotoolbox/audiounitprocessproc)Added [AudioUnitRemovePropertyListenerProc](https://developer.apple.com/documentation/audiotoolbox/audiounitremovepropertylistenerproc)Added [AudioUnitRemovePropertyListenerWithUserDataProc](https://developer.apple.com/documentation/audiotoolbox/audiounitremovepropertylistenerwithuserdataproc)Added [AudioUnitRemoveRenderNotifyProc](https://developer.apple.com/documentation/audiotoolbox/audiounitremoverendernotifyproc)Added [AudioUnitResetProc](https://developer.apple.com/documentation/audiotoolbox/audiounitresetproc)Added [AudioUnitScheduleParametersProc](https://developer.apple.com/documentation/audiotoolbox/audiounitscheduleparametersproc)Added [AudioUnitSetPropertyProc](https://developer.apple.com/documentation/audiotoolbox/audiounitsetpropertyproc)Added [AudioUnitUninitializeProc](https://developer.apple.com/documentation/audiotoolbox/audiounituninitializeproc)Added [kAudioUnitComplexRenderSelect](https://developer.apple.com/documentation/audiotoolbox/1584140-general_audio_unit_function_sele/kaudiounitcomplexrenderselect)Added [kAudioUnitProcessMultipleSelect](https://developer.apple.com/documentation/audiotoolbox/kaudiounitprocessmultipleselect)Added [kAudioUnitProcessSelect](https://developer.apple.com/documentation/audiotoolbox/1584140-general_audio_unit_function_sele/kaudiounitprocessselect)Added [kAudioUnitRenderAction_DoNotCheckRenderArgs](https://developer.apple.com/documentation/audiotoolbox/audiounitrenderactionflags/kaudiounitrenderaction_donotcheckrenderargs)Added [kAudioUnitSubType_AUiPodEQ](https://developer.apple.com/documentation/audiotoolbox/kaudiounitsubtype_auipodeq) (no architecture available)Added kAudioUnitSubType_BoostClipAdded [kAudioUnitSubType_NewTimePitch](https://developer.apple.com/documentation/audiotoolbox/kaudiounitsubtype_newtimepitch)Added [kAudioUnitSubType_RemoteIO](https://developer.apple.com/documentation/audiotoolbox/1619485-anonymous/kaudiounitsubtype_remoteio) (no architecture available)Added [kAudioUnitSubType_RoundTripAAC](https://developer.apple.com/documentation/audiotoolbox/1584145-converter_audio_unit_subtypes/kaudiounitsubtype_roundtripaac)Added [kAudioUnitSubType_Sampler](https://developer.apple.com/documentation/audiotoolbox/1619498-anonymous/kaudiounitsubtype_sampler)Added [kAudioUnitSubType_VoiceProcessingIO](https://developer.apple.com/documentation/audiotoolbox/1584139-input_output_audio_unit_subtypes/kaudiounitsubtype_voiceprocessingio)Added kAudioUnitSubType_VolumeAudioCodec.hAdded [AudioCodecAppendInputBufferList()](https://developer.apple.com/documentation/audiotoolbox/1439811-audiocodecappendinputbufferlist)Added [AudioCodecAppendInputBufferListProc](https://developer.apple.com/documentation/audiotoolbox/audiocodecappendinputbufferlistproc)Added [AudioCodecAppendInputDataProc](https://developer.apple.com/documentation/audiotoolbox/audiocodecappendinputdataproc)Added [AudioCodecGetPropertyInfoProc](https://developer.apple.com/documentation/audiotoolbox/audiocodecgetpropertyinfoproc)Added [AudioCodecGetPropertyProc](https://developer.apple.com/documentation/audiotoolbox/audiocodecgetpropertyproc)Added [AudioCodecInitializeProc](https://developer.apple.com/documentation/audiotoolbox/audiocodecinitializeproc)Added [AudioCodecProduceOutputBufferList()](https://developer.apple.com/documentation/audiotoolbox/1439926-audiocodecproduceoutputbufferlis)Added [AudioCodecProduceOutputBufferListProc](https://developer.apple.com/documentation/audiotoolbox/audiocodecproduceoutputbufferlistproc)Added [AudioCodecProduceOutputPacketsProc](https://developer.apple.com/documentation/audiotoolbox/audiocodecproduceoutputpacketsproc)Added [AudioCodecResetProc](https://developer.apple.com/documentation/audiotoolbox/audiocodecresetproc)Added [AudioCodecSetPropertyProc](https://developer.apple.com/documentation/audiotoolbox/audiocodecsetpropertyproc)Added [AudioCodecUninitializeProc](https://developer.apple.com/documentation/audiotoolbox/audiocodecuninitializeproc)Added [kAudioCodecAppendInputBufferListSelect](https://developer.apple.com/documentation/audiotoolbox/1494074-audio_codec_routine_selectors/kaudiocodecappendinputbufferlistselect)Added [kAudioCodecProduceOutputBufferListSelect](https://developer.apple.com/documentation/audiotoolbox/kaudiocodecproduceoutputbufferlistselect)AudioComponent.hAdded [AudioComponentFactoryFunction](https://developer.apple.com/documentation/audiotoolbox/audiocomponentfactoryfunction)Added [AudioComponentMethod](https://developer.apple.com/documentation/audiotoolbox/audiocomponentmethod)Added [AudioComponentPlugInInterface](https://developer.apple.com/documentation/audiotoolbox/audiocomponentplugininterface)Added [AudioComponentRegister()](https://developer.apple.com/documentation/audiotoolbox/1410487-audiocomponentregister)Added [kAudioComponentFlag_Unsearchable](https://developer.apple.com/documentation/audiotoolbox/audiocomponentflags/kaudiocomponentflag_unsearchable)AudioOutputUnit.hAdded [AudioOutputUnitStartProc](https://developer.apple.com/documentation/audiotoolbox/audiooutputunitstartproc)Added [AudioOutputUnitStopProc](https://developer.apple.com/documentation/audiotoolbox/audiooutputunitstopproc)AudioUnitParameters.hAdded [k3DMixerParam_MaxGain](https://developer.apple.com/documentation/audiotoolbox/k3dmixerparam_maxgain)Added [k3DMixerParam_MinGain](https://developer.apple.com/documentation/audiotoolbox/1389763-3d_mixer_unit_parameters/k3dmixerparam_mingain)Added [kAUGroupParameterID_Sostenuto](https://developer.apple.com/documentation/audiotoolbox/1389613-midi_audio_unit_parameters/kaugroupparameterid_sostenuto)Added [kMultiChannelMixerParam_Pan](https://developer.apple.com/documentation/audiotoolbox/kmultichannelmixerparam_pan)Added [kNewTimePitchParam_EnablePeakLocking](https://developer.apple.com/documentation/audiotoolbox/knewtimepitchparam_enablepeaklocking)Added [kNewTimePitchParam_Overlap](https://developer.apple.com/documentation/audiotoolbox/knewtimepitchparam_overlap)Added [kNewTimePitchParam_Pitch](https://developer.apple.com/documentation/audiotoolbox/1389643-anonymous/knewtimepitchparam_pitch)Added [kNewTimePitchParam_Rate](https://developer.apple.com/documentation/audiotoolbox/1389643-anonymous/knewtimepitchparam_rate)Added [kRoundTripAACParam_BitRate](https://developer.apple.com/documentation/audiotoolbox/1389808-anonymous/kroundtripaacparam_bitrate)Added [kRoundTripAACParam_CompressedFormatSampleRate](https://developer.apple.com/documentation/audiotoolbox/kroundtripaacparam_compressedformatsamplerate)Added [kRoundTripAACParam_Format](https://developer.apple.com/documentation/audiotoolbox/kroundtripaacparam_format)Added [kRoundTripAACParam_Quality](https://developer.apple.com/documentation/audiotoolbox/kroundtripaacparam_quality)AudioUnitProperties.hAdded [AUSamplerBankPresetData](https://developer.apple.com/documentation/audiotoolbox/ausamplerbankpresetdata)Added [AudioUnitParameterHistoryInfo](https://developer.apple.com/documentation/audiotoolbox/audiounitparameterhistoryinfo)Added [kAUSamplerProperty_BankAndPreset](https://developer.apple.com/documentation/audiotoolbox/1534019-anonymous/kausamplerproperty_bankandpreset)Added [kAUSampler_DefaultBankLSB](https://developer.apple.com/documentation/audiotoolbox/kausampler_defaultbanklsb)Added [kAUSampler_DefaultMelodicBankMSB](https://developer.apple.com/documentation/audiotoolbox/1534086-anonymous/kausampler_defaultmelodicbankmsb)Added [kAUSampler_DefaultPercussionBankMSB](https://developer.apple.com/documentation/audiotoolbox/1534086-anonymous/kausampler_defaultpercussionbankmsb)Added [kAUVoiceIOProperty_BypassVoiceProcessing](https://developer.apple.com/documentation/audiotoolbox/kauvoiceioproperty_bypassvoiceprocessing)Added kAUVoiceIOProperty_DisableVPAdded kAUVoiceIOProperty_MaximumMetadataByteSizeAdded kAUVoiceIOProperty_MaximumNumberPacketsAdded kAUVoiceIOProperty_MaximumOutputPacketByteSizeAdded kAUVoiceIOProperty_MaximumRenderFrameSizeAdded [kAUVoiceIOProperty_MuteOutput](https://developer.apple.com/documentation/audiotoolbox/kauvoiceioproperty_muteoutput)Added kAUVoiceIOProperty_RequestMetadataAdded [kAUVoiceIOProperty_VoiceProcessingEnableAGC](https://developer.apple.com/documentation/audiotoolbox/kauvoiceioproperty_voiceprocessingenableagc)Added [kAUVoiceIOProperty_VoiceProcessingQuality](https://developer.apple.com/documentation/audiotoolbox/1534074-anonymous/kauvoiceioproperty_voiceprocessingquality)Added [kAudioUnitParameterFlag_PlotHistory](https://developer.apple.com/documentation/audiotoolbox/audiounitparameteroptions/1439089-flag_plothistory)Added [kAudioUnitProperty_ParameterHistoryInfo](https://developer.apple.com/documentation/audiotoolbox/kaudiounitproperty_parameterhistoryinfo)Added [kAudioUnitScope_Layer](https://developer.apple.com/documentation/audiotoolbox/kaudiounitscope_layer)Added [kAudioUnitScope_LayerItem](https://developer.apple.com/documentation/audiotoolbox/kaudiounitscope_layeritem)

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
