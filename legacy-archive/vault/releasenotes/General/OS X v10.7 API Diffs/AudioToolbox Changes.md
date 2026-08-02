---
title: OS X v10.7 API Diffs
apple_id: TP40010630
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2011-06-06'
source_url: https://developer.apple.com/library/archive/releasenotes/General/MacOSXLionAPIDiffs/AudioToolbox.html
archived_at: '2026-07-18T02:54:26.161594Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.7 API Diffs](OS%20X%20v10.6%20to%20v10.7%20API%20Diffs.md)


# AudioToolbox Changes

## AudioToolbox

|  | Framework Architectures |
| --- | --- |
| From | i386,ppc,x86_64 |
| To | i386,x86_64 |

AudioConverter.hAdded [AudioConverterConvertComplexBuffer()](https://developer.apple.com/documentation/audiotoolbox/1502473-audioconverterconvertcomplexbuff)Added [kAudioConverterErr_HardwareInUse](https://developer.apple.com/documentation/audiotoolbox/1624334-anonymous/kaudioconvertererr_hardwareinuse) (no architecture available)Added [kAudioConverterPropertyCanResumeFromInterruption](https://developer.apple.com/documentation/audiotoolbox/1624333-anonymous/kaudioconverterpropertycanresumefrominterruption) (no architecture available)Added [kAudioConverterPropertyDitherBitDepth](https://developer.apple.com/documentation/audiotoolbox/kaudioconverterpropertyditherbitdepth)Added [kAudioConverterPropertyDithering](https://developer.apple.com/documentation/audiotoolbox/1559925-anonymous/kaudioconverterpropertydithering)Added [kDitherAlgorithm_NoiseShaping](https://developer.apple.com/documentation/audiotoolbox/1559931-anonymous/kditheralgorithm_noiseshaping)Added [kDitherAlgorithm_TPDF](https://developer.apple.com/documentation/audiotoolbox/kditheralgorithm_tpdf)Modified [AudioConverterNewSpecific()](https://developer.apple.com/documentation/audiotoolbox/1503356-audioconverternewspecific)

|  | Declaration |
| --- | --- |
| From | OSStatus AudioConverterNewSpecific ( const AudioStreamBasicDescription \*inSourceFormat, const AudioStreamBasicDescription \*inDestinationFormat, UInt32 inNumberClassDescriptions, AudioClassDescription \*inClassDescriptions, AudioConverterRef \*outAudioConverter); |
| To | OSStatus AudioConverterNewSpecific ( const AudioStreamBasicDescription \*inSourceFormat, const AudioStreamBasicDescription \*inDestinationFormat, UInt32 inNumberClassDescriptions, const AudioClassDescription \*inClassDescriptions, AudioConverterRef \*outAudioConverter); |

AudioFile.hAdded [#def kAFInfoDictionary_ISRC](https://developer.apple.com/documentation/audiotoolbox/kafinfodictionary_isrc)Added [#def kAFInfoDictionary_SourceBitDepth](https://developer.apple.com/documentation/audiotoolbox/kafinfodictionary_sourcebitdepth)Added [#def kAFInfoDictionary_SubTitle](https://developer.apple.com/documentation/audiotoolbox/kafinfodictionary_subtitle)Added [kAudioFileEndOfFileError](https://developer.apple.com/documentation/audiotoolbox/1576500-anonymous/kaudiofileendoffileerror)Added [kAudioFileNotOpenError](https://developer.apple.com/documentation/audiotoolbox/1576500-anonymous/kaudiofilenotopenerror)Added [kAudioFilePositionError](https://developer.apple.com/documentation/audiotoolbox/kaudiofilepositionerror)Added [kAudioFilePropertyAlbumArtwork](https://developer.apple.com/documentation/audiotoolbox/kaudiofilepropertyalbumartwork)Added [kAudioFilePropertySourceBitDepth](https://developer.apple.com/documentation/audiotoolbox/kaudiofilepropertysourcebitdepth)AudioFileComponent.hAdded [AudioFileComponentCloseProc](https://developer.apple.com/documentation/audiotoolbox/audiofilecomponentcloseproc)Added [AudioFileComponentCountUserDataProc](https://developer.apple.com/documentation/audiotoolbox/audiofilecomponentcountuserdataproc)Added [AudioFileComponentCreateURLProc](https://developer.apple.com/documentation/audiotoolbox/audiofilecomponentcreateurlproc)Added [AudioFileComponentExtensionIsThisFormatProc](https://developer.apple.com/documentation/audiotoolbox/audiofilecomponentextensionisthisformatproc)Added [AudioFileComponentFileDataIsThisFormatProc](https://developer.apple.com/documentation/audiotoolbox/audiofilecomponentfiledataisthisformatproc)Added [AudioFileComponentGetGlobalInfoProc](https://developer.apple.com/documentation/audiotoolbox/audiofilecomponentgetglobalinfoproc)Added [AudioFileComponentGetGlobalInfoSizeProc](https://developer.apple.com/documentation/audiotoolbox/audiofilecomponentgetglobalinfosizeproc)Added [AudioFileComponentGetPropertyInfoProc](https://developer.apple.com/documentation/audiotoolbox/audiofilecomponentgetpropertyinfoproc)Added [AudioFileComponentGetPropertyProc](https://developer.apple.com/documentation/audiotoolbox/audiofilecomponentgetpropertyproc)Added [AudioFileComponentGetUserDataProc](https://developer.apple.com/documentation/audiotoolbox/audiofilecomponentgetuserdataproc)Added [AudioFileComponentGetUserDataSizeProc](https://developer.apple.com/documentation/audiotoolbox/audiofilecomponentgetuserdatasizeproc)Added [AudioFileComponentInitializeWithCallbacksProc](https://developer.apple.com/documentation/audiotoolbox/audiofilecomponentinitializewithcallbacksproc)Added [AudioFileComponentOpenURLProc](https://developer.apple.com/documentation/audiotoolbox/audiofilecomponentopenurlproc)Added [AudioFileComponentOpenWithCallbacksProc](https://developer.apple.com/documentation/audiotoolbox/audiofilecomponentopenwithcallbacksproc)Added [AudioFileComponentOptimizeProc](https://developer.apple.com/documentation/audiotoolbox/audiofilecomponentoptimizeproc)Added [AudioFileComponentReadBytesProc](https://developer.apple.com/documentation/audiotoolbox/audiofilecomponentreadbytesproc)Added [AudioFileComponentReadPacketDataProc](https://developer.apple.com/documentation/audiotoolbox/audiofilecomponentreadpacketdataproc)Added [AudioFileComponentReadPacketsProc](https://developer.apple.com/documentation/audiotoolbox/audiofilecomponentreadpacketsproc)Added [AudioFileComponentRemoveUserDataProc](https://developer.apple.com/documentation/audiotoolbox/audiofilecomponentremoveuserdataproc)Added [AudioFileComponentSetPropertyProc](https://developer.apple.com/documentation/audiotoolbox/audiofilecomponentsetpropertyproc)Added [AudioFileComponentSetUserDataProc](https://developer.apple.com/documentation/audiotoolbox/audiofilecomponentsetuserdataproc)Added [AudioFileComponentWriteBytesProc](https://developer.apple.com/documentation/audiotoolbox/audiofilecomponentwritebytesproc)Added [AudioFileComponentWritePacketsProc](https://developer.apple.com/documentation/audiotoolbox/audiofilecomponentwritepacketsproc)Added [kAudioFileComponent_MIMETypesForType](https://developer.apple.com/documentation/audiotoolbox/kaudiofilecomponent_mimetypesfortype)Added [kAudioFileComponent_UTIsForType](https://developer.apple.com/documentation/audiotoolbox/kaudiofilecomponent_utisfortype)AudioFormat.hAdded [ExtendedAudioFormatInfo](https://developer.apple.com/documentation/audiotoolbox/extendedaudioformatinfo)Added [kAppleHardwareAudioCodecManufacturer](https://developer.apple.com/documentation/audiotoolbox/kapplehardwareaudiocodecmanufacturer) (no architecture available)Added [kAppleSoftwareAudioCodecManufacturer](https://developer.apple.com/documentation/audiotoolbox/1620448-audio_codec_manufacturer_and_imp/kapplesoftwareaudiocodecmanufacturer) (no architecture available)Added [kAudioDecoderComponentType](https://developer.apple.com/documentation/audiotoolbox/1494086-audio_codec_component_constants/kaudiodecodercomponenttype) (no architecture available)Added [kAudioEncoderComponentType](https://developer.apple.com/documentation/audiotoolbox/kaudioencodercomponenttype) (no architecture available)Added [kAudioFormatProperty_ChannelLayoutSimpleName](https://developer.apple.com/documentation/audiotoolbox/kaudioformatproperty_channellayoutsimplename)Added [kAudioFormatProperty_HardwareCodecCapabilities](https://developer.apple.com/documentation/audiotoolbox/kaudioformatproperty_hardwarecodeccapabilities) (no architecture available)Added [kAudioFormatProperty_ValidateChannelLayout](https://developer.apple.com/documentation/audiotoolbox/kaudioformatproperty_validatechannellayout)AudioQueue.hAdded [AudioQueueProcessingTapCallback](https://developer.apple.com/documentation/audiotoolbox/audioqueueprocessingtapcallback)Added [AudioQueueProcessingTapDispose()](https://developer.apple.com/documentation/audiotoolbox/1502310-audioqueueprocessingtapdispose)Added [AudioQueueProcessingTapGetSourceAudio()](https://developer.apple.com/documentation/audiotoolbox/1502107-audioqueueprocessingtapgetsource)Added [AudioQueueProcessingTapNew()](https://developer.apple.com/documentation/audiotoolbox/1503209-audioqueueprocessingtapnew)Added [AudioQueueProcessingTapRef](https://developer.apple.com/documentation/audiotoolbox/audioqueueprocessingtapref)Added [kAudioQueueErr_InvalidCodecAccess](https://developer.apple.com/documentation/audiotoolbox/1552627-anonymous/kaudioqueueerr_invalidcodecaccess)Added [kAudioQueueErr_InvalidOfflineMode](https://developer.apple.com/documentation/audiotoolbox/1552627-anonymous/kaudioqueueerr_invalidofflinemode)Added [kAudioQueueErr_InvalidTapContext](https://developer.apple.com/documentation/audiotoolbox/kaudioqueueerr_invalidtapcontext)Added [kAudioQueueErr_QueueInvalidated](https://developer.apple.com/documentation/audiotoolbox/1552627-anonymous/kaudioqueueerr_queueinvalidated)Added [kAudioQueueErr_TooManyTaps](https://developer.apple.com/documentation/audiotoolbox/1552627-anonymous/kaudioqueueerr_toomanytaps)Added [kAudioQueueHardwareCodecPolicy_Default](https://developer.apple.com/documentation/audiotoolbox/1618727-anonymous/kaudioqueuehardwarecodecpolicy_default) (no architecture available)Added [kAudioQueueHardwareCodecPolicy_PreferHardware](https://developer.apple.com/documentation/audiotoolbox/kaudioqueuehardwarecodecpolicy_preferhardware) (no architecture available)Added [kAudioQueueHardwareCodecPolicy_PreferSoftware](https://developer.apple.com/documentation/audiotoolbox/1618727-anonymous/kaudioqueuehardwarecodecpolicy_prefersoftware) (no architecture available)Added [kAudioQueueHardwareCodecPolicy_UseHardwareOnly](https://developer.apple.com/documentation/audiotoolbox/1618727-anonymous/kaudioqueuehardwarecodecpolicy_usehardwareonly) (no architecture available)Added [kAudioQueueHardwareCodecPolicy_UseSoftwareOnly](https://developer.apple.com/documentation/audiotoolbox/1618727-anonymous/kaudioqueuehardwarecodecpolicy_usesoftwareonly) (no architecture available)Added [kAudioQueueParam_Pan](https://developer.apple.com/documentation/audiotoolbox/kaudioqueueparam_pan)Added [kAudioQueueParam_VolumeRampTime](https://developer.apple.com/documentation/audiotoolbox/kaudioqueueparam_volumeramptime)Added [kAudioQueueProcessingTap_EndOfStream](https://developer.apple.com/documentation/audiotoolbox/audioqueueprocessingtapflags/kaudioqueueprocessingtap_endofstream)Added [kAudioQueueProcessingTap_PostEffects](https://developer.apple.com/documentation/audiotoolbox/audioqueueprocessingtapflags/kaudioqueueprocessingtap_posteffects)Added [kAudioQueueProcessingTap_PreEffects](https://developer.apple.com/documentation/audiotoolbox/audioqueueprocessingtapflags/1502092-preeffects)Added [kAudioQueueProcessingTap_Siphon](https://developer.apple.com/documentation/audiotoolbox/audioqueueprocessingtapflags/1502728-siphon)Added [kAudioQueueProcessingTap_StartOfStream](https://developer.apple.com/documentation/audiotoolbox/audioqueueprocessingtapflags/kaudioqueueprocessingtap_startofstream)Added [kAudioQueueProperty_HardwareCodecPolicy](https://developer.apple.com/documentation/audiotoolbox/1618724-hardware_codec_policy_keys/kaudioqueueproperty_hardwarecodecpolicy) (no architecture available)AudioServices.hAdded [kAudioServicesNoHardwareError](https://developer.apple.com/documentation/audiotoolbox/kaudioservicesnohardwareerror) (no architecture available)Added [kAudioSessionCategory_AudioProcessing](https://developer.apple.com/documentation/audiotoolbox/kaudiosessioncategory_audioprocessing) (no architecture available)Added [kAudioSessionIncompatibleCategory](https://developer.apple.com/documentation/audiotoolbox/kaudiosessionincompatiblecategory) (no architecture available)Added [kAudioSessionNoCategorySet](https://developer.apple.com/documentation/audiotoolbox/1618373-anonymous/kaudiosessionnocategoryset) (no architecture available)Added [kAudioSessionProperty_OtherMixableAudioShouldDuck](https://developer.apple.com/documentation/audiotoolbox/kaudiosessionproperty_othermixableaudioshouldduck) (no architecture available)Added [kAudioSessionProperty_OverrideCategoryDefaultToSpeaker](https://developer.apple.com/documentation/audiotoolbox/kaudiosessionproperty_overridecategorydefaulttospeaker) (no architecture available)Added [kAudioSessionProperty_OverrideCategoryEnableBluetoothInput](https://developer.apple.com/documentation/audiotoolbox/1618455-audio_session_property_identifie/kaudiosessionproperty_overridecategoryenablebluetoothinput) (no architecture available)Added [kAudioSessionProperty_OverrideCategoryMixWithOthers](https://developer.apple.com/documentation/audiotoolbox/kaudiosessionproperty_overridecategorymixwithothers) (no architecture available)Added [kAudioSessionProperty_ServerDied](https://developer.apple.com/documentation/audiotoolbox/1618455-audio_session_property_identifie/kaudiosessionproperty_serverdied) (no architecture available)Added [kAudioSessionRouteChangeReason_NoSuitableRouteForCategory](https://developer.apple.com/documentation/audiotoolbox/kaudiosessionroutechangereason_nosuitablerouteforcategory) (no architecture available)Added [kAudioSessionUnspecifiedError](https://developer.apple.com/documentation/audiotoolbox/kaudiosessionunspecifiederror) (no architecture available)CAFFile.hAdded [kCAFMarkerType_KeySignature](https://developer.apple.com/documentation/audiotoolbox/1547272-anonymous/kcafmarkertype_keysignature)Added [kCAFMarkerType_Tempo](https://developer.apple.com/documentation/audiotoolbox/1547272-anonymous/kcafmarkertype_tempo)Added [kCAFMarkerType_TimeSignature](https://developer.apple.com/documentation/audiotoolbox/1547272-anonymous/kcafmarkertype_timesignature)Added [kCAF_iXMLChunkID](https://developer.apple.com/documentation/audiotoolbox/1547266-anonymous/kcaf_ixmlchunkid)ExtendedAudioFile.hAdded [kExtAudioFileError_CodecUnavailableInputConsumed](https://developer.apple.com/documentation/audiotoolbox/kextaudiofileerror_codecunavailableinputconsumed) (no architecture available)Added [kExtAudioFileError_CodecUnavailableInputNotConsumed](https://developer.apple.com/documentation/audiotoolbox/1623673-anonymous/kextaudiofileerror_codecunavailableinputnotconsumed) (no architecture available)Added [kExtAudioFileProperty_CodecManufacturer](https://developer.apple.com/documentation/audiotoolbox/kextaudiofileproperty_codecmanufacturer)Added [kExtAudioFileProperty_PacketTable](https://developer.apple.com/documentation/audiotoolbox/1486859-property_identifiers_for_extende/kextaudiofileproperty_packettable)MusicPlayer.hRemoved MusicSequenceLoadSMF()Removed MusicSequenceSaveSMF()Removed kMusicEventType_LastModified [MusicTrackNewExtendedControlEvent()](https://developer.apple.com/documentation/audiotoolbox/1515457-musictracknewextendedcontroleven)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

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
