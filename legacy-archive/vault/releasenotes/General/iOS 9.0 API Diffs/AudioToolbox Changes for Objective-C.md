---
title: iOS 9.0 API Diffs
apple_id: TP40016222
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS90APIDiffs/Objective-C/AudioToolbox.html
archived_at: '2026-07-18T02:56:30.581465Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 9.0 API Diffs](iOS%208.3%20to%20iOS%209.0%20API%20Differences.md)


# AudioToolbox Changes for Objective-C

### AudioToolbox

#### AudioConverter.h

Added #def AudioToolbox_AudioConverter_h

#### AudioFile.h

Removed [#def NextAudioFileRegion](https://developer.apple.com/documentation/audiotoolbox/audio_file_services/nextaudiofileregion)Removed [#def NumAudioFileMarkersToNumBytes](https://developer.apple.com/documentation/audiotoolbox/audio_file_services/numaudiofilemarkerstonumbytes)Removed [#def NumBytesToNumAudioFileMarkers](https://developer.apple.com/documentation/audiotoolbox/audio_file_services/numbytestonumaudiofilemarkers)Added [AudioBytePacketTranslationFlags](https://developer.apple.com/documentation/audiotoolbox/audiobytepackettranslationflags)Added [AudioFileFlags](https://developer.apple.com/documentation/audiotoolbox/audiofileflags)Added [AudioFilePermissions](https://developer.apple.com/documentation/audiotoolbox/audiofilepermissions)Added [AudioFileRegionFlags](https://developer.apple.com/documentation/audiotoolbox/audiofileregionflags)Added #def AudioToolbox_AudioFile_hAdded [NextAudioFileRegion()](https://developer.apple.com/documentation/audiotoolbox/1501607-nextaudiofileregion)Added [NumAudioFileMarkersToNumBytes()](https://developer.apple.com/documentation/audiotoolbox/1503350-numaudiofilemarkerstonumbytes)Added [NumBytesToNumAudioFileMarkers()](https://developer.apple.com/documentation/audiotoolbox/1502677-numbytestonumaudiofilemarkers)Modified [AudioFileCreateWithURL()](https://developer.apple.com/documentation/audiotoolbox/1502333-audiofilecreatewithurl)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AudioFileCreateWithURL (     CFURLRef inFileRef,     AudioFileTypeID inFileType,     const AudioStreamBasicDescription *inFormat,     UInt32 inFlags,     AudioFileID *outAudioFile ); ``` |
| To | ``` OSStatus AudioFileCreateWithURL (     CFURLRef _Nonnull inFileRef,     AudioFileTypeID inFileType,     const AudioStreamBasicDescription * _Nonnull inFormat,     AudioFileFlags inFlags,     AudioFileID  _Nullable * _Nonnull outAudioFile ); ``` |

Modified [AudioFileInitializeWithCallbacks()](https://developer.apple.com/documentation/audiotoolbox/1502895-audiofileinitializewithcallbacks)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AudioFileInitializeWithCallbacks (     void *inClientData,     AudioFile_ReadProc inReadFunc,     AudioFile_WriteProc inWriteFunc,     AudioFile_GetSizeProc inGetSizeFunc,     AudioFile_SetSizeProc inSetSizeFunc,     AudioFileTypeID inFileType,     const AudioStreamBasicDescription *inFormat,     UInt32 inFlags,     AudioFileID *outAudioFile ); ``` |
| To | ``` OSStatus AudioFileInitializeWithCallbacks (     void * _Nonnull inClientData,     AudioFile_ReadProc _Nonnull inReadFunc,     AudioFile_WriteProc _Nonnull inWriteFunc,     AudioFile_GetSizeProc _Nonnull inGetSizeFunc,     AudioFile_SetSizeProc _Nonnull inSetSizeFunc,     AudioFileTypeID inFileType,     const AudioStreamBasicDescription * _Nonnull inFormat,     AudioFileFlags inFlags,     AudioFileID  _Nullable * _Nonnull outAudioFile ); ``` |

Modified [AudioFileOpenURL()](https://developer.apple.com/documentation/audiotoolbox/1502304-audiofileopenurl)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AudioFileOpenURL (     CFURLRef inFileRef,     SInt8 inPermissions,     AudioFileTypeID inFileTypeHint,     AudioFileID *outAudioFile ); ``` |
| To | ``` OSStatus AudioFileOpenURL (     CFURLRef _Nonnull inFileRef,     AudioFilePermissions inPermissions,     AudioFileTypeID inFileTypeHint,     AudioFileID  _Nullable * _Nonnull outAudioFile ); ``` |

#### AudioFileStream.h

Added [AudioFileStreamParseFlags](https://developer.apple.com/documentation/audiotoolbox/audiofilestreamparseflags)Added [AudioFileStreamPropertyFlags](https://developer.apple.com/documentation/audiotoolbox/audiofilestreampropertyflags)Added [AudioFileStreamSeekFlags](https://developer.apple.com/documentation/audiotoolbox/audiofilestreamseekflags)Added #def AudioToolbox_AudioFileStream_hModified [AudioFileStreamParseBytes()](https://developer.apple.com/documentation/audiotoolbox/1391492-audiofilestreamparsebytes)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AudioFileStreamParseBytes (     AudioFileStreamID inAudioFileStream,     UInt32 inDataByteSize,     const void *inData,     UInt32 inFlags ); ``` |
| To | ``` OSStatus AudioFileStreamParseBytes (     AudioFileStreamID _Nonnull inAudioFileStream,     UInt32 inDataByteSize,     const void * _Nonnull inData,     AudioFileStreamParseFlags inFlags ); ``` |

Modified [AudioFileStreamSeek()](https://developer.apple.com/documentation/audiotoolbox/1391488-audiofilestreamseek)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AudioFileStreamSeek (     AudioFileStreamID inAudioFileStream,     SInt64 inPacketOffset,     SInt64 *outDataByteOffset,     UInt32 *ioFlags ); ``` |
| To | ``` OSStatus AudioFileStreamSeek (     AudioFileStreamID _Nonnull inAudioFileStream,     SInt64 inPacketOffset,     SInt64 * _Nonnull outDataByteOffset,     AudioFileStreamSeekFlags * _Nonnull ioFlags ); ``` |

#### AudioFormat.h

Added [AudioBalanceFadeType](https://developer.apple.com/documentation/audiotoolbox/audiobalancefadetype)Added [AudioPanningMode](https://developer.apple.com/documentation/audiotoolbox/audiopanningmode)Added #def AudioToolbox_AudioFormat_h

#### AudioQueue.h

Added [AudioQueueProcessingTapFlags](https://developer.apple.com/documentation/audiotoolbox/audioqueueprocessingtapflags)Added #def AudioToolbox_AudioQueue_hModified [AudioQueueProcessingTapGetSourceAudio()](https://developer.apple.com/documentation/audiotoolbox/1502107-audioqueueprocessingtapgetsource)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AudioQueueProcessingTapGetSourceAudio (     AudioQueueProcessingTapRef inAQTap,     UInt32 inNumberFrames,     AudioTimeStamp *ioTimeStamp,     UInt32 *outFlags,     UInt32 *outNumberFrames,     AudioBufferList *ioData ); ``` |
| To | ``` OSStatus AudioQueueProcessingTapGetSourceAudio (     AudioQueueProcessingTapRef _Nonnull inAQTap,     UInt32 inNumberFrames,     AudioTimeStamp * _Nonnull ioTimeStamp,     AudioQueueProcessingTapFlags * _Nonnull outFlags,     UInt32 * _Nonnull outNumberFrames,     AudioBufferList * _Nonnull ioData ); ``` |

Modified [AudioQueueProcessingTapNew()](https://developer.apple.com/documentation/audiotoolbox/1503209-audioqueueprocessingtapnew)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AudioQueueProcessingTapNew (     AudioQueueRef inAQ,     AudioQueueProcessingTapCallback inCallback,     void *inClientData,     UInt32 inFlags,     UInt32 *outMaxFrames,     AudioStreamBasicDescription *outProcessingFormat,     AudioQueueProcessingTapRef *outAQTap ); ``` |
| To | ``` OSStatus AudioQueueProcessingTapNew (     AudioQueueRef _Nonnull inAQ,     AudioQueueProcessingTapCallback _Nonnull inCallback,     void * _Nullable inClientData,     AudioQueueProcessingTapFlags inFlags,     UInt32 * _Nonnull outMaxFrames,     AudioStreamBasicDescription * _Nonnull outProcessingFormat,     AudioQueueProcessingTapRef  _Nullable * _Nonnull outAQTap ); ``` |

#### AudioServices.h

Added [AudioServicesPlayAlertSoundWithCompletion()](https://developer.apple.com/documentation/audiotoolbox/1405238-audioservicesplayalertsoundwithc)Added [AudioServicesPlaySystemSoundWithCompletion()](https://developer.apple.com/documentation/audiotoolbox/1405210-audioservicesplaysystemsoundwith)Added #def AudioToolbox_AudioServices_h

#### AudioToolbox.h

Added #def AudioToolbox_AudioToolbox_h

#### AUGraph.h

Added #def AudioToolbox_AUGraph_h

#### CAFFile.h

Added #def AudioToolbox_CAFFile_hAdded [CAFFormatFlags](https://developer.apple.com/documentation/audiotoolbox/cafformatflags)Added [CAFRegionFlags](https://developer.apple.com/documentation/audiotoolbox/cafregionflags)

#### ExtendedAudioFile.h

Added #def AudioToolbox_ExtendedAudioFile_h

#### MusicPlayer.h

Added #def AudioToolbox_MusicPlayer_hAdded [kAudioToolboxError_NoTrackDestination](https://developer.apple.com/documentation/audiotoolbox/1515472-anonymous/kaudiotoolboxerror_notrackdestination)Added [kMusicSequenceFile_AnyType](https://developer.apple.com/documentation/audiotoolbox/musicsequencefiletypeid/anytype)Added [kMusicSequenceFileFlags_Default](https://developer.apple.com/documentation/audiotoolbox/musicsequencefileflags/kmusicsequencefileflags_default)Added [kMusicSequenceLoadSMF_PreserveTracks](https://developer.apple.com/documentation/audiotoolbox/musicsequenceloadflags/1501705-smf_preservetracks)

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
