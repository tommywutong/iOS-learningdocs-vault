---
title: OS X v10.11 API Diffs
apple_id: TP40016197
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_11/Objective-C/AudioToolbox.html
archived_at: '2026-07-18T02:52:55.328779Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.11 API Diffs](OS%20X%20v10.11%20API%20Diffs.md)


# AudioToolbox Changes for Objective-C

### AudioToolbox

#### AudioConverter.h

Added #def AudioToolbox_AudioConverter_hModified [AudioConverterConvertBuffer()](https://developer.apple.com/documentation/audiotoolbox/1503345-audioconverterconvertbuffer)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AudioConverterConvertBuffer (     AudioConverterRef inAudioConverter,     UInt32 inInputDataSize,     const void *inInputData,     UInt32 *ioOutputDataSize,     void *outOutputData ); ``` |
| To | ``` OSStatus AudioConverterConvertBuffer (     AudioConverterRef _Nonnull inAudioConverter,     UInt32 inInputDataSize,     const void * _Nonnull inInputData,     UInt32 * _Nonnull ioOutputDataSize,     void * _Nonnull outOutputData ); ``` |

Modified [AudioConverterConvertComplexBuffer()](https://developer.apple.com/documentation/audiotoolbox/1502473-audioconverterconvertcomplexbuff)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AudioConverterConvertComplexBuffer (     AudioConverterRef inAudioConverter,     UInt32 inNumberPCMFrames,     const AudioBufferList *inInputData,     AudioBufferList *outOutputData ); ``` |
| To | ``` OSStatus AudioConverterConvertComplexBuffer (     AudioConverterRef _Nonnull inAudioConverter,     UInt32 inNumberPCMFrames,     const AudioBufferList * _Nonnull inInputData,     AudioBufferList * _Nonnull outOutputData ); ``` |

Modified [AudioConverterDispose()](https://developer.apple.com/documentation/audiotoolbox/1502671-audioconverterdispose)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AudioConverterDispose (     AudioConverterRef inAudioConverter ); ``` |
| To | ``` OSStatus AudioConverterDispose (     AudioConverterRef _Nonnull inAudioConverter ); ``` |

Modified [AudioConverterFillBuffer()](https://developer.apple.com/documentation/audiotoolbox/1559926-audioconverterfillbuffer)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AudioConverterFillBuffer (     AudioConverterRef inAudioConverter,     AudioConverterInputDataProc inInputDataProc,     void *inInputDataProcUserData,     UInt32 *ioOutputDataSize,     void *outOutputData ); ``` |
| To | ``` OSStatus AudioConverterFillBuffer (     AudioConverterRef _Nonnull inAudioConverter,     AudioConverterInputDataProc _Nonnull inInputDataProc,     void * _Nullable inInputDataProcUserData,     UInt32 * _Nonnull ioOutputDataSize,     void * _Nonnull outOutputData ); ``` |

Modified [AudioConverterFillComplexBuffer()](https://developer.apple.com/documentation/audiotoolbox/1503098-audioconverterfillcomplexbuffer)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AudioConverterFillComplexBuffer (     AudioConverterRef inAudioConverter,     AudioConverterComplexInputDataProc inInputDataProc,     void *inInputDataProcUserData,     UInt32 *ioOutputDataPacketSize,     AudioBufferList *outOutputData,     AudioStreamPacketDescription *outPacketDescription ); ``` |
| To | ``` OSStatus AudioConverterFillComplexBuffer (     AudioConverterRef _Nonnull inAudioConverter,     AudioConverterComplexInputDataProc _Nonnull inInputDataProc,     void * _Nullable inInputDataProcUserData,     UInt32 * _Nonnull ioOutputDataPacketSize,     AudioBufferList * _Nonnull outOutputData,     AudioStreamPacketDescription * _Nullable outPacketDescription ); ``` |

Modified [AudioConverterGetProperty()](https://developer.apple.com/documentation/audiotoolbox/1502731-audioconvertergetproperty)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AudioConverterGetProperty (     AudioConverterRef inAudioConverter,     AudioConverterPropertyID inPropertyID,     UInt32 *ioPropertyDataSize,     void *outPropertyData ); ``` |
| To | ``` OSStatus AudioConverterGetProperty (     AudioConverterRef _Nonnull inAudioConverter,     AudioConverterPropertyID inPropertyID,     UInt32 * _Nonnull ioPropertyDataSize,     void * _Nonnull outPropertyData ); ``` |

Modified [AudioConverterGetPropertyInfo()](https://developer.apple.com/documentation/audiotoolbox/1502563-audioconvertergetpropertyinfo)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AudioConverterGetPropertyInfo (     AudioConverterRef inAudioConverter,     AudioConverterPropertyID inPropertyID,     UInt32 *outSize,     Boolean *outWritable ); ``` |
| To | ``` OSStatus AudioConverterGetPropertyInfo (     AudioConverterRef _Nonnull inAudioConverter,     AudioConverterPropertyID inPropertyID,     UInt32 * _Nullable outSize,     Boolean * _Nullable outWritable ); ``` |

Modified [AudioConverterNew()](https://developer.apple.com/documentation/audiotoolbox/1502936-audioconverternew)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AudioConverterNew (     const AudioStreamBasicDescription *inSourceFormat,     const AudioStreamBasicDescription *inDestinationFormat,     AudioConverterRef *outAudioConverter ); ``` |
| To | ``` OSStatus AudioConverterNew (     const AudioStreamBasicDescription * _Nonnull inSourceFormat,     const AudioStreamBasicDescription * _Nonnull inDestinationFormat,     AudioConverterRef  _Nullable * _Nonnull outAudioConverter ); ``` |

Modified [AudioConverterNewSpecific()](https://developer.apple.com/documentation/audiotoolbox/1503356-audioconverternewspecific)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AudioConverterNewSpecific (     const AudioStreamBasicDescription *inSourceFormat,     const AudioStreamBasicDescription *inDestinationFormat,     UInt32 inNumberClassDescriptions,     const AudioClassDescription *inClassDescriptions,     AudioConverterRef *outAudioConverter ); ``` |
| To | ``` OSStatus AudioConverterNewSpecific (     const AudioStreamBasicDescription * _Nonnull inSourceFormat,     const AudioStreamBasicDescription * _Nonnull inDestinationFormat,     UInt32 inNumberClassDescriptions,     const AudioClassDescription * _Nonnull inClassDescriptions,     AudioConverterRef  _Nullable * _Nonnull outAudioConverter ); ``` |

Modified [AudioConverterReset()](https://developer.apple.com/documentation/audiotoolbox/1503102-audioconverterreset)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AudioConverterReset (     AudioConverterRef inAudioConverter ); ``` |
| To | ``` OSStatus AudioConverterReset (     AudioConverterRef _Nonnull inAudioConverter ); ``` |

Modified [AudioConverterSetProperty()](https://developer.apple.com/documentation/audiotoolbox/1501675-audioconvertersetproperty)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AudioConverterSetProperty (     AudioConverterRef inAudioConverter,     AudioConverterPropertyID inPropertyID,     UInt32 inPropertyDataSize,     const void *inPropertyData ); ``` |
| To | ``` OSStatus AudioConverterSetProperty (     AudioConverterRef _Nonnull inAudioConverter,     AudioConverterPropertyID inPropertyID,     UInt32 inPropertyDataSize,     const void * _Nonnull inPropertyData ); ``` |

#### AudioFile.h

Removed [#def NextAudioFileRegion](https://developer.apple.com/documentation/audiotoolbox/audio_file_services/nextaudiofileregion)Removed [#def NumAudioFileMarkersToNumBytes](https://developer.apple.com/documentation/audiotoolbox/audio_file_services/numaudiofilemarkerstonumbytes)Removed [#def NumBytesToNumAudioFileMarkers](https://developer.apple.com/documentation/audiotoolbox/audio_file_services/numbytestonumaudiofilemarkers)Added [AudioBytePacketTranslationFlags](https://developer.apple.com/documentation/audiotoolbox/audiobytepackettranslationflags)Added [AudioFileFlags](https://developer.apple.com/documentation/audiotoolbox/audiofileflags)Added [AudioFilePermissions](https://developer.apple.com/documentation/audiotoolbox/audiofilepermissions)Added [AudioFileRegionFlags](https://developer.apple.com/documentation/audiotoolbox/audiofileregionflags)Added #def AudioToolbox_AudioFile_hAdded [NextAudioFileRegion()](https://developer.apple.com/documentation/audiotoolbox/1501607-nextaudiofileregion)Added [NumAudioFileMarkersToNumBytes()](https://developer.apple.com/documentation/audiotoolbox/1503350-numaudiofilemarkerstonumbytes)Added [NumBytesToNumAudioFileMarkers()](https://developer.apple.com/documentation/audiotoolbox/1502677-numbytestonumaudiofilemarkers)Modified [AudioFileClose()](https://developer.apple.com/documentation/audiotoolbox/1502041-audiofileclose)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AudioFileClose (     AudioFileID inAudioFile ); ``` |
| To | ``` OSStatus AudioFileClose (     AudioFileID _Nonnull inAudioFile ); ``` |

Modified [AudioFileCountUserData()](https://developer.apple.com/documentation/audiotoolbox/1501680-audiofilecountuserdata)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AudioFileCountUserData (     AudioFileID inAudioFile,     UInt32 inUserDataID,     UInt32 *outNumberItems ); ``` |
| To | ``` OSStatus AudioFileCountUserData (     AudioFileID _Nonnull inAudioFile,     UInt32 inUserDataID,     UInt32 * _Nonnull outNumberItems ); ``` |

Modified [AudioFileCreate()](https://developer.apple.com/documentation/audiotoolbox/1576498-audiofilecreate)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AudioFileCreate (     const struct FSRef *inParentRef,     CFStringRef inFileName,     AudioFileTypeID inFileType,     const AudioStreamBasicDescription *inFormat,     UInt32 inFlags,     struct FSRef *outNewFileRef,     AudioFileID *outAudioFile ); ``` |
| To | ``` OSStatus AudioFileCreate (     const struct FSRef * _Nonnull inParentRef,     CFStringRef _Nonnull inFileName,     AudioFileTypeID inFileType,     const AudioStreamBasicDescription * _Nonnull inFormat,     AudioFileFlags inFlags,     struct FSRef * _Nonnull outNewFileRef,     AudioFileID  _Nullable * _Nonnull outAudioFile ); ``` |

Modified [AudioFileCreateWithURL()](https://developer.apple.com/documentation/audiotoolbox/1502333-audiofilecreatewithurl)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AudioFileCreateWithURL (     CFURLRef inFileRef,     AudioFileTypeID inFileType,     const AudioStreamBasicDescription *inFormat,     UInt32 inFlags,     AudioFileID *outAudioFile ); ``` |
| To | ``` OSStatus AudioFileCreateWithURL (     CFURLRef _Nonnull inFileRef,     AudioFileTypeID inFileType,     const AudioStreamBasicDescription * _Nonnull inFormat,     AudioFileFlags inFlags,     AudioFileID  _Nullable * _Nonnull outAudioFile ); ``` |

Modified [AudioFileGetGlobalInfo()](https://developer.apple.com/documentation/audiotoolbox/1501938-audiofilegetglobalinfo)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AudioFileGetGlobalInfo (     AudioFilePropertyID inPropertyID,     UInt32 inSpecifierSize,     void *inSpecifier,     UInt32 *ioDataSize,     void *outPropertyData ); ``` |
| To | ``` OSStatus AudioFileGetGlobalInfo (     AudioFilePropertyID inPropertyID,     UInt32 inSpecifierSize,     void * _Nullable inSpecifier,     UInt32 * _Nonnull ioDataSize,     void * _Nonnull outPropertyData ); ``` |

Modified [AudioFileGetGlobalInfoSize()](https://developer.apple.com/documentation/audiotoolbox/1502463-audiofilegetglobalinfosize)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AudioFileGetGlobalInfoSize (     AudioFilePropertyID inPropertyID,     UInt32 inSpecifierSize,     void *inSpecifier,     UInt32 *outDataSize ); ``` |
| To | ``` OSStatus AudioFileGetGlobalInfoSize (     AudioFilePropertyID inPropertyID,     UInt32 inSpecifierSize,     void * _Nullable inSpecifier,     UInt32 * _Nonnull outDataSize ); ``` |

Modified [AudioFileGetProperty()](https://developer.apple.com/documentation/audiotoolbox/1502718-audiofilegetproperty)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AudioFileGetProperty (     AudioFileID inAudioFile,     AudioFilePropertyID inPropertyID,     UInt32 *ioDataSize,     void *outPropertyData ); ``` |
| To | ``` OSStatus AudioFileGetProperty (     AudioFileID _Nonnull inAudioFile,     AudioFilePropertyID inPropertyID,     UInt32 * _Nonnull ioDataSize,     void * _Nonnull outPropertyData ); ``` |

Modified [AudioFileGetPropertyInfo()](https://developer.apple.com/documentation/audiotoolbox/1501691-audiofilegetpropertyinfo)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AudioFileGetPropertyInfo (     AudioFileID inAudioFile,     AudioFilePropertyID inPropertyID,     UInt32 *outDataSize,     UInt32 *isWritable ); ``` |
| To | ``` OSStatus AudioFileGetPropertyInfo (     AudioFileID _Nonnull inAudioFile,     AudioFilePropertyID inPropertyID,     UInt32 * _Nullable outDataSize,     UInt32 * _Nullable isWritable ); ``` |

Modified [AudioFileGetUserData()](https://developer.apple.com/documentation/audiotoolbox/1501911-audiofilegetuserdata)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AudioFileGetUserData (     AudioFileID inAudioFile,     UInt32 inUserDataID,     UInt32 inIndex,     UInt32 *ioUserDataSize,     void *outUserData ); ``` |
| To | ``` OSStatus AudioFileGetUserData (     AudioFileID _Nonnull inAudioFile,     UInt32 inUserDataID,     UInt32 inIndex,     UInt32 * _Nonnull ioUserDataSize,     void * _Nonnull outUserData ); ``` |

Modified [AudioFileGetUserDataSize()](https://developer.apple.com/documentation/audiotoolbox/1502455-audiofilegetuserdatasize)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AudioFileGetUserDataSize (     AudioFileID inAudioFile,     UInt32 inUserDataID,     UInt32 inIndex,     UInt32 *outUserDataSize ); ``` |
| To | ``` OSStatus AudioFileGetUserDataSize (     AudioFileID _Nonnull inAudioFile,     UInt32 inUserDataID,     UInt32 inIndex,     UInt32 * _Nonnull outUserDataSize ); ``` |

Modified [AudioFileInitialize()](https://developer.apple.com/documentation/audiotoolbox/1576493-audiofileinitialize)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AudioFileInitialize (     const struct FSRef *inFileRef,     AudioFileTypeID inFileType,     const AudioStreamBasicDescription *inFormat,     UInt32 inFlags,     AudioFileID *outAudioFile ); ``` |
| To | ``` OSStatus AudioFileInitialize (     const struct FSRef * _Nonnull inFileRef,     AudioFileTypeID inFileType,     const AudioStreamBasicDescription * _Nonnull inFormat,     AudioFileFlags inFlags,     AudioFileID  _Nullable * _Nonnull outAudioFile ); ``` |

Modified [AudioFileInitializeWithCallbacks()](https://developer.apple.com/documentation/audiotoolbox/1502895-audiofileinitializewithcallbacks)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AudioFileInitializeWithCallbacks (     void *inClientData,     AudioFile_ReadProc inReadFunc,     AudioFile_WriteProc inWriteFunc,     AudioFile_GetSizeProc inGetSizeFunc,     AudioFile_SetSizeProc inSetSizeFunc,     AudioFileTypeID inFileType,     const AudioStreamBasicDescription *inFormat,     UInt32 inFlags,     AudioFileID *outAudioFile ); ``` |
| To | ``` OSStatus AudioFileInitializeWithCallbacks (     void * _Nonnull inClientData,     AudioFile_ReadProc _Nonnull inReadFunc,     AudioFile_WriteProc _Nonnull inWriteFunc,     AudioFile_GetSizeProc _Nonnull inGetSizeFunc,     AudioFile_SetSizeProc _Nonnull inSetSizeFunc,     AudioFileTypeID inFileType,     const AudioStreamBasicDescription * _Nonnull inFormat,     AudioFileFlags inFlags,     AudioFileID  _Nullable * _Nonnull outAudioFile ); ``` |

Modified [AudioFileOpen()](https://developer.apple.com/documentation/audiotoolbox/1576496-audiofileopen)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AudioFileOpen (     const struct FSRef *inFileRef,     SInt8 inPermissions,     AudioFileTypeID inFileTypeHint,     AudioFileID *outAudioFile ); ``` |
| To | ``` OSStatus AudioFileOpen (     const struct FSRef * _Nonnull inFileRef,     AudioFilePermissions inPermissions,     AudioFileTypeID inFileTypeHint,     AudioFileID  _Nullable * _Nonnull outAudioFile ); ``` |

Modified [AudioFileOpenURL()](https://developer.apple.com/documentation/audiotoolbox/1502304-audiofileopenurl)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AudioFileOpenURL (     CFURLRef inFileRef,     SInt8 inPermissions,     AudioFileTypeID inFileTypeHint,     AudioFileID *outAudioFile ); ``` |
| To | ``` OSStatus AudioFileOpenURL (     CFURLRef _Nonnull inFileRef,     AudioFilePermissions inPermissions,     AudioFileTypeID inFileTypeHint,     AudioFileID  _Nullable * _Nonnull outAudioFile ); ``` |

Modified [AudioFileOpenWithCallbacks()](https://developer.apple.com/documentation/audiotoolbox/1502746-audiofileopenwithcallbacks)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AudioFileOpenWithCallbacks (     void *inClientData,     AudioFile_ReadProc inReadFunc,     AudioFile_WriteProc inWriteFunc,     AudioFile_GetSizeProc inGetSizeFunc,     AudioFile_SetSizeProc inSetSizeFunc,     AudioFileTypeID inFileTypeHint,     AudioFileID *outAudioFile ); ``` |
| To | ``` OSStatus AudioFileOpenWithCallbacks (     void * _Nonnull inClientData,     AudioFile_ReadProc _Nonnull inReadFunc,     AudioFile_WriteProc _Nullable inWriteFunc,     AudioFile_GetSizeProc _Nonnull inGetSizeFunc,     AudioFile_SetSizeProc _Nullable inSetSizeFunc,     AudioFileTypeID inFileTypeHint,     AudioFileID  _Nullable * _Nonnull outAudioFile ); ``` |

Modified [AudioFileOptimize()](https://developer.apple.com/documentation/audiotoolbox/1502253-audiofileoptimize)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AudioFileOptimize (     AudioFileID inAudioFile ); ``` |
| To | ``` OSStatus AudioFileOptimize (     AudioFileID _Nonnull inAudioFile ); ``` |

Modified [AudioFileReadBytes()](https://developer.apple.com/documentation/audiotoolbox/1503247-audiofilereadbytes)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AudioFileReadBytes (     AudioFileID inAudioFile,     Boolean inUseCache,     SInt64 inStartingByte,     UInt32 *ioNumBytes,     void *outBuffer ); ``` |
| To | ``` OSStatus AudioFileReadBytes (     AudioFileID _Nonnull inAudioFile,     Boolean inUseCache,     SInt64 inStartingByte,     UInt32 * _Nonnull ioNumBytes,     void * _Nonnull outBuffer ); ``` |

Modified [AudioFileReadPacketData()](https://developer.apple.com/documentation/audiotoolbox/1502788-audiofilereadpacketdata)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AudioFileReadPacketData (     AudioFileID inAudioFile,     Boolean inUseCache,     UInt32 *ioNumBytes,     AudioStreamPacketDescription *outPacketDescriptions,     SInt64 inStartingPacket,     UInt32 *ioNumPackets,     void *outBuffer ); ``` |
| To | ``` OSStatus AudioFileReadPacketData (     AudioFileID _Nonnull inAudioFile,     Boolean inUseCache,     UInt32 * _Nonnull ioNumBytes,     AudioStreamPacketDescription * _Nullable outPacketDescriptions,     SInt64 inStartingPacket,     UInt32 * _Nonnull ioNumPackets,     void * _Nullable outBuffer ); ``` |

Modified [AudioFileReadPackets()](https://developer.apple.com/documentation/audiotoolbox/1503274-audiofilereadpackets)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AudioFileReadPackets (     AudioFileID inAudioFile,     Boolean inUseCache,     UInt32 *outNumBytes,     AudioStreamPacketDescription *outPacketDescriptions,     SInt64 inStartingPacket,     UInt32 *ioNumPackets,     void *outBuffer ); ``` |
| To | ``` OSStatus AudioFileReadPackets (     AudioFileID _Nonnull inAudioFile,     Boolean inUseCache,     UInt32 * _Nonnull outNumBytes,     AudioStreamPacketDescription * _Nullable outPacketDescriptions,     SInt64 inStartingPacket,     UInt32 * _Nonnull ioNumPackets,     void * _Nullable outBuffer ); ``` |

Modified [AudioFileRemoveUserData()](https://developer.apple.com/documentation/audiotoolbox/1503246-audiofileremoveuserdata)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AudioFileRemoveUserData (     AudioFileID inAudioFile,     UInt32 inUserDataID,     UInt32 inIndex ); ``` |
| To | ``` OSStatus AudioFileRemoveUserData (     AudioFileID _Nonnull inAudioFile,     UInt32 inUserDataID,     UInt32 inIndex ); ``` |

Modified [AudioFileSetProperty()](https://developer.apple.com/documentation/audiotoolbox/1503020-audiofilesetproperty)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AudioFileSetProperty (     AudioFileID inAudioFile,     AudioFilePropertyID inPropertyID,     UInt32 inDataSize,     const void *inPropertyData ); ``` |
| To | ``` OSStatus AudioFileSetProperty (     AudioFileID _Nonnull inAudioFile,     AudioFilePropertyID inPropertyID,     UInt32 inDataSize,     const void * _Nonnull inPropertyData ); ``` |

Modified [AudioFileSetUserData()](https://developer.apple.com/documentation/audiotoolbox/1502308-audiofilesetuserdata)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AudioFileSetUserData (     AudioFileID inAudioFile,     UInt32 inUserDataID,     UInt32 inIndex,     UInt32 inUserDataSize,     const void *inUserData ); ``` |
| To | ``` OSStatus AudioFileSetUserData (     AudioFileID _Nonnull inAudioFile,     UInt32 inUserDataID,     UInt32 inIndex,     UInt32 inUserDataSize,     const void * _Nonnull inUserData ); ``` |

Modified [AudioFileWriteBytes()](https://developer.apple.com/documentation/audiotoolbox/1502379-audiofilewritebytes)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AudioFileWriteBytes (     AudioFileID inAudioFile,     Boolean inUseCache,     SInt64 inStartingByte,     UInt32 *ioNumBytes,     const void *inBuffer ); ``` |
| To | ``` OSStatus AudioFileWriteBytes (     AudioFileID _Nonnull inAudioFile,     Boolean inUseCache,     SInt64 inStartingByte,     UInt32 * _Nonnull ioNumBytes,     const void * _Nonnull inBuffer ); ``` |

Modified [AudioFileWritePackets()](https://developer.apple.com/documentation/audiotoolbox/1502135-audiofilewritepackets)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AudioFileWritePackets (     AudioFileID inAudioFile,     Boolean inUseCache,     UInt32 inNumBytes,     const AudioStreamPacketDescription *inPacketDescriptions,     SInt64 inStartingPacket,     UInt32 *ioNumPackets,     const void *inBuffer ); ``` |
| To | ``` OSStatus AudioFileWritePackets (     AudioFileID _Nonnull inAudioFile,     Boolean inUseCache,     UInt32 inNumBytes,     const AudioStreamPacketDescription * _Nullable inPacketDescriptions,     SInt64 inStartingPacket,     UInt32 * _Nonnull ioNumPackets,     const void * _Nonnull inBuffer ); ``` |

#### AudioFileComponent.h

Added #def AudioToolbox_AudioFileComponent_hModified [AudioFileComponentCloseFile()](https://developer.apple.com/documentation/audiotoolbox/1404159-audiofilecomponentclosefile)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AudioFileComponentCloseFile (     AudioFileComponent inComponent ); ``` |
| To | ``` OSStatus AudioFileComponentCloseFile (     AudioFileComponent _Nonnull inComponent ); ``` |

Modified [AudioFileComponentCountUserData()](https://developer.apple.com/documentation/audiotoolbox/1404167-audiofilecomponentcountuserdata)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AudioFileComponentCountUserData (     AudioFileComponent inComponent,     UInt32 inUserDataID,     UInt32 *outNumberItems ); ``` |
| To | ``` OSStatus AudioFileComponentCountUserData (     AudioFileComponent _Nonnull inComponent,     UInt32 inUserDataID,     UInt32 * _Nonnull outNumberItems ); ``` |

Modified [AudioFileComponentCreate()](https://developer.apple.com/documentation/audiotoolbox/1404179-audiofilecomponentcreate)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` OSStatus AudioFileComponentCreate (     AudioFileComponent inComponent,     const struct FSRef *inParentRef,     CFStringRef inFileName,     const AudioStreamBasicDescription *inFormat,     UInt32 inFlags,     struct FSRef *outNewFileRef ); ``` | -- |
| To | ``` OSStatus AudioFileComponentCreate (     AudioFileComponent _Nonnull inComponent,     const struct FSRef * _Nonnull inParentRef,     CFStringRef _Nonnull inFileName,     const AudioStreamBasicDescription * _Nonnull inFormat,     UInt32 inFlags,     struct FSRef * _Nonnull outNewFileRef ); ``` | OS X 10.6 |

Modified [AudioFileComponentCreateURL()](https://developer.apple.com/documentation/audiotoolbox/1404011-audiofilecomponentcreateurl)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AudioFileComponentCreateURL (     AudioFileComponent inComponent,     CFURLRef inFileRef,     const AudioStreamBasicDescription *inFormat,     UInt32 inFlags ); ``` |
| To | ``` OSStatus AudioFileComponentCreateURL (     AudioFileComponent _Nonnull inComponent,     CFURLRef _Nonnull inFileRef,     const AudioStreamBasicDescription * _Nonnull inFormat,     UInt32 inFlags ); ``` |

Modified [AudioFileComponentDataIsThisFormat()](https://developer.apple.com/documentation/audiotoolbox/1404183-audiofilecomponentdataisthisform)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AudioFileComponentDataIsThisFormat (     AudioFileComponent inComponent,     void *inClientData,     AudioFile_ReadProc inReadFunc,     AudioFile_WriteProc inWriteFunc,     AudioFile_GetSizeProc inGetSizeFunc,     AudioFile_SetSizeProc inSetSizeFunc,     UInt32 *outResult ); ``` |
| To | ``` OSStatus AudioFileComponentDataIsThisFormat (     AudioFileComponent _Nonnull inComponent,     void * _Nullable inClientData,     AudioFile_ReadProc _Nullable inReadFunc,     AudioFile_WriteProc _Nullable inWriteFunc,     AudioFile_GetSizeProc _Nullable inGetSizeFunc,     AudioFile_SetSizeProc _Nullable inSetSizeFunc,     UInt32 * _Nonnull outResult ); ``` |

Modified [AudioFileComponentExtensionIsThisFormat()](https://developer.apple.com/documentation/audiotoolbox/1404027-audiofilecomponentextensionisthi)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AudioFileComponentExtensionIsThisFormat (     AudioFileComponent inComponent,     CFStringRef inExtension,     UInt32 *outResult ); ``` |
| To | ``` OSStatus AudioFileComponentExtensionIsThisFormat (     AudioFileComponent _Nonnull inComponent,     CFStringRef _Nonnull inExtension,     UInt32 * _Nonnull outResult ); ``` |

Modified [AudioFileComponentFileDataIsThisFormat()](https://developer.apple.com/documentation/audiotoolbox/1404210-audiofilecomponentfiledataisthis)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AudioFileComponentFileDataIsThisFormat (     AudioFileComponent inComponent,     UInt32 inDataByteSize,     const void *inData,     UInt32 *outResult ); ``` |
| To | ``` OSStatus AudioFileComponentFileDataIsThisFormat (     AudioFileComponent _Nonnull inComponent,     UInt32 inDataByteSize,     const void * _Nonnull inData,     UInt32 * _Nonnull outResult ); ``` |

Modified [AudioFileComponentFileIsThisFormat()](https://developer.apple.com/documentation/audiotoolbox/1404008-audiofilecomponentfileisthisform)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AudioFileComponentFileIsThisFormat (     AudioFileComponent inComponent,     SInt16 inFileRefNum,     UInt32 *outResult ); ``` |
| To | ``` OSStatus AudioFileComponentFileIsThisFormat (     AudioFileComponent _Nonnull inComponent,     SInt16 inFileRefNum,     UInt32 * _Nonnull outResult ); ``` |

Modified [AudioFileComponentGetGlobalInfo()](https://developer.apple.com/documentation/audiotoolbox/1404156-audiofilecomponentgetglobalinfo)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AudioFileComponentGetGlobalInfo (     AudioFileComponent inComponent,     AudioFileComponentPropertyID inPropertyID,     UInt32 inSpecifierSize,     const void *inSpecifier,     UInt32 *ioPropertyDataSize,     void *outPropertyData ); ``` |
| To | ``` OSStatus AudioFileComponentGetGlobalInfo (     AudioFileComponent _Nonnull inComponent,     AudioFileComponentPropertyID inPropertyID,     UInt32 inSpecifierSize,     const void * _Nullable inSpecifier,     UInt32 * _Nonnull ioPropertyDataSize,     void * _Nonnull outPropertyData ); ``` |

Modified [AudioFileComponentGetGlobalInfoSize()](https://developer.apple.com/documentation/audiotoolbox/1404136-audiofilecomponentgetglobalinfos)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AudioFileComponentGetGlobalInfoSize (     AudioFileComponent inComponent,     AudioFileComponentPropertyID inPropertyID,     UInt32 inSpecifierSize,     const void *inSpecifier,     UInt32 *outPropertySize ); ``` |
| To | ``` OSStatus AudioFileComponentGetGlobalInfoSize (     AudioFileComponent _Nonnull inComponent,     AudioFileComponentPropertyID inPropertyID,     UInt32 inSpecifierSize,     const void * _Nullable inSpecifier,     UInt32 * _Nonnull outPropertySize ); ``` |

Modified [AudioFileComponentGetProperty()](https://developer.apple.com/documentation/audiotoolbox/1403983-audiofilecomponentgetproperty)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AudioFileComponentGetProperty (     AudioFileComponent inComponent,     AudioFileComponentPropertyID inPropertyID,     UInt32 *ioPropertyDataSize,     void *outPropertyData ); ``` |
| To | ``` OSStatus AudioFileComponentGetProperty (     AudioFileComponent _Nonnull inComponent,     AudioFileComponentPropertyID inPropertyID,     UInt32 * _Nonnull ioPropertyDataSize,     void * _Nonnull outPropertyData ); ``` |

Modified [AudioFileComponentGetPropertyInfo()](https://developer.apple.com/documentation/audiotoolbox/1404104-audiofilecomponentgetpropertyinf)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AudioFileComponentGetPropertyInfo (     AudioFileComponent inComponent,     AudioFileComponentPropertyID inPropertyID,     UInt32 *outPropertySize,     UInt32 *outWritable ); ``` |
| To | ``` OSStatus AudioFileComponentGetPropertyInfo (     AudioFileComponent _Nonnull inComponent,     AudioFileComponentPropertyID inPropertyID,     UInt32 * _Nullable outPropertySize,     UInt32 * _Nullable outWritable ); ``` |

Modified [AudioFileComponentGetUserData()](https://developer.apple.com/documentation/audiotoolbox/1404098-audiofilecomponentgetuserdata)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AudioFileComponentGetUserData (     AudioFileComponent inComponent,     UInt32 inUserDataID,     UInt32 inIndex,     UInt32 *ioUserDataSize,     void *outUserData ); ``` |
| To | ``` OSStatus AudioFileComponentGetUserData (     AudioFileComponent _Nonnull inComponent,     UInt32 inUserDataID,     UInt32 inIndex,     UInt32 * _Nonnull ioUserDataSize,     void * _Nonnull outUserData ); ``` |

Modified [AudioFileComponentGetUserDataSize()](https://developer.apple.com/documentation/audiotoolbox/1404146-audiofilecomponentgetuserdatasiz)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AudioFileComponentGetUserDataSize (     AudioFileComponent inComponent,     UInt32 inUserDataID,     UInt32 inIndex,     UInt32 *outUserDataSize ); ``` |
| To | ``` OSStatus AudioFileComponentGetUserDataSize (     AudioFileComponent _Nonnull inComponent,     UInt32 inUserDataID,     UInt32 inIndex,     UInt32 * _Nonnull outUserDataSize ); ``` |

Modified [AudioFileComponentInitialize()](https://developer.apple.com/documentation/audiotoolbox/1404190-audiofilecomponentinitialize)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` OSStatus AudioFileComponentInitialize (     AudioFileComponent inComponent,     const struct FSRef *inFileRef,     const AudioStreamBasicDescription *inFormat,     UInt32 inFlags ); ``` | -- |
| To | ``` OSStatus AudioFileComponentInitialize (     AudioFileComponent _Nonnull inComponent,     const struct FSRef * _Nonnull inFileRef,     const AudioStreamBasicDescription * _Nonnull inFormat,     UInt32 inFlags ); ``` | OS X 10.6 |

Modified [AudioFileComponentInitializeWithCallbacks()](https://developer.apple.com/documentation/audiotoolbox/1404152-audiofilecomponentinitializewith)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AudioFileComponentInitializeWithCallbacks (     AudioFileComponent inComponent,     void *inClientData,     AudioFile_ReadProc inReadFunc,     AudioFile_WriteProc inWriteFunc,     AudioFile_GetSizeProc inGetSizeFunc,     AudioFile_SetSizeProc inSetSizeFunc,     UInt32 inFileType,     const AudioStreamBasicDescription *inFormat,     UInt32 inFlags ); ``` |
| To | ``` OSStatus AudioFileComponentInitializeWithCallbacks (     AudioFileComponent _Nonnull inComponent,     void * _Nonnull inClientData,     AudioFile_ReadProc _Nonnull inReadFunc,     AudioFile_WriteProc _Nonnull inWriteFunc,     AudioFile_GetSizeProc _Nonnull inGetSizeFunc,     AudioFile_SetSizeProc _Nonnull inSetSizeFunc,     UInt32 inFileType,     const AudioStreamBasicDescription * _Nonnull inFormat,     UInt32 inFlags ); ``` |

Modified [AudioFileComponentOpenFile()](https://developer.apple.com/documentation/audiotoolbox/1404202-audiofilecomponentopenfile)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` OSStatus AudioFileComponentOpenFile (     AudioFileComponent inComponent,     const struct FSRef *inFileRef,     SInt8 inPermissions,     SInt16 inRefNum ); ``` | -- |
| To | ``` OSStatus AudioFileComponentOpenFile (     AudioFileComponent _Nonnull inComponent,     const struct FSRef * _Nonnull inFileRef,     SInt8 inPermissions,     SInt16 inRefNum ); ``` | OS X 10.6 |

Modified [AudioFileComponentOpenURL()](https://developer.apple.com/documentation/audiotoolbox/1404059-audiofilecomponentopenurl)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AudioFileComponentOpenURL (     AudioFileComponent inComponent,     CFURLRef inFileRef,     SInt8 inPermissions,     int inFileDescriptor ); ``` |
| To | ``` OSStatus AudioFileComponentOpenURL (     AudioFileComponent _Nonnull inComponent,     CFURLRef _Nonnull inFileRef,     SInt8 inPermissions,     int inFileDescriptor ); ``` |

Modified [AudioFileComponentOpenWithCallbacks()](https://developer.apple.com/documentation/audiotoolbox/1404114-audiofilecomponentopenwithcallba)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AudioFileComponentOpenWithCallbacks (     AudioFileComponent inComponent,     void *inClientData,     AudioFile_ReadProc inReadFunc,     AudioFile_WriteProc inWriteFunc,     AudioFile_GetSizeProc inGetSizeFunc,     AudioFile_SetSizeProc inSetSizeFunc ); ``` |
| To | ``` OSStatus AudioFileComponentOpenWithCallbacks (     AudioFileComponent _Nonnull inComponent,     void * _Nonnull inClientData,     AudioFile_ReadProc _Nonnull inReadFunc,     AudioFile_WriteProc _Nonnull inWriteFunc,     AudioFile_GetSizeProc _Nonnull inGetSizeFunc,     AudioFile_SetSizeProc _Nonnull inSetSizeFunc ); ``` |

Modified [AudioFileComponentOptimize()](https://developer.apple.com/documentation/audiotoolbox/1404208-audiofilecomponentoptimize)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AudioFileComponentOptimize (     AudioFileComponent inComponent ); ``` |
| To | ``` OSStatus AudioFileComponentOptimize (     AudioFileComponent _Nonnull inComponent ); ``` |

Modified [AudioFileComponentReadBytes()](https://developer.apple.com/documentation/audiotoolbox/1404218-audiofilecomponentreadbytes)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AudioFileComponentReadBytes (     AudioFileComponent inComponent,     Boolean inUseCache,     SInt64 inStartingByte,     UInt32 *ioNumBytes,     void *outBuffer ); ``` |
| To | ``` OSStatus AudioFileComponentReadBytes (     AudioFileComponent _Nonnull inComponent,     Boolean inUseCache,     SInt64 inStartingByte,     UInt32 * _Nonnull ioNumBytes,     void * _Nonnull outBuffer ); ``` |

Modified [AudioFileComponentReadPacketData()](https://developer.apple.com/documentation/audiotoolbox/1404083-audiofilecomponentreadpacketdata)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AudioFileComponentReadPacketData (     AudioFileComponent inComponent,     Boolean inUseCache,     UInt32 *ioNumBytes,     AudioStreamPacketDescription *outPacketDescriptions,     SInt64 inStartingPacket,     UInt32 *ioNumPackets,     void *outBuffer ); ``` |
| To | ``` OSStatus AudioFileComponentReadPacketData (     AudioFileComponent _Nonnull inComponent,     Boolean inUseCache,     UInt32 * _Nonnull ioNumBytes,     AudioStreamPacketDescription * _Nullable outPacketDescriptions,     SInt64 inStartingPacket,     UInt32 * _Nonnull ioNumPackets,     void * _Nonnull outBuffer ); ``` |

Modified [AudioFileComponentReadPackets()](https://developer.apple.com/documentation/audiotoolbox/1404067-audiofilecomponentreadpackets)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AudioFileComponentReadPackets (     AudioFileComponent inComponent,     Boolean inUseCache,     UInt32 *outNumBytes,     AudioStreamPacketDescription *outPacketDescriptions,     SInt64 inStartingPacket,     UInt32 *ioNumPackets,     void *outBuffer ); ``` |
| To | ``` OSStatus AudioFileComponentReadPackets (     AudioFileComponent _Nonnull inComponent,     Boolean inUseCache,     UInt32 * _Nonnull outNumBytes,     AudioStreamPacketDescription * _Nullable outPacketDescriptions,     SInt64 inStartingPacket,     UInt32 * _Nonnull ioNumPackets,     void * _Nonnull outBuffer ); ``` |

Modified [AudioFileComponentRemoveUserData()](https://developer.apple.com/documentation/audiotoolbox/1404142-audiofilecomponentremoveuserdata)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AudioFileComponentRemoveUserData (     AudioFileComponent inComponent,     UInt32 inUserDataID,     UInt32 inIndex ); ``` |
| To | ``` OSStatus AudioFileComponentRemoveUserData (     AudioFileComponent _Nonnull inComponent,     UInt32 inUserDataID,     UInt32 inIndex ); ``` |

Modified [AudioFileComponentSetProperty()](https://developer.apple.com/documentation/audiotoolbox/1404188-audiofilecomponentsetproperty)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AudioFileComponentSetProperty (     AudioFileComponent inComponent,     AudioFileComponentPropertyID inPropertyID,     UInt32 inPropertyDataSize,     const void *inPropertyData ); ``` |
| To | ``` OSStatus AudioFileComponentSetProperty (     AudioFileComponent _Nonnull inComponent,     AudioFileComponentPropertyID inPropertyID,     UInt32 inPropertyDataSize,     const void * _Nonnull inPropertyData ); ``` |

Modified [AudioFileComponentSetUserData()](https://developer.apple.com/documentation/audiotoolbox/1403993-audiofilecomponentsetuserdata)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AudioFileComponentSetUserData (     AudioFileComponent inComponent,     UInt32 inUserDataID,     UInt32 inIndex,     UInt32 inUserDataSize,     const void *inUserData ); ``` |
| To | ``` OSStatus AudioFileComponentSetUserData (     AudioFileComponent _Nonnull inComponent,     UInt32 inUserDataID,     UInt32 inIndex,     UInt32 inUserDataSize,     const void * _Nonnull inUserData ); ``` |

Modified [AudioFileComponentWriteBytes()](https://developer.apple.com/documentation/audiotoolbox/1404118-audiofilecomponentwritebytes)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AudioFileComponentWriteBytes (     AudioFileComponent inComponent,     Boolean inUseCache,     SInt64 inStartingByte,     UInt32 *ioNumBytes,     const void *inBuffer ); ``` |
| To | ``` OSStatus AudioFileComponentWriteBytes (     AudioFileComponent _Nonnull inComponent,     Boolean inUseCache,     SInt64 inStartingByte,     UInt32 * _Nonnull ioNumBytes,     const void * _Nonnull inBuffer ); ``` |

Modified [AudioFileComponentWritePackets()](https://developer.apple.com/documentation/audiotoolbox/1403969-audiofilecomponentwritepackets)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AudioFileComponentWritePackets (     AudioFileComponent inComponent,     Boolean inUseCache,     UInt32 inNumBytes,     const AudioStreamPacketDescription *inPacketDescriptions,     SInt64 inStartingPacket,     UInt32 *ioNumPackets,     const void *inBuffer ); ``` |
| To | ``` OSStatus AudioFileComponentWritePackets (     AudioFileComponent _Nonnull inComponent,     Boolean inUseCache,     UInt32 inNumBytes,     const AudioStreamPacketDescription * _Nullable inPacketDescriptions,     SInt64 inStartingPacket,     UInt32 * _Nonnull ioNumPackets,     const void * _Nonnull inBuffer ); ``` |

Modified [AudioFileFDFTable](https://developer.apple.com/documentation/audiotoolbox/audiofilefdftable)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.3 | -- |
| To | OS X 10.4 | OS X 10.7 |

Modified [AudioFileFDFTableExtended](https://developer.apple.com/documentation/audiotoolbox/audiofilefdftableextended)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.6 | -- |
| To | OS X 10.4 | OS X 10.7 |

#### AudioFileStream.h

Added [AudioFileStreamParseFlags](https://developer.apple.com/documentation/audiotoolbox/audiofilestreamparseflags)Added [AudioFileStreamPropertyFlags](https://developer.apple.com/documentation/audiotoolbox/audiofilestreampropertyflags)Added [AudioFileStreamSeekFlags](https://developer.apple.com/documentation/audiotoolbox/audiofilestreamseekflags)Added #def AudioToolbox_AudioFileStream_hModified [AudioFileStreamClose()](https://developer.apple.com/documentation/audiotoolbox/1391524-audiofilestreamclose)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AudioFileStreamClose (     AudioFileStreamID inAudioFileStream ); ``` |
| To | ``` OSStatus AudioFileStreamClose (     AudioFileStreamID _Nonnull inAudioFileStream ); ``` |

Modified [AudioFileStreamGetProperty()](https://developer.apple.com/documentation/audiotoolbox/1391490-audiofilestreamgetproperty)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AudioFileStreamGetProperty (     AudioFileStreamID inAudioFileStream,     AudioFileStreamPropertyID inPropertyID,     UInt32 *ioPropertyDataSize,     void *outPropertyData ); ``` |
| To | ``` OSStatus AudioFileStreamGetProperty (     AudioFileStreamID _Nonnull inAudioFileStream,     AudioFileStreamPropertyID inPropertyID,     UInt32 * _Nonnull ioPropertyDataSize,     void * _Nonnull outPropertyData ); ``` |

Modified [AudioFileStreamGetPropertyInfo()](https://developer.apple.com/documentation/audiotoolbox/1391500-audiofilestreamgetpropertyinfo)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AudioFileStreamGetPropertyInfo (     AudioFileStreamID inAudioFileStream,     AudioFileStreamPropertyID inPropertyID,     UInt32 *outPropertyDataSize,     Boolean *outWritable ); ``` |
| To | ``` OSStatus AudioFileStreamGetPropertyInfo (     AudioFileStreamID _Nonnull inAudioFileStream,     AudioFileStreamPropertyID inPropertyID,     UInt32 * _Nullable outPropertyDataSize,     Boolean * _Nullable outWritable ); ``` |

Modified [AudioFileStreamOpen()](https://developer.apple.com/documentation/audiotoolbox/1391498-audiofilestreamopen)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AudioFileStreamOpen (     void *inClientData,     AudioFileStream_PropertyListenerProc inPropertyListenerProc,     AudioFileStream_PacketsProc inPacketsProc,     AudioFileTypeID inFileTypeHint,     AudioFileStreamID *outAudioFileStream ); ``` |
| To | ``` OSStatus AudioFileStreamOpen (     void * _Nullable inClientData,     AudioFileStream_PropertyListenerProc _Nonnull inPropertyListenerProc,     AudioFileStream_PacketsProc _Nonnull inPacketsProc,     AudioFileTypeID inFileTypeHint,     AudioFileStreamID  _Nullable * _Nonnull outAudioFileStream ); ``` |

Modified [AudioFileStreamParseBytes()](https://developer.apple.com/documentation/audiotoolbox/1391492-audiofilestreamparsebytes)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AudioFileStreamParseBytes (     AudioFileStreamID inAudioFileStream,     UInt32 inDataByteSize,     const void *inData,     UInt32 inFlags ); ``` |
| To | ``` OSStatus AudioFileStreamParseBytes (     AudioFileStreamID _Nonnull inAudioFileStream,     UInt32 inDataByteSize,     const void * _Nonnull inData,     AudioFileStreamParseFlags inFlags ); ``` |

Modified [AudioFileStreamSeek()](https://developer.apple.com/documentation/audiotoolbox/1391488-audiofilestreamseek)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AudioFileStreamSeek (     AudioFileStreamID inAudioFileStream,     SInt64 inPacketOffset,     SInt64 *outDataByteOffset,     UInt32 *ioFlags ); ``` |
| To | ``` OSStatus AudioFileStreamSeek (     AudioFileStreamID _Nonnull inAudioFileStream,     SInt64 inPacketOffset,     SInt64 * _Nonnull outDataByteOffset,     AudioFileStreamSeekFlags * _Nonnull ioFlags ); ``` |

Modified [AudioFileStreamSetProperty()](https://developer.apple.com/documentation/audiotoolbox/1391576-audiofilestreamsetproperty)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AudioFileStreamSetProperty (     AudioFileStreamID inAudioFileStream,     AudioFileStreamPropertyID inPropertyID,     UInt32 inPropertyDataSize,     const void *inPropertyData ); ``` |
| To | ``` OSStatus AudioFileStreamSetProperty (     AudioFileStreamID _Nonnull inAudioFileStream,     AudioFileStreamPropertyID inPropertyID,     UInt32 inPropertyDataSize,     const void * _Nonnull inPropertyData ); ``` |

#### AudioFormat.h

Added [AudioBalanceFadeType](https://developer.apple.com/documentation/audiotoolbox/audiobalancefadetype)Added [AudioPanningMode](https://developer.apple.com/documentation/audiotoolbox/audiopanningmode)Added #def AudioToolbox_AudioFormat_hModified [AudioFormatGetProperty()](https://developer.apple.com/documentation/audiotoolbox/1501860-audioformatgetproperty)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AudioFormatGetProperty (     AudioFormatPropertyID inPropertyID,     UInt32 inSpecifierSize,     const void *inSpecifier,     UInt32 *ioPropertyDataSize,     void *outPropertyData ); ``` |
| To | ``` OSStatus AudioFormatGetProperty (     AudioFormatPropertyID inPropertyID,     UInt32 inSpecifierSize,     const void * _Nullable inSpecifier,     UInt32 * _Nullable ioPropertyDataSize,     void * _Nullable outPropertyData ); ``` |

Modified [AudioFormatGetPropertyInfo()](https://developer.apple.com/documentation/audiotoolbox/1502065-audioformatgetpropertyinfo)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AudioFormatGetPropertyInfo (     AudioFormatPropertyID inPropertyID,     UInt32 inSpecifierSize,     const void *inSpecifier,     UInt32 *outPropertyDataSize ); ``` |
| To | ``` OSStatus AudioFormatGetPropertyInfo (     AudioFormatPropertyID inPropertyID,     UInt32 inSpecifierSize,     const void * _Nullable inSpecifier,     UInt32 * _Nonnull outPropertyDataSize ); ``` |

#### AudioQueue.h

Added [AudioQueueProcessingTapFlags](https://developer.apple.com/documentation/audiotoolbox/audioqueueprocessingtapflags)Added #def AudioToolbox_AudioQueue_hModified [AudioQueueAddPropertyListener()](https://developer.apple.com/documentation/audiotoolbox/1502091-audioqueueaddpropertylistener)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AudioQueueAddPropertyListener (     AudioQueueRef inAQ,     AudioQueuePropertyID inID,     AudioQueuePropertyListenerProc inProc,     void *inUserData ); ``` |
| To | ``` OSStatus AudioQueueAddPropertyListener (     AudioQueueRef _Nonnull inAQ,     AudioQueuePropertyID inID,     AudioQueuePropertyListenerProc _Nonnull inProc,     void * _Nullable inUserData ); ``` |

Modified [AudioQueueAllocateBuffer()](https://developer.apple.com/documentation/audiotoolbox/1502248-audioqueueallocatebuffer)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AudioQueueAllocateBuffer (     AudioQueueRef inAQ,     UInt32 inBufferByteSize,     AudioQueueBufferRef *outBuffer ); ``` |
| To | ``` OSStatus AudioQueueAllocateBuffer (     AudioQueueRef _Nonnull inAQ,     UInt32 inBufferByteSize,     AudioQueueBufferRef  _Nullable * _Nonnull outBuffer ); ``` |

Modified [AudioQueueAllocateBufferWithPacketDescriptions()](https://developer.apple.com/documentation/audiotoolbox/1502389-audioqueueallocatebufferwithpack)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AudioQueueAllocateBufferWithPacketDescriptions (     AudioQueueRef inAQ,     UInt32 inBufferByteSize,     UInt32 inNumberPacketDescriptions,     AudioQueueBufferRef *outBuffer ); ``` |
| To | ``` OSStatus AudioQueueAllocateBufferWithPacketDescriptions (     AudioQueueRef _Nonnull inAQ,     UInt32 inBufferByteSize,     UInt32 inNumberPacketDescriptions,     AudioQueueBufferRef  _Nullable * _Nonnull outBuffer ); ``` |

Modified [AudioQueueCreateTimeline()](https://developer.apple.com/documentation/audiotoolbox/1501704-audioqueuecreatetimeline)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AudioQueueCreateTimeline (     AudioQueueRef inAQ,     AudioQueueTimelineRef *outTimeline ); ``` |
| To | ``` OSStatus AudioQueueCreateTimeline (     AudioQueueRef _Nonnull inAQ,     AudioQueueTimelineRef  _Nullable * _Nonnull outTimeline ); ``` |

Modified [AudioQueueDeviceGetCurrentTime()](https://developer.apple.com/documentation/audiotoolbox/1502907-audioqueuedevicegetcurrenttime)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AudioQueueDeviceGetCurrentTime (     AudioQueueRef inAQ,     AudioTimeStamp *outTimeStamp ); ``` |
| To | ``` OSStatus AudioQueueDeviceGetCurrentTime (     AudioQueueRef _Nonnull inAQ,     AudioTimeStamp * _Nonnull outTimeStamp ); ``` |

Modified [AudioQueueDeviceGetNearestStartTime()](https://developer.apple.com/documentation/audiotoolbox/1503373-audioqueuedevicegetneareststartt)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AudioQueueDeviceGetNearestStartTime (     AudioQueueRef inAQ,     AudioTimeStamp *ioRequestedStartTime,     UInt32 inFlags ); ``` |
| To | ``` OSStatus AudioQueueDeviceGetNearestStartTime (     AudioQueueRef _Nonnull inAQ,     AudioTimeStamp * _Nonnull ioRequestedStartTime,     UInt32 inFlags ); ``` |

Modified [AudioQueueDeviceTranslateTime()](https://developer.apple.com/documentation/audiotoolbox/1503302-audioqueuedevicetranslatetime)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AudioQueueDeviceTranslateTime (     AudioQueueRef inAQ,     const AudioTimeStamp *inTime,     AudioTimeStamp *outTime ); ``` |
| To | ``` OSStatus AudioQueueDeviceTranslateTime (     AudioQueueRef _Nonnull inAQ,     const AudioTimeStamp * _Nonnull inTime,     AudioTimeStamp * _Nonnull outTime ); ``` |

Modified [AudioQueueDispose()](https://developer.apple.com/documentation/audiotoolbox/1502229-audioqueuedispose)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AudioQueueDispose (     AudioQueueRef inAQ,     Boolean inImmediate ); ``` |
| To | ``` OSStatus AudioQueueDispose (     AudioQueueRef _Nonnull inAQ,     Boolean inImmediate ); ``` |

Modified [AudioQueueDisposeTimeline()](https://developer.apple.com/documentation/audiotoolbox/1502426-audioqueuedisposetimeline)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AudioQueueDisposeTimeline (     AudioQueueRef inAQ,     AudioQueueTimelineRef inTimeline ); ``` |
| To | ``` OSStatus AudioQueueDisposeTimeline (     AudioQueueRef _Nonnull inAQ,     AudioQueueTimelineRef _Nonnull inTimeline ); ``` |

Modified [AudioQueueEnqueueBuffer()](https://developer.apple.com/documentation/audiotoolbox/1502779-audioqueueenqueuebuffer)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AudioQueueEnqueueBuffer (     AudioQueueRef inAQ,     AudioQueueBufferRef inBuffer,     UInt32 inNumPacketDescs,     const AudioStreamPacketDescription *inPacketDescs ); ``` |
| To | ``` OSStatus AudioQueueEnqueueBuffer (     AudioQueueRef _Nonnull inAQ,     AudioQueueBufferRef _Nonnull inBuffer,     UInt32 inNumPacketDescs,     const AudioStreamPacketDescription * _Nullable inPacketDescs ); ``` |

Modified [AudioQueueEnqueueBufferWithParameters()](https://developer.apple.com/documentation/audiotoolbox/1503258-audioqueueenqueuebufferwithparam)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AudioQueueEnqueueBufferWithParameters (     AudioQueueRef inAQ,     AudioQueueBufferRef inBuffer,     UInt32 inNumPacketDescs,     const AudioStreamPacketDescription *inPacketDescs,     UInt32 inTrimFramesAtStart,     UInt32 inTrimFramesAtEnd,     UInt32 inNumParamValues,     const AudioQueueParameterEvent *inParamValues,     const AudioTimeStamp *inStartTime,     AudioTimeStamp *outActualStartTime ); ``` |
| To | ``` OSStatus AudioQueueEnqueueBufferWithParameters (     AudioQueueRef _Nonnull inAQ,     AudioQueueBufferRef _Nonnull inBuffer,     UInt32 inNumPacketDescs,     const AudioStreamPacketDescription * _Nullable inPacketDescs,     UInt32 inTrimFramesAtStart,     UInt32 inTrimFramesAtEnd,     UInt32 inNumParamValues,     const AudioQueueParameterEvent * _Nullable inParamValues,     const AudioTimeStamp * _Nullable inStartTime,     AudioTimeStamp * _Nullable outActualStartTime ); ``` |

Modified [AudioQueueFlush()](https://developer.apple.com/documentation/audiotoolbox/1502477-audioqueueflush)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AudioQueueFlush (     AudioQueueRef inAQ ); ``` |
| To | ``` OSStatus AudioQueueFlush (     AudioQueueRef _Nonnull inAQ ); ``` |

Modified [AudioQueueFreeBuffer()](https://developer.apple.com/documentation/audiotoolbox/1503332-audioqueuefreebuffer)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AudioQueueFreeBuffer (     AudioQueueRef inAQ,     AudioQueueBufferRef inBuffer ); ``` |
| To | ``` OSStatus AudioQueueFreeBuffer (     AudioQueueRef _Nonnull inAQ,     AudioQueueBufferRef _Nonnull inBuffer ); ``` |

Modified [AudioQueueGetCurrentTime()](https://developer.apple.com/documentation/audiotoolbox/1502244-audioqueuegetcurrenttime)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AudioQueueGetCurrentTime (     AudioQueueRef inAQ,     AudioQueueTimelineRef inTimeline,     AudioTimeStamp *outTimeStamp,     Boolean *outTimelineDiscontinuity ); ``` |
| To | ``` OSStatus AudioQueueGetCurrentTime (     AudioQueueRef _Nonnull inAQ,     AudioQueueTimelineRef _Nullable inTimeline,     AudioTimeStamp * _Nullable outTimeStamp,     Boolean * _Nullable outTimelineDiscontinuity ); ``` |

Modified [AudioQueueGetParameter()](https://developer.apple.com/documentation/audiotoolbox/1503353-audioqueuegetparameter)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AudioQueueGetParameter (     AudioQueueRef inAQ,     AudioQueueParameterID inParamID,     AudioQueueParameterValue *outValue ); ``` |
| To | ``` OSStatus AudioQueueGetParameter (     AudioQueueRef _Nonnull inAQ,     AudioQueueParameterID inParamID,     AudioQueueParameterValue * _Nonnull outValue ); ``` |

Modified [AudioQueueGetProperty()](https://developer.apple.com/documentation/audiotoolbox/1502998-audioqueuegetproperty)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AudioQueueGetProperty (     AudioQueueRef inAQ,     AudioQueuePropertyID inID,     void *outData,     UInt32 *ioDataSize ); ``` |
| To | ``` OSStatus AudioQueueGetProperty (     AudioQueueRef _Nonnull inAQ,     AudioQueuePropertyID inID,     void * _Nonnull outData,     UInt32 * _Nonnull ioDataSize ); ``` |

Modified [AudioQueueGetPropertySize()](https://developer.apple.com/documentation/audiotoolbox/1501624-audioqueuegetpropertysize)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AudioQueueGetPropertySize (     AudioQueueRef inAQ,     AudioQueuePropertyID inID,     UInt32 *outDataSize ); ``` |
| To | ``` OSStatus AudioQueueGetPropertySize (     AudioQueueRef _Nonnull inAQ,     AudioQueuePropertyID inID,     UInt32 * _Nonnull outDataSize ); ``` |

Modified [AudioQueueNewInput()](https://developer.apple.com/documentation/audiotoolbox/1501687-audioqueuenewinput)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AudioQueueNewInput (     const AudioStreamBasicDescription *inFormat,     AudioQueueInputCallback inCallbackProc,     void *inUserData,     CFRunLoopRef inCallbackRunLoop,     CFStringRef inCallbackRunLoopMode,     UInt32 inFlags,     AudioQueueRef *outAQ ); ``` |
| To | ``` OSStatus AudioQueueNewInput (     const AudioStreamBasicDescription * _Nonnull inFormat,     AudioQueueInputCallback _Nonnull inCallbackProc,     void * _Nullable inUserData,     CFRunLoopRef _Nullable inCallbackRunLoop,     CFStringRef _Nullable inCallbackRunLoopMode,     UInt32 inFlags,     AudioQueueRef  _Nullable * _Nonnull outAQ ); ``` |

Modified [AudioQueueNewInputWithDispatchQueue()](https://developer.apple.com/documentation/audiotoolbox/1503196-audioqueuenewinputwithdispatchqu)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AudioQueueNewInputWithDispatchQueue (     AudioQueueRef *outAQ,     const AudioStreamBasicDescription *inFormat,     UInt32 inFlags,     dispatch_queue_t inCallbackDispatchQueue,     AudioQueueInputCallbackBlock inCallbackBlock ); ``` |
| To | ``` OSStatus AudioQueueNewInputWithDispatchQueue (     AudioQueueRef  _Nullable * _Nonnull outAQ,     const AudioStreamBasicDescription * _Nonnull inFormat,     UInt32 inFlags,     dispatch_queue_t _Nonnull inCallbackDispatchQueue,     AudioQueueInputCallbackBlock _Nonnull inCallbackBlock ); ``` |

Modified [AudioQueueNewOutput()](https://developer.apple.com/documentation/audiotoolbox/1503207-audioqueuenewoutput)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AudioQueueNewOutput (     const AudioStreamBasicDescription *inFormat,     AudioQueueOutputCallback inCallbackProc,     void *inUserData,     CFRunLoopRef inCallbackRunLoop,     CFStringRef inCallbackRunLoopMode,     UInt32 inFlags,     AudioQueueRef *outAQ ); ``` |
| To | ``` OSStatus AudioQueueNewOutput (     const AudioStreamBasicDescription * _Nonnull inFormat,     AudioQueueOutputCallback _Nonnull inCallbackProc,     void * _Nullable inUserData,     CFRunLoopRef _Nullable inCallbackRunLoop,     CFStringRef _Nullable inCallbackRunLoopMode,     UInt32 inFlags,     AudioQueueRef  _Nullable * _Nonnull outAQ ); ``` |

Modified [AudioQueueNewOutputWithDispatchQueue()](https://developer.apple.com/documentation/audiotoolbox/1503124-audioqueuenewoutputwithdispatchq)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AudioQueueNewOutputWithDispatchQueue (     AudioQueueRef *outAQ,     const AudioStreamBasicDescription *inFormat,     UInt32 inFlags,     dispatch_queue_t inCallbackDispatchQueue,     AudioQueueOutputCallbackBlock inCallbackBlock ); ``` |
| To | ``` OSStatus AudioQueueNewOutputWithDispatchQueue (     AudioQueueRef  _Nullable * _Nonnull outAQ,     const AudioStreamBasicDescription * _Nonnull inFormat,     UInt32 inFlags,     dispatch_queue_t _Nonnull inCallbackDispatchQueue,     AudioQueueOutputCallbackBlock _Nonnull inCallbackBlock ); ``` |

Modified [AudioQueueOfflineRender()](https://developer.apple.com/documentation/audiotoolbox/1502237-audioqueueofflinerender)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AudioQueueOfflineRender (     AudioQueueRef inAQ,     const AudioTimeStamp *inTimestamp,     AudioQueueBufferRef ioBuffer,     UInt32 inNumberFrames ); ``` |
| To | ``` OSStatus AudioQueueOfflineRender (     AudioQueueRef _Nonnull inAQ,     const AudioTimeStamp * _Nonnull inTimestamp,     AudioQueueBufferRef _Nonnull ioBuffer,     UInt32 inNumberFrames ); ``` |

Modified [AudioQueuePause()](https://developer.apple.com/documentation/audiotoolbox/1502109-audioqueuepause)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AudioQueuePause (     AudioQueueRef inAQ ); ``` |
| To | ``` OSStatus AudioQueuePause (     AudioQueueRef _Nonnull inAQ ); ``` |

Modified [AudioQueuePrime()](https://developer.apple.com/documentation/audiotoolbox/1503220-audioqueueprime)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AudioQueuePrime (     AudioQueueRef inAQ,     UInt32 inNumberOfFramesToPrepare,     UInt32 *outNumberOfFramesPrepared ); ``` |
| To | ``` OSStatus AudioQueuePrime (     AudioQueueRef _Nonnull inAQ,     UInt32 inNumberOfFramesToPrepare,     UInt32 * _Nullable outNumberOfFramesPrepared ); ``` |

Modified [AudioQueueProcessingTapDispose()](https://developer.apple.com/documentation/audiotoolbox/1502310-audioqueueprocessingtapdispose)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AudioQueueProcessingTapDispose (     AudioQueueProcessingTapRef inAQTap ); ``` |
| To | ``` OSStatus AudioQueueProcessingTapDispose (     AudioQueueProcessingTapRef _Nonnull inAQTap ); ``` |

Modified [AudioQueueProcessingTapGetQueueTime()](https://developer.apple.com/documentation/audiotoolbox/1502087-audioqueueprocessingtapgetqueuet)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AudioQueueProcessingTapGetQueueTime (     AudioQueueProcessingTapRef inAQTap,     Float64 *outQueueSampleTime,     UInt32 *outQueueFrameCount ); ``` |
| To | ``` OSStatus AudioQueueProcessingTapGetQueueTime (     AudioQueueProcessingTapRef _Nonnull inAQTap,     Float64 * _Nonnull outQueueSampleTime,     UInt32 * _Nonnull outQueueFrameCount ); ``` |

Modified [AudioQueueProcessingTapGetSourceAudio()](https://developer.apple.com/documentation/audiotoolbox/1502107-audioqueueprocessingtapgetsource)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AudioQueueProcessingTapGetSourceAudio (     AudioQueueProcessingTapRef inAQTap,     UInt32 inNumberFrames,     AudioTimeStamp *ioTimeStamp,     UInt32 *outFlags,     UInt32 *outNumberFrames,     AudioBufferList *ioData ); ``` |
| To | ``` OSStatus AudioQueueProcessingTapGetSourceAudio (     AudioQueueProcessingTapRef _Nonnull inAQTap,     UInt32 inNumberFrames,     AudioTimeStamp * _Nonnull ioTimeStamp,     AudioQueueProcessingTapFlags * _Nonnull outFlags,     UInt32 * _Nonnull outNumberFrames,     AudioBufferList * _Nonnull ioData ); ``` |

Modified [AudioQueueProcessingTapNew()](https://developer.apple.com/documentation/audiotoolbox/1503209-audioqueueprocessingtapnew)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AudioQueueProcessingTapNew (     AudioQueueRef inAQ,     AudioQueueProcessingTapCallback inCallback,     void *inClientData,     UInt32 inFlags,     UInt32 *outMaxFrames,     AudioStreamBasicDescription *outProcessingFormat,     AudioQueueProcessingTapRef *outAQTap ); ``` |
| To | ``` OSStatus AudioQueueProcessingTapNew (     AudioQueueRef _Nonnull inAQ,     AudioQueueProcessingTapCallback _Nonnull inCallback,     void * _Nullable inClientData,     AudioQueueProcessingTapFlags inFlags,     UInt32 * _Nonnull outMaxFrames,     AudioStreamBasicDescription * _Nonnull outProcessingFormat,     AudioQueueProcessingTapRef  _Nullable * _Nonnull outAQTap ); ``` |

Modified [AudioQueueRemovePropertyListener()](https://developer.apple.com/documentation/audiotoolbox/1502357-audioqueueremovepropertylistener)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AudioQueueRemovePropertyListener (     AudioQueueRef inAQ,     AudioQueuePropertyID inID,     AudioQueuePropertyListenerProc inProc,     void *inUserData ); ``` |
| To | ``` OSStatus AudioQueueRemovePropertyListener (     AudioQueueRef _Nonnull inAQ,     AudioQueuePropertyID inID,     AudioQueuePropertyListenerProc _Nonnull inProc,     void * _Nullable inUserData ); ``` |

Modified [AudioQueueReset()](https://developer.apple.com/documentation/audiotoolbox/1502329-audioqueuereset)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AudioQueueReset (     AudioQueueRef inAQ ); ``` |
| To | ``` OSStatus AudioQueueReset (     AudioQueueRef _Nonnull inAQ ); ``` |

Modified [AudioQueueSetOfflineRenderFormat()](https://developer.apple.com/documentation/audiotoolbox/1502289-audioqueuesetofflinerenderformat)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AudioQueueSetOfflineRenderFormat (     AudioQueueRef inAQ,     const AudioStreamBasicDescription *inFormat,     const AudioChannelLayout *inLayout ); ``` |
| To | ``` OSStatus AudioQueueSetOfflineRenderFormat (     AudioQueueRef _Nonnull inAQ,     const AudioStreamBasicDescription * _Nullable inFormat,     const AudioChannelLayout * _Nullable inLayout ); ``` |

Modified [AudioQueueSetParameter()](https://developer.apple.com/documentation/audiotoolbox/1503293-audioqueuesetparameter)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AudioQueueSetParameter (     AudioQueueRef inAQ,     AudioQueueParameterID inParamID,     AudioQueueParameterValue inValue ); ``` |
| To | ``` OSStatus AudioQueueSetParameter (     AudioQueueRef _Nonnull inAQ,     AudioQueueParameterID inParamID,     AudioQueueParameterValue inValue ); ``` |

Modified [AudioQueueSetProperty()](https://developer.apple.com/documentation/audiotoolbox/1503282-audioqueuesetproperty)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AudioQueueSetProperty (     AudioQueueRef inAQ,     AudioQueuePropertyID inID,     const void *inData,     UInt32 inDataSize ); ``` |
| To | ``` OSStatus AudioQueueSetProperty (     AudioQueueRef _Nonnull inAQ,     AudioQueuePropertyID inID,     const void * _Nonnull inData,     UInt32 inDataSize ); ``` |

Modified [AudioQueueStart()](https://developer.apple.com/documentation/audiotoolbox/1502689-audioqueuestart)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AudioQueueStart (     AudioQueueRef inAQ,     const AudioTimeStamp *inStartTime ); ``` |
| To | ``` OSStatus AudioQueueStart (     AudioQueueRef _Nonnull inAQ,     const AudioTimeStamp * _Nullable inStartTime ); ``` |

Modified [AudioQueueStop()](https://developer.apple.com/documentation/audiotoolbox/1501970-audioqueuestop)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AudioQueueStop (     AudioQueueRef inAQ,     Boolean inImmediate ); ``` |
| To | ``` OSStatus AudioQueueStop (     AudioQueueRef _Nonnull inAQ,     Boolean inImmediate ); ``` |

#### AudioServices.h

Added [AudioServicesPlayAlertSoundWithCompletion()](https://developer.apple.com/documentation/audiotoolbox/1405238-audioservicesplayalertsoundwithc)Added [AudioServicesPlaySystemSoundWithCompletion()](https://developer.apple.com/documentation/audiotoolbox/1405210-audioservicesplaysystemsoundwith)Added #def AudioToolbox_AudioServices_hModified [AudioHardwareServiceAddPropertyListener()](https://developer.apple.com/documentation/audiotoolbox/1405236-audiohardwareserviceaddpropertyl)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` OSStatus AudioHardwareServiceAddPropertyListener (     AudioObjectID inObjectID,     const AudioObjectPropertyAddress *inAddress,     AudioObjectPropertyListenerProc inListener,     void *inClientData ); ``` | -- |
| To | ``` OSStatus AudioHardwareServiceAddPropertyListener (     AudioObjectID inObjectID,     const AudioObjectPropertyAddress * _Nonnull inAddress,     AudioObjectPropertyListenerProc _Nonnull inListener,     void * _Nonnull inClientData ); ``` | OS X 10.11 |

Modified [AudioHardwareServiceGetPropertyData()](https://developer.apple.com/documentation/audiotoolbox/1405234-audiohardwareservicegetpropertyd)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` OSStatus AudioHardwareServiceGetPropertyData (     AudioObjectID inObjectID,     const AudioObjectPropertyAddress *inAddress,     UInt32 inQualifierDataSize,     const void *inQualifierData,     UInt32 *ioDataSize,     void *outData ); ``` | -- |
| To | ``` OSStatus AudioHardwareServiceGetPropertyData (     AudioObjectID inObjectID,     const AudioObjectPropertyAddress * _Nonnull inAddress,     UInt32 inQualifierDataSize,     const void * _Nonnull inQualifierData,     UInt32 * _Nonnull ioDataSize,     void * _Nonnull outData ); ``` | OS X 10.11 |

Modified [AudioHardwareServiceGetPropertyDataSize()](https://developer.apple.com/documentation/audiotoolbox/1405196-audiohardwareservicegetpropertyd)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` OSStatus AudioHardwareServiceGetPropertyDataSize (     AudioObjectID inObjectID,     const AudioObjectPropertyAddress *inAddress,     UInt32 inQualifierDataSize,     const void *inQualifierData,     UInt32 *outDataSize ); ``` | -- |
| To | ``` OSStatus AudioHardwareServiceGetPropertyDataSize (     AudioObjectID inObjectID,     const AudioObjectPropertyAddress * _Nonnull inAddress,     UInt32 inQualifierDataSize,     const void * _Nonnull inQualifierData,     UInt32 * _Nonnull outDataSize ); ``` | OS X 10.11 |

Modified [AudioHardwareServiceHasProperty()](https://developer.apple.com/documentation/audiotoolbox/1405224-audiohardwareservicehasproperty)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` Boolean AudioHardwareServiceHasProperty (     AudioObjectID inObjectID,     const AudioObjectPropertyAddress *inAddress ); ``` | -- |
| To | ``` Boolean AudioHardwareServiceHasProperty (     AudioObjectID inObjectID,     const AudioObjectPropertyAddress * _Nonnull inAddress ); ``` | OS X 10.11 |

Modified [AudioHardwareServiceIsPropertySettable()](https://developer.apple.com/documentation/audiotoolbox/1405212-audiohardwareserviceispropertyse)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` OSStatus AudioHardwareServiceIsPropertySettable (     AudioObjectID inObjectID,     const AudioObjectPropertyAddress *inAddress,     Boolean *outIsSettable ); ``` | -- |
| To | ``` OSStatus AudioHardwareServiceIsPropertySettable (     AudioObjectID inObjectID,     const AudioObjectPropertyAddress * _Nonnull inAddress,     Boolean * _Nonnull outIsSettable ); ``` | OS X 10.11 |

Modified [AudioHardwareServiceRemovePropertyListener()](https://developer.apple.com/documentation/audiotoolbox/1405266-audiohardwareserviceremoveproper)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` OSStatus AudioHardwareServiceRemovePropertyListener (     AudioObjectID inObjectID,     const AudioObjectPropertyAddress *inAddress,     AudioObjectPropertyListenerProc inListener,     void *inClientData ); ``` | -- |
| To | ``` OSStatus AudioHardwareServiceRemovePropertyListener (     AudioObjectID inObjectID,     const AudioObjectPropertyAddress * _Nonnull inAddress,     AudioObjectPropertyListenerProc _Nonnull inListener,     void * _Nonnull inClientData ); ``` | OS X 10.11 |

Modified [AudioHardwareServiceSetPropertyData()](https://developer.apple.com/documentation/audiotoolbox/1405250-audiohardwareservicesetpropertyd)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` OSStatus AudioHardwareServiceSetPropertyData (     AudioObjectID inObjectID,     const AudioObjectPropertyAddress *inAddress,     UInt32 inQualifierDataSize,     const void *inQualifierData,     UInt32 inDataSize,     const void *inData ); ``` | -- |
| To | ``` OSStatus AudioHardwareServiceSetPropertyData (     AudioObjectID inObjectID,     const AudioObjectPropertyAddress * _Nonnull inAddress,     UInt32 inQualifierDataSize,     const void * _Nonnull inQualifierData,     UInt32 inDataSize,     const void * _Nonnull inData ); ``` | OS X 10.11 |

Modified [AudioServicesAddSystemSoundCompletion()](https://developer.apple.com/documentation/audiotoolbox/1405244-audioservicesaddsystemsoundcompl)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AudioServicesAddSystemSoundCompletion (     SystemSoundID inSystemSoundID,     CFRunLoopRef inRunLoop,     CFStringRef inRunLoopMode,     AudioServicesSystemSoundCompletionProc inCompletionRoutine,     void *inClientData ); ``` |
| To | ``` OSStatus AudioServicesAddSystemSoundCompletion (     SystemSoundID inSystemSoundID,     CFRunLoopRef _Nullable inRunLoop,     CFStringRef _Nullable inRunLoopMode,     AudioServicesSystemSoundCompletionProc _Nonnull inCompletionRoutine,     void * _Nullable inClientData ); ``` |

Modified [AudioServicesCreateSystemSoundID()](https://developer.apple.com/documentation/audiotoolbox/1405240-audioservicescreatesystemsoundid)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AudioServicesCreateSystemSoundID (     CFURLRef inFileURL,     SystemSoundID *outSystemSoundID ); ``` |
| To | ``` OSStatus AudioServicesCreateSystemSoundID (     CFURLRef _Nonnull inFileURL,     SystemSoundID * _Nonnull outSystemSoundID ); ``` |

Modified [AudioServicesGetProperty()](https://developer.apple.com/documentation/audiotoolbox/1405206-audioservicesgetproperty)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AudioServicesGetProperty (     AudioServicesPropertyID inPropertyID,     UInt32 inSpecifierSize,     const void *inSpecifier,     UInt32 *ioPropertyDataSize,     void *outPropertyData ); ``` |
| To | ``` OSStatus AudioServicesGetProperty (     AudioServicesPropertyID inPropertyID,     UInt32 inSpecifierSize,     const void * _Nullable inSpecifier,     UInt32 * _Nonnull ioPropertyDataSize,     void * _Nullable outPropertyData ); ``` |

Modified [AudioServicesGetPropertyInfo()](https://developer.apple.com/documentation/audiotoolbox/1405258-audioservicesgetpropertyinfo)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AudioServicesGetPropertyInfo (     AudioServicesPropertyID inPropertyID,     UInt32 inSpecifierSize,     const void *inSpecifier,     UInt32 *outPropertyDataSize,     Boolean *outWritable ); ``` |
| To | ``` OSStatus AudioServicesGetPropertyInfo (     AudioServicesPropertyID inPropertyID,     UInt32 inSpecifierSize,     const void * _Nullable inSpecifier,     UInt32 * _Nullable outPropertyDataSize,     Boolean * _Nullable outWritable ); ``` |

Modified [AudioServicesSetProperty()](https://developer.apple.com/documentation/audiotoolbox/1405226-audioservicessetproperty)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AudioServicesSetProperty (     AudioServicesPropertyID inPropertyID,     UInt32 inSpecifierSize,     const void *inSpecifier,     UInt32 inPropertyDataSize,     const void *inPropertyData ); ``` |
| To | ``` OSStatus AudioServicesSetProperty (     AudioServicesPropertyID inPropertyID,     UInt32 inSpecifierSize,     const void * _Nullable inSpecifier,     UInt32 inPropertyDataSize,     const void * _Nonnull inPropertyData ); ``` |

#### AudioToolbox.h

Added #def AudioToolbox_AudioToolbox_hModified [CAShow()](https://developer.apple.com/documentation/audiotoolbox/1475988-cashow)

|  | Declaration |
| --- | --- |
| From | ``` void CAShow (     void *inObject ); ``` |
| To | ``` void CAShow (     void * _Nonnull inObject ); ``` |

Modified [CAShowFile()](https://developer.apple.com/documentation/audiotoolbox/1475990-cashowfile)

|  | Declaration |
| --- | --- |
| From | ``` void CAShowFile (     void *inObject,     FILE *inFile ); ``` |
| To | ``` void CAShowFile (     void * _Nonnull inObject,     FILE * _Nonnull inFile ); ``` |

Modified [CopyInstrumentInfoFromSoundBank()](https://developer.apple.com/documentation/audiotoolbox/1475995-copyinstrumentinfofromsoundbank)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus CopyInstrumentInfoFromSoundBank (     CFURLRef inURL,     CFArrayRef *outInstrumentInfo ); ``` |
| To | ``` OSStatus CopyInstrumentInfoFromSoundBank (     CFURLRef _Nonnull inURL,     CFArrayRef  _Nullable * _Nonnull outInstrumentInfo ); ``` |

Modified [CopyNameFromSoundBank()](https://developer.apple.com/documentation/audiotoolbox/1475986-copynamefromsoundbank)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus CopyNameFromSoundBank (     CFURLRef inURL,     CFStringRef *outName ); ``` |
| To | ``` OSStatus CopyNameFromSoundBank (     CFURLRef _Nonnull inURL,     CFStringRef  _Nullable * _Nonnull outName ); ``` |

Modified [GetNameFromSoundBank()](https://developer.apple.com/documentation/audiotoolbox/1475999-getnamefromsoundbank)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus GetNameFromSoundBank (     const struct FSRef *inSoundBankRef,     CFStringRef *outName ); ``` |
| To | ``` OSStatus GetNameFromSoundBank (     const struct FSRef * _Nonnull inSoundBankRef,     CFStringRef  _Nullable * _Nonnull outName ); ``` |

#### AudioUnitUtilities.h

Added #def AudioToolbox_AudioUnitUtilities_hModified [AUEventListenerAddEventType()](https://developer.apple.com/documentation/audiotoolbox/1501987-aueventlisteneraddeventtype)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AUEventListenerAddEventType (     AUEventListenerRef inListener,     void *inObject,     const AudioUnitEvent *inEvent ); ``` |
| To | ``` OSStatus AUEventListenerAddEventType (     AUEventListenerRef _Nonnull inListener,     void * _Nullable inObject,     const AudioUnitEvent * _Nonnull inEvent ); ``` |

Modified [AUEventListenerCreate()](https://developer.apple.com/documentation/audiotoolbox/1503194-aueventlistenercreate)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AUEventListenerCreate (     AUEventListenerProc inProc,     void *inUserData,     CFRunLoopRef inRunLoop,     CFStringRef inRunLoopMode,     Float32 inNotificationInterval,     Float32 inValueChangeGranularity,     AUEventListenerRef *outListener ); ``` |
| To | ``` OSStatus AUEventListenerCreate (     AUEventListenerProc _Nonnull inProc,     void * _Nullable inUserData,     CFRunLoopRef _Nullable inRunLoop,     CFStringRef _Nullable inRunLoopMode,     Float32 inNotificationInterval,     Float32 inValueChangeGranularity,     AUEventListenerRef  _Nullable * _Nonnull outListener ); ``` |

Modified [AUEventListenerCreateWithDispatchQueue()](https://developer.apple.com/documentation/audiotoolbox/1503202-aueventlistenercreatewithdispatc)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AUEventListenerCreateWithDispatchQueue (     AUEventListenerRef *outListener,     Float32 inNotificationInterval,     Float32 inValueChangeGranularity,     dispatch_queue_t inDispatchQueue,     AUEventListenerBlock inBlock ); ``` |
| To | ``` OSStatus AUEventListenerCreateWithDispatchQueue (     AUEventListenerRef  _Nullable * _Nonnull outListener,     Float32 inNotificationInterval,     Float32 inValueChangeGranularity,     dispatch_queue_t _Nonnull inDispatchQueue,     AUEventListenerBlock _Nonnull inBlock ); ``` |

Modified [AUEventListenerNotify()](https://developer.apple.com/documentation/audiotoolbox/1503031-aueventlistenernotify)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AUEventListenerNotify (     AUEventListenerRef inSendingListener,     void *inSendingObject,     const AudioUnitEvent *inEvent ); ``` |
| To | ``` OSStatus AUEventListenerNotify (     AUEventListenerRef _Nullable inSendingListener,     void * _Nullable inSendingObject,     const AudioUnitEvent * _Nonnull inEvent ); ``` |

Modified [AUEventListenerRemoveEventType()](https://developer.apple.com/documentation/audiotoolbox/1502857-aueventlistenerremoveeventtype)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AUEventListenerRemoveEventType (     AUEventListenerRef inListener,     void *inObject,     const AudioUnitEvent *inEvent ); ``` |
| To | ``` OSStatus AUEventListenerRemoveEventType (     AUEventListenerRef _Nonnull inListener,     void * _Nullable inObject,     const AudioUnitEvent * _Nonnull inEvent ); ``` |

Modified [AUListenerAddParameter()](https://developer.apple.com/documentation/audiotoolbox/1503093-aulisteneraddparameter)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AUListenerAddParameter (     AUParameterListenerRef inListener,     void *inObject,     const AudioUnitParameter *inParameter ); ``` |
| To | ``` OSStatus AUListenerAddParameter (     AUParameterListenerRef _Nonnull inListener,     void * _Nullable inObject,     const AudioUnitParameter * _Nonnull inParameter ); ``` |

Modified [AUListenerCreate()](https://developer.apple.com/documentation/audiotoolbox/1503369-aulistenercreate)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AUListenerCreate (     AUParameterListenerProc inProc,     void *inUserData,     CFRunLoopRef inRunLoop,     CFStringRef inRunLoopMode,     Float32 inNotificationInterval,     AUParameterListenerRef *outListener ); ``` |
| To | ``` OSStatus AUListenerCreate (     AUParameterListenerProc _Nonnull inProc,     void * _Nonnull inUserData,     CFRunLoopRef _Nullable inRunLoop,     CFStringRef _Nullable inRunLoopMode,     Float32 inNotificationInterval,     AUParameterListenerRef  _Nullable * _Nonnull outListener ); ``` |

Modified [AUListenerCreateWithDispatchQueue()](https://developer.apple.com/documentation/audiotoolbox/1502393-aulistenercreatewithdispatchqueu)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AUListenerCreateWithDispatchQueue (     AUParameterListenerRef *outListener,     Float32 inNotificationInterval,     dispatch_queue_t inDispatchQueue,     AUParameterListenerBlock inBlock ); ``` |
| To | ``` OSStatus AUListenerCreateWithDispatchQueue (     AUParameterListenerRef  _Nullable * _Nonnull outListener,     Float32 inNotificationInterval,     dispatch_queue_t _Nonnull inDispatchQueue,     AUParameterListenerBlock _Nonnull inBlock ); ``` |

Modified [AUListenerDispose()](https://developer.apple.com/documentation/audiotoolbox/1502283-aulistenerdispose)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AUListenerDispose (     AUParameterListenerRef inListener ); ``` |
| To | ``` OSStatus AUListenerDispose (     AUParameterListenerRef _Nonnull inListener ); ``` |

Modified [AUListenerRemoveParameter()](https://developer.apple.com/documentation/audiotoolbox/1501781-aulistenerremoveparameter)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AUListenerRemoveParameter (     AUParameterListenerRef inListener,     void *inObject,     const AudioUnitParameter *inParameter ); ``` |
| To | ``` OSStatus AUListenerRemoveParameter (     AUParameterListenerRef _Nonnull inListener,     void * _Nullable inObject,     const AudioUnitParameter * _Nonnull inParameter ); ``` |

Modified [AUParameterFormatValue()](https://developer.apple.com/documentation/audiotoolbox/1502901-auparameterformatvalue)

|  | Declaration |
| --- | --- |
| From | ``` char * AUParameterFormatValue (     Float64 inParameterValue,     const AudioUnitParameter *inParameter,     char *inTextBuffer,     UInt32 inDigits ); ``` |
| To | ``` char * _Nonnull AUParameterFormatValue (     Float64 inParameterValue,     const AudioUnitParameter * _Nonnull inParameter,     char * _Nonnull inTextBuffer,     UInt32 inDigits ); ``` |

Modified [AUParameterListenerNotify()](https://developer.apple.com/documentation/audiotoolbox/1501642-auparameterlistenernotify)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AUParameterListenerNotify (     AUParameterListenerRef inSendingListener,     void *inSendingObject,     const AudioUnitParameter *inParameter ); ``` |
| To | ``` OSStatus AUParameterListenerNotify (     AUParameterListenerRef _Nullable inSendingListener,     void * _Nullable inSendingObject,     const AudioUnitParameter * _Nonnull inParameter ); ``` |

Modified [AUParameterSet()](https://developer.apple.com/documentation/audiotoolbox/1502261-auparameterset)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AUParameterSet (     AUParameterListenerRef inSendingListener,     void *inSendingObject,     const AudioUnitParameter *inParameter,     AudioUnitParameterValue inValue,     UInt32 inBufferOffsetInFrames ); ``` |
| To | ``` OSStatus AUParameterSet (     AUParameterListenerRef _Nullable inSendingListener,     void * _Nullable inSendingObject,     const AudioUnitParameter * _Nonnull inParameter,     AudioUnitParameterValue inValue,     UInt32 inBufferOffsetInFrames ); ``` |

Modified [AUParameterValueFromLinear()](https://developer.apple.com/documentation/audiotoolbox/1502675-auparametervaluefromlinear)

|  | Declaration |
| --- | --- |
| From | ``` AudioUnitParameterValue AUParameterValueFromLinear (     Float32 inLinearValue,     const AudioUnitParameter *inParameter ); ``` |
| To | ``` AudioUnitParameterValue AUParameterValueFromLinear (     Float32 inLinearValue,     const AudioUnitParameter * _Nonnull inParameter ); ``` |

Modified [AUParameterValueToLinear()](https://developer.apple.com/documentation/audiotoolbox/1502508-auparametervaluetolinear)

|  | Declaration |
| --- | --- |
| From | ``` Float32 AUParameterValueToLinear (     AudioUnitParameterValue inParameterValue,     const AudioUnitParameter *inParameter ); ``` |
| To | ``` Float32 AUParameterValueToLinear (     AudioUnitParameterValue inParameterValue,     const AudioUnitParameter * _Nonnull inParameter ); ``` |

#### AUGraph.h

Added #def AudioToolbox_AUGraph_hModified [AUGraphAddNode()](https://developer.apple.com/documentation/audiotoolbox/1501671-augraphaddnode)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AUGraphAddNode (     AUGraph inGraph,     const AudioComponentDescription *inDescription,     AUNode *outNode ); ``` |
| To | ``` OSStatus AUGraphAddNode (     AUGraph _Nonnull inGraph,     const AudioComponentDescription * _Nonnull inDescription,     AUNode * _Nonnull outNode ); ``` |

Modified [AUGraphAddRenderNotify()](https://developer.apple.com/documentation/audiotoolbox/1501636-augraphaddrendernotify)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AUGraphAddRenderNotify (     AUGraph inGraph,     AURenderCallback inCallback,     void *inRefCon ); ``` |
| To | ``` OSStatus AUGraphAddRenderNotify (     AUGraph _Nonnull inGraph,     AURenderCallback _Nonnull inCallback,     void * _Nullable inRefCon ); ``` |

Modified [AUGraphClearConnections()](https://developer.apple.com/documentation/audiotoolbox/1501850-augraphclearconnections)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AUGraphClearConnections (     AUGraph inGraph ); ``` |
| To | ``` OSStatus AUGraphClearConnections (     AUGraph _Nonnull inGraph ); ``` |

Modified [AUGraphClose()](https://developer.apple.com/documentation/audiotoolbox/1503109-augraphclose)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AUGraphClose (     AUGraph inGraph ); ``` |
| To | ``` OSStatus AUGraphClose (     AUGraph _Nonnull inGraph ); ``` |

Modified [AUGraphConnectNodeInput()](https://developer.apple.com/documentation/audiotoolbox/1502636-augraphconnectnodeinput)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AUGraphConnectNodeInput (     AUGraph inGraph,     AUNode inSourceNode,     UInt32 inSourceOutputNumber,     AUNode inDestNode,     UInt32 inDestInputNumber ); ``` |
| To | ``` OSStatus AUGraphConnectNodeInput (     AUGraph _Nonnull inGraph,     AUNode inSourceNode,     UInt32 inSourceOutputNumber,     AUNode inDestNode,     UInt32 inDestInputNumber ); ``` |

Modified [AUGraphCountNodeConnections()](https://developer.apple.com/documentation/audiotoolbox/1537634-augraphcountnodeconnections)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AUGraphCountNodeConnections (     AUGraph inGraph,     AUNode inNode,     UInt32 *outNumConnections ); ``` |
| To | ``` OSStatus AUGraphCountNodeConnections (     AUGraph _Nonnull inGraph,     AUNode inNode,     UInt32 * _Nonnull outNumConnections ); ``` |

Modified [AUGraphCountNodeInteractions()](https://developer.apple.com/documentation/audiotoolbox/1502094-augraphcountnodeinteractions)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AUGraphCountNodeInteractions (     AUGraph inGraph,     AUNode inNode,     UInt32 *outNumInteractions ); ``` |
| To | ``` OSStatus AUGraphCountNodeInteractions (     AUGraph _Nonnull inGraph,     AUNode inNode,     UInt32 * _Nonnull outNumInteractions ); ``` |

Modified [AUGraphDisconnectNodeInput()](https://developer.apple.com/documentation/audiotoolbox/1502008-augraphdisconnectnodeinput)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AUGraphDisconnectNodeInput (     AUGraph inGraph,     AUNode inDestNode,     UInt32 inDestInputNumber ); ``` |
| To | ``` OSStatus AUGraphDisconnectNodeInput (     AUGraph _Nonnull inGraph,     AUNode inDestNode,     UInt32 inDestInputNumber ); ``` |

Modified [AUGraphGetConnectionInfo()](https://developer.apple.com/documentation/audiotoolbox/1537629-augraphgetconnectioninfo)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AUGraphGetConnectionInfo (     AUGraph inGraph,     UInt32 inConnectionIndex,     AUNode *outSourceNode,     UInt32 *outSourceOutputNumber,     AUNode *outDestNode,     UInt32 *outDestInputNumber ); ``` |
| To | ``` OSStatus AUGraphGetConnectionInfo (     AUGraph _Nonnull inGraph,     UInt32 inConnectionIndex,     AUNode * _Nonnull outSourceNode,     UInt32 * _Nonnull outSourceOutputNumber,     AUNode * _Nonnull outDestNode,     UInt32 * _Nonnull outDestInputNumber ); ``` |

Modified [AUGraphGetCPULoad()](https://developer.apple.com/documentation/audiotoolbox/1501618-augraphgetcpuload)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AUGraphGetCPULoad (     AUGraph inGraph,     Float32 *outAverageCPULoad ); ``` |
| To | ``` OSStatus AUGraphGetCPULoad (     AUGraph _Nonnull inGraph,     Float32 * _Nonnull outAverageCPULoad ); ``` |

Modified [AUGraphGetIndNode()](https://developer.apple.com/documentation/audiotoolbox/1502903-augraphgetindnode)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AUGraphGetIndNode (     AUGraph inGraph,     UInt32 inIndex,     AUNode *outNode ); ``` |
| To | ``` OSStatus AUGraphGetIndNode (     AUGraph _Nonnull inGraph,     UInt32 inIndex,     AUNode * _Nonnull outNode ); ``` |

Modified [AUGraphGetInteractionInfo()](https://developer.apple.com/documentation/audiotoolbox/1501848-augraphgetinteractioninfo)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AUGraphGetInteractionInfo (     AUGraph inGraph,     UInt32 inInteractionIndex,     AUNodeInteraction *outInteraction ); ``` |
| To | ``` OSStatus AUGraphGetInteractionInfo (     AUGraph _Nonnull inGraph,     UInt32 inInteractionIndex,     AUNodeInteraction * _Nonnull outInteraction ); ``` |

Modified [AUGraphGetMaxCPULoad()](https://developer.apple.com/documentation/audiotoolbox/1502201-augraphgetmaxcpuload)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AUGraphGetMaxCPULoad (     AUGraph inGraph,     Float32 *outMaxLoad ); ``` |
| To | ``` OSStatus AUGraphGetMaxCPULoad (     AUGraph _Nonnull inGraph,     Float32 * _Nonnull outMaxLoad ); ``` |

Modified [AUGraphGetNodeConnections()](https://developer.apple.com/documentation/audiotoolbox/1537626-augraphgetnodeconnections)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AUGraphGetNodeConnections (     AUGraph inGraph,     AUNode inNode,     AudioUnitNodeConnection *outConnections,     UInt32 *ioNumConnections ); ``` |
| To | ``` OSStatus AUGraphGetNodeConnections (     AUGraph _Nonnull inGraph,     AUNode inNode,     AudioUnitNodeConnection * _Nonnull outConnections,     UInt32 * _Nonnull ioNumConnections ); ``` |

Modified [AUGraphGetNodeCount()](https://developer.apple.com/documentation/audiotoolbox/1503284-augraphgetnodecount)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AUGraphGetNodeCount (     AUGraph inGraph,     UInt32 *outNumberOfNodes ); ``` |
| To | ``` OSStatus AUGraphGetNodeCount (     AUGraph _Nonnull inGraph,     UInt32 * _Nonnull outNumberOfNodes ); ``` |

Modified [AUGraphGetNodeInfo()](https://developer.apple.com/documentation/audiotoolbox/1537614-augraphgetnodeinfo)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AUGraphGetNodeInfo (     AUGraph inGraph,     AUNode inNode,     struct ComponentDescription *outDescription,     UInt32 *outClassDataSize,     void **outClassData,     AudioUnit *outAudioUnit ); ``` |
| To | ``` OSStatus AUGraphGetNodeInfo (     AUGraph _Nonnull inGraph,     AUNode inNode,     struct ComponentDescription * _Nonnull outDescription,     UInt32 * _Nonnull outClassDataSize,     void * _Nullable * _Nullable outClassData,     AudioUnit  _Nullable * _Nullable outAudioUnit ); ``` |

Modified [AUGraphGetNodeInfoSubGraph()](https://developer.apple.com/documentation/audiotoolbox/1503000-augraphgetnodeinfosubgraph)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AUGraphGetNodeInfoSubGraph (     const AUGraph inGraph,     AUNode inNode,     AUGraph *outSubGraph ); ``` |
| To | ``` OSStatus AUGraphGetNodeInfoSubGraph (     const AUGraph _Nonnull inGraph,     AUNode inNode,     AUGraph  _Nullable * _Nonnull outSubGraph ); ``` |

Modified [AUGraphGetNodeInteractions()](https://developer.apple.com/documentation/audiotoolbox/1503077-augraphgetnodeinteractions)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AUGraphGetNodeInteractions (     AUGraph inGraph,     AUNode inNode,     UInt32 *ioNumInteractions,     AUNodeInteraction *outInteractions ); ``` |
| To | ``` OSStatus AUGraphGetNodeInteractions (     AUGraph _Nonnull inGraph,     AUNode inNode,     UInt32 * _Nonnull ioNumInteractions,     AUNodeInteraction * _Nonnull outInteractions ); ``` |

Modified [AUGraphGetNumberOfConnections()](https://developer.apple.com/documentation/audiotoolbox/1537617-augraphgetnumberofconnections)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AUGraphGetNumberOfConnections (     AUGraph inGraph,     UInt32 *outNumConnections ); ``` |
| To | ``` OSStatus AUGraphGetNumberOfConnections (     AUGraph _Nonnull inGraph,     UInt32 * _Nonnull outNumConnections ); ``` |

Modified [AUGraphGetNumberOfInteractions()](https://developer.apple.com/documentation/audiotoolbox/1501599-augraphgetnumberofinteractions)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AUGraphGetNumberOfInteractions (     AUGraph inGraph,     UInt32 *outNumInteractions ); ``` |
| To | ``` OSStatus AUGraphGetNumberOfInteractions (     AUGraph _Nonnull inGraph,     UInt32 * _Nonnull outNumInteractions ); ``` |

Modified [AUGraphInitialize()](https://developer.apple.com/documentation/audiotoolbox/1503251-augraphinitialize)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AUGraphInitialize (     AUGraph inGraph ); ``` |
| To | ``` OSStatus AUGraphInitialize (     AUGraph _Nonnull inGraph ); ``` |

Modified [AUGraphIsInitialized()](https://developer.apple.com/documentation/audiotoolbox/1502424-augraphisinitialized)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AUGraphIsInitialized (     AUGraph inGraph,     Boolean *outIsInitialized ); ``` |
| To | ``` OSStatus AUGraphIsInitialized (     AUGraph _Nonnull inGraph,     Boolean * _Nonnull outIsInitialized ); ``` |

Modified [AUGraphIsNodeSubGraph()](https://developer.apple.com/documentation/audiotoolbox/1502260-augraphisnodesubgraph)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AUGraphIsNodeSubGraph (     const AUGraph inGraph,     AUNode inNode,     Boolean *outFlag ); ``` |
| To | ``` OSStatus AUGraphIsNodeSubGraph (     const AUGraph _Nonnull inGraph,     AUNode inNode,     Boolean * _Nonnull outFlag ); ``` |

Modified [AUGraphIsOpen()](https://developer.apple.com/documentation/audiotoolbox/1502285-augraphisopen)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AUGraphIsOpen (     AUGraph inGraph,     Boolean *outIsOpen ); ``` |
| To | ``` OSStatus AUGraphIsOpen (     AUGraph _Nonnull inGraph,     Boolean * _Nonnull outIsOpen ); ``` |

Modified [AUGraphIsRunning()](https://developer.apple.com/documentation/audiotoolbox/1501730-augraphisrunning)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AUGraphIsRunning (     AUGraph inGraph,     Boolean *outIsRunning ); ``` |
| To | ``` OSStatus AUGraphIsRunning (     AUGraph _Nonnull inGraph,     Boolean * _Nonnull outIsRunning ); ``` |

Modified [AUGraphNewNode()](https://developer.apple.com/documentation/audiotoolbox/1537621-augraphnewnode)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AUGraphNewNode (     AUGraph inGraph,     const struct ComponentDescription *inDescription,     UInt32 inClassDataSize,     const void *inClassData,     AUNode *outNode ); ``` |
| To | ``` OSStatus AUGraphNewNode (     AUGraph _Nonnull inGraph,     const struct ComponentDescription * _Nonnull inDescription,     UInt32 inClassDataSize,     const void * _Nonnull inClassData,     AUNode * _Nonnull outNode ); ``` |

Modified [AUGraphNewNodeSubGraph()](https://developer.apple.com/documentation/audiotoolbox/1502250-augraphnewnodesubgraph)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AUGraphNewNodeSubGraph (     AUGraph inGraph,     AUNode *outNode ); ``` |
| To | ``` OSStatus AUGraphNewNodeSubGraph (     AUGraph _Nonnull inGraph,     AUNode * _Nonnull outNode ); ``` |

Modified [AUGraphNodeInfo()](https://developer.apple.com/documentation/audiotoolbox/1502407-augraphnodeinfo)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AUGraphNodeInfo (     AUGraph inGraph,     AUNode inNode,     AudioComponentDescription *outDescription,     AudioUnit *outAudioUnit ); ``` |
| To | ``` OSStatus AUGraphNodeInfo (     AUGraph _Nonnull inGraph,     AUNode inNode,     AudioComponentDescription * _Nullable outDescription,     AudioUnit  _Nullable * _Nullable outAudioUnit ); ``` |

Modified [AUGraphOpen()](https://developer.apple.com/documentation/audiotoolbox/1502571-augraphopen)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AUGraphOpen (     AUGraph inGraph ); ``` |
| To | ``` OSStatus AUGraphOpen (     AUGraph _Nonnull inGraph ); ``` |

Modified [AUGraphRemoveNode()](https://developer.apple.com/documentation/audiotoolbox/1502439-augraphremovenode)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AUGraphRemoveNode (     AUGraph inGraph,     AUNode inNode ); ``` |
| To | ``` OSStatus AUGraphRemoveNode (     AUGraph _Nonnull inGraph,     AUNode inNode ); ``` |

Modified [AUGraphRemoveRenderNotify()](https://developer.apple.com/documentation/audiotoolbox/1503352-augraphremoverendernotify)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AUGraphRemoveRenderNotify (     AUGraph inGraph,     AURenderCallback inCallback,     void *inRefCon ); ``` |
| To | ``` OSStatus AUGraphRemoveRenderNotify (     AUGraph _Nonnull inGraph,     AURenderCallback _Nonnull inCallback,     void * _Nullable inRefCon ); ``` |

Modified [AUGraphSetNodeInputCallback()](https://developer.apple.com/documentation/audiotoolbox/1501948-augraphsetnodeinputcallback)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AUGraphSetNodeInputCallback (     AUGraph inGraph,     AUNode inDestNode,     UInt32 inDestInputNumber,     const AURenderCallbackStruct *inInputCallback ); ``` |
| To | ``` OSStatus AUGraphSetNodeInputCallback (     AUGraph _Nonnull inGraph,     AUNode inDestNode,     UInt32 inDestInputNumber,     const AURenderCallbackStruct * _Nonnull inInputCallback ); ``` |

Modified [AUGraphStart()](https://developer.apple.com/documentation/audiotoolbox/1502297-augraphstart)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AUGraphStart (     AUGraph inGraph ); ``` |
| To | ``` OSStatus AUGraphStart (     AUGraph _Nonnull inGraph ); ``` |

Modified [AUGraphStop()](https://developer.apple.com/documentation/audiotoolbox/1503233-augraphstop)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AUGraphStop (     AUGraph inGraph ); ``` |
| To | ``` OSStatus AUGraphStop (     AUGraph _Nonnull inGraph ); ``` |

Modified [AUGraphUninitialize()](https://developer.apple.com/documentation/audiotoolbox/1503119-augraphuninitialize)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AUGraphUninitialize (     AUGraph inGraph ); ``` |
| To | ``` OSStatus AUGraphUninitialize (     AUGraph _Nonnull inGraph ); ``` |

Modified [AUGraphUpdate()](https://developer.apple.com/documentation/audiotoolbox/1502855-augraphupdate)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AUGraphUpdate (     AUGraph inGraph,     Boolean *outIsUpdated ); ``` |
| To | ``` OSStatus AUGraphUpdate (     AUGraph _Nonnull inGraph,     Boolean * _Nullable outIsUpdated ); ``` |

Modified [DisposeAUGraph()](https://developer.apple.com/documentation/audiotoolbox/1502806-disposeaugraph)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus DisposeAUGraph (     AUGraph inGraph ); ``` |
| To | ``` OSStatus DisposeAUGraph (     AUGraph _Nonnull inGraph ); ``` |

Modified [NewAUGraph()](https://developer.apple.com/documentation/audiotoolbox/1502296-newaugraph)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus NewAUGraph (     AUGraph *outGraph ); ``` |
| To | ``` OSStatus NewAUGraph (     AUGraph  _Nullable * _Nonnull outGraph ); ``` |

#### AUMIDIController.h

Added #def AudioToolbox_AUMIDIController_h

#### CAFFile.h

Added #def AudioToolbox_CAFFile_hAdded [CAFFormatFlags](https://developer.apple.com/documentation/audiotoolbox/cafformatflags)Added [CAFRegionFlags](https://developer.apple.com/documentation/audiotoolbox/cafregionflags)

#### CoreAudioClock.h

Added #def AudioToolbox_CoreAudioClock_hAdded [kCAClockTimeFormat_AbsoluteSeconds](https://developer.apple.com/documentation/audiotoolbox/caclocktimeformat/kcaclocktimeformat_absoluteseconds)Modified [CAClockAddListener()](https://developer.apple.com/documentation/audiotoolbox/1503156-caclockaddlistener)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus CAClockAddListener (     CAClockRef inCAClock,     CAClockListenerProc inListenerProc,     void *inUserData ); ``` |
| To | ``` OSStatus CAClockAddListener (     CAClockRef _Nonnull inCAClock,     CAClockListenerProc _Nonnull inListenerProc,     void * _Nonnull inUserData ); ``` |

Modified [CAClockArm()](https://developer.apple.com/documentation/audiotoolbox/1501820-caclockarm)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus CAClockArm (     CAClockRef inCAClock ); ``` |
| To | ``` OSStatus CAClockArm (     CAClockRef _Nonnull inCAClock ); ``` |

Modified [CAClockBarBeatTimeToBeats()](https://developer.apple.com/documentation/audiotoolbox/1501885-caclockbarbeattimetobeats)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus CAClockBarBeatTimeToBeats (     CAClockRef inCAClock,     const CABarBeatTime *inBarBeatTime,     CAClockBeats *outBeats ); ``` |
| To | ``` OSStatus CAClockBarBeatTimeToBeats (     CAClockRef _Nonnull inCAClock,     const CABarBeatTime * _Nonnull inBarBeatTime,     CAClockBeats * _Nonnull outBeats ); ``` |

Modified [CAClockBeatsToBarBeatTime()](https://developer.apple.com/documentation/audiotoolbox/1502240-caclockbeatstobarbeattime)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus CAClockBeatsToBarBeatTime (     CAClockRef inCAClock,     CAClockBeats inBeats,     UInt16 inSubbeatDivisor,     CABarBeatTime *outBarBeatTime ); ``` |
| To | ``` OSStatus CAClockBeatsToBarBeatTime (     CAClockRef _Nonnull inCAClock,     CAClockBeats inBeats,     UInt16 inSubbeatDivisor,     CABarBeatTime * _Nonnull outBarBeatTime ); ``` |

Modified [CAClockDisarm()](https://developer.apple.com/documentation/audiotoolbox/1503291-caclockdisarm)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus CAClockDisarm (     CAClockRef inCAClock ); ``` |
| To | ``` OSStatus CAClockDisarm (     CAClockRef _Nonnull inCAClock ); ``` |

Modified [CAClockDispose()](https://developer.apple.com/documentation/audiotoolbox/1503166-caclockdispose)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus CAClockDispose (     CAClockRef inCAClock ); ``` |
| To | ``` OSStatus CAClockDispose (     CAClockRef _Nonnull inCAClock ); ``` |

Modified [CAClockGetCurrentTempo()](https://developer.apple.com/documentation/audiotoolbox/1503295-caclockgetcurrenttempo)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus CAClockGetCurrentTempo (     CAClockRef inCAClock,     CAClockTempo *outTempo,     CAClockTime *outTimestamp ); ``` |
| To | ``` OSStatus CAClockGetCurrentTempo (     CAClockRef _Nonnull inCAClock,     CAClockTempo * _Nonnull outTempo,     CAClockTime * _Nullable outTimestamp ); ``` |

Modified [CAClockGetCurrentTime()](https://developer.apple.com/documentation/audiotoolbox/1502868-caclockgetcurrenttime)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus CAClockGetCurrentTime (     CAClockRef inCAClock,     CAClockTimeFormat inTimeFormat,     CAClockTime *outTime ); ``` |
| To | ``` OSStatus CAClockGetCurrentTime (     CAClockRef _Nonnull inCAClock,     CAClockTimeFormat inTimeFormat,     CAClockTime * _Nonnull outTime ); ``` |

Modified [CAClockGetPlayRate()](https://developer.apple.com/documentation/audiotoolbox/1502951-caclockgetplayrate)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus CAClockGetPlayRate (     CAClockRef inCAClock,     Float64 *outPlayRate ); ``` |
| To | ``` OSStatus CAClockGetPlayRate (     CAClockRef _Nonnull inCAClock,     Float64 * _Nonnull outPlayRate ); ``` |

Modified [CAClockGetProperty()](https://developer.apple.com/documentation/audiotoolbox/1503318-caclockgetproperty)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus CAClockGetProperty (     CAClockRef inCAClock,     CAClockPropertyID inPropertyID,     UInt32 *ioPropertyDataSize,     void *outPropertyData ); ``` |
| To | ``` OSStatus CAClockGetProperty (     CAClockRef _Nonnull inCAClock,     CAClockPropertyID inPropertyID,     UInt32 * _Nonnull ioPropertyDataSize,     void * _Nonnull outPropertyData ); ``` |

Modified [CAClockGetPropertyInfo()](https://developer.apple.com/documentation/audiotoolbox/1501760-caclockgetpropertyinfo)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus CAClockGetPropertyInfo (     CAClockRef inCAClock,     CAClockPropertyID inPropertyID,     UInt32 *outSize,     Boolean *outWritable ); ``` |
| To | ``` OSStatus CAClockGetPropertyInfo (     CAClockRef _Nonnull inCAClock,     CAClockPropertyID inPropertyID,     UInt32 * _Nullable outSize,     Boolean * _Nullable outWritable ); ``` |

Modified [CAClockGetStartTime()](https://developer.apple.com/documentation/audiotoolbox/1501711-caclockgetstarttime)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus CAClockGetStartTime (     CAClockRef inCAClock,     CAClockTimeFormat inTimeFormat,     CAClockTime *outTime ); ``` |
| To | ``` OSStatus CAClockGetStartTime (     CAClockRef _Nonnull inCAClock,     CAClockTimeFormat inTimeFormat,     CAClockTime * _Nonnull outTime ); ``` |

Modified [CAClockNew()](https://developer.apple.com/documentation/audiotoolbox/1501709-caclocknew)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus CAClockNew (     UInt32 inReservedFlags,     CAClockRef *outCAClock ); ``` |
| To | ``` OSStatus CAClockNew (     UInt32 inReservedFlags,     CAClockRef  _Nullable * _Nonnull outCAClock ); ``` |

Modified [CAClockParseMIDI()](https://developer.apple.com/documentation/audiotoolbox/1502552-caclockparsemidi)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus CAClockParseMIDI (     CAClockRef inCAClock,     const struct MIDIPacketList *inMIDIPacketList ); ``` |
| To | ``` OSStatus CAClockParseMIDI (     CAClockRef _Nonnull inCAClock,     const struct MIDIPacketList * _Nonnull inMIDIPacketList ); ``` |

Modified [CAClockRemoveListener()](https://developer.apple.com/documentation/audiotoolbox/1502441-caclockremovelistener)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus CAClockRemoveListener (     CAClockRef inCAClock,     CAClockListenerProc inListenerProc,     void *inUserData ); ``` |
| To | ``` OSStatus CAClockRemoveListener (     CAClockRef _Nonnull inCAClock,     CAClockListenerProc _Nonnull inListenerProc,     void * _Nonnull inUserData ); ``` |

Modified [CAClockSecondsToSMPTETime()](https://developer.apple.com/documentation/audiotoolbox/1503117-caclocksecondstosmptetime)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus CAClockSecondsToSMPTETime (     CAClockRef inCAClock,     CAClockSeconds inSeconds,     UInt16 inSubframeDivisor,     SMPTETime *outSMPTETime ); ``` |
| To | ``` OSStatus CAClockSecondsToSMPTETime (     CAClockRef _Nonnull inCAClock,     CAClockSeconds inSeconds,     UInt16 inSubframeDivisor,     SMPTETime * _Nonnull outSMPTETime ); ``` |

Modified [CAClockSetCurrentTempo()](https://developer.apple.com/documentation/audiotoolbox/1502209-caclocksetcurrenttempo)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus CAClockSetCurrentTempo (     CAClockRef inCAClock,     CAClockTempo inTempo,     const CAClockTime *inTimestamp ); ``` |
| To | ``` OSStatus CAClockSetCurrentTempo (     CAClockRef _Nonnull inCAClock,     CAClockTempo inTempo,     const CAClockTime * _Nullable inTimestamp ); ``` |

Modified [CAClockSetCurrentTime()](https://developer.apple.com/documentation/audiotoolbox/1503169-caclocksetcurrenttime)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus CAClockSetCurrentTime (     CAClockRef inCAClock,     const CAClockTime *inTime ); ``` |
| To | ``` OSStatus CAClockSetCurrentTime (     CAClockRef _Nonnull inCAClock,     const CAClockTime * _Nonnull inTime ); ``` |

Modified [CAClockSetPlayRate()](https://developer.apple.com/documentation/audiotoolbox/1502264-caclocksetplayrate)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus CAClockSetPlayRate (     CAClockRef inCAClock,     Float64 inPlayRate ); ``` |
| To | ``` OSStatus CAClockSetPlayRate (     CAClockRef _Nonnull inCAClock,     Float64 inPlayRate ); ``` |

Modified [CAClockSetProperty()](https://developer.apple.com/documentation/audiotoolbox/1502700-caclocksetproperty)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus CAClockSetProperty (     CAClockRef inCAClock,     CAClockPropertyID inPropertyID,     UInt32 inPropertyDataSize,     const void *inPropertyData ); ``` |
| To | ``` OSStatus CAClockSetProperty (     CAClockRef _Nonnull inCAClock,     CAClockPropertyID inPropertyID,     UInt32 inPropertyDataSize,     const void * _Nonnull inPropertyData ); ``` |

Modified [CAClockSMPTETimeToSeconds()](https://developer.apple.com/documentation/audiotoolbox/1501940-caclocksmptetimetoseconds)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus CAClockSMPTETimeToSeconds (     CAClockRef inCAClock,     const SMPTETime *inSMPTETime,     CAClockSeconds *outSeconds ); ``` |
| To | ``` OSStatus CAClockSMPTETimeToSeconds (     CAClockRef _Nonnull inCAClock,     const SMPTETime * _Nonnull inSMPTETime,     CAClockSeconds * _Nonnull outSeconds ); ``` |

Modified [CAClockStart()](https://developer.apple.com/documentation/audiotoolbox/1501801-caclockstart)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus CAClockStart (     CAClockRef inCAClock ); ``` |
| To | ``` OSStatus CAClockStart (     CAClockRef _Nonnull inCAClock ); ``` |

Modified [CAClockStop()](https://developer.apple.com/documentation/audiotoolbox/1501689-caclockstop)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus CAClockStop (     CAClockRef inCAClock ); ``` |
| To | ``` OSStatus CAClockStop (     CAClockRef _Nonnull inCAClock ); ``` |

Modified [CAClockTranslateTime()](https://developer.apple.com/documentation/audiotoolbox/1503278-caclocktranslatetime)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus CAClockTranslateTime (     CAClockRef inCAClock,     const CAClockTime *inTime,     CAClockTimeFormat inOutputTimeFormat,     CAClockTime *outTime ); ``` |
| To | ``` OSStatus CAClockTranslateTime (     CAClockRef _Nonnull inCAClock,     const CAClockTime * _Nonnull inTime,     CAClockTimeFormat inOutputTimeFormat,     CAClockTime * _Nonnull outTime ); ``` |

#### DefaultAudioOutput.h

Added #def AudioToolbox_DefaultAudioOutput_h

#### ExtendedAudioFile.h

Added #def AudioToolbox_ExtendedAudioFile_hModified [ExtAudioFileCreateNew()](https://developer.apple.com/documentation/audiotoolbox/1486842-extaudiofilecreatenew)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus ExtAudioFileCreateNew (     const struct FSRef *inParentDir,     CFStringRef inFileName,     AudioFileTypeID inFileType,     const AudioStreamBasicDescription *inStreamDesc,     const AudioChannelLayout *inChannelLayout,     ExtAudioFileRef *outExtAudioFile ); ``` |
| To | ``` OSStatus ExtAudioFileCreateNew (     const struct FSRef * _Nonnull inParentDir,     CFStringRef _Nonnull inFileName,     AudioFileTypeID inFileType,     const AudioStreamBasicDescription * _Nonnull inStreamDesc,     const AudioChannelLayout * _Nullable inChannelLayout,     ExtAudioFileRef  _Nullable * _Nonnull outExtAudioFile ); ``` |

Modified [ExtAudioFileCreateWithURL()](https://developer.apple.com/documentation/audiotoolbox/1486878-extaudiofilecreatewithurl)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus ExtAudioFileCreateWithURL (     CFURLRef inURL,     AudioFileTypeID inFileType,     const AudioStreamBasicDescription *inStreamDesc,     const AudioChannelLayout *inChannelLayout,     UInt32 inFlags,     ExtAudioFileRef *outExtAudioFile ); ``` |
| To | ``` OSStatus ExtAudioFileCreateWithURL (     CFURLRef _Nonnull inURL,     AudioFileTypeID inFileType,     const AudioStreamBasicDescription * _Nonnull inStreamDesc,     const AudioChannelLayout * _Nullable inChannelLayout,     UInt32 inFlags,     ExtAudioFileRef  _Nullable * _Nonnull outExtAudioFile ); ``` |

Modified [ExtAudioFileDispose()](https://developer.apple.com/documentation/audiotoolbox/1486832-extaudiofiledispose)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus ExtAudioFileDispose (     ExtAudioFileRef inExtAudioFile ); ``` |
| To | ``` OSStatus ExtAudioFileDispose (     ExtAudioFileRef _Nonnull inExtAudioFile ); ``` |

Modified [ExtAudioFileGetProperty()](https://developer.apple.com/documentation/audiotoolbox/1486840-extaudiofilegetproperty)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus ExtAudioFileGetProperty (     ExtAudioFileRef inExtAudioFile,     ExtAudioFilePropertyID inPropertyID,     UInt32 *ioPropertyDataSize,     void *outPropertyData ); ``` |
| To | ``` OSStatus ExtAudioFileGetProperty (     ExtAudioFileRef _Nonnull inExtAudioFile,     ExtAudioFilePropertyID inPropertyID,     UInt32 * _Nonnull ioPropertyDataSize,     void * _Nonnull outPropertyData ); ``` |

Modified [ExtAudioFileGetPropertyInfo()](https://developer.apple.com/documentation/audiotoolbox/1486871-extaudiofilegetpropertyinfo)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus ExtAudioFileGetPropertyInfo (     ExtAudioFileRef inExtAudioFile,     ExtAudioFilePropertyID inPropertyID,     UInt32 *outSize,     Boolean *outWritable ); ``` |
| To | ``` OSStatus ExtAudioFileGetPropertyInfo (     ExtAudioFileRef _Nonnull inExtAudioFile,     ExtAudioFilePropertyID inPropertyID,     UInt32 * _Nullable outSize,     Boolean * _Nullable outWritable ); ``` |

Modified [ExtAudioFileOpen()](https://developer.apple.com/documentation/audiotoolbox/1486836-extaudiofileopen)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus ExtAudioFileOpen (     const struct FSRef *inFSRef,     ExtAudioFileRef *outExtAudioFile ); ``` |
| To | ``` OSStatus ExtAudioFileOpen (     const struct FSRef * _Nonnull inFSRef,     ExtAudioFileRef  _Nullable * _Nonnull outExtAudioFile ); ``` |

Modified [ExtAudioFileOpenURL()](https://developer.apple.com/documentation/audiotoolbox/1486873-extaudiofileopenurl)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus ExtAudioFileOpenURL (     CFURLRef inURL,     ExtAudioFileRef *outExtAudioFile ); ``` |
| To | ``` OSStatus ExtAudioFileOpenURL (     CFURLRef _Nonnull inURL,     ExtAudioFileRef  _Nullable * _Nonnull outExtAudioFile ); ``` |

Modified [ExtAudioFileRead()](https://developer.apple.com/documentation/audiotoolbox/1486821-extaudiofileread)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus ExtAudioFileRead (     ExtAudioFileRef inExtAudioFile,     UInt32 *ioNumberFrames,     AudioBufferList *ioData ); ``` |
| To | ``` OSStatus ExtAudioFileRead (     ExtAudioFileRef _Nonnull inExtAudioFile,     UInt32 * _Nonnull ioNumberFrames,     AudioBufferList * _Nonnull ioData ); ``` |

Modified [ExtAudioFileSeek()](https://developer.apple.com/documentation/audiotoolbox/1486830-extaudiofileseek)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus ExtAudioFileSeek (     ExtAudioFileRef inExtAudioFile,     SInt64 inFrameOffset ); ``` |
| To | ``` OSStatus ExtAudioFileSeek (     ExtAudioFileRef _Nonnull inExtAudioFile,     SInt64 inFrameOffset ); ``` |

Modified [ExtAudioFileSetProperty()](https://developer.apple.com/documentation/audiotoolbox/1486884-extaudiofilesetproperty)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus ExtAudioFileSetProperty (     ExtAudioFileRef inExtAudioFile,     ExtAudioFilePropertyID inPropertyID,     UInt32 inPropertyDataSize,     const void *inPropertyData ); ``` |
| To | ``` OSStatus ExtAudioFileSetProperty (     ExtAudioFileRef _Nonnull inExtAudioFile,     ExtAudioFilePropertyID inPropertyID,     UInt32 inPropertyDataSize,     const void * _Nonnull inPropertyData ); ``` |

Modified [ExtAudioFileTell()](https://developer.apple.com/documentation/audiotoolbox/1486813-extaudiofiletell)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus ExtAudioFileTell (     ExtAudioFileRef inExtAudioFile,     SInt64 *outFrameOffset ); ``` |
| To | ``` OSStatus ExtAudioFileTell (     ExtAudioFileRef _Nonnull inExtAudioFile,     SInt64 * _Nonnull outFrameOffset ); ``` |

Modified [ExtAudioFileWrapAudioFileID()](https://developer.apple.com/documentation/audiotoolbox/1486852-extaudiofilewrapaudiofileid)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus ExtAudioFileWrapAudioFileID (     AudioFileID inFileID,     Boolean inForWriting,     ExtAudioFileRef *outExtAudioFile ); ``` |
| To | ``` OSStatus ExtAudioFileWrapAudioFileID (     AudioFileID _Nonnull inFileID,     Boolean inForWriting,     ExtAudioFileRef  _Nullable * _Nonnull outExtAudioFile ); ``` |

Modified [ExtAudioFileWrite()](https://developer.apple.com/documentation/audiotoolbox/1486846-extaudiofilewrite)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus ExtAudioFileWrite (     ExtAudioFileRef inExtAudioFile,     UInt32 inNumberFrames,     const AudioBufferList *ioData ); ``` |
| To | ``` OSStatus ExtAudioFileWrite (     ExtAudioFileRef _Nonnull inExtAudioFile,     UInt32 inNumberFrames,     const AudioBufferList * _Nonnull ioData ); ``` |

Modified [ExtAudioFileWriteAsync()](https://developer.apple.com/documentation/audiotoolbox/1486834-extaudiofilewriteasync)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus ExtAudioFileWriteAsync (     ExtAudioFileRef inExtAudioFile,     UInt32 inNumberFrames,     const AudioBufferList *ioData ); ``` |
| To | ``` OSStatus ExtAudioFileWriteAsync (     ExtAudioFileRef _Nonnull inExtAudioFile,     UInt32 inNumberFrames,     const AudioBufferList * _Nullable ioData ); ``` |

#### MusicPlayer.h

Added #def AudioToolbox_MusicPlayer_hAdded [kAudioToolboxError_NoTrackDestination](https://developer.apple.com/documentation/audiotoolbox/1515472-anonymous/kaudiotoolboxerror_notrackdestination)Added [kMusicSequenceFile_AnyType](https://developer.apple.com/documentation/audiotoolbox/musicsequencefiletypeid/anytype)Added [kMusicSequenceFileFlags_Default](https://developer.apple.com/documentation/audiotoolbox/musicsequencefileflags/kmusicsequencefileflags_default)Added [kMusicSequenceLoadSMF_PreserveTracks](https://developer.apple.com/documentation/audiotoolbox/musicsequenceloadflags/1501705-smf_preservetracks)Modified [DisposeMusicEventIterator()](https://developer.apple.com/documentation/audiotoolbox/1503301-disposemusiceventiterator)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus DisposeMusicEventIterator (     MusicEventIterator inIterator ); ``` |
| To | ``` OSStatus DisposeMusicEventIterator (     MusicEventIterator _Nonnull inIterator ); ``` |

Modified [DisposeMusicPlayer()](https://developer.apple.com/documentation/audiotoolbox/1502985-disposemusicplayer)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus DisposeMusicPlayer (     MusicPlayer inPlayer ); ``` |
| To | ``` OSStatus DisposeMusicPlayer (     MusicPlayer _Nonnull inPlayer ); ``` |

Modified [DisposeMusicSequence()](https://developer.apple.com/documentation/audiotoolbox/1501909-disposemusicsequence)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus DisposeMusicSequence (     MusicSequence inSequence ); ``` |
| To | ``` OSStatus DisposeMusicSequence (     MusicSequence _Nonnull inSequence ); ``` |

Modified [MusicEventIteratorDeleteEvent()](https://developer.apple.com/documentation/audiotoolbox/1502605-musiceventiteratordeleteevent)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus MusicEventIteratorDeleteEvent (     MusicEventIterator inIterator ); ``` |
| To | ``` OSStatus MusicEventIteratorDeleteEvent (     MusicEventIterator _Nonnull inIterator ); ``` |

Modified [MusicEventIteratorGetEventInfo()](https://developer.apple.com/documentation/audiotoolbox/1501702-musiceventiteratorgeteventinfo)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus MusicEventIteratorGetEventInfo (     MusicEventIterator inIterator,     MusicTimeStamp *outTimeStamp,     MusicEventType *outEventType,     const void **outEventData,     UInt32 *outEventDataSize ); ``` |
| To | ``` OSStatus MusicEventIteratorGetEventInfo (     MusicEventIterator _Nonnull inIterator,     MusicTimeStamp * _Nonnull outTimeStamp,     MusicEventType * _Nonnull outEventType,     const void * _Nullable * _Nonnull outEventData,     UInt32 * _Nonnull outEventDataSize ); ``` |

Modified [MusicEventIteratorHasCurrentEvent()](https://developer.apple.com/documentation/audiotoolbox/1503065-musiceventiteratorhascurrenteven)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus MusicEventIteratorHasCurrentEvent (     MusicEventIterator inIterator,     Boolean *outHasCurEvent ); ``` |
| To | ``` OSStatus MusicEventIteratorHasCurrentEvent (     MusicEventIterator _Nonnull inIterator,     Boolean * _Nonnull outHasCurEvent ); ``` |

Modified [MusicEventIteratorHasNextEvent()](https://developer.apple.com/documentation/audiotoolbox/1503205-musiceventiteratorhasnextevent)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus MusicEventIteratorHasNextEvent (     MusicEventIterator inIterator,     Boolean *outHasNextEvent ); ``` |
| To | ``` OSStatus MusicEventIteratorHasNextEvent (     MusicEventIterator _Nonnull inIterator,     Boolean * _Nonnull outHasNextEvent ); ``` |

Modified [MusicEventIteratorHasPreviousEvent()](https://developer.apple.com/documentation/audiotoolbox/1502205-musiceventiteratorhaspreviouseve)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus MusicEventIteratorHasPreviousEvent (     MusicEventIterator inIterator,     Boolean *outHasPrevEvent ); ``` |
| To | ``` OSStatus MusicEventIteratorHasPreviousEvent (     MusicEventIterator _Nonnull inIterator,     Boolean * _Nonnull outHasPrevEvent ); ``` |

Modified [MusicEventIteratorNextEvent()](https://developer.apple.com/documentation/audiotoolbox/1503143-musiceventiteratornextevent)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus MusicEventIteratorNextEvent (     MusicEventIterator inIterator ); ``` |
| To | ``` OSStatus MusicEventIteratorNextEvent (     MusicEventIterator _Nonnull inIterator ); ``` |

Modified [MusicEventIteratorPreviousEvent()](https://developer.apple.com/documentation/audiotoolbox/1501710-musiceventiteratorpreviousevent)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus MusicEventIteratorPreviousEvent (     MusicEventIterator inIterator ); ``` |
| To | ``` OSStatus MusicEventIteratorPreviousEvent (     MusicEventIterator _Nonnull inIterator ); ``` |

Modified [MusicEventIteratorSeek()](https://developer.apple.com/documentation/audiotoolbox/1502108-musiceventiteratorseek)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus MusicEventIteratorSeek (     MusicEventIterator inIterator,     MusicTimeStamp inTimeStamp ); ``` |
| To | ``` OSStatus MusicEventIteratorSeek (     MusicEventIterator _Nonnull inIterator,     MusicTimeStamp inTimeStamp ); ``` |

Modified [MusicEventIteratorSetEventInfo()](https://developer.apple.com/documentation/audiotoolbox/1503101-musiceventiteratorseteventinfo)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus MusicEventIteratorSetEventInfo (     MusicEventIterator inIterator,     MusicEventType inEventType,     const void *inEventData ); ``` |
| To | ``` OSStatus MusicEventIteratorSetEventInfo (     MusicEventIterator _Nonnull inIterator,     MusicEventType inEventType,     const void * _Nonnull inEventData ); ``` |

Modified [MusicEventIteratorSetEventTime()](https://developer.apple.com/documentation/audiotoolbox/1503403-musiceventiteratorseteventtime)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus MusicEventIteratorSetEventTime (     MusicEventIterator inIterator,     MusicTimeStamp inTimeStamp ); ``` |
| To | ``` OSStatus MusicEventIteratorSetEventTime (     MusicEventIterator _Nonnull inIterator,     MusicTimeStamp inTimeStamp ); ``` |

Modified [MusicPlayerGetBeatsForHostTime()](https://developer.apple.com/documentation/audiotoolbox/1502501-musicplayergetbeatsforhosttime)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus MusicPlayerGetBeatsForHostTime (     MusicPlayer inPlayer,     UInt64 inHostTime,     MusicTimeStamp *outBeats ); ``` |
| To | ``` OSStatus MusicPlayerGetBeatsForHostTime (     MusicPlayer _Nonnull inPlayer,     UInt64 inHostTime,     MusicTimeStamp * _Nonnull outBeats ); ``` |

Modified [MusicPlayerGetHostTimeForBeats()](https://developer.apple.com/documentation/audiotoolbox/1502486-musicplayergethosttimeforbeats)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus MusicPlayerGetHostTimeForBeats (     MusicPlayer inPlayer,     MusicTimeStamp inBeats,     UInt64 *outHostTime ); ``` |
| To | ``` OSStatus MusicPlayerGetHostTimeForBeats (     MusicPlayer _Nonnull inPlayer,     MusicTimeStamp inBeats,     UInt64 * _Nonnull outHostTime ); ``` |

Modified [MusicPlayerGetPlayRateScalar()](https://developer.apple.com/documentation/audiotoolbox/1501767-musicplayergetplayratescalar)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus MusicPlayerGetPlayRateScalar (     MusicPlayer inPlayer,     Float64 *outScaleRate ); ``` |
| To | ``` OSStatus MusicPlayerGetPlayRateScalar (     MusicPlayer _Nonnull inPlayer,     Float64 * _Nonnull outScaleRate ); ``` |

Modified [MusicPlayerGetSequence()](https://developer.apple.com/documentation/audiotoolbox/1502355-musicplayergetsequence)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus MusicPlayerGetSequence (     MusicPlayer inPlayer,     MusicSequence *outSequence ); ``` |
| To | ``` OSStatus MusicPlayerGetSequence (     MusicPlayer _Nonnull inPlayer,     MusicSequence  _Nullable * _Nonnull outSequence ); ``` |

Modified [MusicPlayerGetTime()](https://developer.apple.com/documentation/audiotoolbox/1502259-musicplayergettime)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus MusicPlayerGetTime (     MusicPlayer inPlayer,     MusicTimeStamp *outTime ); ``` |
| To | ``` OSStatus MusicPlayerGetTime (     MusicPlayer _Nonnull inPlayer,     MusicTimeStamp * _Nonnull outTime ); ``` |

Modified [MusicPlayerIsPlaying()](https://developer.apple.com/documentation/audiotoolbox/1502241-musicplayerisplaying)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus MusicPlayerIsPlaying (     MusicPlayer inPlayer,     Boolean *outIsPlaying ); ``` |
| To | ``` OSStatus MusicPlayerIsPlaying (     MusicPlayer _Nonnull inPlayer,     Boolean * _Nonnull outIsPlaying ); ``` |

Modified [MusicPlayerPreroll()](https://developer.apple.com/documentation/audiotoolbox/1503131-musicplayerpreroll)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus MusicPlayerPreroll (     MusicPlayer inPlayer ); ``` |
| To | ``` OSStatus MusicPlayerPreroll (     MusicPlayer _Nonnull inPlayer ); ``` |

Modified [MusicPlayerSetPlayRateScalar()](https://developer.apple.com/documentation/audiotoolbox/1502928-musicplayersetplayratescalar)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus MusicPlayerSetPlayRateScalar (     MusicPlayer inPlayer,     Float64 inScaleRate ); ``` |
| To | ``` OSStatus MusicPlayerSetPlayRateScalar (     MusicPlayer _Nonnull inPlayer,     Float64 inScaleRate ); ``` |

Modified [MusicPlayerSetSequence()](https://developer.apple.com/documentation/audiotoolbox/1502518-musicplayersetsequence)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus MusicPlayerSetSequence (     MusicPlayer inPlayer,     MusicSequence inSequence ); ``` |
| To | ``` OSStatus MusicPlayerSetSequence (     MusicPlayer _Nonnull inPlayer,     MusicSequence _Nonnull inSequence ); ``` |

Modified [MusicPlayerSetTime()](https://developer.apple.com/documentation/audiotoolbox/1501770-musicplayersettime)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus MusicPlayerSetTime (     MusicPlayer inPlayer,     MusicTimeStamp inTime ); ``` |
| To | ``` OSStatus MusicPlayerSetTime (     MusicPlayer _Nonnull inPlayer,     MusicTimeStamp inTime ); ``` |

Modified [MusicPlayerStart()](https://developer.apple.com/documentation/audiotoolbox/1503255-musicplayerstart)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus MusicPlayerStart (     MusicPlayer inPlayer ); ``` |
| To | ``` OSStatus MusicPlayerStart (     MusicPlayer _Nonnull inPlayer ); ``` |

Modified [MusicPlayerStop()](https://developer.apple.com/documentation/audiotoolbox/1502668-musicplayerstop)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus MusicPlayerStop (     MusicPlayer inPlayer ); ``` |
| To | ``` OSStatus MusicPlayerStop (     MusicPlayer _Nonnull inPlayer ); ``` |

Modified [MusicSequenceBarBeatTimeToBeats()](https://developer.apple.com/documentation/audiotoolbox/1503191-musicsequencebarbeattimetobeats)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus MusicSequenceBarBeatTimeToBeats (     MusicSequence inSequence,     const CABarBeatTime *inBarBeatTime,     MusicTimeStamp *outBeats ); ``` |
| To | ``` OSStatus MusicSequenceBarBeatTimeToBeats (     MusicSequence _Nonnull inSequence,     const CABarBeatTime * _Nonnull inBarBeatTime,     MusicTimeStamp * _Nonnull outBeats ); ``` |

Modified [MusicSequenceBeatsToBarBeatTime()](https://developer.apple.com/documentation/audiotoolbox/1503366-musicsequencebeatstobarbeattime)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus MusicSequenceBeatsToBarBeatTime (     MusicSequence inSequence,     MusicTimeStamp inBeats,     UInt32 inSubbeatDivisor,     CABarBeatTime *outBarBeatTime ); ``` |
| To | ``` OSStatus MusicSequenceBeatsToBarBeatTime (     MusicSequence _Nonnull inSequence,     MusicTimeStamp inBeats,     UInt32 inSubbeatDivisor,     CABarBeatTime * _Nonnull outBarBeatTime ); ``` |

Modified [MusicSequenceDisposeTrack()](https://developer.apple.com/documentation/audiotoolbox/1502673-musicsequencedisposetrack)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus MusicSequenceDisposeTrack (     MusicSequence inSequence,     MusicTrack inTrack ); ``` |
| To | ``` OSStatus MusicSequenceDisposeTrack (     MusicSequence _Nonnull inSequence,     MusicTrack _Nonnull inTrack ); ``` |

Modified [MusicSequenceFileCreate()](https://developer.apple.com/documentation/audiotoolbox/1502760-musicsequencefilecreate)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus MusicSequenceFileCreate (     MusicSequence inSequence,     CFURLRef inFileRef,     MusicSequenceFileTypeID inFileType,     MusicSequenceFileFlags inFlags,     SInt16 inResolution ); ``` |
| To | ``` OSStatus MusicSequenceFileCreate (     MusicSequence _Nonnull inSequence,     CFURLRef _Nonnull inFileRef,     MusicSequenceFileTypeID inFileType,     MusicSequenceFileFlags inFlags,     SInt16 inResolution ); ``` |

Modified [MusicSequenceFileCreateData()](https://developer.apple.com/documentation/audiotoolbox/1503006-musicsequencefilecreatedata)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus MusicSequenceFileCreateData (     MusicSequence inSequence,     MusicSequenceFileTypeID inFileType,     MusicSequenceFileFlags inFlags,     SInt16 inResolution,     CFDataRef *outData ); ``` |
| To | ``` OSStatus MusicSequenceFileCreateData (     MusicSequence _Nonnull inSequence,     MusicSequenceFileTypeID inFileType,     MusicSequenceFileFlags inFlags,     SInt16 inResolution,     CFDataRef  _Nullable * _Nonnull outData ); ``` |

Modified [MusicSequenceFileLoad()](https://developer.apple.com/documentation/audiotoolbox/1502222-musicsequencefileload)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus MusicSequenceFileLoad (     MusicSequence inSequence,     CFURLRef inFileRef,     MusicSequenceFileTypeID inFileTypeHint,     MusicSequenceLoadFlags inFlags ); ``` |
| To | ``` OSStatus MusicSequenceFileLoad (     MusicSequence _Nonnull inSequence,     CFURLRef _Nonnull inFileRef,     MusicSequenceFileTypeID inFileTypeHint,     MusicSequenceLoadFlags inFlags ); ``` |

Modified [MusicSequenceFileLoadData()](https://developer.apple.com/documentation/audiotoolbox/1502465-musicsequencefileloaddata)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus MusicSequenceFileLoadData (     MusicSequence inSequence,     CFDataRef inData,     MusicSequenceFileTypeID inFileTypeHint,     MusicSequenceLoadFlags inFlags ); ``` |
| To | ``` OSStatus MusicSequenceFileLoadData (     MusicSequence _Nonnull inSequence,     CFDataRef _Nonnull inData,     MusicSequenceFileTypeID inFileTypeHint,     MusicSequenceLoadFlags inFlags ); ``` |

Modified [MusicSequenceGetAUGraph()](https://developer.apple.com/documentation/audiotoolbox/1502317-musicsequencegetaugraph)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus MusicSequenceGetAUGraph (     MusicSequence inSequence,     AUGraph *outGraph ); ``` |
| To | ``` OSStatus MusicSequenceGetAUGraph (     MusicSequence _Nonnull inSequence,     AUGraph  _Nullable * _Nonnull outGraph ); ``` |

Modified [MusicSequenceGetBeatsForSeconds()](https://developer.apple.com/documentation/audiotoolbox/1503378-musicsequencegetbeatsforseconds)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus MusicSequenceGetBeatsForSeconds (     MusicSequence inSequence,     Float64 inSeconds,     MusicTimeStamp *outBeats ); ``` |
| To | ``` OSStatus MusicSequenceGetBeatsForSeconds (     MusicSequence _Nonnull inSequence,     Float64 inSeconds,     MusicTimeStamp * _Nonnull outBeats ); ``` |

Modified [MusicSequenceGetIndTrack()](https://developer.apple.com/documentation/audiotoolbox/1501623-musicsequencegetindtrack)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus MusicSequenceGetIndTrack (     MusicSequence inSequence,     UInt32 inTrackIndex,     MusicTrack *outTrack ); ``` |
| To | ``` OSStatus MusicSequenceGetIndTrack (     MusicSequence _Nonnull inSequence,     UInt32 inTrackIndex,     MusicTrack  _Nullable * _Nonnull outTrack ); ``` |

Modified [MusicSequenceGetInfoDictionary()](https://developer.apple.com/documentation/audiotoolbox/1502298-musicsequencegetinfodictionary)

|  | Declaration |
| --- | --- |
| From | ``` CFDictionaryRef MusicSequenceGetInfoDictionary (     MusicSequence inSequence ); ``` |
| To | ``` CFDictionaryRef _Nonnull MusicSequenceGetInfoDictionary (     MusicSequence _Nonnull inSequence ); ``` |

Modified [MusicSequenceGetSecondsForBeats()](https://developer.apple.com/documentation/audiotoolbox/1502781-musicsequencegetsecondsforbeats)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus MusicSequenceGetSecondsForBeats (     MusicSequence inSequence,     MusicTimeStamp inBeats,     Float64 *outSeconds ); ``` |
| To | ``` OSStatus MusicSequenceGetSecondsForBeats (     MusicSequence _Nonnull inSequence,     MusicTimeStamp inBeats,     Float64 * _Nonnull outSeconds ); ``` |

Modified [MusicSequenceGetSequenceType()](https://developer.apple.com/documentation/audiotoolbox/1501659-musicsequencegetsequencetype)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus MusicSequenceGetSequenceType (     MusicSequence inSequence,     MusicSequenceType *outType ); ``` |
| To | ``` OSStatus MusicSequenceGetSequenceType (     MusicSequence _Nonnull inSequence,     MusicSequenceType * _Nonnull outType ); ``` |

Modified [MusicSequenceGetSMPTEResolution()](https://developer.apple.com/documentation/audiotoolbox/1502035-musicsequencegetsmpteresolution)

|  | Declaration |
| --- | --- |
| From | ``` void MusicSequenceGetSMPTEResolution (     SInt16 inRes,     SignedByte *fps,     Byte *ticks ); ``` |
| To | ``` void MusicSequenceGetSMPTEResolution (     SInt16 inRes,     SignedByte * _Nonnull fps,     Byte * _Nonnull ticks ); ``` |

Modified [MusicSequenceGetTempoTrack()](https://developer.apple.com/documentation/audiotoolbox/1502277-musicsequencegettempotrack)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus MusicSequenceGetTempoTrack (     MusicSequence inSequence,     MusicTrack *outTrack ); ``` |
| To | ``` OSStatus MusicSequenceGetTempoTrack (     MusicSequence _Nonnull inSequence,     MusicTrack  _Nullable * _Nonnull outTrack ); ``` |

Modified [MusicSequenceGetTrackCount()](https://developer.apple.com/documentation/audiotoolbox/1503390-musicsequencegettrackcount)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus MusicSequenceGetTrackCount (     MusicSequence inSequence,     UInt32 *outNumberOfTracks ); ``` |
| To | ``` OSStatus MusicSequenceGetTrackCount (     MusicSequence _Nonnull inSequence,     UInt32 * _Nonnull outNumberOfTracks ); ``` |

Modified [MusicSequenceGetTrackIndex()](https://developer.apple.com/documentation/audiotoolbox/1503150-musicsequencegettrackindex)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus MusicSequenceGetTrackIndex (     MusicSequence inSequence,     MusicTrack inTrack,     UInt32 *outTrackIndex ); ``` |
| To | ``` OSStatus MusicSequenceGetTrackIndex (     MusicSequence _Nonnull inSequence,     MusicTrack _Nonnull inTrack,     UInt32 * _Nonnull outTrackIndex ); ``` |

Modified MusicSequenceLoadSMFData()

|  | Declaration |
| --- | --- |
| From | ``` OSStatus MusicSequenceLoadSMFData (     MusicSequence inSequence,     CFDataRef inData ); ``` |
| To | ``` OSStatus MusicSequenceLoadSMFData (     MusicSequence _Nonnull inSequence,     CFDataRef _Nonnull inData ); ``` |

Modified [MusicSequenceLoadSMFDataWithFlags()](https://developer.apple.com/documentation/audiotoolbox/1515430-musicsequenceloadsmfdatawithflag)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus MusicSequenceLoadSMFDataWithFlags (     MusicSequence inSequence,     CFDataRef inData,     MusicSequenceLoadFlags inFlags ); ``` |
| To | ``` OSStatus MusicSequenceLoadSMFDataWithFlags (     MusicSequence _Nonnull inSequence,     CFDataRef _Nonnull inData,     MusicSequenceLoadFlags inFlags ); ``` |

Modified [MusicSequenceLoadSMFWithFlags()](https://developer.apple.com/documentation/audiotoolbox/1515448-musicsequenceloadsmfwithflags)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus MusicSequenceLoadSMFWithFlags (     MusicSequence inSequence,     const struct FSRef *inFileRef,     MusicSequenceLoadFlags inFlags ); ``` |
| To | ``` OSStatus MusicSequenceLoadSMFWithFlags (     MusicSequence _Nonnull inSequence,     const struct FSRef * _Nonnull inFileRef,     MusicSequenceLoadFlags inFlags ); ``` |

Modified [MusicSequenceNewTrack()](https://developer.apple.com/documentation/audiotoolbox/1503090-musicsequencenewtrack)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus MusicSequenceNewTrack (     MusicSequence inSequence,     MusicTrack *outTrack ); ``` |
| To | ``` OSStatus MusicSequenceNewTrack (     MusicSequence _Nonnull inSequence,     MusicTrack  _Nullable * _Nonnull outTrack ); ``` |

Modified [MusicSequenceReverse()](https://developer.apple.com/documentation/audiotoolbox/1502802-musicsequencereverse)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus MusicSequenceReverse (     MusicSequence inSequence ); ``` |
| To | ``` OSStatus MusicSequenceReverse (     MusicSequence _Nonnull inSequence ); ``` |

Modified [MusicSequenceSaveMIDIFile()](https://developer.apple.com/documentation/audiotoolbox/1515434-musicsequencesavemidifile)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus MusicSequenceSaveMIDIFile (     MusicSequence inSequence,     const struct FSRef *inParentDirectory,     CFStringRef inFileName,     UInt16 inResolution,     UInt32 inFlags ); ``` |
| To | ``` OSStatus MusicSequenceSaveMIDIFile (     MusicSequence _Nonnull inSequence,     const struct FSRef * _Nonnull inParentDirectory,     CFStringRef _Nonnull inFileName,     UInt16 inResolution,     UInt32 inFlags ); ``` |

Modified [MusicSequenceSaveSMFData()](https://developer.apple.com/documentation/audiotoolbox/1515490-musicsequencesavesmfdata)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus MusicSequenceSaveSMFData (     MusicSequence inSequence,     CFDataRef *outData,     UInt16 inResolution ); ``` |
| To | ``` OSStatus MusicSequenceSaveSMFData (     MusicSequence _Nonnull inSequence,     CFDataRef  _Nullable * _Nonnull outData,     UInt16 inResolution ); ``` |

Modified [MusicSequenceSetAUGraph()](https://developer.apple.com/documentation/audiotoolbox/1503097-musicsequencesetaugraph)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus MusicSequenceSetAUGraph (     MusicSequence inSequence,     AUGraph inGraph ); ``` |
| To | ``` OSStatus MusicSequenceSetAUGraph (     MusicSequence _Nonnull inSequence,     AUGraph _Nullable inGraph ); ``` |

Modified [MusicSequenceSetMIDIEndpoint()](https://developer.apple.com/documentation/audiotoolbox/1501917-musicsequencesetmidiendpoint)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus MusicSequenceSetMIDIEndpoint (     MusicSequence inSequence,     MIDIEndpointRef inEndpoint ); ``` |
| To | ``` OSStatus MusicSequenceSetMIDIEndpoint (     MusicSequence _Nonnull inSequence,     MIDIEndpointRef inEndpoint ); ``` |

Modified [MusicSequenceSetSequenceType()](https://developer.apple.com/documentation/audiotoolbox/1501664-musicsequencesetsequencetype)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus MusicSequenceSetSequenceType (     MusicSequence inSequence,     MusicSequenceType inType ); ``` |
| To | ``` OSStatus MusicSequenceSetSequenceType (     MusicSequence _Nonnull inSequence,     MusicSequenceType inType ); ``` |

Modified [MusicSequenceSetUserCallback()](https://developer.apple.com/documentation/audiotoolbox/1503188-musicsequencesetusercallback)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus MusicSequenceSetUserCallback (     MusicSequence inSequence,     MusicSequenceUserCallback inCallback,     void *inClientData ); ``` |
| To | ``` OSStatus MusicSequenceSetUserCallback (     MusicSequence _Nonnull inSequence,     MusicSequenceUserCallback _Nullable inCallback,     void * _Nullable inClientData ); ``` |

Modified [MusicTrackClear()](https://developer.apple.com/documentation/audiotoolbox/1503074-musictrackclear)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus MusicTrackClear (     MusicTrack inTrack,     MusicTimeStamp inStartTime,     MusicTimeStamp inEndTime ); ``` |
| To | ``` OSStatus MusicTrackClear (     MusicTrack _Nonnull inTrack,     MusicTimeStamp inStartTime,     MusicTimeStamp inEndTime ); ``` |

Modified [MusicTrackCopyInsert()](https://developer.apple.com/documentation/audiotoolbox/1501985-musictrackcopyinsert)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus MusicTrackCopyInsert (     MusicTrack inSourceTrack,     MusicTimeStamp inSourceStartTime,     MusicTimeStamp inSourceEndTime,     MusicTrack inDestTrack,     MusicTimeStamp inDestInsertTime ); ``` |
| To | ``` OSStatus MusicTrackCopyInsert (     MusicTrack _Nonnull inSourceTrack,     MusicTimeStamp inSourceStartTime,     MusicTimeStamp inSourceEndTime,     MusicTrack _Nonnull inDestTrack,     MusicTimeStamp inDestInsertTime ); ``` |

Modified [MusicTrackCut()](https://developer.apple.com/documentation/audiotoolbox/1502402-musictrackcut)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus MusicTrackCut (     MusicTrack inTrack,     MusicTimeStamp inStartTime,     MusicTimeStamp inEndTime ); ``` |
| To | ``` OSStatus MusicTrackCut (     MusicTrack _Nonnull inTrack,     MusicTimeStamp inStartTime,     MusicTimeStamp inEndTime ); ``` |

Modified [MusicTrackGetDestMIDIEndpoint()](https://developer.apple.com/documentation/audiotoolbox/1502965-musictrackgetdestmidiendpoint)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus MusicTrackGetDestMIDIEndpoint (     MusicTrack inTrack,     MIDIEndpointRef *outEndpoint ); ``` |
| To | ``` OSStatus MusicTrackGetDestMIDIEndpoint (     MusicTrack _Nonnull inTrack,     MIDIEndpointRef * _Nonnull outEndpoint ); ``` |

Modified [MusicTrackGetDestNode()](https://developer.apple.com/documentation/audiotoolbox/1501907-musictrackgetdestnode)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus MusicTrackGetDestNode (     MusicTrack inTrack,     AUNode *outNode ); ``` |
| To | ``` OSStatus MusicTrackGetDestNode (     MusicTrack _Nonnull inTrack,     AUNode * _Nonnull outNode ); ``` |

Modified [MusicTrackGetProperty()](https://developer.apple.com/documentation/audiotoolbox/1503210-musictrackgetproperty)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus MusicTrackGetProperty (     MusicTrack inTrack,     UInt32 inPropertyID,     void *outData,     UInt32 *ioLength ); ``` |
| To | ``` OSStatus MusicTrackGetProperty (     MusicTrack _Nonnull inTrack,     UInt32 inPropertyID,     void * _Nonnull outData,     UInt32 * _Nonnull ioLength ); ``` |

Modified [MusicTrackGetSequence()](https://developer.apple.com/documentation/audiotoolbox/1502453-musictrackgetsequence)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus MusicTrackGetSequence (     MusicTrack inTrack,     MusicSequence *outSequence ); ``` |
| To | ``` OSStatus MusicTrackGetSequence (     MusicTrack _Nonnull inTrack,     MusicSequence  _Nullable * _Nonnull outSequence ); ``` |

Modified [MusicTrackMerge()](https://developer.apple.com/documentation/audiotoolbox/1502959-musictrackmerge)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus MusicTrackMerge (     MusicTrack inSourceTrack,     MusicTimeStamp inSourceStartTime,     MusicTimeStamp inSourceEndTime,     MusicTrack inDestTrack,     MusicTimeStamp inDestInsertTime ); ``` |
| To | ``` OSStatus MusicTrackMerge (     MusicTrack _Nonnull inSourceTrack,     MusicTimeStamp inSourceStartTime,     MusicTimeStamp inSourceEndTime,     MusicTrack _Nonnull inDestTrack,     MusicTimeStamp inDestInsertTime ); ``` |

Modified [MusicTrackMoveEvents()](https://developer.apple.com/documentation/audiotoolbox/1503297-musictrackmoveevents)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus MusicTrackMoveEvents (     MusicTrack inTrack,     MusicTimeStamp inStartTime,     MusicTimeStamp inEndTime,     MusicTimeStamp inMoveTime ); ``` |
| To | ``` OSStatus MusicTrackMoveEvents (     MusicTrack _Nonnull inTrack,     MusicTimeStamp inStartTime,     MusicTimeStamp inEndTime,     MusicTimeStamp inMoveTime ); ``` |

Modified [MusicTrackNewAUPresetEvent()](https://developer.apple.com/documentation/audiotoolbox/1502115-musictracknewaupresetevent)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus MusicTrackNewAUPresetEvent (     MusicTrack inTrack,     MusicTimeStamp inTimeStamp,     const AUPresetEvent *inPresetEvent ); ``` |
| To | ``` OSStatus MusicTrackNewAUPresetEvent (     MusicTrack _Nonnull inTrack,     MusicTimeStamp inTimeStamp,     const AUPresetEvent * _Nonnull inPresetEvent ); ``` |

Modified [MusicTrackNewExtendedControlEvent()](https://developer.apple.com/documentation/audiotoolbox/1515457-musictracknewextendedcontroleven)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus MusicTrackNewExtendedControlEvent (     MusicTrack inTrack,     MusicTimeStamp inTimeStamp,     const ExtendedControlEvent *inInfo ); ``` |
| To | ``` OSStatus MusicTrackNewExtendedControlEvent (     MusicTrack _Nonnull inTrack,     MusicTimeStamp inTimeStamp,     const ExtendedControlEvent * _Nonnull inInfo ); ``` |

Modified [MusicTrackNewExtendedNoteEvent()](https://developer.apple.com/documentation/audiotoolbox/1501902-musictracknewextendednoteevent)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus MusicTrackNewExtendedNoteEvent (     MusicTrack inTrack,     MusicTimeStamp inTimeStamp,     const ExtendedNoteOnEvent *inInfo ); ``` |
| To | ``` OSStatus MusicTrackNewExtendedNoteEvent (     MusicTrack _Nonnull inTrack,     MusicTimeStamp inTimeStamp,     const ExtendedNoteOnEvent * _Nonnull inInfo ); ``` |

Modified [MusicTrackNewExtendedTempoEvent()](https://developer.apple.com/documentation/audiotoolbox/1502846-musictracknewextendedtempoevent)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus MusicTrackNewExtendedTempoEvent (     MusicTrack inTrack,     MusicTimeStamp inTimeStamp,     Float64 inBPM ); ``` |
| To | ``` OSStatus MusicTrackNewExtendedTempoEvent (     MusicTrack _Nonnull inTrack,     MusicTimeStamp inTimeStamp,     Float64 inBPM ); ``` |

Modified [MusicTrackNewMetaEvent()](https://developer.apple.com/documentation/audiotoolbox/1503236-musictracknewmetaevent)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus MusicTrackNewMetaEvent (     MusicTrack inTrack,     MusicTimeStamp inTimeStamp,     const MIDIMetaEvent *inMetaEvent ); ``` |
| To | ``` OSStatus MusicTrackNewMetaEvent (     MusicTrack _Nonnull inTrack,     MusicTimeStamp inTimeStamp,     const MIDIMetaEvent * _Nonnull inMetaEvent ); ``` |

Modified [MusicTrackNewMIDIChannelEvent()](https://developer.apple.com/documentation/audiotoolbox/1502640-musictracknewmidichannelevent)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus MusicTrackNewMIDIChannelEvent (     MusicTrack inTrack,     MusicTimeStamp inTimeStamp,     const MIDIChannelMessage *inMessage ); ``` |
| To | ``` OSStatus MusicTrackNewMIDIChannelEvent (     MusicTrack _Nonnull inTrack,     MusicTimeStamp inTimeStamp,     const MIDIChannelMessage * _Nonnull inMessage ); ``` |

Modified [MusicTrackNewMIDINoteEvent()](https://developer.apple.com/documentation/audiotoolbox/1502187-musictracknewmidinoteevent)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus MusicTrackNewMIDINoteEvent (     MusicTrack inTrack,     MusicTimeStamp inTimeStamp,     const MIDINoteMessage *inMessage ); ``` |
| To | ``` OSStatus MusicTrackNewMIDINoteEvent (     MusicTrack _Nonnull inTrack,     MusicTimeStamp inTimeStamp,     const MIDINoteMessage * _Nonnull inMessage ); ``` |

Modified [MusicTrackNewMIDIRawDataEvent()](https://developer.apple.com/documentation/audiotoolbox/1501632-musictracknewmidirawdataevent)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus MusicTrackNewMIDIRawDataEvent (     MusicTrack inTrack,     MusicTimeStamp inTimeStamp,     const MIDIRawData *inRawData ); ``` |
| To | ``` OSStatus MusicTrackNewMIDIRawDataEvent (     MusicTrack _Nonnull inTrack,     MusicTimeStamp inTimeStamp,     const MIDIRawData * _Nonnull inRawData ); ``` |

Modified [MusicTrackNewParameterEvent()](https://developer.apple.com/documentation/audiotoolbox/1502270-musictracknewparameterevent)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus MusicTrackNewParameterEvent (     MusicTrack inTrack,     MusicTimeStamp inTimeStamp,     const ParameterEvent *inInfo ); ``` |
| To | ``` OSStatus MusicTrackNewParameterEvent (     MusicTrack _Nonnull inTrack,     MusicTimeStamp inTimeStamp,     const ParameterEvent * _Nonnull inInfo ); ``` |

Modified [MusicTrackNewUserEvent()](https://developer.apple.com/documentation/audiotoolbox/1503370-musictracknewuserevent)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus MusicTrackNewUserEvent (     MusicTrack inTrack,     MusicTimeStamp inTimeStamp,     const MusicEventUserData *inUserData ); ``` |
| To | ``` OSStatus MusicTrackNewUserEvent (     MusicTrack _Nonnull inTrack,     MusicTimeStamp inTimeStamp,     const MusicEventUserData * _Nonnull inUserData ); ``` |

Modified [MusicTrackSetDestMIDIEndpoint()](https://developer.apple.com/documentation/audiotoolbox/1503337-musictracksetdestmidiendpoint)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus MusicTrackSetDestMIDIEndpoint (     MusicTrack inTrack,     MIDIEndpointRef inEndpoint ); ``` |
| To | ``` OSStatus MusicTrackSetDestMIDIEndpoint (     MusicTrack _Nonnull inTrack,     MIDIEndpointRef inEndpoint ); ``` |

Modified [MusicTrackSetDestNode()](https://developer.apple.com/documentation/audiotoolbox/1502931-musictracksetdestnode)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus MusicTrackSetDestNode (     MusicTrack inTrack,     AUNode inNode ); ``` |
| To | ``` OSStatus MusicTrackSetDestNode (     MusicTrack _Nonnull inTrack,     AUNode inNode ); ``` |

Modified [MusicTrackSetProperty()](https://developer.apple.com/documentation/audiotoolbox/1501688-musictracksetproperty)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus MusicTrackSetProperty (     MusicTrack inTrack,     UInt32 inPropertyID,     void *inData,     UInt32 inLength ); ``` |
| To | ``` OSStatus MusicTrackSetProperty (     MusicTrack _Nonnull inTrack,     UInt32 inPropertyID,     void * _Nonnull inData,     UInt32 inLength ); ``` |

Modified [NewMusicEventIterator()](https://developer.apple.com/documentation/audiotoolbox/1502076-newmusiceventiterator)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus NewMusicEventIterator (     MusicTrack inTrack,     MusicEventIterator *outIterator ); ``` |
| To | ``` OSStatus NewMusicEventIterator (     MusicTrack _Nonnull inTrack,     MusicEventIterator  _Nullable * _Nonnull outIterator ); ``` |

Modified [NewMusicPlayer()](https://developer.apple.com/documentation/audiotoolbox/1503211-newmusicplayer)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus NewMusicPlayer (     MusicPlayer *outPlayer ); ``` |
| To | ``` OSStatus NewMusicPlayer (     MusicPlayer  _Nullable * _Nonnull outPlayer ); ``` |

Modified [NewMusicSequence()](https://developer.apple.com/documentation/audiotoolbox/1502634-newmusicsequence)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus NewMusicSequence (     MusicSequence *outSequence ); ``` |
| To | ``` OSStatus NewMusicSequence (     MusicSequence  _Nullable * _Nonnull outSequence ); ``` |

Modified [NewMusicTrackFrom()](https://developer.apple.com/documentation/audiotoolbox/1515469-newmusictrackfrom)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus NewMusicTrackFrom (     MusicTrack inSourceTrack,     MusicTimeStamp inSourceStartTime,     MusicTimeStamp inSourceEndTime,     MusicTrack *outNewTrack ); ``` |
| To | ``` OSStatus NewMusicTrackFrom (     MusicTrack _Nonnull inSourceTrack,     MusicTimeStamp inSourceStartTime,     MusicTimeStamp inSourceEndTime,     MusicTrack  _Nullable * _Nonnull outNewTrack ); ``` |

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
