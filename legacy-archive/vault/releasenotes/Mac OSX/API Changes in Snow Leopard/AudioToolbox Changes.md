---
title: API Changes in Snow Leopard
apple_id: TP40007673
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2008-06-09'
source_url: https://developer.apple.com/library/archive/releasenotes/MacOSX/SnowLeopard_API_ReleaseNote/AudioToolbox.html
archived_at: '2026-07-18T02:58:42.050528Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [API Changes in Snow Leopard](API%20Changes%20in%20Snow%20Leopard.md)


[ADC Home](https://developer.apple.com/) >
[Reference Library](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30000943) >
Release Notes >
OS X >
[API Changes in Snow Leopard Developer Preview](API%20Changes%20in%20Snow%20Leopard.md) >

# AudioToolbox Changes

## AudioToolbox

AUGraph.hModified [AUGraphSetRenderNotification()](https://developer.apple.com/documentation/audiotoolbox/audio_unit_processing_graph_services/1805624-augraphsetrendernotification)

|  | Deprecation |
| --- | --- |
| Old | 10.3 |
| New |  |

Modified [AUGraphNewNode()](https://developer.apple.com/documentation/audiotoolbox/1537621-augraphnewnode)

|  | Deprecation | Declaration |
| --- | --- | --- |
| Old | 10.5 | OSStatus AUGraphNewNode ( AUGraph inGraph, const ComponentDescription \*inDescription, UInt32 inClassDataSize, const void \*inClassData, AUNode \*outNode); |
| New |  | OSStatus AUGraphNewNode ( AUGraph inGraph, const struct ComponentDescription \*inDescription, UInt32 inClassDataSize, const void \*inClassData, AUNode \*outNode); |

Modified [AUGraphRemoveRenderNotification()](https://developer.apple.com/documentation/audiotoolbox/audio_unit_processing_graph_services/1805618-augraphremoverendernotification)

|  | Deprecation |
| --- | --- |
| Old | 10.3 |
| New |  |

Modified [AUGraphNodeInfo()](https://developer.apple.com/documentation/audiotoolbox/1502407-augraphnodeinfo)

|  | Declaration |
| --- | --- |
| Old | OSStatus AUGraphNodeInfo ( AUGraph inGraph, AUNode inNode, ComponentDescription \*outDescription, AudioUnit \*outAudioUnit); |
| New | OSStatus AUGraphNodeInfo ( AUGraph inGraph, AUNode inNode, AudioComponentDescription \*outDescription, AudioUnit \*outAudioUnit); |

Modified [AUGraphGetConnectionInfo()](https://developer.apple.com/documentation/audiotoolbox/1537629-augraphgetconnectioninfo)

|  | Deprecation |
| --- | --- |
| Old | 10.5 |
| New |  |

Modified [AUGraphAddNode()](https://developer.apple.com/documentation/audiotoolbox/1501671-augraphaddnode)

|  | Declaration |
| --- | --- |
| Old | OSStatus AUGraphAddNode ( AUGraph inGraph, const ComponentDescription \*inDescription, AUNode \*outNode); |
| New | OSStatus AUGraphAddNode ( AUGraph inGraph, const AudioComponentDescription \*inDescription, AUNode \*outNode); |

Modified [AUGraphGetNodeConnections()](https://developer.apple.com/documentation/audiotoolbox/1537626-augraphgetnodeconnections)

|  | Deprecation |
| --- | --- |
| Old | 10.5 |
| New |  |

Modified [AUGraphGetNumberOfConnections()](https://developer.apple.com/documentation/audiotoolbox/1537617-augraphgetnumberofconnections)

|  | Deprecation |
| --- | --- |
| Old | 10.5 |
| New |  |

Modified [AUGraphCountNodeConnections()](https://developer.apple.com/documentation/audiotoolbox/1537634-augraphcountnodeconnections)

|  | Deprecation |
| --- | --- |
| Old | 10.5 |
| New |  |

Modified [AUGraphGetNodeInfo()](https://developer.apple.com/documentation/audiotoolbox/1537614-augraphgetnodeinfo)

|  | Deprecation | Declaration |
| --- | --- | --- |
| Old | 10.5 | OSStatus AUGraphGetNodeInfo ( AUGraph inGraph, AUNode inNode, ComponentDescription \*outDescription, UInt32 \*outClassDataSize, void \*\*outClassData, AudioUnit \*outAudioUnit); |
| New |  | OSStatus AUGraphGetNodeInfo ( AUGraph inGraph, AUNode inNode, struct ComponentDescription \*outDescription, UInt32 \*outClassDataSize, void \*\*outClassData, AudioUnit \*outAudioUnit); |

AUMIDIController.hModified AUMIDIControllerMapChannelToAU()

|  | Deprecation |
| --- | --- |
| Old | 10.5 |
| New |  |

Modified AUMIDIControllerExportXMLNames()

|  | Deprecation |
| --- | --- |
| Old | 10.5 |
| New |  |

Modified AUMIDIControllerHandleMIDI()

|  | Deprecation |
| --- | --- |
| Old | 10.5 |
| New |  |

Modified AUMIDIControllerCreate()

|  | Deprecation |
| --- | --- |
| Old | 10.5 |
| New |  |

Modified AUMIDIControllerUnmapAudioUnit()

|  | Deprecation |
| --- | --- |
| Old | 10.5 |
| New |  |

Modified AUMIDIControllerConnectSource()

|  | Deprecation |
| --- | --- |
| Old | 10.5 |
| New |  |

Modified AUMIDIControllerMapEventToParameter()

|  | Deprecation |
| --- | --- |
| Old | 10.5 |
| New |  |

Modified AUMIDIControllerDisconnectSource()

|  | Deprecation |
| --- | --- |
| Old | 10.5 |
| New |  |

Modified AUMIDIControllerDispose()

|  | Deprecation |
| --- | --- |
| Old | 10.5 |
| New |  |

AudioConverter.hModified [AudioConverterFillBuffer()](https://developer.apple.com/documentation/audiotoolbox/1559926-audioconverterfillbuffer)

|  | Deprecation |
| --- | --- |
| Old | 10.5 |
| New |  |

AudioFile.hAdded [AudioBytePacketTranslation](https://developer.apple.com/documentation/audiotoolbox/audiobytepackettranslation)Added [kAudioFilePropertyByteToPacket](https://developer.apple.com/documentation/audiotoolbox/kaudiofilepropertybytetopacket)Added [kAudioFilePropertyPacketToByte](https://developer.apple.com/documentation/audiotoolbox/1576499-audio_file_properties/kaudiofilepropertypackettobyte)Added [kAudioFileReadPermission](https://developer.apple.com/documentation/audiotoolbox/audiofilepermissions/kaudiofilereadpermission)Added [kAudioFileReadWritePermission](https://developer.apple.com/documentation/audiotoolbox/audiofilepermissions/kaudiofilereadwritepermission)Added [kAudioFileWritePermission](https://developer.apple.com/documentation/audiotoolbox/audiofilepermissions/kaudiofilewritepermission)Added [kBytePacketTranslationFlag_IsEstimate](https://developer.apple.com/documentation/audiotoolbox/audiobytepackettranslationflags/1502170-bytepackettranslationflag_isesti)AudioFileComponent.hModified [AudioFileComponentReadBytes()](https://developer.apple.com/documentation/audiotoolbox/1404218-audiofilecomponentreadbytes)

|  | Declaration |
| --- | --- |
| Old | ComponentResult AudioFileComponentReadBytes ( AudioFileComponent inComponent, Boolean inUseCache, SInt64 inStartingByte, UInt32 \*ioNumBytes, void \*outBuffer); |
| New | OSStatus AudioFileComponentReadBytes ( AudioFileComponent inComponent, Boolean inUseCache, SInt64 inStartingByte, UInt32 \*ioNumBytes, void \*outBuffer); |

Modified [AudioFileComponentOptimize()](https://developer.apple.com/documentation/audiotoolbox/1404208-audiofilecomponentoptimize)

|  | Declaration |
| --- | --- |
| Old | ComponentResult AudioFileComponentOptimize ( AudioFileComponent inComponent); |
| New | OSStatus AudioFileComponentOptimize ( AudioFileComponent inComponent); |

Modified [AudioFileComponentExtensionIsThisFormat()](https://developer.apple.com/documentation/audiotoolbox/1404027-audiofilecomponentextensionisthi)

|  | Declaration |
| --- | --- |
| Old | ComponentResult AudioFileComponentExtensionIsThisFormat ( AudioFileComponent inComponent, CFStringRef inExtension, UInt32 \*outResult); |
| New | OSStatus AudioFileComponentExtensionIsThisFormat ( AudioFileComponent inComponent, CFStringRef inExtension, UInt32 \*outResult); |

Modified [AudioFileComponentOpenFile()](https://developer.apple.com/documentation/audiotoolbox/1404202-audiofilecomponentopenfile)

|  | Declaration |
| --- | --- |
| Old | ComponentResult AudioFileComponentOpenFile ( AudioFileComponent inComponent, const FSRef \*inFileRef, SInt8 inPermissions, SInt16 inRefNum); |
| New | OSStatus AudioFileComponentOpenFile ( AudioFileComponent inComponent, const struct FSRef \*inFileRef, SInt8 inPermissions, SInt16 inRefNum); |

Modified [AudioFileComponentGetUserData()](https://developer.apple.com/documentation/audiotoolbox/1404098-audiofilecomponentgetuserdata)

|  | Declaration |
| --- | --- |
| Old | ComponentResult AudioFileComponentGetUserData ( AudioFileComponent inComponent, UInt32 inUserDataID, UInt32 inIndex, UInt32 \*ioUserDataSize, void \*outUserData); |
| New | OSStatus AudioFileComponentGetUserData ( AudioFileComponent inComponent, UInt32 inUserDataID, UInt32 inIndex, UInt32 \*ioUserDataSize, void \*outUserData); |

Modified [AudioFileComponentSetUserData()](https://developer.apple.com/documentation/audiotoolbox/1403993-audiofilecomponentsetuserdata)

|  | Declaration |
| --- | --- |
| Old | ComponentResult AudioFileComponentSetUserData ( AudioFileComponent inComponent, UInt32 inUserDataID, UInt32 inIndex, UInt32 inUserDataSize, const void \*inUserData); |
| New | OSStatus AudioFileComponentSetUserData ( AudioFileComponent inComponent, UInt32 inUserDataID, UInt32 inIndex, UInt32 inUserDataSize, const void \*inUserData); |

Modified [AudioFileComponentCloseFile()](https://developer.apple.com/documentation/audiotoolbox/1404159-audiofilecomponentclosefile)

|  | Declaration |
| --- | --- |
| Old | ComponentResult AudioFileComponentCloseFile ( AudioFileComponent inComponent); |
| New | OSStatus AudioFileComponentCloseFile ( AudioFileComponent inComponent); |

Modified [AudioFileComponentGetGlobalInfo()](https://developer.apple.com/documentation/audiotoolbox/1404156-audiofilecomponentgetglobalinfo)

|  | Declaration |
| --- | --- |
| Old | ComponentResult AudioFileComponentGetGlobalInfo ( AudioFileComponent inComponent, AudioFileComponentPropertyID inPropertyID, UInt32 inSpecifierSize, const void \*inSpecifier, UInt32 \*ioPropertyDataSize, void \*outPropertyData); |
| New | OSStatus AudioFileComponentGetGlobalInfo ( AudioFileComponent inComponent, AudioFileComponentPropertyID inPropertyID, UInt32 inSpecifierSize, const void \*inSpecifier, UInt32 \*ioPropertyDataSize, void \*outPropertyData); |

Modified [AudioFileComponentInitialize()](https://developer.apple.com/documentation/audiotoolbox/1404190-audiofilecomponentinitialize)

|  | Declaration |
| --- | --- |
| Old | ComponentResult AudioFileComponentInitialize ( AudioFileComponent inComponent, const FSRef \*inFileRef, const AudioStreamBasicDescription \*inFormat, UInt32 inFlags); |
| New | OSStatus AudioFileComponentInitialize ( AudioFileComponent inComponent, const struct FSRef \*inFileRef, const AudioStreamBasicDescription \*inFormat, UInt32 inFlags); |

Modified [AudioFileComponentGetUserDataSize()](https://developer.apple.com/documentation/audiotoolbox/1404146-audiofilecomponentgetuserdatasiz)

|  | Declaration |
| --- | --- |
| Old | ComponentResult AudioFileComponentGetUserDataSize ( AudioFileComponent inComponent, UInt32 inUserDataID, UInt32 inIndex, UInt32 \*outUserDataSize); |
| New | OSStatus AudioFileComponentGetUserDataSize ( AudioFileComponent inComponent, UInt32 inUserDataID, UInt32 inIndex, UInt32 \*outUserDataSize); |

Modified [AudioFileComponentInitializeWithCallbacks()](https://developer.apple.com/documentation/audiotoolbox/1404152-audiofilecomponentinitializewith)

|  | Declaration |
| --- | --- |
| Old | ComponentResult AudioFileComponentInitializeWithCallbacks ( AudioFileComponent inComponent, void \*inClientData, AudioFile_ReadProc inReadFunc, AudioFile_WriteProc inWriteFunc, AudioFile_GetSizeProc inGetSizeFunc, AudioFile_SetSizeProc inSetSizeFunc, UInt32 inFileType, const AudioStreamBasicDescription \*inFormat, UInt32 inFlags); |
| New | OSStatus AudioFileComponentInitializeWithCallbacks ( AudioFileComponent inComponent, void \*inClientData, AudioFile_ReadProc inReadFunc, AudioFile_WriteProc inWriteFunc, AudioFile_GetSizeProc inGetSizeFunc, AudioFile_SetSizeProc inSetSizeFunc, UInt32 inFileType, const AudioStreamBasicDescription \*inFormat, UInt32 inFlags); |

Modified [AudioFileComponentRemoveUserData()](https://developer.apple.com/documentation/audiotoolbox/1404142-audiofilecomponentremoveuserdata)

|  | Declaration |
| --- | --- |
| Old | ComponentResult AudioFileComponentRemoveUserData ( AudioFileComponent inComponent, UInt32 inUserDataID, UInt32 inIndex); |
| New | OSStatus AudioFileComponentRemoveUserData ( AudioFileComponent inComponent, UInt32 inUserDataID, UInt32 inIndex); |

Modified [AudioFileComponentGetGlobalInfoSize()](https://developer.apple.com/documentation/audiotoolbox/1404136-audiofilecomponentgetglobalinfos)

|  | Declaration |
| --- | --- |
| Old | ComponentResult AudioFileComponentGetGlobalInfoSize ( AudioFileComponent inComponent, AudioFileComponentPropertyID inPropertyID, UInt32 inSpecifierSize, const void \*inSpecifier, UInt32 \*outPropertySize); |
| New | OSStatus AudioFileComponentGetGlobalInfoSize ( AudioFileComponent inComponent, AudioFileComponentPropertyID inPropertyID, UInt32 inSpecifierSize, const void \*inSpecifier, UInt32 \*outPropertySize); |

Modified [AudioFileComponentCountUserData()](https://developer.apple.com/documentation/audiotoolbox/1404167-audiofilecomponentcountuserdata)

|  | Declaration |
| --- | --- |
| Old | ComponentResult AudioFileComponentCountUserData ( AudioFileComponent inComponent, UInt32 inUserDataID, UInt32 \*outNumberItems); |
| New | OSStatus AudioFileComponentCountUserData ( AudioFileComponent inComponent, UInt32 inUserDataID, UInt32 \*outNumberItems); |

Modified [AudioFileComponentSetProperty()](https://developer.apple.com/documentation/audiotoolbox/1404188-audiofilecomponentsetproperty)

|  | Declaration |
| --- | --- |
| Old | ComponentResult AudioFileComponentSetProperty ( AudioFileComponent inComponent, AudioFileComponentPropertyID inPropertyID, UInt32 inPropertyDataSize, const void \*inPropertyData); |
| New | OSStatus AudioFileComponentSetProperty ( AudioFileComponent inComponent, AudioFileComponentPropertyID inPropertyID, UInt32 inPropertyDataSize, const void \*inPropertyData); |

Modified [AudioFileComponentOpenWithCallbacks()](https://developer.apple.com/documentation/audiotoolbox/1404114-audiofilecomponentopenwithcallba)

|  | Declaration |
| --- | --- |
| Old | ComponentResult AudioFileComponentOpenWithCallbacks ( AudioFileComponent inComponent, void \*inClientData, AudioFile_ReadProc inReadFunc, AudioFile_WriteProc inWriteFunc, AudioFile_GetSizeProc inGetSizeFunc, AudioFile_SetSizeProc inSetSizeFunc); |
| New | OSStatus AudioFileComponentOpenWithCallbacks ( AudioFileComponent inComponent, void \*inClientData, AudioFile_ReadProc inReadFunc, AudioFile_WriteProc inWriteFunc, AudioFile_GetSizeProc inGetSizeFunc, AudioFile_SetSizeProc inSetSizeFunc); |

Modified [AudioFileComponentGetProperty()](https://developer.apple.com/documentation/audiotoolbox/1403983-audiofilecomponentgetproperty)

|  | Declaration |
| --- | --- |
| Old | ComponentResult AudioFileComponentGetProperty ( AudioFileComponent inComponent, AudioFileComponentPropertyID inPropertyID, UInt32 \*ioPropertyDataSize, void \*outPropertyData); |
| New | OSStatus AudioFileComponentGetProperty ( AudioFileComponent inComponent, AudioFileComponentPropertyID inPropertyID, UInt32 \*ioPropertyDataSize, void \*outPropertyData); |

Modified [AudioFileComponentFileDataIsThisFormat()](https://developer.apple.com/documentation/audiotoolbox/1404210-audiofilecomponentfiledataisthis)

|  | Declaration |
| --- | --- |
| Old | ComponentResult AudioFileComponentFileDataIsThisFormat ( AudioFileComponent inComponent, UInt32 inDataByteSize, const void \*inData, UInt32 \*outResult); |
| New | OSStatus AudioFileComponentFileDataIsThisFormat ( AudioFileComponent inComponent, UInt32 inDataByteSize, const void \*inData, UInt32 \*outResult); |

Modified [AudioFileComponentWritePackets()](https://developer.apple.com/documentation/audiotoolbox/1403969-audiofilecomponentwritepackets)

|  | Declaration |
| --- | --- |
| Old | ComponentResult AudioFileComponentWritePackets ( AudioFileComponent inComponent, Boolean inUseCache, UInt32 inNumBytes, const AudioStreamPacketDescription \*inPacketDescriptions, SInt64 inStartingPacket, UInt32 \*ioNumPackets, const void \*inBuffer); |
| New | OSStatus AudioFileComponentWritePackets ( AudioFileComponent inComponent, Boolean inUseCache, UInt32 inNumBytes, const AudioStreamPacketDescription \*inPacketDescriptions, SInt64 inStartingPacket, UInt32 \*ioNumPackets, const void \*inBuffer); |

Modified [AudioFileComponentDataIsThisFormat()](https://developer.apple.com/documentation/audiotoolbox/1404183-audiofilecomponentdataisthisform)

|  | Deprecation | Declaration |
| --- | --- | --- |
| Old | 10.5 | ComponentResult AudioFileComponentDataIsThisFormat ( AudioFileComponent inComponent, void \*inClientData, AudioFile_ReadProc inReadFunc, AudioFile_WriteProc inWriteFunc, AudioFile_GetSizeProc inGetSizeFunc, AudioFile_SetSizeProc inSetSizeFunc, UInt32 \*outResult); |
| New |  | OSStatus AudioFileComponentDataIsThisFormat ( AudioFileComponent inComponent, void \*inClientData, AudioFile_ReadProc inReadFunc, AudioFile_WriteProc inWriteFunc, AudioFile_GetSizeProc inGetSizeFunc, AudioFile_SetSizeProc inSetSizeFunc, UInt32 \*outResult); |

Modified [AudioFileComponentGetPropertyInfo()](https://developer.apple.com/documentation/audiotoolbox/1404104-audiofilecomponentgetpropertyinf)

|  | Declaration |
| --- | --- |
| Old | ComponentResult AudioFileComponentGetPropertyInfo ( AudioFileComponent inComponent, AudioFileComponentPropertyID inPropertyID, UInt32 \*outPropertySize, UInt32 \*outWritable); |
| New | OSStatus AudioFileComponentGetPropertyInfo ( AudioFileComponent inComponent, AudioFileComponentPropertyID inPropertyID, UInt32 \*outPropertySize, UInt32 \*outWritable); |

Modified [AudioFileComponentFileIsThisFormat()](https://developer.apple.com/documentation/audiotoolbox/1404008-audiofilecomponentfileisthisform)

|  | Deprecation | Declaration |
| --- | --- | --- |
| Old | 10.5 | ComponentResult AudioFileComponentFileIsThisFormat ( AudioFileComponent inComponent, SInt16 inFileRefNum, UInt32 \*outResult); |
| New |  | OSStatus AudioFileComponentFileIsThisFormat ( AudioFileComponent inComponent, SInt16 inFileRefNum, UInt32 \*outResult); |

Modified [AudioFileComponentReadPackets()](https://developer.apple.com/documentation/audiotoolbox/1404067-audiofilecomponentreadpackets)

|  | Declaration |
| --- | --- |
| Old | ComponentResult AudioFileComponentReadPackets ( AudioFileComponent inComponent, Boolean inUseCache, UInt32 \*outNumBytes, AudioStreamPacketDescription \*outPacketDescriptions, SInt64 inStartingPacket, UInt32 \*ioNumPackets, void \*outBuffer); |
| New | OSStatus AudioFileComponentReadPackets ( AudioFileComponent inComponent, Boolean inUseCache, UInt32 \*outNumBytes, AudioStreamPacketDescription \*outPacketDescriptions, SInt64 inStartingPacket, UInt32 \*ioNumPackets, void \*outBuffer); |

Modified [AudioFileComponentCreate()](https://developer.apple.com/documentation/audiotoolbox/1404179-audiofilecomponentcreate)

|  | Declaration |
| --- | --- |
| Old | ComponentResult AudioFileComponentCreate ( AudioFileComponent inComponent, const FSRef \*inParentRef, CFStringRef inFileName, const AudioStreamBasicDescription \*inFormat, UInt32 inFlags, FSRef \*outNewFileRef); |
| New | OSStatus AudioFileComponentCreate ( AudioFileComponent inComponent, const struct FSRef \*inParentRef, CFStringRef inFileName, const AudioStreamBasicDescription \*inFormat, UInt32 inFlags, struct FSRef \*outNewFileRef); |

Modified [AudioFileComponentWriteBytes()](https://developer.apple.com/documentation/audiotoolbox/1404118-audiofilecomponentwritebytes)

|  | Declaration |
| --- | --- |
| Old | ComponentResult AudioFileComponentWriteBytes ( AudioFileComponent inComponent, Boolean inUseCache, SInt64 inStartingByte, UInt32 \*ioNumBytes, const void \*inBuffer); |
| New | OSStatus AudioFileComponentWriteBytes ( AudioFileComponent inComponent, Boolean inUseCache, SInt64 inStartingByte, UInt32 \*ioNumBytes, const void \*inBuffer); |

AudioFileStream.hAdded [kAudioFileStreamProperty_AverageBytesPerPacket](https://developer.apple.com/documentation/audiotoolbox/kaudiofilestreamproperty_averagebytesperpacket)Added [kAudioFileStreamProperty_ByteToPacket](https://developer.apple.com/documentation/audiotoolbox/1391506-audio_file_stream_properties/kaudiofilestreamproperty_bytetopacket)Added [kAudioFileStreamProperty_PacketToByte](https://developer.apple.com/documentation/audiotoolbox/kaudiofilestreamproperty_packettobyte)AudioQueue.hAdded AudioQueueBuffer::AudioQueueBuffer()Added [AudioQueueAllocateBufferWithPacketDescriptions()](https://developer.apple.com/documentation/audiotoolbox/1502389-audioqueueallocatebufferwithpack)Added [kAudioQueueErr_InvalidPropertyValue](https://developer.apple.com/documentation/audiotoolbox/1552627-anonymous/kaudioqueueerr_invalidpropertyvalue)Added [kAudioQueueErr_Permissions](https://developer.apple.com/documentation/audiotoolbox/1552627-anonymous/kaudioqueueerr_permissions)Added [kAudioQueueProperty_DecodeBufferSizeFrames](https://developer.apple.com/documentation/audiotoolbox/1552629-anonymous/kaudioqueueproperty_decodebuffersizeframes)Added [kAudioQueueProperty_MaximumOutputPacketSize](https://developer.apple.com/documentation/audiotoolbox/kaudioqueueproperty_maximumoutputpacketsize)Added [kAudioQueueProperty_StreamDescription](https://developer.apple.com/documentation/audiotoolbox/kaudioqueueproperty_streamdescription)AudioServices.hAdded [AudioSessionInterruptionListener](https://developer.apple.com/documentation/audiotoolbox/audiosessioninterruptionlistener) (no architecture available)Added [AudioSessionPropertyID](https://developer.apple.com/documentation/audiotoolbox/audiosessionpropertyid) (no architecture available)Added [AudioSessionPropertyListener](https://developer.apple.com/documentation/audiotoolbox/audiosessionpropertylistener) (no architecture available)Added [kAudioSessionAlreadyInitialized](https://developer.apple.com/documentation/audiotoolbox/kaudiosessionalreadyinitialized) (no architecture available)Added [kAudioSessionBadPropertySizeError](https://developer.apple.com/documentation/audiotoolbox/kaudiosessionbadpropertysizeerror) (no architecture available)Added [kAudioSessionBeginInterruption](https://developer.apple.com/documentation/audiotoolbox/kaudiosessionbegininterruption) (no architecture available)Added [kAudioSessionCategory_AmbientSound](https://developer.apple.com/documentation/audiotoolbox/kaudiosessioncategory_ambientsound) (no architecture available)Added [kAudioSessionCategory_LiveAudio](https://developer.apple.com/documentation/audiotoolbox/1618459-deprecated_audio_session_categor/kaudiosessioncategory_liveaudio) (no architecture available)Added [kAudioSessionCategory_MediaPlayback](https://developer.apple.com/documentation/audiotoolbox/1618427-audio_session_categories/kaudiosessioncategory_mediaplayback) (no architecture available)Added [kAudioSessionCategory_PlayAndRecord](https://developer.apple.com/documentation/audiotoolbox/kaudiosessioncategory_playandrecord) (no architecture available)Added [kAudioSessionCategory_RecordAudio](https://developer.apple.com/documentation/audiotoolbox/kaudiosessioncategory_recordaudio) (no architecture available)Added [kAudioSessionCategory_UserInterfaceSoundEffects](https://developer.apple.com/documentation/audiotoolbox/kaudiosessioncategory_userinterfacesoundeffects) (no architecture available)Added [kAudioSessionEndInterruption](https://developer.apple.com/documentation/audiotoolbox/kaudiosessionendinterruption) (no architecture available)Added [kAudioSessionInitializationError](https://developer.apple.com/documentation/audiotoolbox/1618373-anonymous/kaudiosessioninitializationerror) (no architecture available)Added [kAudioSessionNoError](https://developer.apple.com/documentation/audiotoolbox/1618373-anonymous/kaudiosessionnoerror) (no architecture available)Added [kAudioSessionNotInitialized](https://developer.apple.com/documentation/audiotoolbox/1618373-anonymous/kaudiosessionnotinitialized) (no architecture available)Added [kAudioSessionProperty_AudioCategory](https://developer.apple.com/documentation/audiotoolbox/kaudiosessionproperty_audiocategory) (no architecture available)Added [kAudioSessionProperty_AudioRoute](https://developer.apple.com/documentation/audiotoolbox/kaudiosessionproperty_audioroute) (no architecture available)Added [kAudioSessionProperty_AudioRouteChange](https://developer.apple.com/documentation/audiotoolbox/kaudiosessionproperty_audioroutechange) (no architecture available)Added [kAudioSessionProperty_PreferredHardwareIOBufferDuration](https://developer.apple.com/documentation/audiotoolbox/1618455-audio_session_property_identifie/kaudiosessionproperty_preferredhardwareiobufferduration) (no architecture available)Added [kAudioSessionProperty_PreferredHardwareSampleRate](https://developer.apple.com/documentation/audiotoolbox/kaudiosessionproperty_preferredhardwaresamplerate) (no architecture available)Added kAudioSessionRouteChangeReason_BroadcastUpdate (no architecture available)Added [kAudioSessionRouteChangeReason_NewDeviceAvailable](https://developer.apple.com/documentation/audiotoolbox/1618380-audio_route_change_reasons/kaudiosessionroutechangereason_newdeviceavailable) (no architecture available)Added [kAudioSessionRouteChangeReason_OldDeviceUnavailable](https://developer.apple.com/documentation/audiotoolbox/1618380-audio_route_change_reasons/kaudiosessionroutechangereason_olddeviceunavailable) (no architecture available)Added [kAudioSessionRouteChangeReason_Override](https://developer.apple.com/documentation/audiotoolbox/1618380-audio_route_change_reasons/kaudiosessionroutechangereason_override) (no architecture available)Added kAudioSessionRouteChangeReason_PolicyChange (no architecture available)Added [kAudioSessionRouteChangeReason_Unknown](https://developer.apple.com/documentation/audiotoolbox/kaudiosessionroutechangereason_unknown) (no architecture available)Added [kAudioSessionRouteChangeReason_WakeFromSleep](https://developer.apple.com/documentation/audiotoolbox/kaudiosessionroutechangereason_wakefromsleep) (no architecture available)Added [kAudioSessionUnsupportedPropertyError](https://developer.apple.com/documentation/audiotoolbox/kaudiosessionunsupportedpropertyerror) (no architecture available)Added [kSystemSoundID_FlashScreen](https://developer.apple.com/documentation/audiotoolbox/ksystemsoundid_flashscreen)Added [kSystemSoundID_UserPreferredAlert](https://developer.apple.com/documentation/audiotoolbox/1405222-anonymous/ksystemsoundid_userpreferredalert)Added [kSystemSoundID_Vibrate](https://developer.apple.com/documentation/audiotoolbox/1618202-alert_sound_identifiers/ksystemsoundid_vibrate) (no architecture available)AudioToolbox.hAdded [#def AUDIO_TOOLBOX_VERSION](https://developer.apple.com/documentation/audiotoolbox/audio_toolbox_version)Modified [GetNameFromSoundBank()](https://developer.apple.com/documentation/audiotoolbox/1475999-getnamefromsoundbank)

|  | Deprecation |
| --- | --- |
| Old | 10.5 |
| New |  |

DefaultAudioOutput.hModified OpenSystemSoundAudioOutput()

|  | Deprecation |
| --- | --- |
| Old | 10.3 |
| New |  |

Modified OpenDefaultAudioOutput()

|  | Deprecation |
| --- | --- |
| Old | 10.3 |
| New |  |

ExtendedAudioFile.hModified [ExtAudioFileOpen()](https://developer.apple.com/documentation/audiotoolbox/1486836-extaudiofileopen)

|  | Declaration |
| --- | --- |
| Old | OSStatus ExtAudioFileOpen ( const FSRef \*inFSRef, ExtAudioFileRef \*outExtAudioFile); |
| New | OSStatus ExtAudioFileOpen ( const struct FSRef \*inFSRef, ExtAudioFileRef \*outExtAudioFile); |

Modified [ExtAudioFileCreateNew()](https://developer.apple.com/documentation/audiotoolbox/1486842-extaudiofilecreatenew)

|  | Declaration |
| --- | --- |
| Old | OSStatus ExtAudioFileCreateNew ( const FSRef \*inParentDir, CFStringRef inFileName, AudioFileTypeID inFileType, const AudioStreamBasicDescription \*inStreamDesc, const AudioChannelLayout \*inChannelLayout, ExtAudioFileRef \*outExtAudioFile); |
| New | OSStatus ExtAudioFileCreateNew ( const struct FSRef \*inParentDir, CFStringRef inFileName, AudioFileTypeID inFileType, const AudioStreamBasicDescription \*inStreamDesc, const AudioChannelLayout \*inChannelLayout, ExtAudioFileRef \*outExtAudioFile); |

MusicPlayer.hModified MusicSequenceSaveSMF()

|  | Deprecation | Declaration |
| --- | --- | --- |
| Old | 10.4 | OSStatus MusicSequenceSaveSMF ( MusicSequence inSequence, const FSSpec \*inFileSpec, UInt16 inResolution); |
| New |  | OSStatus MusicSequenceSaveSMF ( MusicSequence inSequence, const struct FSSpec \*inFileSpec, UInt16 inResolution); |

Modified [MusicSequenceSaveMIDIFile()](https://developer.apple.com/documentation/audiotoolbox/1515434-musicsequencesavemidifile)

|  | Deprecation | Declaration |
| --- | --- | --- |
| Old | 10.5 | OSStatus MusicSequenceSaveMIDIFile ( MusicSequence inSequence, const FSRef \*inParentDirectory, CFStringRef inFileName, UInt16 inResolution, UInt32 inFlags); |
| New |  | OSStatus MusicSequenceSaveMIDIFile ( MusicSequence inSequence, const struct FSRef \*inParentDirectory, CFStringRef inFileName, UInt16 inResolution, UInt32 inFlags); |

Modified [MusicSequenceLoadSMFWithFlags()](https://developer.apple.com/documentation/audiotoolbox/1515448-musicsequenceloadsmfwithflags)

|  | Deprecation | Declaration |
| --- | --- | --- |
| Old | 10.5 | OSStatus MusicSequenceLoadSMFWithFlags ( MusicSequence inSequence, const FSRef \*inFileRef, MusicSequenceLoadFlags inFlags); |
| New |  | OSStatus MusicSequenceLoadSMFWithFlags ( MusicSequence inSequence, const struct FSRef \*inFileRef, MusicSequenceLoadFlags inFlags); |

Modified MusicSequenceLoadSMF()

|  | Deprecation | Declaration |
| --- | --- | --- |
| Old | 10.4 | OSStatus MusicSequenceLoadSMF ( MusicSequence inSequence, const FSSpec \*inFileSpec); |
| New |  | OSStatus MusicSequenceLoadSMF ( MusicSequence inSequence, const struct FSSpec \*inFileSpec); |

Modified [MusicSequenceLoadSMFDataWithFlags()](https://developer.apple.com/documentation/audiotoolbox/1515430-musicsequenceloadsmfdatawithflag)

|  | Deprecation |
| --- | --- |
| Old | 10.5 |
| New |  |

Modified MusicSequenceLoadSMFData()

|  | Deprecation |
| --- | --- |
| Old | 10.5 |
| New |  |

Modified [MusicSequenceSaveSMFData()](https://developer.apple.com/documentation/audiotoolbox/1515490-musicsequencesavesmfdata)

|  | Deprecation |
| --- | --- |
| Old | 10.5 |
| New |  |

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
