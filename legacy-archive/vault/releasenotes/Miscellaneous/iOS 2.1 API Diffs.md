---
title: iOS 2.1 API Diffs
apple_id: TP40007961
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2015-03-09'
source_url: https://developer.apple.com/library/archive/releasenotes/Miscellaneous/iPhone21APIDiffs/iPhoneOS21GMDiffs.html
archived_at: '2026-07-18T02:58:58.828146Z'
---
> 导航：[总目录](../../README.md) · [releasenotes](../../_indexes/releasenotes.md)


# iOS 2.0 to 2.1 API Changes

## AddressBook

No changes

## AddressBookUI

No changes

## AudioToolbox

AudioConverter.hAdded [AudioConverterComplexInputDataProc](https://developer.apple.com/documentation/audiotoolbox/audioconvertercomplexinputdataproc)Added [AudioConverterConvertBuffer()](https://developer.apple.com/documentation/audiotoolbox/1503345-audioconverterconvertbuffer)Added [AudioConverterDispose()](https://developer.apple.com/documentation/audiotoolbox/1502671-audioconverterdispose)Added [AudioConverterFillComplexBuffer()](https://developer.apple.com/documentation/audiotoolbox/1503098-audioconverterfillcomplexbuffer)Added [AudioConverterGetProperty()](https://developer.apple.com/documentation/audiotoolbox/1502731-audioconvertergetproperty)Added [AudioConverterGetPropertyInfo()](https://developer.apple.com/documentation/audiotoolbox/1502563-audioconvertergetpropertyinfo)Added [AudioConverterInputDataProc](https://developer.apple.com/documentation/audiotoolbox/audioconverterinputdataproc)Added [AudioConverterNew()](https://developer.apple.com/documentation/audiotoolbox/1502936-audioconverternew)Added [AudioConverterNewSpecific()](https://developer.apple.com/documentation/audiotoolbox/1503356-audioconverternewspecific)Added [AudioConverterPrimeInfo](https://developer.apple.com/documentation/audiotoolbox/audioconverterprimeinfo)Added [AudioConverterPropertyID](https://developer.apple.com/documentation/audiotoolbox/audioconverterpropertyid)Added [AudioConverterRef](https://developer.apple.com/documentation/audiotoolbox/audioconverterref)Added [AudioConverterReset()](https://developer.apple.com/documentation/audiotoolbox/1503102-audioconverterreset)Added [AudioConverterSetProperty()](https://developer.apple.com/documentation/audiotoolbox/1501675-audioconvertersetproperty)Added [kAudioConverterApplicableEncodeBitRates](https://developer.apple.com/documentation/audiotoolbox/1559928-audio_converter_properties/kaudioconverterapplicableencodebitrates)Added [kAudioConverterApplicableEncodeSampleRates](https://developer.apple.com/documentation/audiotoolbox/1559928-audio_converter_properties/kaudioconverterapplicableencodesamplerates)Added [kAudioConverterAvailableEncodeBitRates](https://developer.apple.com/documentation/audiotoolbox/kaudioconverteravailableencodebitrates)Added [kAudioConverterAvailableEncodeChannelLayoutTags](https://developer.apple.com/documentation/audiotoolbox/kaudioconverteravailableencodechannellayouttags)Added [kAudioConverterAvailableEncodeSampleRates](https://developer.apple.com/documentation/audiotoolbox/1559928-audio_converter_properties/kaudioconverteravailableencodesamplerates)Added [kAudioConverterChannelMap](https://developer.apple.com/documentation/audiotoolbox/1559928-audio_converter_properties/kaudioconverterchannelmap)Added [kAudioConverterCodecQuality](https://developer.apple.com/documentation/audiotoolbox/kaudioconvertercodecquality)Added [kAudioConverterCompressionMagicCookie](https://developer.apple.com/documentation/audiotoolbox/kaudioconvertercompressionmagiccookie)Added [kAudioConverterCurrentInputStreamDescription](https://developer.apple.com/documentation/audiotoolbox/kaudioconvertercurrentinputstreamdescription)Added [kAudioConverterCurrentOutputStreamDescription](https://developer.apple.com/documentation/audiotoolbox/1559928-audio_converter_properties/kaudioconvertercurrentoutputstreamdescription)Added [kAudioConverterDecompressionMagicCookie](https://developer.apple.com/documentation/audiotoolbox/kaudioconverterdecompressionmagiccookie)Added [kAudioConverterEncodeAdjustableSampleRate](https://developer.apple.com/documentation/audiotoolbox/kaudioconverterencodeadjustablesamplerate)Added [kAudioConverterEncodeBitRate](https://developer.apple.com/documentation/audiotoolbox/1559928-audio_converter_properties/kaudioconverterencodebitrate)Added [kAudioConverterErr_BadPropertySizeError](https://developer.apple.com/documentation/audiotoolbox/kaudioconvertererr_badpropertysizeerror)Added [kAudioConverterErr_FormatNotSupported](https://developer.apple.com/documentation/audiotoolbox/1559930-anonymous/kaudioconvertererr_formatnotsupported)Added [kAudioConverterErr_InputSampleRateOutOfRange](https://developer.apple.com/documentation/audiotoolbox/1559930-anonymous/kaudioconvertererr_inputsamplerateoutofrange)Added [kAudioConverterErr_InvalidInputSize](https://developer.apple.com/documentation/audiotoolbox/1559930-anonymous/kaudioconvertererr_invalidinputsize)Added [kAudioConverterErr_InvalidOutputSize](https://developer.apple.com/documentation/audiotoolbox/1559930-anonymous/kaudioconvertererr_invalidoutputsize)Added [kAudioConverterErr_OperationNotSupported](https://developer.apple.com/documentation/audiotoolbox/1559930-anonymous/kaudioconvertererr_operationnotsupported)Added [kAudioConverterErr_OutputSampleRateOutOfRange](https://developer.apple.com/documentation/audiotoolbox/kaudioconvertererr_outputsamplerateoutofrange)Added [kAudioConverterErr_PropertyNotSupported](https://developer.apple.com/documentation/audiotoolbox/kaudioconvertererr_propertynotsupported)Added [kAudioConverterErr_RequiresPacketDescriptionsError](https://developer.apple.com/documentation/audiotoolbox/kaudioconvertererr_requirespacketdescriptionserror)Added [kAudioConverterErr_UnspecifiedError](https://developer.apple.com/documentation/audiotoolbox/kaudioconvertererr_unspecifiederror)Added [kAudioConverterInputChannelLayout](https://developer.apple.com/documentation/audiotoolbox/1559928-audio_converter_properties/kaudioconverterinputchannellayout)Added [kAudioConverterOutputChannelLayout](https://developer.apple.com/documentation/audiotoolbox/kaudioconverteroutputchannellayout)Added [kAudioConverterPrimeInfo](https://developer.apple.com/documentation/audiotoolbox/kaudioconverterprimeinfo)Added [kAudioConverterPrimeMethod](https://developer.apple.com/documentation/audiotoolbox/kaudioconverterprimemethod)Added [kAudioConverterPropertyBitDepthHint](https://developer.apple.com/documentation/audiotoolbox/1559928-audio_converter_properties/kaudioconverterpropertybitdepthhint)Added [kAudioConverterPropertyCalculateInputBufferSize](https://developer.apple.com/documentation/audiotoolbox/1559928-audio_converter_properties/kaudioconverterpropertycalculateinputbuffersize)Added [kAudioConverterPropertyCalculateOutputBufferSize](https://developer.apple.com/documentation/audiotoolbox/1559928-audio_converter_properties/kaudioconverterpropertycalculateoutputbuffersize)Added [kAudioConverterPropertyFormatList](https://developer.apple.com/documentation/audiotoolbox/kaudioconverterpropertyformatlist)Added [kAudioConverterPropertyInputCodecParameters](https://developer.apple.com/documentation/audiotoolbox/kaudioconverterpropertyinputcodecparameters)Added [kAudioConverterPropertyMaximumInputBufferSize](https://developer.apple.com/documentation/audiotoolbox/1559928-audio_converter_properties/kaudioconverterpropertymaximuminputbuffersize)Added [kAudioConverterPropertyMaximumInputPacketSize](https://developer.apple.com/documentation/audiotoolbox/kaudioconverterpropertymaximuminputpacketsize)Added [kAudioConverterPropertyMaximumOutputPacketSize](https://developer.apple.com/documentation/audiotoolbox/kaudioconverterpropertymaximumoutputpacketsize)Added [kAudioConverterPropertyMinimumInputBufferSize](https://developer.apple.com/documentation/audiotoolbox/1559928-audio_converter_properties/kaudioconverterpropertyminimuminputbuffersize)Added [kAudioConverterPropertyMinimumOutputBufferSize](https://developer.apple.com/documentation/audiotoolbox/1559928-audio_converter_properties/kaudioconverterpropertyminimumoutputbuffersize)Added [kAudioConverterPropertyOutputCodecParameters](https://developer.apple.com/documentation/audiotoolbox/1559928-audio_converter_properties/kaudioconverterpropertyoutputcodecparameters)Added [kAudioConverterPropertySettings](https://developer.apple.com/documentation/audiotoolbox/1559928-audio_converter_properties/kaudioconverterpropertysettings)Added [kAudioConverterQuality_High](https://developer.apple.com/documentation/audiotoolbox/kaudioconverterquality_high)Added [kAudioConverterQuality_Low](https://developer.apple.com/documentation/audiotoolbox/1559924-sample_rate_conversion_quality_i/kaudioconverterquality_low)Added [kAudioConverterQuality_Max](https://developer.apple.com/documentation/audiotoolbox/1559924-sample_rate_conversion_quality_i/kaudioconverterquality_max)Added [kAudioConverterQuality_Medium](https://developer.apple.com/documentation/audiotoolbox/kaudioconverterquality_medium)Added [kAudioConverterQuality_Min](https://developer.apple.com/documentation/audiotoolbox/1559924-sample_rate_conversion_quality_i/kaudioconverterquality_min)Added [kAudioConverterSampleRateConverterAlgorithm](https://developer.apple.com/documentation/audiotoolbox/1559928-audio_converter_properties/kaudioconvertersamplerateconverteralgorithm)Added [kAudioConverterSampleRateConverterComplexity](https://developer.apple.com/documentation/audiotoolbox/kaudioconvertersamplerateconvertercomplexity)Added [kAudioConverterSampleRateConverterComplexity_Linear](https://developer.apple.com/documentation/audiotoolbox/kaudioconvertersamplerateconvertercomplexity_linear)Added [kAudioConverterSampleRateConverterComplexity_Mastering](https://developer.apple.com/documentation/audiotoolbox/kaudioconvertersamplerateconvertercomplexity_mastering)Added [kAudioConverterSampleRateConverterComplexity_Normal](https://developer.apple.com/documentation/audiotoolbox/kaudioconvertersamplerateconvertercomplexity_normal)Added [kAudioConverterSampleRateConverterInitialPhase](https://developer.apple.com/documentation/audiotoolbox/kaudioconvertersamplerateconverterinitialphase)Added [kAudioConverterSampleRateConverterQuality](https://developer.apple.com/documentation/audiotoolbox/1559928-audio_converter_properties/kaudioconvertersamplerateconverterquality)Added [kConverterPrimeMethod_None](https://developer.apple.com/documentation/audiotoolbox/kconverterprimemethod_none)Added [kConverterPrimeMethod_Normal](https://developer.apple.com/documentation/audiotoolbox/1559927-converter_priming_constants/kconverterprimemethod_normal)Added [kConverterPrimeMethod_Pre](https://developer.apple.com/documentation/audiotoolbox/1559927-converter_priming_constants/kconverterprimemethod_pre)AudioFile.hAdded [kAudioFilePropertyID3Tag](https://developer.apple.com/documentation/audiotoolbox/1576499-audio_file_properties/kaudiofilepropertyid3tag)AudioServices.hRemoved kAudioSessionRouteChangeReason_BroadcastUpdateRemoved kAudioSessionRouteChangeReason_PolicyChangeAdded [AudioSessionRemovePropertyListenerWithUserData()](https://developer.apple.com/documentation/audiotoolbox/1618396-audiosessionremovepropertylisten)Added [kAudioSessionOverrideAudioRoute_None](https://developer.apple.com/documentation/audiotoolbox/1618372-audio_session_category_route_ove/kaudiosessionoverrideaudioroute_none)Added [kAudioSessionOverrideAudioRoute_Speaker](https://developer.apple.com/documentation/audiotoolbox/kaudiosessionoverrideaudioroute_speaker)Added [kAudioSessionProperty_CurrentHardwareIOBufferDuration](https://developer.apple.com/documentation/audiotoolbox/1618455-audio_session_property_identifie/kaudiosessionproperty_currenthardwareiobufferduration)Added [kAudioSessionProperty_CurrentHardwareInputLatency](https://developer.apple.com/documentation/audiotoolbox/1618455-audio_session_property_identifie/kaudiosessionproperty_currenthardwareinputlatency)Added kAudioSessionProperty_CurrentHardwareInputVolumeAdded [kAudioSessionProperty_CurrentHardwareOutputLatency](https://developer.apple.com/documentation/audiotoolbox/kaudiosessionproperty_currenthardwareoutputlatency)Added [kAudioSessionProperty_CurrentHardwareOutputVolume](https://developer.apple.com/documentation/audiotoolbox/kaudiosessionproperty_currenthardwareoutputvolume)Added [kAudioSessionProperty_OtherAudioIsPlaying](https://developer.apple.com/documentation/audiotoolbox/kaudiosessionproperty_otheraudioisplaying)Added [kAudioSessionProperty_OverrideAudioRoute](https://developer.apple.com/documentation/audiotoolbox/1618455-audio_session_property_identifie/kaudiosessionproperty_overrideaudioroute)Added [kAudioSessionRouteChangeReason_CategoryChange](https://developer.apple.com/documentation/audiotoolbox/kaudiosessionroutechangereason_categorychange)Modified [AudioSessionRemovePropertyListener()](https://developer.apple.com/documentation/audiotoolbox/1618364-audiosessionremovepropertylisten)

|  | Deprecation |
| --- | --- |
| Old |  |
| New | iOS 2.0 |

ExtendedAudioFile.hAdded [ExtAudioFileCreateWithURL()](https://developer.apple.com/documentation/audiotoolbox/1486878-extaudiofilecreatewithurl)Added [ExtAudioFileDispose()](https://developer.apple.com/documentation/audiotoolbox/1486832-extaudiofiledispose)Added [ExtAudioFileGetProperty()](https://developer.apple.com/documentation/audiotoolbox/1486840-extaudiofilegetproperty)Added [ExtAudioFileGetPropertyInfo()](https://developer.apple.com/documentation/audiotoolbox/1486871-extaudiofilegetpropertyinfo)Added [ExtAudioFileOpenURL()](https://developer.apple.com/documentation/audiotoolbox/1486873-extaudiofileopenurl)Added [ExtAudioFilePropertyID](https://developer.apple.com/documentation/audiotoolbox/extaudiofilepropertyid)Added [ExtAudioFileRead()](https://developer.apple.com/documentation/audiotoolbox/1486821-extaudiofileread)Added [ExtAudioFileRef](https://developer.apple.com/documentation/audiotoolbox/extaudiofileref)Added [ExtAudioFileSeek()](https://developer.apple.com/documentation/audiotoolbox/1486830-extaudiofileseek)Added [ExtAudioFileSetProperty()](https://developer.apple.com/documentation/audiotoolbox/1486884-extaudiofilesetproperty)Added [ExtAudioFileTell()](https://developer.apple.com/documentation/audiotoolbox/1486813-extaudiofiletell)Added [ExtAudioFileWrapAudioFileID()](https://developer.apple.com/documentation/audiotoolbox/1486852-extaudiofilewrapaudiofileid)Added [ExtAudioFileWrite()](https://developer.apple.com/documentation/audiotoolbox/1486846-extaudiofilewrite)Added [ExtAudioFileWriteAsync()](https://developer.apple.com/documentation/audiotoolbox/1486834-extaudiofilewriteasync)Added [kExtAudioFileError_AsyncWriteBufferOverflow](https://developer.apple.com/documentation/audiotoolbox/1486883-anonymous/kextaudiofileerror_asyncwritebufferoverflow)Added [kExtAudioFileError_AsyncWriteTooLarge](https://developer.apple.com/documentation/audiotoolbox/1486883-anonymous/kextaudiofileerror_asyncwritetoolarge)Added [kExtAudioFileError_InvalidChannelMap](https://developer.apple.com/documentation/audiotoolbox/1486883-anonymous/kextaudiofileerror_invalidchannelmap)Added [kExtAudioFileError_InvalidDataFormat](https://developer.apple.com/documentation/audiotoolbox/1486883-anonymous/kextaudiofileerror_invaliddataformat)Added [kExtAudioFileError_InvalidOperationOrder](https://developer.apple.com/documentation/audiotoolbox/kextaudiofileerror_invalidoperationorder)Added [kExtAudioFileError_InvalidProperty](https://developer.apple.com/documentation/audiotoolbox/1486883-anonymous/kextaudiofileerror_invalidproperty)Added [kExtAudioFileError_InvalidPropertySize](https://developer.apple.com/documentation/audiotoolbox/1486883-anonymous/kextaudiofileerror_invalidpropertysize)Added [kExtAudioFileError_InvalidSeek](https://developer.apple.com/documentation/audiotoolbox/kextaudiofileerror_invalidseek)Added [kExtAudioFileError_MaxPacketSizeUnknown](https://developer.apple.com/documentation/audiotoolbox/kextaudiofileerror_maxpacketsizeunknown)Added [kExtAudioFileError_NonPCMClientFormat](https://developer.apple.com/documentation/audiotoolbox/kextaudiofileerror_nonpcmclientformat)Added [kExtAudioFileProperty_AudioConverter](https://developer.apple.com/documentation/audiotoolbox/1486859-property_identifiers_for_extende/kextaudiofileproperty_audioconverter)Added [kExtAudioFileProperty_AudioFile](https://developer.apple.com/documentation/audiotoolbox/1486859-property_identifiers_for_extende/kextaudiofileproperty_audiofile)Added [kExtAudioFileProperty_ClientChannelLayout](https://developer.apple.com/documentation/audiotoolbox/kextaudiofileproperty_clientchannellayout)Added [kExtAudioFileProperty_ClientDataFormat](https://developer.apple.com/documentation/audiotoolbox/1486859-property_identifiers_for_extende/kextaudiofileproperty_clientdataformat)Added [kExtAudioFileProperty_ClientMaxPacketSize](https://developer.apple.com/documentation/audiotoolbox/1486859-property_identifiers_for_extende/kextaudiofileproperty_clientmaxpacketsize)Added [kExtAudioFileProperty_ConverterConfig](https://developer.apple.com/documentation/audiotoolbox/kextaudiofileproperty_converterconfig)Added [kExtAudioFileProperty_FileChannelLayout](https://developer.apple.com/documentation/audiotoolbox/kextaudiofileproperty_filechannellayout)Added [kExtAudioFileProperty_FileDataFormat](https://developer.apple.com/documentation/audiotoolbox/1486859-property_identifiers_for_extende/kextaudiofileproperty_filedataformat)Added [kExtAudioFileProperty_FileLengthFrames](https://developer.apple.com/documentation/audiotoolbox/1486859-property_identifiers_for_extende/kextaudiofileproperty_filelengthframes)Added [kExtAudioFileProperty_FileMaxPacketSize](https://developer.apple.com/documentation/audiotoolbox/1486859-property_identifiers_for_extende/kextaudiofileproperty_filemaxpacketsize)Added [kExtAudioFileProperty_IOBuffer](https://developer.apple.com/documentation/audiotoolbox/kextaudiofileproperty_iobuffer)Added [kExtAudioFileProperty_IOBufferSizeBytes](https://developer.apple.com/documentation/audiotoolbox/1486859-property_identifiers_for_extende/kextaudiofileproperty_iobuffersizebytes)

## AudioUnit

AUComponent.hAdded [kAudioUnitSubType_AUiPodTime](https://developer.apple.com/documentation/audiotoolbox/1619504-anonymous/kaudiounitsubtype_auipodtime)Modified [kAudioUnitSubType_TimePitch](https://developer.apple.com/documentation/audiotoolbox/1584152-anonymous/kaudiounitsubtype_timepitch)

|  | Architectures |
| --- | --- |
| Old | arm |
| New | none? |

AudioUnitParameters.hAdded [kDynamicsProcessorParam_InputAmplitude](https://developer.apple.com/documentation/audiotoolbox/1389787-dynamics_processor_unit_paramete/kdynamicsprocessorparam_inputamplitude) (no architecture available)Added [kDynamicsProcessorParam_OutputAmplitude](https://developer.apple.com/documentation/audiotoolbox/kdynamicsprocessorparam_outputamplitude) (no architecture available)Added [kMultibandCompressorParam_InputAmplitude1](https://developer.apple.com/documentation/audiotoolbox/1389781-anonymous/kmultibandcompressorparam_inputamplitude1) (no architecture available)Added [kMultibandCompressorParam_InputAmplitude2](https://developer.apple.com/documentation/audiotoolbox/1389781-anonymous/kmultibandcompressorparam_inputamplitude2) (no architecture available)Added [kMultibandCompressorParam_InputAmplitude3](https://developer.apple.com/documentation/audiotoolbox/kmultibandcompressorparam_inputamplitude3) (no architecture available)Added [kMultibandCompressorParam_InputAmplitude4](https://developer.apple.com/documentation/audiotoolbox/kmultibandcompressorparam_inputamplitude4) (no architecture available)Added [kMultibandCompressorParam_OutputAmplitude1](https://developer.apple.com/documentation/audiotoolbox/kmultibandcompressorparam_outputamplitude1) (no architecture available)Added [kMultibandCompressorParam_OutputAmplitude2](https://developer.apple.com/documentation/audiotoolbox/1389781-anonymous/kmultibandcompressorparam_outputamplitude2) (no architecture available)Added [kMultibandCompressorParam_OutputAmplitude3](https://developer.apple.com/documentation/audiotoolbox/1389781-anonymous/kmultibandcompressorparam_outputamplitude3) (no architecture available)Added [kMultibandCompressorParam_OutputAmplitude4](https://developer.apple.com/documentation/audiotoolbox/kmultibandcompressorparam_outputamplitude4) (no architecture available)Modified [kTimePitchParam_Pitch](https://developer.apple.com/documentation/audiotoolbox/1389946-autimepitch_autimepitch_offline_/ktimepitchparam_pitch)

|  | Architectures |
| --- | --- |
| Old | arm |
| New | none? |

Modified [kTimePitchParam_EffectBlend](https://developer.apple.com/documentation/audiotoolbox/1389946-autimepitch_autimepitch_offline_/ktimepitchparam_effectblend)

|  | Architectures |
| --- | --- |
| Old | arm |
| New | none? |

AudioUnitProperties.hAdded [AudioUnitFrequencyResponseBin](https://developer.apple.com/documentation/audiotoolbox/audiounitfrequencyresponsebin)Added [kAudioUnitProperty_FrequencyResponse](https://developer.apple.com/documentation/audiotoolbox/kaudiounitproperty_frequencyresponse)Added [kNumberOfResponseFrequencies](https://developer.apple.com/documentation/audiotoolbox/1534092-frequency_response_constants/knumberofresponsefrequencies)

## CFNetwork

No changes

## CoreAudio

No changes

## CoreFoundation

No changes

## CoreGraphics

No changes

## CoreLocation

No changes

## Foundation

No changes

## MediaPlayer

MPVolumeView.hModified [MPVolumeView](https://developer.apple.com/documentation/mediaplayer/mpvolumeview)

|  | Protocols |
| --- | --- |
| Old |  |
| New | NSCoding |

## OpenAL

No changes

## OpenGLES

No changes

## QuartzCore

No changes

## Security

No changes

## SystemConfiguration

No changes

## UIKit

UIViewController.hAdded [-[UIViewController didAnimateFirstHalfOfRotationToInterfaceOrientation:]](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621496-didanimatefirsthalfofrotationtoi)

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
