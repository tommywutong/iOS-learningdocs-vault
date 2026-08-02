---
title: OS X v10.8 API Diffs
apple_id: TP40011748
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_8/CoreAudio.html
archived_at: '2026-07-18T02:53:57.371713Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.8 API Diffs](OS%20X%20v10.7%20to%20OS%20X%20v10.8%20API%20Differences.md)


# CoreAudio Changes

## CoreAudio

AudioHardware.hAdded [kAudioDevicePropertyClipLight](https://developer.apple.com/documentation/coreaudio/kaudiodevicepropertycliplight)Added [kAudioDevicePropertyListenback](https://developer.apple.com/documentation/coreaudio/kaudiodevicepropertylistenback)Added [kAudioDevicePropertyTalkback](https://developer.apple.com/documentation/coreaudio/kaudiodevicepropertytalkback)Added [kAudioHardwarePropertyServiceRestarted](https://developer.apple.com/documentation/coreaudio/1545886-anonymous/kaudiohardwarepropertyservicerestarted)Added [kAudioHardwarePropertyTranslateBundleIDToTransportManager](https://developer.apple.com/documentation/coreaudio/kaudiohardwarepropertytranslatebundleidtotransportmanager)Added [kAudioHardwarePropertyTranslateUIDToDevice](https://developer.apple.com/documentation/coreaudio/kaudiohardwarepropertytranslateuidtodevice)Added [kAudioHardwarePropertyTransportManagerList](https://developer.apple.com/documentation/coreaudio/1545886-anonymous/kaudiohardwarepropertytransportmanagerlist)Added [kAudioTransportManagerCreateEndPointDevice](https://developer.apple.com/documentation/coreaudio/1545857-anonymous/kaudiotransportmanagercreateendpointdevice)Added [kAudioTransportManagerDestroyEndPointDevice](https://developer.apple.com/documentation/coreaudio/1545857-anonymous/kaudiotransportmanagerdestroyendpointdevice)Modified [AudioDeviceStop()](https://developer.apple.com/documentation/coreaudio/1421761-audiodevicestop)

|  | Declaration |
| --- | --- |
| From | OSStatus AudioDeviceStop ( AudioDeviceID inDevice, AudioDeviceIOProcID inProcID); |
| To | OSStatus AudioDeviceStop ( AudioObjectID inDevice, AudioDeviceIOProcID inProcID); |

Modified [AudioDeviceCreateIOProcID()](https://developer.apple.com/documentation/coreaudio/1423215-audiodevicecreateioprocid)

|  | Declaration |
| --- | --- |
| From | OSStatus AudioDeviceCreateIOProcID ( AudioDeviceID inDevice, AudioDeviceIOProc inProc, void \*inClientData, AudioDeviceIOProcID \*outIOProcID); |
| To | OSStatus AudioDeviceCreateIOProcID ( AudioObjectID inDevice, AudioDeviceIOProc inProc, void \*inClientData, AudioDeviceIOProcID \*outIOProcID); |

Modified [AudioDeviceTranslateTime()](https://developer.apple.com/documentation/coreaudio/1422786-audiodevicetranslatetime)

|  | Declaration |
| --- | --- |
| From | OSStatus AudioDeviceTranslateTime ( AudioDeviceID inDevice, const AudioTimeStamp \*inTime, AudioTimeStamp \*outTime); |
| To | OSStatus AudioDeviceTranslateTime ( AudioObjectID inDevice, const AudioTimeStamp \*inTime, AudioTimeStamp \*outTime); |

Modified [AudioDeviceGetCurrentTime()](https://developer.apple.com/documentation/coreaudio/1421759-audiodevicegetcurrenttime)

|  | Declaration |
| --- | --- |
| From | OSStatus AudioDeviceGetCurrentTime ( AudioDeviceID inDevice, AudioTimeStamp \*outTime); |
| To | OSStatus AudioDeviceGetCurrentTime ( AudioObjectID inDevice, AudioTimeStamp \*outTime); |

Modified [AudioDeviceDestroyIOProcID()](https://developer.apple.com/documentation/coreaudio/1422982-audiodevicedestroyioprocid)

|  | Declaration |
| --- | --- |
| From | OSStatus AudioDeviceDestroyIOProcID ( AudioDeviceID inDevice, AudioDeviceIOProcID inIOProcID); |
| To | OSStatus AudioDeviceDestroyIOProcID ( AudioObjectID inDevice, AudioDeviceIOProcID inIOProcID); |

Modified [AudioDeviceGetNearestStartTime()](https://developer.apple.com/documentation/coreaudio/1421818-audiodevicegetneareststarttime)

|  | Declaration |
| --- | --- |
| From | OSStatus AudioDeviceGetNearestStartTime ( AudioDeviceID inDevice, AudioTimeStamp \*ioRequestedStartTime, UInt32 inFlags); |
| To | OSStatus AudioDeviceGetNearestStartTime ( AudioObjectID inDevice, AudioTimeStamp \*ioRequestedStartTime, UInt32 inFlags); |

Modified [AudioDeviceStartAtTime()](https://developer.apple.com/documentation/coreaudio/1422331-audiodevicestartattime)

|  | Declaration |
| --- | --- |
| From | OSStatus AudioDeviceStartAtTime ( AudioDeviceID inDevice, AudioDeviceIOProcID inProcID, AudioTimeStamp \*ioRequestedStartTime, UInt32 inFlags); |
| To | OSStatus AudioDeviceStartAtTime ( AudioObjectID inDevice, AudioDeviceIOProcID inProcID, AudioTimeStamp \*ioRequestedStartTime, UInt32 inFlags); |

Modified [AudioDeviceStart()](https://developer.apple.com/documentation/coreaudio/1422884-audiodevicestart)

|  | Declaration |
| --- | --- |
| From | OSStatus AudioDeviceStart ( AudioDeviceID inDevice, AudioDeviceIOProcID inProcID); |
| To | OSStatus AudioDeviceStart ( AudioObjectID inDevice, AudioDeviceIOProcID inProcID); |

Modified [AudioDeviceCreateIOProcIDWithBlock()](https://developer.apple.com/documentation/coreaudio/1422986-audiodevicecreateioprocidwithblo)

|  | Declaration |
| --- | --- |
| From | OSStatus AudioDeviceCreateIOProcIDWithBlock ( AudioDeviceIOProcID \*outIOProcID, AudioDeviceID inDevice, dispatch_queue_t inDispatchQueue, AudioDeviceIOBlock inIOBlock); |
| To | OSStatus AudioDeviceCreateIOProcIDWithBlock ( AudioDeviceIOProcID \*outIOProcID, AudioObjectID inDevice, dispatch_queue_t inDispatchQueue, AudioDeviceIOBlock inIOBlock); |

AudioHardwareBase.hAdded [kAudioClipLightControlClassID](https://developer.apple.com/documentation/coreaudio/kaudiocliplightcontrolclassid)Added [kAudioDeviceTransportTypeAVB](https://developer.apple.com/documentation/coreaudio/1494580-anonymous/kaudiodevicetransporttypeavb)Added [kAudioDeviceTransportTypeAirPlay](https://developer.apple.com/documentation/coreaudio/1494580-anonymous/kaudiodevicetransporttypeairplay)Added [kAudioDeviceTransportTypeThunderbolt](https://developer.apple.com/documentation/coreaudio/kaudiodevicetransporttypethunderbolt)Added [kAudioEndPointClassID](https://developer.apple.com/documentation/coreaudio/1494587-anonymous/kaudioendpointclassid)Added [kAudioEndPointDeviceClassID](https://developer.apple.com/documentation/coreaudio/1494441-anonymous/kaudioendpointdeviceclassid)Added [#def kAudioEndPointDeviceEndPointListKey](https://developer.apple.com/documentation/coreaudio/kaudioendpointdeviceendpointlistkey)Added [#def kAudioEndPointDeviceIsPrivateKey](https://developer.apple.com/documentation/coreaudio/kaudioendpointdeviceisprivatekey)Added [#def kAudioEndPointDeviceMasterEndPointKey](https://developer.apple.com/documentation/coreaudio/kaudioendpointdevicemasterendpointkey)Added [#def kAudioEndPointDeviceNameKey](https://developer.apple.com/documentation/coreaudio/kaudioendpointdevicenamekey)Added [kAudioEndPointDevicePropertyComposition](https://developer.apple.com/documentation/coreaudio/kaudioendpointdevicepropertycomposition)Added [kAudioEndPointDevicePropertyEndPointList](https://developer.apple.com/documentation/coreaudio/kaudioendpointdevicepropertyendpointlist)Added [kAudioEndPointDevicePropertyIsPrivate](https://developer.apple.com/documentation/coreaudio/kaudioendpointdevicepropertyisprivate)Added [#def kAudioEndPointDeviceUIDKey](https://developer.apple.com/documentation/coreaudio/kaudioendpointdeviceuidkey)Added [#def kAudioEndPointInputChannelsKey](https://developer.apple.com/documentation/coreaudio/kaudioendpointinputchannelskey)Added [#def kAudioEndPointNameKey](https://developer.apple.com/documentation/coreaudio/kaudioendpointnamekey)Added [#def kAudioEndPointOutputChannelsKey](https://developer.apple.com/documentation/coreaudio/kaudioendpointoutputchannelskey)Added [#def kAudioEndPointUIDKey](https://developer.apple.com/documentation/coreaudio/kaudioendpointuidkey)Added [kAudioListenbackControlClassID](https://developer.apple.com/documentation/coreaudio/kaudiolistenbackcontrolclassid)Added [kAudioObjectPropertyControlList](https://developer.apple.com/documentation/coreaudio/1494454-anonymous/kaudioobjectpropertycontrollist)Added [kAudioObjectPropertyModelName](https://developer.apple.com/documentation/coreaudio/kaudioobjectpropertymodelname)Added [kAudioObjectPropertyScopeInput](https://developer.apple.com/documentation/coreaudio/kaudioobjectpropertyscopeinput)Added [kAudioObjectPropertyScopeOutput](https://developer.apple.com/documentation/coreaudio/kaudioobjectpropertyscopeoutput)Added [kAudioObjectPropertyScopePlayThrough](https://developer.apple.com/documentation/coreaudio/kaudioobjectpropertyscopeplaythrough)Added [kAudioPlugInPropertyDeviceList](https://developer.apple.com/documentation/coreaudio/kaudiopluginpropertydevicelist)Added [kAudioPlugInPropertyTranslateUIDToDevice](https://developer.apple.com/documentation/coreaudio/kaudiopluginpropertytranslateuidtodevice)Added [kAudioTalkbackControlClassID](https://developer.apple.com/documentation/coreaudio/1494512-anonymous/kaudiotalkbackcontrolclassid)Added [kAudioTransportManagerClassID](https://developer.apple.com/documentation/coreaudio/1494472-anonymous/kaudiotransportmanagerclassid)Added [kAudioTransportManagerPropertyEndPointList](https://developer.apple.com/documentation/coreaudio/kaudiotransportmanagerpropertyendpointlist)Added [kAudioTransportManagerPropertyTranslateUIDToEndPoint](https://developer.apple.com/documentation/coreaudio/kaudiotransportmanagerpropertytranslateuidtoendpoint)Added [kAudioTransportManagerPropertyTransportType](https://developer.apple.com/documentation/coreaudio/kaudiotransportmanagerpropertytransporttype)Modified [kAudioLevelControlClassID](https://developer.apple.com/documentation/coreaudio/kaudiolevelcontrolclassid)

|  | Header |
| --- | --- |
| From | AudioHardware.h |
| To | AudioHardwareBase.h |

Modified [AudioClassID](https://developer.apple.com/documentation/coreaudio/audioclassid)

|  | Header |
| --- | --- |
| From | AudioHardware.h |
| To | AudioHardwareBase.h |

Modified [kAudioHardwareUnknownPropertyError](https://developer.apple.com/documentation/coreaudio/1494531-anonymous/kaudiohardwareunknownpropertyerror)

|  | Header |
| --- | --- |
| From | AudioHardware.h |
| To | AudioHardwareBase.h |

Modified [kAudioVolumeControlClassID](https://developer.apple.com/documentation/coreaudio/kaudiovolumecontrolclassid)

|  | Header |
| --- | --- |
| From | AudioHardware.h |
| To | AudioHardwareBase.h |

Modified [kAudioStreamPropertyPhysicalFormat](https://developer.apple.com/documentation/coreaudio/1494541-anonymous/kaudiostreampropertyphysicalformat)

|  | Header |
| --- | --- |
| From | AudioHardware.h |
| To | AudioHardwareBase.h |

Modified [kAudioObjectPropertyElementCategoryName](https://developer.apple.com/documentation/coreaudio/kaudioobjectpropertyelementcategoryname)

|  | Header |
| --- | --- |
| From | AudioHardware.h |
| To | AudioHardwareBase.h |

Modified [kAudioStreamTerminalTypeReceiverMicrophone](https://developer.apple.com/documentation/coreaudio/kaudiostreamterminaltypereceivermicrophone)

|  | Header |
| --- | --- |
| From | AudioHardware.h |
| To | AudioHardwareBase.h |

Modified [kAudioDevicePropertyIsHidden](https://developer.apple.com/documentation/coreaudio/kaudiodevicepropertyishidden)

|  | Header |
| --- | --- |
| From | AudioHardware.h |
| To | AudioHardwareBase.h |

Modified [kAudioDevicePropertyDeviceIsAlive](https://developer.apple.com/documentation/coreaudio/kaudiodevicepropertydeviceisalive)

|  | Header |
| --- | --- |
| From | AudioHardware.h |
| To | AudioHardwareBase.h |

Modified [kAudioStreamTerminalTypeLFESpeaker](https://developer.apple.com/documentation/coreaudio/kaudiostreamterminaltypelfespeaker)

|  | Header |
| --- | --- |
| From | AudioHardware.h |
| To | AudioHardwareBase.h |

Modified [kAudioObjectPropertyElementWildcard](https://developer.apple.com/documentation/coreaudio/kaudioobjectpropertyelementwildcard)

|  | Header |
| --- | --- |
| From | AudioHardware.h |
| To | AudioHardwareBase.h |

Modified [kAudioSliderControlPropertyRange](https://developer.apple.com/documentation/coreaudio/1494510-anonymous/kaudioslidercontrolpropertyrange)

|  | Header |
| --- | --- |
| From | AudioHardware.h |
| To | AudioHardwareBase.h |

Modified [kAudioObjectPropertyName](https://developer.apple.com/documentation/coreaudio/1494449-anonymous/kaudioobjectpropertyname)

|  | Header |
| --- | --- |
| From | AudioHardware.h |
| To | AudioHardwareBase.h |

Modified [kAudioDeviceUnsupportedFormatError](https://developer.apple.com/documentation/coreaudio/kaudiodeviceunsupportedformaterror)

|  | Header |
| --- | --- |
| From | AudioHardware.h |
| To | AudioHardwareBase.h |

Modified [kAudioDevicePropertyDeviceCanBeDefaultSystemDevice](https://developer.apple.com/documentation/coreaudio/kaudiodevicepropertydevicecanbedefaultsystemdevice)

|  | Header |
| --- | --- |
| From | AudioHardware.h |
| To | AudioHardwareBase.h |

Modified [kAudioDevicePropertyStreams](https://developer.apple.com/documentation/coreaudio/kaudiodevicepropertystreams)

|  | Header |
| --- | --- |
| From | AudioHardware.h |
| To | AudioHardwareBase.h |

Modified [kAudioDevicePropertyPreferredChannelLayout](https://developer.apple.com/documentation/coreaudio/1494454-anonymous/kaudiodevicepropertypreferredchannellayout)

|  | Header |
| --- | --- |
| From | AudioHardware.h |
| To | AudioHardwareBase.h |

Modified [kAudioDevicePropertyRelatedDevices](https://developer.apple.com/documentation/coreaudio/1494454-anonymous/kaudiodevicepropertyrelateddevices)

|  | Header |
| --- | --- |
| From | AudioHardware.h |
| To | AudioHardwareBase.h |

Modified [kAudioDataSourceControlClassID](https://developer.apple.com/documentation/coreaudio/kaudiodatasourcecontrolclassid)

|  | Header |
| --- | --- |
| From | AudioHardware.h |
| To | AudioHardwareBase.h |

Modified [kAudioLFEVolumeControlClassID](https://developer.apple.com/documentation/coreaudio/kaudiolfevolumecontrolclassid)

|  | Header |
| --- | --- |
| From | AudioHardware.h |
| To | AudioHardwareBase.h |

Modified [kAudioDeviceTransportTypeHDMI](https://developer.apple.com/documentation/coreaudio/1494580-anonymous/kaudiodevicetransporttypehdmi)

|  | Header |
| --- | --- |
| From | AudioHardware.h |
| To | AudioHardwareBase.h |

Modified [kAudioDeviceTransportTypeDisplayPort](https://developer.apple.com/documentation/coreaudio/kaudiodevicetransporttypedisplayport)

|  | Header |
| --- | --- |
| From | AudioHardware.h |
| To | AudioHardwareBase.h |

Modified [kAudioObjectPropertyElementName](https://developer.apple.com/documentation/coreaudio/kaudioobjectpropertyelementname)

|  | Header |
| --- | --- |
| From | AudioHardware.h |
| To | AudioHardwareBase.h |

Modified [kAudioStreamTerminalTypeHeadsetMicrophone](https://developer.apple.com/documentation/coreaudio/kaudiostreamterminaltypeheadsetmicrophone)

|  | Header |
| --- | --- |
| From | AudioHardware.h |
| To | AudioHardwareBase.h |

Modified [kAudioDevicePropertyLatency](https://developer.apple.com/documentation/coreaudio/1494454-anonymous/kaudiodevicepropertylatency)

|  | Header |
| --- | --- |
| From | AudioHardware.h |
| To | AudioHardwareBase.h |

Modified [kAudioLevelControlPropertyDecibelRange](https://developer.apple.com/documentation/coreaudio/1494536-anonymous/kaudiolevelcontrolpropertydecibelrange)

|  | Header |
| --- | --- |
| From | AudioHardware.h |
| To | AudioHardwareBase.h |

Modified [kAudioStreamPropertyStartingChannel](https://developer.apple.com/documentation/coreaudio/1494541-anonymous/kaudiostreampropertystartingchannel)

|  | Header |
| --- | --- |
| From | AudioHardware.h |
| To | AudioHardwareBase.h |

Modified [kAudioHardwareBadStreamError](https://developer.apple.com/documentation/coreaudio/1494531-anonymous/kaudiohardwarebadstreamerror)

|  | Header |
| --- | --- |
| From | AudioHardware.h |
| To | AudioHardwareBase.h |

Modified [kAudioStreamPropertyTerminalType](https://developer.apple.com/documentation/coreaudio/1494541-anonymous/kaudiostreampropertyterminaltype)

|  | Header |
| --- | --- |
| From | AudioHardware.h |
| To | AudioHardwareBase.h |

Modified [AudioObjectPropertyScope](https://developer.apple.com/documentation/coreaudio/audioobjectpropertyscope)

|  | Header |
| --- | --- |
| From | AudioHardware.h |
| To | AudioHardwareBase.h |

Modified [kAudioLevelControlPropertyConvertScalarToDecibels](https://developer.apple.com/documentation/coreaudio/kaudiolevelcontrolpropertyconvertscalartodecibels)

|  | Header |
| --- | --- |
| From | AudioHardware.h |
| To | AudioHardwareBase.h |

Modified [kAudioHardwareNotRunningError](https://developer.apple.com/documentation/coreaudio/1494531-anonymous/kaudiohardwarenotrunningerror)

|  | Header |
| --- | --- |
| From | AudioHardware.h |
| To | AudioHardwareBase.h |

Modified [kAudioObjectPropertyBaseClass](https://developer.apple.com/documentation/coreaudio/1494449-anonymous/kaudioobjectpropertybaseclass)

|  | Header |
| --- | --- |
| From | AudioHardware.h |
| To | AudioHardwareBase.h |

Modified [kAudioObjectPropertyOwnedObjects](https://developer.apple.com/documentation/coreaudio/1494449-anonymous/kaudioobjectpropertyownedobjects)

|  | Header |
| --- | --- |
| From | AudioHardware.h |
| To | AudioHardwareBase.h |

Modified [kAudioJackControlClassID](https://developer.apple.com/documentation/coreaudio/1494512-anonymous/kaudiojackcontrolclassid)

|  | Header |
| --- | --- |
| From | AudioHardware.h |
| To | AudioHardwareBase.h |

Modified [kAudioSelectorControlClassID](https://developer.apple.com/documentation/coreaudio/kaudioselectorcontrolclassid)

|  | Header |
| --- | --- |
| From | AudioHardware.h |
| To | AudioHardwareBase.h |

Modified [kAudioStreamTerminalTypeDigitalAudioInterface](https://developer.apple.com/documentation/coreaudio/1494543-anonymous/kaudiostreamterminaltypedigitalaudiointerface)

|  | Header |
| --- | --- |
| From | AudioHardware.h |
| To | AudioHardwareBase.h |

Modified [kAudioHardwareUnsupportedOperationError](https://developer.apple.com/documentation/coreaudio/1494531-anonymous/kaudiohardwareunsupportedoperationerror)

|  | Header |
| --- | --- |
| From | AudioHardware.h |
| To | AudioHardwareBase.h |

Modified [kAudioHighPassFilterControlClassID](https://developer.apple.com/documentation/coreaudio/kaudiohighpassfiltercontrolclassid)

|  | Header |
| --- | --- |
| From | AudioHardware.h |
| To | AudioHardwareBase.h |

Modified [kAudioStreamPropertyAvailablePhysicalFormats](https://developer.apple.com/documentation/coreaudio/1494541-anonymous/kaudiostreampropertyavailablephysicalformats)

|  | Header |
| --- | --- |
| From | AudioHardware.h |
| To | AudioHardwareBase.h |

Modified [kAudioDeviceClassID](https://developer.apple.com/documentation/coreaudio/1494483-anonymous/kaudiodeviceclassid)

|  | Header |
| --- | --- |
| From | AudioHardware.h |
| To | AudioHardwareBase.h |

Modified [kAudioStreamTerminalTypeSpeaker](https://developer.apple.com/documentation/coreaudio/1494543-anonymous/kaudiostreamterminaltypespeaker)

|  | Header |
| --- | --- |
| From | AudioHardware.h |
| To | AudioHardwareBase.h |

Modified [kAudioStreamTerminalTypeTTY](https://developer.apple.com/documentation/coreaudio/kaudiostreamterminaltypetty)

|  | Header |
| --- | --- |
| From | AudioHardware.h |
| To | AudioHardwareBase.h |

Modified [kAudioLevelControlPropertyDecibelValue](https://developer.apple.com/documentation/coreaudio/kaudiolevelcontrolpropertydecibelvalue)

|  | Header |
| --- | --- |
| From | AudioHardware.h |
| To | AudioHardwareBase.h |

Modified [kAudioDevicePropertyTransportType](https://developer.apple.com/documentation/coreaudio/1494454-anonymous/kaudiodevicepropertytransporttype)

|  | Header |
| --- | --- |
| From | AudioHardware.h |
| To | AudioHardwareBase.h |

Modified [kAudioDeviceTransportTypeUnknown](https://developer.apple.com/documentation/coreaudio/kaudiodevicetransporttypeunknown)

|  | Header |
| --- | --- |
| From | AudioHardware.h |
| To | AudioHardwareBase.h |

Modified [kAudioControlPropertyScope](https://developer.apple.com/documentation/coreaudio/1494571-anonymous/kaudiocontrolpropertyscope)

|  | Header |
| --- | --- |
| From | AudioHardware.h |
| To | AudioHardwareBase.h |

Modified [AudioStreamRangedDescription](https://developer.apple.com/documentation/coreaudio/audiostreamrangeddescription)

|  | Header |
| --- | --- |
| From | AudioHardware.h |
| To | AudioHardwareBase.h |

Modified [kAudioBooleanControlClassID](https://developer.apple.com/documentation/coreaudio/1494512-anonymous/kaudiobooleancontrolclassid)

|  | Header |
| --- | --- |
| From | AudioHardware.h |
| To | AudioHardwareBase.h |

Modified [kAudioDevicePropertyDeviceUID](https://developer.apple.com/documentation/coreaudio/1494454-anonymous/kaudiodevicepropertydeviceuid)

|  | Header |
| --- | --- |
| From | AudioHardware.h |
| To | AudioHardwareBase.h |

Modified [kAudioSelectorControlPropertyItemKind](https://developer.apple.com/documentation/coreaudio/kaudioselectorcontrolpropertyitemkind)

|  | Header |
| --- | --- |
| From | AudioHardware.h |
| To | AudioHardwareBase.h |

Modified [kAudioControlClassID](https://developer.apple.com/documentation/coreaudio/kaudiocontrolclassid)

|  | Header |
| --- | --- |
| From | AudioHardware.h |
| To | AudioHardwareBase.h |

Modified [kAudioObjectPropertyElementNumberName](https://developer.apple.com/documentation/coreaudio/1494449-anonymous/kaudioobjectpropertyelementnumbername)

|  | Header |
| --- | --- |
| From | AudioHardware.h |
| To | AudioHardwareBase.h |

Modified [kAudioSliderControlPropertyValue](https://developer.apple.com/documentation/coreaudio/1494510-anonymous/kaudioslidercontrolpropertyvalue)

|  | Header |
| --- | --- |
| From | AudioHardware.h |
| To | AudioHardwareBase.h |

Modified [kAudioDeviceTransportTypeBluetooth](https://developer.apple.com/documentation/coreaudio/1494580-anonymous/kaudiodevicetransporttypebluetooth)

|  | Header |
| --- | --- |
| From | AudioHardware.h |
| To | AudioHardwareBase.h |

Modified [kAudioStreamTerminalTypeLine](https://developer.apple.com/documentation/coreaudio/1494543-anonymous/kaudiostreamterminaltypeline)

|  | Header |
| --- | --- |
| From | AudioHardware.h |
| To | AudioHardwareBase.h |

Modified [kAudioDevicePropertySafetyOffset](https://developer.apple.com/documentation/coreaudio/kaudiodevicepropertysafetyoffset)

|  | Header |
| --- | --- |
| From | AudioHardware.h |
| To | AudioHardwareBase.h |

Modified [kAudioHardwareUnspecifiedError](https://developer.apple.com/documentation/coreaudio/1494531-anonymous/kaudiohardwareunspecifiederror)

|  | Header |
| --- | --- |
| From | AudioHardware.h |
| To | AudioHardwareBase.h |

Modified [kAudioObjectPropertyScopeWildcard](https://developer.apple.com/documentation/coreaudio/1494576-anonymous/kaudioobjectpropertyscopewildcard)

|  | Header |
| --- | --- |
| From | AudioHardware.h |
| To | AudioHardwareBase.h |

Modified [kAudioStreamPropertyAvailableVirtualFormats](https://developer.apple.com/documentation/coreaudio/1494541-anonymous/kaudiostreampropertyavailablevirtualformats)

|  | Header |
| --- | --- |
| From | AudioHardware.h |
| To | AudioHardwareBase.h |

Modified [kAudioSoloControlClassID](https://developer.apple.com/documentation/coreaudio/1494512-anonymous/kaudiosolocontrolclassid)

|  | Header |
| --- | --- |
| From | AudioHardware.h |
| To | AudioHardwareBase.h |

Modified [kAudioObjectClassIDWildcard](https://developer.apple.com/documentation/coreaudio/kaudioobjectclassidwildcard)

|  | Header |
| --- | --- |
| From | AudioHardware.h |
| To | AudioHardwareBase.h |

Modified [AudioObjectPropertyElement](https://developer.apple.com/documentation/coreaudio/audioobjectpropertyelement)

|  | Header |
| --- | --- |
| From | AudioHardware.h |
| To | AudioHardwareBase.h |

Modified [kAudioDeviceTransportTypeFireWire](https://developer.apple.com/documentation/coreaudio/kaudiodevicetransporttypefirewire)

|  | Header |
| --- | --- |
| From | AudioHardware.h |
| To | AudioHardwareBase.h |

Modified [kAudioStreamPropertyVirtualFormat](https://developer.apple.com/documentation/coreaudio/1494541-anonymous/kaudiostreampropertyvirtualformat)

|  | Header |
| --- | --- |
| From | AudioHardware.h |
| To | AudioHardwareBase.h |

Modified [kAudioStereoPanControlClassID](https://developer.apple.com/documentation/coreaudio/kaudiostereopancontrolclassid)

|  | Header |
| --- | --- |
| From | AudioHardware.h |
| To | AudioHardwareBase.h |

Modified [kAudioControlPropertyElement](https://developer.apple.com/documentation/coreaudio/kaudiocontrolpropertyelement)

|  | Header |
| --- | --- |
| From | AudioHardware.h |
| To | AudioHardwareBase.h |

Modified [kAudioLevelControlPropertyConvertDecibelsToScalar](https://developer.apple.com/documentation/coreaudio/1494536-anonymous/kaudiolevelcontrolpropertyconvertdecibelstoscalar)

|  | Header |
| --- | --- |
| From | AudioHardware.h |
| To | AudioHardwareBase.h |

Modified [kAudioLFEMuteControlClassID](https://developer.apple.com/documentation/coreaudio/1494512-anonymous/kaudiolfemutecontrolclassid)

|  | Header |
| --- | --- |
| From | AudioHardware.h |
| To | AudioHardwareBase.h |

Modified [kAudioBooleanControlPropertyValue](https://developer.apple.com/documentation/coreaudio/kaudiobooleancontrolpropertyvalue)

|  | Header |
| --- | --- |
| From | AudioHardware.h |
| To | AudioHardwareBase.h |

Modified [kAudioStreamPropertyLatency](https://developer.apple.com/documentation/coreaudio/kaudiostreampropertylatency)

|  | Header |
| --- | --- |
| From | AudioHardware.h |
| To | AudioHardwareBase.h |

Modified [kAudioDevicePropertyDeviceCanBeDefaultDevice](https://developer.apple.com/documentation/coreaudio/1494454-anonymous/kaudiodevicepropertydevicecanbedefaultdevice)

|  | Header |
| --- | --- |
| From | AudioHardware.h |
| To | AudioHardwareBase.h |

Modified [kAudioObjectPropertySelectorWildcard](https://developer.apple.com/documentation/coreaudio/1494591-anonymous/kaudioobjectpropertyselectorwildcard)

|  | Header |
| --- | --- |
| From | AudioHardware.h |
| To | AudioHardwareBase.h |

Modified [kAudioObjectClassID](https://developer.apple.com/documentation/coreaudio/kaudioobjectclassid)

|  | Header |
| --- | --- |
| From | AudioHardware.h |
| To | AudioHardwareBase.h |

Modified [kAudioClockSourceControlClassID](https://developer.apple.com/documentation/coreaudio/1494554-anonymous/kaudioclocksourcecontrolclassid)

|  | Header |
| --- | --- |
| From | AudioHardware.h |
| To | AudioHardwareBase.h |

Modified [kAudioStreamPropertyDirection](https://developer.apple.com/documentation/coreaudio/kaudiostreampropertydirection)

|  | Header |
| --- | --- |
| From | AudioHardware.h |
| To | AudioHardwareBase.h |

Modified [kAudioStereoPanControlPropertyPanningChannels](https://developer.apple.com/documentation/coreaudio/1494557-anonymous/kaudiostereopancontrolpropertypanningchannels)

|  | Header |
| --- | --- |
| From | AudioHardware.h |
| To | AudioHardwareBase.h |

Modified [kAudioPhaseInvertControlClassID](https://developer.apple.com/documentation/coreaudio/1494512-anonymous/kaudiophaseinvertcontrolclassid)

|  | Header |
| --- | --- |
| From | AudioHardware.h |
| To | AudioHardwareBase.h |

Modified [kAudioDevicePropertyModelUID](https://developer.apple.com/documentation/coreaudio/1494454-anonymous/kaudiodevicepropertymodeluid)

|  | Header |
| --- | --- |
| From | AudioHardware.h |
| To | AudioHardwareBase.h |

Modified [kAudioDevicePropertyConfigurationApplication](https://developer.apple.com/documentation/coreaudio/1494454-anonymous/kaudiodevicepropertyconfigurationapplication)

|  | Header |
| --- | --- |
| From | AudioHardware.h |
| To | AudioHardwareBase.h |

Modified [kAudioSelectorControlPropertyItemName](https://developer.apple.com/documentation/coreaudio/1494594-anonymous/kaudioselectorcontrolpropertyitemname)

|  | Header |
| --- | --- |
| From | AudioHardware.h |
| To | AudioHardwareBase.h |

Modified [AudioObjectID](https://developer.apple.com/documentation/coreaudio/audioobjectid)

|  | Header |
| --- | --- |
| From | AudioHardware.h |
| To | AudioHardwareBase.h |

Modified [kAudioStreamClassID](https://developer.apple.com/documentation/coreaudio/kaudiostreamclassid)

|  | Header |
| --- | --- |
| From | AudioHardware.h |
| To | AudioHardwareBase.h |

Modified [kAudioDeviceTransportTypeAutoAggregate](https://developer.apple.com/documentation/coreaudio/kaudiodevicetransporttypeautoaggregate)

|  | Header |
| --- | --- |
| From | AudioHardware.h |
| To | AudioHardwareBase.h |

Modified [kAudioDevicePropertyNominalSampleRate](https://developer.apple.com/documentation/coreaudio/1494454-anonymous/kaudiodevicepropertynominalsamplerate)

|  | Header |
| --- | --- |
| From | AudioHardware.h |
| To | AudioHardwareBase.h |

Modified [kAudioStreamTerminalTypeDisplayPort](https://developer.apple.com/documentation/coreaudio/1494543-anonymous/kaudiostreamterminaltypedisplayport)

|  | Header |
| --- | --- |
| From | AudioHardware.h |
| To | AudioHardwareBase.h |

Modified [kAudioStreamTerminalTypeHeadphones](https://developer.apple.com/documentation/coreaudio/kaudiostreamterminaltypeheadphones)

|  | Header |
| --- | --- |
| From | AudioHardware.h |
| To | AudioHardwareBase.h |

Modified [kAudioStreamTerminalTypeHDMI](https://developer.apple.com/documentation/coreaudio/kaudiostreamterminaltypehdmi)

|  | Header |
| --- | --- |
| From | AudioHardware.h |
| To | AudioHardwareBase.h |

Modified [kAudioPlugInClassID](https://developer.apple.com/documentation/coreaudio/kaudiopluginclassid)

|  | Header |
| --- | --- |
| From | AudioHardware.h |
| To | AudioHardwareBase.h |

Modified [AudioObjectPropertySelector](https://developer.apple.com/documentation/coreaudio/audioobjectpropertyselector)

|  | Header |
| --- | --- |
| From | AudioHardware.h |
| To | AudioHardwareBase.h |

Modified [kAudioDevicePropertyClockDomain](https://developer.apple.com/documentation/coreaudio/1494454-anonymous/kaudiodevicepropertyclockdomain)

|  | Header |
| --- | --- |
| From | AudioHardware.h |
| To | AudioHardwareBase.h |

Modified [kAudioHardwareNoError](https://developer.apple.com/documentation/coreaudio/kaudiohardwarenoerror)

|  | Header |
| --- | --- |
| From | AudioHardware.h |
| To | AudioHardwareBase.h |

Modified [kAudioObjectUnknown](https://developer.apple.com/documentation/coreaudio/1494461-anonymous/kaudioobjectunknown)

|  | Header |
| --- | --- |
| From | AudioHardware.h |
| To | AudioHardwareBase.h |

Modified [kAudioObjectPropertyElementMaster](https://developer.apple.com/documentation/coreaudio/1494464-anonymous/kaudioobjectpropertyelementmaster)

|  | Header |
| --- | --- |
| From | AudioHardware.h |
| To | AudioHardwareBase.h |

Modified [kAudioClockSourceItemKindInternal](https://developer.apple.com/documentation/coreaudio/kaudioclocksourceitemkindinternal)

|  | Header |
| --- | --- |
| From | AudioHardware.h |
| To | AudioHardwareBase.h |

Modified [kAudioHardwareBadObjectError](https://developer.apple.com/documentation/coreaudio/kaudiohardwarebadobjecterror)

|  | Header |
| --- | --- |
| From | AudioHardware.h |
| To | AudioHardwareBase.h |

Modified [kAudioLineLevelControlClassID](https://developer.apple.com/documentation/coreaudio/kaudiolinelevelcontrolclassid)

|  | Header |
| --- | --- |
| From | AudioHardware.h |
| To | AudioHardwareBase.h |

Modified [kAudioSelectorControlPropertyCurrentItem](https://developer.apple.com/documentation/coreaudio/kaudioselectorcontrolpropertycurrentitem)

|  | Header |
| --- | --- |
| From | AudioHardware.h |
| To | AudioHardwareBase.h |

Modified [kAudioDeviceTransportTypeUSB](https://developer.apple.com/documentation/coreaudio/kaudiodevicetransporttypeusb)

|  | Header |
| --- | --- |
| From | AudioHardware.h |
| To | AudioHardwareBase.h |

Modified [kAudioStreamPropertyIsActive](https://developer.apple.com/documentation/coreaudio/1494541-anonymous/kaudiostreampropertyisactive)

|  | Header |
| --- | --- |
| From | AudioHardware.h |
| To | AudioHardwareBase.h |

Modified [kAudioDevicePropertyDeviceIsRunning](https://developer.apple.com/documentation/coreaudio/1494454-anonymous/kaudiodevicepropertydeviceisrunning)

|  | Header |
| --- | --- |
| From | AudioHardware.h |
| To | AudioHardwareBase.h |

Modified [kAudioSelectorControlItemKindSpacer](https://developer.apple.com/documentation/coreaudio/1494470-anonymous/kaudioselectorcontrolitemkindspacer)

|  | Header |
| --- | --- |
| From | AudioHardware.h |
| To | AudioHardwareBase.h |

Modified [kAudioDeviceTransportTypeVirtual](https://developer.apple.com/documentation/coreaudio/1494580-anonymous/kaudiodevicetransporttypevirtual)

|  | Header |
| --- | --- |
| From | AudioHardware.h |
| To | AudioHardwareBase.h |

Modified [kAudioDataDestinationControlClassID](https://developer.apple.com/documentation/coreaudio/kaudiodatadestinationcontrolclassid)

|  | Header |
| --- | --- |
| From | AudioHardware.h |
| To | AudioHardwareBase.h |

Modified [kAudioStreamTerminalTypeReceiverSpeaker](https://developer.apple.com/documentation/coreaudio/kaudiostreamterminaltypereceiverspeaker)

|  | Header |
| --- | --- |
| From | AudioHardware.h |
| To | AudioHardwareBase.h |

Modified [kAudioSliderControlClassID](https://developer.apple.com/documentation/coreaudio/kaudioslidercontrolclassid)

|  | Header |
| --- | --- |
| From | AudioHardware.h |
| To | AudioHardwareBase.h |

Modified [kAudioPlugInPropertyBundleID](https://developer.apple.com/documentation/coreaudio/1494489-anonymous/kaudiopluginpropertybundleid)

|  | Header |
| --- | --- |
| From | AudioHardware.h |
| To | AudioHardwareBase.h |

Modified [kAudioObjectPropertyManufacturer](https://developer.apple.com/documentation/coreaudio/1494449-anonymous/kaudioobjectpropertymanufacturer)

|  | Header |
| --- | --- |
| From | AudioHardware.h |
| To | AudioHardwareBase.h |

Modified [kAudioObjectPropertyOwner](https://developer.apple.com/documentation/coreaudio/1494449-anonymous/kaudioobjectpropertyowner)

|  | Header |
| --- | --- |
| From | AudioHardware.h |
| To | AudioHardwareBase.h |

Modified [kAudioStreamTerminalTypeUnknown](https://developer.apple.com/documentation/coreaudio/1494543-anonymous/kaudiostreamterminaltypeunknown)

|  | Header |
| --- | --- |
| From | AudioHardware.h |
| To | AudioHardwareBase.h |

Modified [kAudioDevicePropertyAvailableNominalSampleRates](https://developer.apple.com/documentation/coreaudio/1494454-anonymous/kaudiodevicepropertyavailablenominalsamplerates)

|  | Header |
| --- | --- |
| From | AudioHardware.h |
| To | AudioHardwareBase.h |

Modified [kAudioHardwareIllegalOperationError](https://developer.apple.com/documentation/coreaudio/1494531-anonymous/kaudiohardwareillegaloperationerror)

|  | Header |
| --- | --- |
| From | AudioHardware.h |
| To | AudioHardwareBase.h |

Modified [kAudioDeviceTransportTypeBuiltIn](https://developer.apple.com/documentation/coreaudio/1494580-anonymous/kaudiodevicetransporttypebuiltin)

|  | Header |
| --- | --- |
| From | AudioHardware.h |
| To | AudioHardwareBase.h |

Modified [kAudioObjectPropertyScopeGlobal](https://developer.apple.com/documentation/coreaudio/kaudioobjectpropertyscopeglobal)

|  | Header |
| --- | --- |
| From | AudioHardware.h |
| To | AudioHardwareBase.h |

Modified [kAudioDevicePermissionsError](https://developer.apple.com/documentation/coreaudio/kaudiodevicepermissionserror)

|  | Header |
| --- | --- |
| From | AudioHardware.h |
| To | AudioHardwareBase.h |

Modified [kAudioDeviceTransportTypeAggregate](https://developer.apple.com/documentation/coreaudio/kaudiodevicetransporttypeaggregate)

|  | Header |
| --- | --- |
| From | AudioHardware.h |
| To | AudioHardwareBase.h |

Modified [AudioObjectPropertyAddress](https://developer.apple.com/documentation/coreaudio/audioobjectpropertyaddress)

|  | Header |
| --- | --- |
| From | AudioHardware.h |
| To | AudioHardwareBase.h |

Modified [kAudioStereoPanControlPropertyValue](https://developer.apple.com/documentation/coreaudio/1494557-anonymous/kaudiostereopancontrolpropertyvalue)

|  | Header |
| --- | --- |
| From | AudioHardware.h |
| To | AudioHardwareBase.h |

Modified [kAudioStreamTerminalTypeMicrophone](https://developer.apple.com/documentation/coreaudio/1494543-anonymous/kaudiostreamterminaltypemicrophone)

|  | Header |
| --- | --- |
| From | AudioHardware.h |
| To | AudioHardwareBase.h |

Modified [kAudioDevicePropertyIcon](https://developer.apple.com/documentation/coreaudio/kaudiodevicepropertyicon)

|  | Header |
| --- | --- |
| From | AudioHardware.h |
| To | AudioHardwareBase.h |

Modified [kAudioObjectPropertyClass](https://developer.apple.com/documentation/coreaudio/kaudioobjectpropertyclass)

|  | Header |
| --- | --- |
| From | AudioHardware.h |
| To | AudioHardwareBase.h |

Modified [kAudioMuteControlClassID](https://developer.apple.com/documentation/coreaudio/1494512-anonymous/kaudiomutecontrolclassid)

|  | Header |
| --- | --- |
| From | AudioHardware.h |
| To | AudioHardwareBase.h |

Modified [kAudioDevicePropertyPreferredChannelsForStereo](https://developer.apple.com/documentation/coreaudio/1494454-anonymous/kaudiodevicepropertypreferredchannelsforstereo)

|  | Header |
| --- | --- |
| From | AudioHardware.h |
| To | AudioHardwareBase.h |

Modified [kAudioSelectorControlPropertyAvailableItems](https://developer.apple.com/documentation/coreaudio/1494594-anonymous/kaudioselectorcontrolpropertyavailableitems)

|  | Header |
| --- | --- |
| From | AudioHardware.h |
| To | AudioHardwareBase.h |

Modified [kAudioLevelControlPropertyScalarValue](https://developer.apple.com/documentation/coreaudio/1494536-anonymous/kaudiolevelcontrolpropertyscalarvalue)

|  | Header |
| --- | --- |
| From | AudioHardware.h |
| To | AudioHardwareBase.h |

Modified [kAudioHardwareBadDeviceError](https://developer.apple.com/documentation/coreaudio/1494531-anonymous/kaudiohardwarebaddeviceerror)

|  | Header |
| --- | --- |
| From | AudioHardware.h |
| To | AudioHardwareBase.h |

Modified [kAudioHardwareBadPropertySizeError](https://developer.apple.com/documentation/coreaudio/kaudiohardwarebadpropertysizeerror)

|  | Header |
| --- | --- |
| From | AudioHardware.h |
| To | AudioHardwareBase.h |

Modified [kAudioPhantomPowerControlClassID](https://developer.apple.com/documentation/coreaudio/1494512-anonymous/kaudiophantompowercontrolclassid)

|  | Header |
| --- | --- |
| From | AudioHardware.h |
| To | AudioHardwareBase.h |

Modified [kAudioDeviceTransportTypePCI](https://developer.apple.com/documentation/coreaudio/kaudiodevicetransporttypepci)

|  | Header |
| --- | --- |
| From | AudioHardware.h |
| To | AudioHardwareBase.h |

AudioHardwareDeprecated.hModified [kAudioDevicePropertyDeviceManufacturerCFString](https://developer.apple.com/documentation/coreaudio/kaudiodevicepropertydevicemanufacturercfstring)

|  | Header |
| --- | --- |
| From | AudioHardware.h |
| To | AudioHardwareDeprecated.h |

Modified [kAudioDevicePropertyScopeInput](https://developer.apple.com/documentation/coreaudio/1580726-anonymous/kaudiodevicepropertyscopeinput)

|  | Header |
| --- | --- |
| From | AudioHardware.h |
| To | AudioHardwareDeprecated.h |

Modified [AudioHardwarePropertyID](https://developer.apple.com/documentation/coreaudio/audiohardwarepropertyid)

|  | Header |
| --- | --- |
| From | AudioHardware.h |
| To | AudioHardwareDeprecated.h |

Modified [kAudioLevelControlTranferFunction4Over1](https://developer.apple.com/documentation/coreaudio/audiolevelcontroltransferfunction/kaudiolevelcontroltranferfunction4over1)

|  | Header |
| --- | --- |
| From | AudioHardware.h |
| To | AudioHardwareDeprecated.h |

Modified [kAudioISubOwnerControlClassID](https://developer.apple.com/documentation/coreaudio/1580720-anonymous/kaudioisubownercontrolclassid)

|  | Header |
| --- | --- |
| From | AudioHardware.h |
| To | AudioHardwareDeprecated.h |

Modified [kAudioLevelControlTranferFunction8Over1](https://developer.apple.com/documentation/coreaudio/audiolevelcontroltransferfunction/tranferfunction8over1)

|  | Header |
| --- | --- |
| From | AudioHardware.h |
| To | AudioHardwareDeprecated.h |

Modified [AudioStreamID](https://developer.apple.com/documentation/coreaudio/audiostreamid)

|  | Header |
| --- | --- |
| From | AudioHardware.h |
| To | AudioHardwareDeprecated.h |

Modified [kAudioLevelControlTranferFunction5Over1](https://developer.apple.com/documentation/coreaudio/audiolevelcontroltransferfunction/kaudiolevelcontroltranferfunction5over1)

|  | Header |
| --- | --- |
| From | AudioHardware.h |
| To | AudioHardwareDeprecated.h |

Modified [AudioHardwareGetPropertyInfo()](https://developer.apple.com/documentation/coreaudio/1580716-audiohardwaregetpropertyinfo)

|  | Header |
| --- | --- |
| From | AudioHardware.h |
| To | AudioHardwareDeprecated.h |

Modified [AudioStreamGetPropertyInfo()](https://developer.apple.com/documentation/coreaudio/1580745-audiostreamgetpropertyinfo)

|  | Header |
| --- | --- |
| From | AudioHardware.h |
| To | AudioHardwareDeprecated.h |

Modified [kAudioLevelControlTranferFunction9Over1](https://developer.apple.com/documentation/coreaudio/audiolevelcontroltransferfunction/kaudiolevelcontroltranferfunction9over1)

|  | Header |
| --- | --- |
| From | AudioHardware.h |
| To | AudioHardwareDeprecated.h |

Modified [kAudioDevicePropertyStreamFormatMatch](https://developer.apple.com/documentation/coreaudio/1580731-anonymous/kaudiodevicepropertystreamformatmatch)

|  | Header |
| --- | --- |
| From | AudioHardware.h |
| To | AudioHardwareDeprecated.h |

Modified [kAudioDevicePropertyDataSourceNameForID](https://developer.apple.com/documentation/coreaudio/kaudiodevicepropertydatasourcenameforid)

|  | Header |
| --- | --- |
| From | AudioHardware.h |
| To | AudioHardwareDeprecated.h |

Modified [kAudioControlPropertyVariant](https://developer.apple.com/documentation/coreaudio/kaudiocontrolpropertyvariant)

|  | Header |
| --- | --- |
| From | AudioHardware.h |
| To | AudioHardwareDeprecated.h |

Modified [kAudioDevicePropertyHighPassFilterSettingNameForID](https://developer.apple.com/documentation/coreaudio/kaudiodevicepropertyhighpassfiltersettingnameforid)

|  | Header |
| --- | --- |
| From | AudioHardware.h |
| To | AudioHardwareDeprecated.h |

Modified [kAudioDevicePropertyBufferSize](https://developer.apple.com/documentation/coreaudio/1580731-anonymous/kaudiodevicepropertybuffersize)

|  | Header |
| --- | --- |
| From | AudioHardware.h |
| To | AudioHardwareDeprecated.h |

Modified [AudioDeviceRead()](https://developer.apple.com/documentation/coreaudio/1580734-audiodeviceread)

|  | Header |
| --- | --- |
| From | AudioHardware.h |
| To | AudioHardwareDeprecated.h |

Modified [kAudioLevelControlTranferFunction3Over2](https://developer.apple.com/documentation/coreaudio/audiolevelcontroltransferfunction/tranferfunction3over2)

|  | Header |
| --- | --- |
| From | AudioHardware.h |
| To | AudioHardwareDeprecated.h |

Modified [kAudioDevicePropertyDeviceManufacturer](https://developer.apple.com/documentation/coreaudio/1580731-anonymous/kaudiodevicepropertydevicemanufacturer)

|  | Header |
| --- | --- |
| From | AudioHardware.h |
| To | AudioHardwareDeprecated.h |

Modified [AudioDeviceRemoveIOProc()](https://developer.apple.com/documentation/coreaudio/1580735-audiodeviceremoveioproc)

|  | Header |
| --- | --- |
| From | AudioHardware.h |
| To | AudioHardwareDeprecated.h |

Modified [kAudioLevelControlTranferFunction12Over1](https://developer.apple.com/documentation/coreaudio/audiolevelcontroltransferfunction/kaudiolevelcontroltranferfunction12over1)

|  | Header |
| --- | --- |
| From | AudioHardware.h |
| To | AudioHardwareDeprecated.h |

Modified [kAudioClockSourceControlPropertyItemKind](https://developer.apple.com/documentation/coreaudio/kaudioclocksourcecontrolpropertyitemkind)

|  | Header |
| --- | --- |
| From | AudioHardware.h |
| To | AudioHardwareDeprecated.h |

Modified [kAudioDevicePropertyChannelNumberNameCFString](https://developer.apple.com/documentation/coreaudio/kaudiodevicepropertychannelnumbernamecfstring)

|  | Header |
| --- | --- |
| From | AudioHardware.h |
| To | AudioHardwareDeprecated.h |

Modified [#def kAudioHardwareRunLoopMode](https://developer.apple.com/documentation/coreaudio/kaudiohardwarerunloopmode)

|  | Header |
| --- | --- |
| From | AudioHardware.h |
| To | AudioHardwareDeprecated.h |

Modified [kAudioDevicePropertyChannelNominalLineLevelNameForID](https://developer.apple.com/documentation/coreaudio/kaudiodevicepropertychannelnominallinelevelnameforid)

|  | Header |
| --- | --- |
| From | AudioHardware.h |
| To | AudioHardwareDeprecated.h |

Modified [AudioHardwareRemoveRunLoopSource()](https://developer.apple.com/documentation/coreaudio/1580717-audiohardwareremoverunloopsource)

|  | Header |
| --- | --- |
| From | AudioHardware.h |
| To | AudioHardwareDeprecated.h |

Modified [kAudioDevicePropertyStreamFormats](https://developer.apple.com/documentation/coreaudio/1580731-anonymous/kaudiodevicepropertystreamformats)

|  | Header |
| --- | --- |
| From | AudioHardware.h |
| To | AudioHardwareDeprecated.h |

Modified [AudioDevicePropertyID](https://developer.apple.com/documentation/coreaudio/audiodevicepropertyid)

|  | Header |
| --- | --- |
| From | AudioHardware.h |
| To | AudioHardwareDeprecated.h |

Modified [kAudioDevicePropertySupportsMixing](https://developer.apple.com/documentation/coreaudio/1580731-anonymous/kaudiodevicepropertysupportsmixing)

|  | Header |
| --- | --- |
| From | AudioHardware.h |
| To | AudioHardwareDeprecated.h |

Modified [kAudioLevelControlTranferFunctionLinear](https://developer.apple.com/documentation/coreaudio/audiolevelcontroltransferfunction/tranferfunctionlinear)

|  | Header |
| --- | --- |
| From | AudioHardware.h |
| To | AudioHardwareDeprecated.h |

Modified [AudioDeviceRemovePropertyListener()](https://developer.apple.com/documentation/coreaudio/1580714-audiodeviceremovepropertylistene)

|  | Header |
| --- | --- |
| From | AudioHardware.h |
| To | AudioHardwareDeprecated.h |

Modified [kAudioHardwarePropertyBootChimeVolumeScalar](https://developer.apple.com/documentation/coreaudio/kaudiohardwarepropertybootchimevolumescalar)

|  | Header |
| --- | --- |
| From | AudioHardware.h |
| To | AudioHardwareDeprecated.h |

Modified [AudioHardwareSetProperty()](https://developer.apple.com/documentation/coreaudio/1580730-audiohardwaresetproperty)

|  | Header |
| --- | --- |
| From | AudioHardware.h |
| To | AudioHardwareDeprecated.h |

Modified [kAudioLevelControlTranferFunction1Over2](https://developer.apple.com/documentation/coreaudio/audiolevelcontroltransferfunction/kaudiolevelcontroltranferfunction1over2)

|  | Header |
| --- | --- |
| From | AudioHardware.h |
| To | AudioHardwareDeprecated.h |

Modified [kAudioDevicePropertyStreamFormatSupported](https://developer.apple.com/documentation/coreaudio/kaudiodevicepropertystreamformatsupported)

|  | Header |
| --- | --- |
| From | AudioHardware.h |
| To | AudioHardwareDeprecated.h |

Modified [kAudioDevicePropertyChannelName](https://developer.apple.com/documentation/coreaudio/kaudiodevicepropertychannelname)

|  | Header |
| --- | --- |
| From | AudioHardware.h |
| To | AudioHardwareDeprecated.h |

Modified [AudioStreamRemovePropertyListener()](https://developer.apple.com/documentation/coreaudio/1580751-audiostreamremovepropertylistene)

|  | Header |
| --- | --- |
| From | AudioHardware.h |
| To | AudioHardwareDeprecated.h |

Modified [kAudioDevicePropertyChannelCategoryName](https://developer.apple.com/documentation/coreaudio/1580731-anonymous/kaudiodevicepropertychannelcategoryname)

|  | Header |
| --- | --- |
| From | AudioHardware.h |
| To | AudioHardwareDeprecated.h |

Modified [kAudioDevicePropertyBufferSizeRange](https://developer.apple.com/documentation/coreaudio/1580731-anonymous/kaudiodevicepropertybuffersizerange)

|  | Header |
| --- | --- |
| From | AudioHardware.h |
| To | AudioHardwareDeprecated.h |

Modified [AudioHardwareAddRunLoopSource()](https://developer.apple.com/documentation/coreaudio/1580725-audiohardwareaddrunloopsource)

|  | Header |
| --- | --- |
| From | AudioHardware.h |
| To | AudioHardwareDeprecated.h |

Modified [kAudioLevelControlPropertyDecibelsToScalarTransferFunction](https://developer.apple.com/documentation/coreaudio/kaudiolevelcontrolpropertydecibelstoscalartransferfunction)

|  | Header |
| --- | --- |
| From | AudioHardware.h |
| To | AudioHardwareDeprecated.h |

Modified [AudioDeviceAddPropertyListener()](https://developer.apple.com/documentation/coreaudio/1580727-audiodeviceaddpropertylistener)

|  | Header |
| --- | --- |
| From | AudioHardware.h |
| To | AudioHardwareDeprecated.h |

Modified [kAudioDevicePropertyDeviceNameCFString](https://developer.apple.com/documentation/coreaudio/1580731-anonymous/kaudiodevicepropertydevicenamecfstring)

|  | Header |
| --- | --- |
| From | AudioHardware.h |
| To | AudioHardwareDeprecated.h |

Modified [AudioHardwareGetProperty()](https://developer.apple.com/documentation/coreaudio/1580718-audiohardwaregetproperty)

|  | Header |
| --- | --- |
| From | AudioHardware.h |
| To | AudioHardwareDeprecated.h |

Modified [kAudioDevicePropertyPlayThruDestinationNameForID](https://developer.apple.com/documentation/coreaudio/1580731-anonymous/kaudiodevicepropertyplaythrudestinationnameforid)

|  | Header |
| --- | --- |
| From | AudioHardware.h |
| To | AudioHardwareDeprecated.h |

Modified [kAudioHardwarePropertyDeviceForUID](https://developer.apple.com/documentation/coreaudio/kaudiohardwarepropertydeviceforuid)

|  | Header |
| --- | --- |
| From | AudioHardware.h |
| To | AudioHardwareDeprecated.h |

Modified [AudioDeviceGetPropertyInfo()](https://developer.apple.com/documentation/coreaudio/1580721-audiodevicegetpropertyinfo)

|  | Header |
| --- | --- |
| From | AudioHardware.h |
| To | AudioHardwareDeprecated.h |

Modified [kAudioLevelControlTranferFunction11Over1](https://developer.apple.com/documentation/coreaudio/audiolevelcontroltransferfunction/kaudiolevelcontroltranferfunction11over1)

|  | Header |
| --- | --- |
| From | AudioHardware.h |
| To | AudioHardwareDeprecated.h |

Modified [kAudioLevelControlTranferFunction3Over4](https://developer.apple.com/documentation/coreaudio/audiolevelcontroltransferfunction/kaudiolevelcontroltranferfunction3over4)

|  | Header |
| --- | --- |
| From | AudioHardware.h |
| To | AudioHardwareDeprecated.h |

Modified [AudioHardwarePropertyListenerProc](https://developer.apple.com/documentation/coreaudio/audiohardwarepropertylistenerproc)

|  | Header |
| --- | --- |
| From | AudioHardware.h |
| To | AudioHardwareDeprecated.h |

Modified [AudioStreamSetProperty()](https://developer.apple.com/documentation/coreaudio/1580733-audiostreamsetproperty)

|  | Header |
| --- | --- |
| From | AudioHardware.h |
| To | AudioHardwareDeprecated.h |

Modified [kAudioLevelControlTranferFunction3Over1](https://developer.apple.com/documentation/coreaudio/audiolevelcontroltransferfunction/kaudiolevelcontroltranferfunction3over1)

|  | Header |
| --- | --- |
| From | AudioHardware.h |
| To | AudioHardwareDeprecated.h |

Modified [kAudioLevelControlTranferFunction7Over1](https://developer.apple.com/documentation/coreaudio/audiolevelcontroltransferfunction/tranferfunction7over1)

|  | Header |
| --- | --- |
| From | AudioHardware.h |
| To | AudioHardwareDeprecated.h |

Modified [kAudioLevelControlTranferFunction2Over1](https://developer.apple.com/documentation/coreaudio/audiolevelcontroltransferfunction/tranferfunction2over1)

|  | Header |
| --- | --- |
| From | AudioHardware.h |
| To | AudioHardwareDeprecated.h |

Modified [AudioDeviceSetProperty()](https://developer.apple.com/documentation/coreaudio/1580742-audiodevicesetproperty)

|  | Header |
| --- | --- |
| From | AudioHardware.h |
| To | AudioHardwareDeprecated.h |

Modified [kAudioDevicePropertyDeviceName](https://developer.apple.com/documentation/coreaudio/kaudiodevicepropertydevicename)

|  | Header |
| --- | --- |
| From | AudioHardware.h |
| To | AudioHardwareDeprecated.h |

Modified [kAudioHardwarePropertyBootChimeVolumeDecibelsToScalar](https://developer.apple.com/documentation/coreaudio/1580738-anonymous/kaudiohardwarepropertybootchimevolumedecibelstoscalar)

|  | Header |
| --- | --- |
| From | AudioHardware.h |
| To | AudioHardwareDeprecated.h |

Modified [kAudioPropertyWildcardChannel](https://developer.apple.com/documentation/coreaudio/1580740-anonymous/kaudiopropertywildcardchannel)

|  | Header |
| --- | --- |
| From | AudioHardware.h |
| To | AudioHardwareDeprecated.h |

Modified [kAudioStreamUnknown](https://developer.apple.com/documentation/coreaudio/kaudiostreamunknown)

|  | Header |
| --- | --- |
| From | AudioHardware.h |
| To | AudioHardwareDeprecated.h |

Modified [AudioStreamAddPropertyListener()](https://developer.apple.com/documentation/coreaudio/1580732-audiostreamaddpropertylistener)

|  | Header |
| --- | --- |
| From | AudioHardware.h |
| To | AudioHardwareDeprecated.h |

Modified [kAudioLevelControlTranferFunction6Over1](https://developer.apple.com/documentation/coreaudio/audiolevelcontroltransferfunction/kaudiolevelcontroltranferfunction6over1)

|  | Header |
| --- | --- |
| From | AudioHardware.h |
| To | AudioHardwareDeprecated.h |

Modified [kAudioPropertyWildcardSection](https://developer.apple.com/documentation/coreaudio/1580737-anonymous/kaudiopropertywildcardsection)

|  | Header |
| --- | --- |
| From | AudioHardware.h |
| To | AudioHardwareDeprecated.h |

Modified [kAudioDevicePropertyStreamFormat](https://developer.apple.com/documentation/coreaudio/kaudiodevicepropertystreamformat)

|  | Header |
| --- | --- |
| From | AudioHardware.h |
| To | AudioHardwareDeprecated.h |

Modified [kAudioHardwarePropertyRunLoop](https://developer.apple.com/documentation/coreaudio/1580723-anonymous/kaudiohardwarepropertyrunloop)

|  | Header |
| --- | --- |
| From | AudioHardware.h |
| To | AudioHardwareDeprecated.h |

Modified [kAudioHardwarePropertyBootChimeVolumeDecibelsToScalarTransferFunction](https://developer.apple.com/documentation/coreaudio/kaudiohardwarepropertybootchimevolumedecibelstoscalartransferfunction)

|  | Header |
| --- | --- |
| From | AudioHardware.h |
| To | AudioHardwareDeprecated.h |

Modified [AudioHardwareRemovePropertyListener()](https://developer.apple.com/documentation/coreaudio/1580739-audiohardwareremovepropertyliste)

|  | Header |
| --- | --- |
| From | AudioHardware.h |
| To | AudioHardwareDeprecated.h |

Modified [kAudioDevicePropertyVolumeDecibelsToScalarTransferFunction](https://developer.apple.com/documentation/coreaudio/kaudiodevicepropertyvolumedecibelstoscalartransferfunction)

|  | Header |
| --- | --- |
| From | AudioHardware.h |
| To | AudioHardwareDeprecated.h |

Modified [kAudioDevicePropertyClockSourceNameForID](https://developer.apple.com/documentation/coreaudio/1580731-anonymous/kaudiodevicepropertyclocksourcenameforid)

|  | Header |
| --- | --- |
| From | AudioHardware.h |
| To | AudioHardwareDeprecated.h |

Modified [AudioDeviceAddIOProc()](https://developer.apple.com/documentation/coreaudio/1580729-audiodeviceaddioproc)

|  | Header |
| --- | --- |
| From | AudioHardware.h |
| To | AudioHardwareDeprecated.h |

Modified [kAudioHardwarePropertyBootChimeVolumeScalarToDecibels](https://developer.apple.com/documentation/coreaudio/kaudiohardwarepropertybootchimevolumescalartodecibels)

|  | Header |
| --- | --- |
| From | AudioHardware.h |
| To | AudioHardwareDeprecated.h |

Modified [AudioDeviceGetProperty()](https://developer.apple.com/documentation/coreaudio/1580744-audiodevicegetproperty)

|  | Header |
| --- | --- |
| From | AudioHardware.h |
| To | AudioHardwareDeprecated.h |

Modified [kAudioStreamPropertyOwningDevice](https://developer.apple.com/documentation/coreaudio/1580748-anonymous/kaudiostreampropertyowningdevice)

|  | Header |
| --- | --- |
| From | AudioHardware.h |
| To | AudioHardwareDeprecated.h |

Modified [kAudioDevicePropertyScopePlayThrough](https://developer.apple.com/documentation/coreaudio/kaudiodevicepropertyscopeplaythrough)

|  | Header |
| --- | --- |
| From | AudioHardware.h |
| To | AudioHardwareDeprecated.h |

Modified [kAudioDeviceUnknown](https://developer.apple.com/documentation/coreaudio/1580746-anonymous/kaudiodeviceunknown)

|  | Header |
| --- | --- |
| From | AudioHardware.h |
| To | AudioHardwareDeprecated.h |

Modified [kAudioDevicePropertyChannelNumberName](https://developer.apple.com/documentation/coreaudio/1580731-anonymous/kaudiodevicepropertychannelnumbername)

|  | Header |
| --- | --- |
| From | AudioHardware.h |
| To | AudioHardwareDeprecated.h |

Modified [kAudioDevicePropertyChannelNameCFString](https://developer.apple.com/documentation/coreaudio/1580731-anonymous/kaudiodevicepropertychannelnamecfstring)

|  | Header |
| --- | --- |
| From | AudioHardware.h |
| To | AudioHardwareDeprecated.h |

Modified [kAudioStreamPropertyPhysicalFormatSupported](https://developer.apple.com/documentation/coreaudio/1580748-anonymous/kaudiostreampropertyphysicalformatsupported)

|  | Header |
| --- | --- |
| From | AudioHardware.h |
| To | AudioHardwareDeprecated.h |

Modified [kAudioPropertyWildcardPropertyID](https://developer.apple.com/documentation/coreaudio/kaudiopropertywildcardpropertyid)

|  | Header |
| --- | --- |
| From | AudioHardware.h |
| To | AudioHardwareDeprecated.h |

Modified [kAudioBootChimeVolumeControlClassID](https://developer.apple.com/documentation/coreaudio/kaudiobootchimevolumecontrolclassid)

|  | Header |
| --- | --- |
| From | AudioHardware.h |
| To | AudioHardwareDeprecated.h |

Modified [kAudioHardwarePropertyBootChimeVolumeRangeDecibels](https://developer.apple.com/documentation/coreaudio/kaudiohardwarepropertybootchimevolumerangedecibels)

|  | Header |
| --- | --- |
| From | AudioHardware.h |
| To | AudioHardwareDeprecated.h |

Modified [kAudioDevicePropertyPlayThruVolumeDecibelsToScalarTransferFunction](https://developer.apple.com/documentation/coreaudio/kaudiodevicepropertyplaythruvolumedecibelstoscalartransferfunction)

|  | Header |
| --- | --- |
| From | AudioHardware.h |
| To | AudioHardwareDeprecated.h |

Modified [AudioHardwareAddPropertyListener()](https://developer.apple.com/documentation/coreaudio/1580750-audiohardwareaddpropertylistener)

|  | Header |
| --- | --- |
| From | AudioHardware.h |
| To | AudioHardwareDeprecated.h |

Modified [kAudioDevicePropertyScopeOutput](https://developer.apple.com/documentation/coreaudio/kaudiodevicepropertyscopeoutput)

|  | Header |
| --- | --- |
| From | AudioHardware.h |
| To | AudioHardwareDeprecated.h |

Modified [kAudioStreamPropertyPhysicalFormatMatch](https://developer.apple.com/documentation/coreaudio/kaudiostreampropertyphysicalformatmatch)

|  | Header |
| --- | --- |
| From | AudioHardware.h |
| To | AudioHardwareDeprecated.h |

Modified [kAudioDevicePropertyChannelCategoryNameCFString](https://developer.apple.com/documentation/coreaudio/1580731-anonymous/kaudiodevicepropertychannelcategorynamecfstring)

|  | Header |
| --- | --- |
| From | AudioHardware.h |
| To | AudioHardwareDeprecated.h |

Modified [kAudioLevelControlTranferFunction10Over1](https://developer.apple.com/documentation/coreaudio/audiolevelcontroltransferfunction/tranferfunction10over1)

|  | Header |
| --- | --- |
| From | AudioHardware.h |
| To | AudioHardwareDeprecated.h |

Modified [AudioDeviceID](https://developer.apple.com/documentation/coreaudio/audiodeviceid)

|  | Header |
| --- | --- |
| From | AudioHardware.h |
| To | AudioHardwareDeprecated.h |

Modified [kAudioHardwarePropertyBootChimeVolumeDecibels](https://developer.apple.com/documentation/coreaudio/1580738-anonymous/kaudiohardwarepropertybootchimevolumedecibels)

|  | Header |
| --- | --- |
| From | AudioHardware.h |
| To | AudioHardwareDeprecated.h |

Modified [AudioDevicePropertyListenerProc](https://developer.apple.com/documentation/coreaudio/audiodevicepropertylistenerproc)

|  | Header |
| --- | --- |
| From | AudioHardware.h |
| To | AudioHardwareDeprecated.h |

Modified [kAudioDevicePropertyRegisterBufferList](https://developer.apple.com/documentation/coreaudio/1580731-anonymous/kaudiodevicepropertyregisterbufferlist)

|  | Header |
| --- | --- |
| From | AudioHardware.h |
| To | AudioHardwareDeprecated.h |

Modified [kAudioStreamPropertyPhysicalFormats](https://developer.apple.com/documentation/coreaudio/kaudiostreampropertyphysicalformats)

|  | Header |
| --- | --- |
| From | AudioHardware.h |
| To | AudioHardwareDeprecated.h |

Modified [kAudioDevicePropertySubVolumeDecibelsToScalarTransferFunction](https://developer.apple.com/documentation/coreaudio/kaudiodevicepropertysubvolumedecibelstoscalartransferfunction)

|  | Header |
| --- | --- |
| From | AudioHardware.h |
| To | AudioHardwareDeprecated.h |

Modified [AudioStreamPropertyListenerProc](https://developer.apple.com/documentation/coreaudio/audiostreampropertylistenerproc)

|  | Header |
| --- | --- |
| From | AudioHardware.h |
| To | AudioHardwareDeprecated.h |

Modified [AudioStreamGetProperty()](https://developer.apple.com/documentation/coreaudio/1580743-audiostreamgetproperty)

|  | Header |
| --- | --- |
| From | AudioHardware.h |
| To | AudioHardwareDeprecated.h |

Modified [kAudioLevelControlTranferFunction1Over3](https://developer.apple.com/documentation/coreaudio/audiolevelcontroltransferfunction/tranferfunction1over3)

|  | Header |
| --- | --- |
| From | AudioHardware.h |
| To | AudioHardwareDeprecated.h |

Modified [kAudioDevicePropertyDriverShouldOwniSub](https://developer.apple.com/documentation/coreaudio/kaudiodevicepropertydrivershouldownisub)

|  | Header |
| --- | --- |
| From | AudioHardware.h |
| To | AudioHardwareDeprecated.h |

AudioHardwarePlugIn.hModified [AudioObjectsPublishedAndDied()](https://developer.apple.com/documentation/coreaudio/1585908-audioobjectspublishedanddied)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.8 |

Modified [AudioObjectPropertiesChanged()](https://developer.apple.com/documentation/coreaudio/1585917-audioobjectpropertieschanged)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.8 |

Modified [AudioObjectCreate()](https://developer.apple.com/documentation/coreaudio/1585905-audioobjectcreate)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.8 |

AudioServerPlugIn.hAdded AudioServerPlugInDriverInterface::Boolean() (no architecture available)Added AudioServerPlugInDriverInterface::HRESULT() (no architecture available)Added AudioServerPlugInDriverInterface::OSStatus() (no architecture available)Added AudioServerPlugInDriverInterface::ULONG() (no architecture available)Added [AudioServerPlugInClientInfo](https://developer.apple.com/documentation/coreaudio/audioserverpluginclientinfo)Added [AudioServerPlugInCustomPropertyInfo](https://developer.apple.com/documentation/coreaudio/audioserverplugincustompropertyinfo)Added [AudioServerPlugInDriverInterface](https://developer.apple.com/documentation/coreaudio/audioserverplugindriverinterface)Added [AudioServerPlugInDriverRef](https://developer.apple.com/documentation/coreaudio/audioserverplugindriverref)Added [AudioServerPlugInHostInterface](https://developer.apple.com/documentation/coreaudio/audioserverpluginhostinterface)Added [AudioServerPlugInHostRef](https://developer.apple.com/documentation/coreaudio/audioserverpluginhostref)Added [AudioServerPlugInIOCycleInfo](https://developer.apple.com/documentation/coreaudio/audioserverpluginiocycleinfo)Added [kAudioDeviceClockAlgorithmRaw](https://developer.apple.com/documentation/coreaudio/audiodeviceclockalgorithmselector/kaudiodeviceclockalgorithmraw)Added [kAudioDeviceClockAlgorithmSimpleIIR](https://developer.apple.com/documentation/coreaudio/audiodeviceclockalgorithmselector/kaudiodeviceclockalgorithmsimpleiir)Added kAudioDeviceClockAlgorithmUnclockedAdded [kAudioDevicePropertyClockAlgorithm](https://developer.apple.com/documentation/coreaudio/1583996-anonymous/kaudiodevicepropertyclockalgorithm)Added [kAudioDevicePropertyZeroTimeStampPeriod](https://developer.apple.com/documentation/coreaudio/1583996-anonymous/kaudiodevicepropertyzerotimestampperiod)Added [kAudioObjectPlugInObject](https://developer.apple.com/documentation/coreaudio/1584034-anonymous/kaudioobjectpluginobject)Added [kAudioObjectPropertyCustomPropertyInfoList](https://developer.apple.com/documentation/coreaudio/1583991-anonymous/kaudioobjectpropertycustompropertyinfolist)Added [kAudioPlugInPropertyResourceBundle](https://developer.apple.com/documentation/coreaudio/1583990-anonymous/kaudiopluginpropertyresourcebundle)Added [kAudioServerPlugInCustomPropertyDataTypeCFPropertyList](https://developer.apple.com/documentation/coreaudio/1584023-anonymous/kaudioserverplugincustompropertydatatypecfpropertylist)Added [kAudioServerPlugInCustomPropertyDataTypeCFString](https://developer.apple.com/documentation/coreaudio/1584023-anonymous/kaudioserverplugincustompropertydatatypecfstring)Added [kAudioServerPlugInCustomPropertyDataTypeNone](https://developer.apple.com/documentation/coreaudio/1584023-anonymous/kaudioserverplugincustompropertydatatypenone)Added #def kAudioServerPlugInDriverInterfaceUUIDAdded [kAudioServerPlugInHostClientID](https://developer.apple.com/documentation/coreaudio/1583975-anonymous/kaudioserverpluginhostclientid)Added [kAudioServerPlugInIOOperationConvertInput](https://developer.apple.com/documentation/coreaudio/audioserverpluginiooperation/kaudioserverpluginiooperationconvertinput)Added [kAudioServerPlugInIOOperationConvertMix](https://developer.apple.com/documentation/coreaudio/audioserverpluginiooperation/kaudioserverpluginiooperationconvertmix)Added [kAudioServerPlugInIOOperationCycle](https://developer.apple.com/documentation/coreaudio/audioserverpluginiooperation/kaudioserverpluginiooperationcycle)Added [kAudioServerPlugInIOOperationMixOutput](https://developer.apple.com/documentation/coreaudio/audioserverpluginiooperation/kaudioserverpluginiooperationmixoutput)Added [kAudioServerPlugInIOOperationProcessInput](https://developer.apple.com/documentation/coreaudio/audioserverpluginiooperation/kaudioserverpluginiooperationprocessinput)Added [kAudioServerPlugInIOOperationProcessMix](https://developer.apple.com/documentation/coreaudio/audioserverpluginiooperation/kaudioserverpluginiooperationprocessmix)Added [kAudioServerPlugInIOOperationProcessOutput](https://developer.apple.com/documentation/coreaudio/audioserverpluginiooperation/kaudioserverpluginiooperationprocessoutput)Added [kAudioServerPlugInIOOperationReadInput](https://developer.apple.com/documentation/coreaudio/audioserverpluginiooperation/kaudioserverpluginiooperationreadinput)Added [kAudioServerPlugInIOOperationThread](https://developer.apple.com/documentation/coreaudio/audioserverpluginiooperation/kaudioserverpluginiooperationthread)Added [kAudioServerPlugInIOOperationWriteMix](https://developer.apple.com/documentation/coreaudio/audioserverpluginiooperation/kaudioserverpluginiooperationwritemix)Added #def kAudioServerPlugInTypeUUIDCoreAudioTypes.hAdded AudioBufferList::AudioBufferList() (no architecture available)Added AudioChannelLayout::AudioChannelLayout() (no architecture available)Added [kAudioChannelLayoutTag_AAC_7_1_B](https://developer.apple.com/documentation/coreaudio/kaudiochannellayouttag_aac_7_1_b)Added [kAudioFormatMPEG4AAC_ELD_V2](https://developer.apple.com/documentation/coreaudio/kaudioformatmpeg4aac_eld_v2)

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
