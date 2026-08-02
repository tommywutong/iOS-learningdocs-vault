---
title: OS X v10.11 API Diffs
apple_id: TP40016197
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_11/Objective-C/CoreAudio.html
archived_at: '2026-07-18T02:52:57.458813Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.11 API Diffs](OS%20X%20v10.11%20API%20Diffs.md)


# CoreAudio Changes for Objective-C

### CoreAudio

#### AudioDriverPlugIn.h

Added #def CoreAudio_AudioDriverPlugIn_hModified [AudioDriverPlugInDeviceGetProperty()](https://developer.apple.com/documentation/coreaudio/1534803-audiodriverplugindevicegetproper)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AudioDriverPlugInDeviceGetProperty (     AudioDeviceID inDevice,     UInt32 inChannel,     Boolean isInput,     AudioDevicePropertyID inPropertyID,     UInt32 *ioPropertyDataSize,     void *outPropertyData ); ``` |
| To | ``` OSStatus AudioDriverPlugInDeviceGetProperty (     AudioDeviceID inDevice,     UInt32 inChannel,     Boolean isInput,     AudioDevicePropertyID inPropertyID,     UInt32 * _Nonnull ioPropertyDataSize,     void * _Nonnull outPropertyData ); ``` |

Modified [AudioDriverPlugInDeviceGetPropertyInfo()](https://developer.apple.com/documentation/coreaudio/1534802-audiodriverplugindevicegetproper)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AudioDriverPlugInDeviceGetPropertyInfo (     AudioDeviceID inDevice,     UInt32 inChannel,     Boolean isInput,     AudioDevicePropertyID inPropertyID,     UInt32 *outSize,     Boolean *outWritable ); ``` |
| To | ``` OSStatus AudioDriverPlugInDeviceGetPropertyInfo (     AudioDeviceID inDevice,     UInt32 inChannel,     Boolean isInput,     AudioDevicePropertyID inPropertyID,     UInt32 * _Nullable outSize,     Boolean * _Nullable outWritable ); ``` |

Modified [AudioDriverPlugInDeviceSetProperty()](https://developer.apple.com/documentation/coreaudio/1534796-audiodriverplugindevicesetproper)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AudioDriverPlugInDeviceSetProperty (     AudioDeviceID inDevice,     const AudioTimeStamp *inWhen,     UInt32 inChannel,     Boolean isInput,     AudioDevicePropertyID inPropertyID,     UInt32 inPropertyDataSize,     const void *inPropertyData ); ``` |
| To | ``` OSStatus AudioDriverPlugInDeviceSetProperty (     AudioDeviceID inDevice,     const AudioTimeStamp * _Nullable inWhen,     UInt32 inChannel,     Boolean isInput,     AudioDevicePropertyID inPropertyID,     UInt32 inPropertyDataSize,     const void * _Nonnull inPropertyData ); ``` |

Modified [AudioDriverPlugInOpen()](https://developer.apple.com/documentation/coreaudio/1534791-audiodriverpluginopen)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AudioDriverPlugInOpen (     AudioDriverPlugInHostInfo *inHostInfo ); ``` |
| To | ``` OSStatus AudioDriverPlugInOpen (     AudioDriverPlugInHostInfo * _Nonnull inHostInfo ); ``` |

Modified [AudioDriverPlugInStreamGetProperty()](https://developer.apple.com/documentation/coreaudio/1534780-audiodriverpluginstreamgetproper)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AudioDriverPlugInStreamGetProperty (     AudioDeviceID inDevice,     io_object_t inIOAudioStream,     UInt32 inChannel,     AudioDevicePropertyID inPropertyID,     UInt32 *ioPropertyDataSize,     void *outPropertyData ); ``` |
| To | ``` OSStatus AudioDriverPlugInStreamGetProperty (     AudioDeviceID inDevice,     io_object_t inIOAudioStream,     UInt32 inChannel,     AudioDevicePropertyID inPropertyID,     UInt32 * _Nonnull ioPropertyDataSize,     void * _Nonnull outPropertyData ); ``` |

Modified [AudioDriverPlugInStreamGetPropertyInfo()](https://developer.apple.com/documentation/coreaudio/1534801-audiodriverpluginstreamgetproper)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AudioDriverPlugInStreamGetPropertyInfo (     AudioDeviceID inDevice,     io_object_t inIOAudioStream,     UInt32 inChannel,     AudioDevicePropertyID inPropertyID,     UInt32 *outSize,     Boolean *outWritable ); ``` |
| To | ``` OSStatus AudioDriverPlugInStreamGetPropertyInfo (     AudioDeviceID inDevice,     io_object_t inIOAudioStream,     UInt32 inChannel,     AudioDevicePropertyID inPropertyID,     UInt32 * _Nullable outSize,     Boolean * _Nullable outWritable ); ``` |

Modified [AudioDriverPlugInStreamSetProperty()](https://developer.apple.com/documentation/coreaudio/1534790-audiodriverpluginstreamsetproper)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AudioDriverPlugInStreamSetProperty (     AudioDeviceID inDevice,     io_object_t inIOAudioStream,     const AudioTimeStamp *inWhen,     UInt32 inChannel,     AudioDevicePropertyID inPropertyID,     UInt32 inPropertyDataSize,     const void *inPropertyData ); ``` |
| To | ``` OSStatus AudioDriverPlugInStreamSetProperty (     AudioDeviceID inDevice,     io_object_t inIOAudioStream,     const AudioTimeStamp * _Nullable inWhen,     UInt32 inChannel,     AudioDevicePropertyID inPropertyID,     UInt32 inPropertyDataSize,     const void * _Nonnull inPropertyData ); ``` |

#### AudioHardware.h

Added [AudioHardwarePowerHint](https://developer.apple.com/documentation/coreaudio/audiohardwarepowerhint)Added #def CoreAudio_AudioHardware_hModified [AudioDeviceCreateIOProcID()](https://developer.apple.com/documentation/coreaudio/1423215-audiodevicecreateioprocid)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AudioDeviceCreateIOProcID (     AudioObjectID inDevice,     AudioDeviceIOProc inProc,     void *inClientData,     AudioDeviceIOProcID *outIOProcID ); ``` |
| To | ``` OSStatus AudioDeviceCreateIOProcID (     AudioObjectID inDevice,     AudioDeviceIOProc _Nonnull inProc,     void * _Nullable inClientData,     AudioDeviceIOProcID  _Nullable * _Nonnull outIOProcID ); ``` |

Modified [AudioDeviceCreateIOProcIDWithBlock()](https://developer.apple.com/documentation/coreaudio/1422986-audiodevicecreateioprocidwithblo)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AudioDeviceCreateIOProcIDWithBlock (     AudioDeviceIOProcID *outIOProcID,     AudioObjectID inDevice,     dispatch_queue_t inDispatchQueue,     AudioDeviceIOBlock inIOBlock ); ``` |
| To | ``` OSStatus AudioDeviceCreateIOProcIDWithBlock (     AudioDeviceIOProcID  _Nullable * _Nonnull outIOProcID,     AudioObjectID inDevice,     dispatch_queue_t _Nullable inDispatchQueue,     AudioDeviceIOBlock _Nonnull inIOBlock ); ``` |

Modified [AudioDeviceDestroyIOProcID()](https://developer.apple.com/documentation/coreaudio/1422982-audiodevicedestroyioprocid)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AudioDeviceDestroyIOProcID (     AudioObjectID inDevice,     AudioDeviceIOProcID inIOProcID ); ``` |
| To | ``` OSStatus AudioDeviceDestroyIOProcID (     AudioObjectID inDevice,     AudioDeviceIOProcID _Nonnull inIOProcID ); ``` |

Modified [AudioDeviceGetCurrentTime()](https://developer.apple.com/documentation/coreaudio/1421759-audiodevicegetcurrenttime)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AudioDeviceGetCurrentTime (     AudioObjectID inDevice,     AudioTimeStamp *outTime ); ``` |
| To | ``` OSStatus AudioDeviceGetCurrentTime (     AudioObjectID inDevice,     AudioTimeStamp * _Nonnull outTime ); ``` |

Modified [AudioDeviceGetNearestStartTime()](https://developer.apple.com/documentation/coreaudio/1421818-audiodevicegetneareststarttime)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AudioDeviceGetNearestStartTime (     AudioObjectID inDevice,     AudioTimeStamp *ioRequestedStartTime,     UInt32 inFlags ); ``` |
| To | ``` OSStatus AudioDeviceGetNearestStartTime (     AudioObjectID inDevice,     AudioTimeStamp * _Nonnull ioRequestedStartTime,     UInt32 inFlags ); ``` |

Modified [AudioDeviceStart()](https://developer.apple.com/documentation/coreaudio/1422884-audiodevicestart)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AudioDeviceStart (     AudioObjectID inDevice,     AudioDeviceIOProcID inProcID ); ``` |
| To | ``` OSStatus AudioDeviceStart (     AudioObjectID inDevice,     AudioDeviceIOProcID _Nullable inProcID ); ``` |

Modified [AudioDeviceStartAtTime()](https://developer.apple.com/documentation/coreaudio/1422331-audiodevicestartattime)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AudioDeviceStartAtTime (     AudioObjectID inDevice,     AudioDeviceIOProcID inProcID,     AudioTimeStamp *ioRequestedStartTime,     UInt32 inFlags ); ``` |
| To | ``` OSStatus AudioDeviceStartAtTime (     AudioObjectID inDevice,     AudioDeviceIOProcID _Nullable inProcID,     AudioTimeStamp * _Nonnull ioRequestedStartTime,     UInt32 inFlags ); ``` |

Modified [AudioDeviceStop()](https://developer.apple.com/documentation/coreaudio/1421761-audiodevicestop)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AudioDeviceStop (     AudioObjectID inDevice,     AudioDeviceIOProcID inProcID ); ``` |
| To | ``` OSStatus AudioDeviceStop (     AudioObjectID inDevice,     AudioDeviceIOProcID _Nullable inProcID ); ``` |

Modified [AudioDeviceTranslateTime()](https://developer.apple.com/documentation/coreaudio/1422786-audiodevicetranslatetime)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AudioDeviceTranslateTime (     AudioObjectID inDevice,     const AudioTimeStamp *inTime,     AudioTimeStamp *outTime ); ``` |
| To | ``` OSStatus AudioDeviceTranslateTime (     AudioObjectID inDevice,     const AudioTimeStamp * _Nonnull inTime,     AudioTimeStamp * _Nonnull outTime ); ``` |

Modified [AudioHardwareCreateAggregateDevice()](https://developer.apple.com/documentation/coreaudio/1422096-audiohardwarecreateaggregatedevi)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AudioHardwareCreateAggregateDevice (     CFDictionaryRef inDescription,     AudioObjectID *outDeviceID ); ``` |
| To | ``` OSStatus AudioHardwareCreateAggregateDevice (     CFDictionaryRef _Nonnull inDescription,     AudioObjectID * _Nonnull outDeviceID ); ``` |

Modified [AudioObjectAddPropertyListener()](https://developer.apple.com/documentation/coreaudio/1422472-audioobjectaddpropertylistener)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AudioObjectAddPropertyListener (     AudioObjectID inObjectID,     const AudioObjectPropertyAddress *inAddress,     AudioObjectPropertyListenerProc inListener,     void *inClientData ); ``` |
| To | ``` OSStatus AudioObjectAddPropertyListener (     AudioObjectID inObjectID,     const AudioObjectPropertyAddress * _Nonnull inAddress,     AudioObjectPropertyListenerProc _Nonnull inListener,     void * _Nullable inClientData ); ``` |

Modified [AudioObjectAddPropertyListenerBlock()](https://developer.apple.com/documentation/coreaudio/1422686-audioobjectaddpropertylistenerbl)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AudioObjectAddPropertyListenerBlock (     AudioObjectID inObjectID,     const AudioObjectPropertyAddress *inAddress,     dispatch_queue_t inDispatchQueue,     AudioObjectPropertyListenerBlock inListener ); ``` |
| To | ``` OSStatus AudioObjectAddPropertyListenerBlock (     AudioObjectID inObjectID,     const AudioObjectPropertyAddress * _Nonnull inAddress,     dispatch_queue_t _Nullable inDispatchQueue,     AudioObjectPropertyListenerBlock _Nonnull inListener ); ``` |

Modified [AudioObjectGetPropertyData()](https://developer.apple.com/documentation/coreaudio/1422524-audioobjectgetpropertydata)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AudioObjectGetPropertyData (     AudioObjectID inObjectID,     const AudioObjectPropertyAddress *inAddress,     UInt32 inQualifierDataSize,     const void *inQualifierData,     UInt32 *ioDataSize,     void *outData ); ``` |
| To | ``` OSStatus AudioObjectGetPropertyData (     AudioObjectID inObjectID,     const AudioObjectPropertyAddress * _Nonnull inAddress,     UInt32 inQualifierDataSize,     const void * _Nullable inQualifierData,     UInt32 * _Nonnull ioDataSize,     void * _Nonnull outData ); ``` |

Modified [AudioObjectGetPropertyDataSize()](https://developer.apple.com/documentation/coreaudio/1422305-audioobjectgetpropertydatasize)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AudioObjectGetPropertyDataSize (     AudioObjectID inObjectID,     const AudioObjectPropertyAddress *inAddress,     UInt32 inQualifierDataSize,     const void *inQualifierData,     UInt32 *outDataSize ); ``` |
| To | ``` OSStatus AudioObjectGetPropertyDataSize (     AudioObjectID inObjectID,     const AudioObjectPropertyAddress * _Nonnull inAddress,     UInt32 inQualifierDataSize,     const void * _Nullable inQualifierData,     UInt32 * _Nonnull outDataSize ); ``` |

Modified [AudioObjectHasProperty()](https://developer.apple.com/documentation/coreaudio/1422538-audioobjecthasproperty)

|  | Declaration |
| --- | --- |
| From | ``` Boolean AudioObjectHasProperty (     AudioObjectID inObjectID,     const AudioObjectPropertyAddress *inAddress ); ``` |
| To | ``` Boolean AudioObjectHasProperty (     AudioObjectID inObjectID,     const AudioObjectPropertyAddress * _Nonnull inAddress ); ``` |

Modified [AudioObjectIsPropertySettable()](https://developer.apple.com/documentation/coreaudio/1423182-audioobjectispropertysettable)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AudioObjectIsPropertySettable (     AudioObjectID inObjectID,     const AudioObjectPropertyAddress *inAddress,     Boolean *outIsSettable ); ``` |
| To | ``` OSStatus AudioObjectIsPropertySettable (     AudioObjectID inObjectID,     const AudioObjectPropertyAddress * _Nonnull inAddress,     Boolean * _Nonnull outIsSettable ); ``` |

Modified [AudioObjectRemovePropertyListener()](https://developer.apple.com/documentation/coreaudio/1422593-audioobjectremovepropertylistene)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AudioObjectRemovePropertyListener (     AudioObjectID inObjectID,     const AudioObjectPropertyAddress *inAddress,     AudioObjectPropertyListenerProc inListener,     void *inClientData ); ``` |
| To | ``` OSStatus AudioObjectRemovePropertyListener (     AudioObjectID inObjectID,     const AudioObjectPropertyAddress * _Nonnull inAddress,     AudioObjectPropertyListenerProc _Nonnull inListener,     void * _Nullable inClientData ); ``` |

Modified [AudioObjectRemovePropertyListenerBlock()](https://developer.apple.com/documentation/coreaudio/1421640-audioobjectremovepropertylistene)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AudioObjectRemovePropertyListenerBlock (     AudioObjectID inObjectID,     const AudioObjectPropertyAddress *inAddress,     dispatch_queue_t inDispatchQueue,     AudioObjectPropertyListenerBlock inListener ); ``` |
| To | ``` OSStatus AudioObjectRemovePropertyListenerBlock (     AudioObjectID inObjectID,     const AudioObjectPropertyAddress * _Nonnull inAddress,     dispatch_queue_t _Nullable inDispatchQueue,     AudioObjectPropertyListenerBlock _Nonnull inListener ); ``` |

Modified [AudioObjectSetPropertyData()](https://developer.apple.com/documentation/coreaudio/1422920-audioobjectsetpropertydata)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AudioObjectSetPropertyData (     AudioObjectID inObjectID,     const AudioObjectPropertyAddress *inAddress,     UInt32 inQualifierDataSize,     const void *inQualifierData,     UInt32 inDataSize,     const void *inData ); ``` |
| To | ``` OSStatus AudioObjectSetPropertyData (     AudioObjectID inObjectID,     const AudioObjectPropertyAddress * _Nonnull inAddress,     UInt32 inQualifierDataSize,     const void * _Nullable inQualifierData,     UInt32 inDataSize,     const void * _Nonnull inData ); ``` |

#### AudioHardwareBase.h

Added #def CoreAudio_AudioHardwareBase_h

#### AudioHardwareDeprecated.h

Added [AudioLevelControlTransferFunction](https://developer.apple.com/documentation/coreaudio/audiolevelcontroltransferfunction)Added #def CoreAudio_AudioHardwareDeprecated_hModified [AudioDeviceAddIOProc()](https://developer.apple.com/documentation/coreaudio/1580729-audiodeviceaddioproc)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AudioDeviceAddIOProc (     AudioDeviceID inDevice,     AudioDeviceIOProc inProc,     void *inClientData ); ``` |
| To | ``` OSStatus AudioDeviceAddIOProc (     AudioDeviceID inDevice,     AudioDeviceIOProc _Nonnull inProc,     void * _Nullable inClientData ); ``` |

Modified [AudioDeviceAddPropertyListener()](https://developer.apple.com/documentation/coreaudio/1580727-audiodeviceaddpropertylistener)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AudioDeviceAddPropertyListener (     AudioDeviceID inDevice,     UInt32 inChannel,     Boolean isInput,     AudioDevicePropertyID inPropertyID,     AudioDevicePropertyListenerProc inProc,     void *inClientData ); ``` |
| To | ``` OSStatus AudioDeviceAddPropertyListener (     AudioDeviceID inDevice,     UInt32 inChannel,     Boolean isInput,     AudioDevicePropertyID inPropertyID,     AudioDevicePropertyListenerProc _Nonnull inProc,     void * _Nullable inClientData ); ``` |

Modified [AudioDeviceGetProperty()](https://developer.apple.com/documentation/coreaudio/1580744-audiodevicegetproperty)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AudioDeviceGetProperty (     AudioDeviceID inDevice,     UInt32 inChannel,     Boolean isInput,     AudioDevicePropertyID inPropertyID,     UInt32 *ioPropertyDataSize,     void *outPropertyData ); ``` |
| To | ``` OSStatus AudioDeviceGetProperty (     AudioDeviceID inDevice,     UInt32 inChannel,     Boolean isInput,     AudioDevicePropertyID inPropertyID,     UInt32 * _Nonnull ioPropertyDataSize,     void * _Nonnull outPropertyData ); ``` |

Modified [AudioDeviceGetPropertyInfo()](https://developer.apple.com/documentation/coreaudio/1580721-audiodevicegetpropertyinfo)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AudioDeviceGetPropertyInfo (     AudioDeviceID inDevice,     UInt32 inChannel,     Boolean isInput,     AudioDevicePropertyID inPropertyID,     UInt32 *outSize,     Boolean *outWritable ); ``` |
| To | ``` OSStatus AudioDeviceGetPropertyInfo (     AudioDeviceID inDevice,     UInt32 inChannel,     Boolean isInput,     AudioDevicePropertyID inPropertyID,     UInt32 * _Nullable outSize,     Boolean * _Nullable outWritable ); ``` |

Modified [AudioDeviceRead()](https://developer.apple.com/documentation/coreaudio/1580734-audiodeviceread)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AudioDeviceRead (     AudioDeviceID inDevice,     const AudioTimeStamp *inStartTime,     AudioBufferList *outData ); ``` |
| To | ``` OSStatus AudioDeviceRead (     AudioDeviceID inDevice,     const AudioTimeStamp * _Nonnull inStartTime,     AudioBufferList * _Nonnull outData ); ``` |

Modified [AudioDeviceRemoveIOProc()](https://developer.apple.com/documentation/coreaudio/1580735-audiodeviceremoveioproc)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AudioDeviceRemoveIOProc (     AudioDeviceID inDevice,     AudioDeviceIOProc inProc ); ``` |
| To | ``` OSStatus AudioDeviceRemoveIOProc (     AudioDeviceID inDevice,     AudioDeviceIOProc _Nonnull inProc ); ``` |

Modified [AudioDeviceRemovePropertyListener()](https://developer.apple.com/documentation/coreaudio/1580714-audiodeviceremovepropertylistene)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AudioDeviceRemovePropertyListener (     AudioDeviceID inDevice,     UInt32 inChannel,     Boolean isInput,     AudioDevicePropertyID inPropertyID,     AudioDevicePropertyListenerProc inProc ); ``` |
| To | ``` OSStatus AudioDeviceRemovePropertyListener (     AudioDeviceID inDevice,     UInt32 inChannel,     Boolean isInput,     AudioDevicePropertyID inPropertyID,     AudioDevicePropertyListenerProc _Nonnull inProc ); ``` |

Modified [AudioDeviceSetProperty()](https://developer.apple.com/documentation/coreaudio/1580742-audiodevicesetproperty)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AudioDeviceSetProperty (     AudioDeviceID inDevice,     const AudioTimeStamp *inWhen,     UInt32 inChannel,     Boolean isInput,     AudioDevicePropertyID inPropertyID,     UInt32 inPropertyDataSize,     const void *inPropertyData ); ``` |
| To | ``` OSStatus AudioDeviceSetProperty (     AudioDeviceID inDevice,     const AudioTimeStamp * _Nullable inWhen,     UInt32 inChannel,     Boolean isInput,     AudioDevicePropertyID inPropertyID,     UInt32 inPropertyDataSize,     const void * _Nonnull inPropertyData ); ``` |

Modified [AudioHardwareAddPropertyListener()](https://developer.apple.com/documentation/coreaudio/1580750-audiohardwareaddpropertylistener)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AudioHardwareAddPropertyListener (     AudioHardwarePropertyID inPropertyID,     AudioHardwarePropertyListenerProc inProc,     void *inClientData ); ``` |
| To | ``` OSStatus AudioHardwareAddPropertyListener (     AudioHardwarePropertyID inPropertyID,     AudioHardwarePropertyListenerProc _Nonnull inProc,     void * _Nullable inClientData ); ``` |

Modified [AudioHardwareAddRunLoopSource()](https://developer.apple.com/documentation/coreaudio/1580725-audiohardwareaddrunloopsource)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AudioHardwareAddRunLoopSource (     CFRunLoopSourceRef inRunLoopSource ); ``` |
| To | ``` OSStatus AudioHardwareAddRunLoopSource (     CFRunLoopSourceRef _Nonnull inRunLoopSource ); ``` |

Modified [AudioHardwareGetProperty()](https://developer.apple.com/documentation/coreaudio/1580718-audiohardwaregetproperty)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AudioHardwareGetProperty (     AudioHardwarePropertyID inPropertyID,     UInt32 *ioPropertyDataSize,     void *outPropertyData ); ``` |
| To | ``` OSStatus AudioHardwareGetProperty (     AudioHardwarePropertyID inPropertyID,     UInt32 * _Nonnull ioPropertyDataSize,     void * _Nonnull outPropertyData ); ``` |

Modified [AudioHardwareGetPropertyInfo()](https://developer.apple.com/documentation/coreaudio/1580716-audiohardwaregetpropertyinfo)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AudioHardwareGetPropertyInfo (     AudioHardwarePropertyID inPropertyID,     UInt32 *outSize,     Boolean *outWritable ); ``` |
| To | ``` OSStatus AudioHardwareGetPropertyInfo (     AudioHardwarePropertyID inPropertyID,     UInt32 * _Nullable outSize,     Boolean * _Nullable outWritable ); ``` |

Modified [AudioHardwareRemovePropertyListener()](https://developer.apple.com/documentation/coreaudio/1580739-audiohardwareremovepropertyliste)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AudioHardwareRemovePropertyListener (     AudioHardwarePropertyID inPropertyID,     AudioHardwarePropertyListenerProc inProc ); ``` |
| To | ``` OSStatus AudioHardwareRemovePropertyListener (     AudioHardwarePropertyID inPropertyID,     AudioHardwarePropertyListenerProc _Nonnull inProc ); ``` |

Modified [AudioHardwareRemoveRunLoopSource()](https://developer.apple.com/documentation/coreaudio/1580717-audiohardwareremoverunloopsource)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AudioHardwareRemoveRunLoopSource (     CFRunLoopSourceRef inRunLoopSource ); ``` |
| To | ``` OSStatus AudioHardwareRemoveRunLoopSource (     CFRunLoopSourceRef _Nonnull inRunLoopSource ); ``` |

Modified [AudioHardwareSetProperty()](https://developer.apple.com/documentation/coreaudio/1580730-audiohardwaresetproperty)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AudioHardwareSetProperty (     AudioHardwarePropertyID inPropertyID,     UInt32 inPropertyDataSize,     const void *inPropertyData ); ``` |
| To | ``` OSStatus AudioHardwareSetProperty (     AudioHardwarePropertyID inPropertyID,     UInt32 inPropertyDataSize,     const void * _Nonnull inPropertyData ); ``` |

Modified [AudioStreamAddPropertyListener()](https://developer.apple.com/documentation/coreaudio/1580732-audiostreamaddpropertylistener)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AudioStreamAddPropertyListener (     AudioStreamID inStream,     UInt32 inChannel,     AudioDevicePropertyID inPropertyID,     AudioStreamPropertyListenerProc inProc,     void *inClientData ); ``` |
| To | ``` OSStatus AudioStreamAddPropertyListener (     AudioStreamID inStream,     UInt32 inChannel,     AudioDevicePropertyID inPropertyID,     AudioStreamPropertyListenerProc _Nonnull inProc,     void * _Nullable inClientData ); ``` |

Modified [AudioStreamGetProperty()](https://developer.apple.com/documentation/coreaudio/1580743-audiostreamgetproperty)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AudioStreamGetProperty (     AudioStreamID inStream,     UInt32 inChannel,     AudioDevicePropertyID inPropertyID,     UInt32 *ioPropertyDataSize,     void *outPropertyData ); ``` |
| To | ``` OSStatus AudioStreamGetProperty (     AudioStreamID inStream,     UInt32 inChannel,     AudioDevicePropertyID inPropertyID,     UInt32 * _Nonnull ioPropertyDataSize,     void * _Nonnull outPropertyData ); ``` |

Modified [AudioStreamGetPropertyInfo()](https://developer.apple.com/documentation/coreaudio/1580745-audiostreamgetpropertyinfo)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AudioStreamGetPropertyInfo (     AudioStreamID inStream,     UInt32 inChannel,     AudioDevicePropertyID inPropertyID,     UInt32 *outSize,     Boolean *outWritable ); ``` |
| To | ``` OSStatus AudioStreamGetPropertyInfo (     AudioStreamID inStream,     UInt32 inChannel,     AudioDevicePropertyID inPropertyID,     UInt32 * _Nullable outSize,     Boolean * _Nullable outWritable ); ``` |

Modified [AudioStreamRemovePropertyListener()](https://developer.apple.com/documentation/coreaudio/1580751-audiostreamremovepropertylistene)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AudioStreamRemovePropertyListener (     AudioStreamID inStream,     UInt32 inChannel,     AudioDevicePropertyID inPropertyID,     AudioStreamPropertyListenerProc inProc ); ``` |
| To | ``` OSStatus AudioStreamRemovePropertyListener (     AudioStreamID inStream,     UInt32 inChannel,     AudioDevicePropertyID inPropertyID,     AudioStreamPropertyListenerProc _Nonnull inProc ); ``` |

Modified [AudioStreamSetProperty()](https://developer.apple.com/documentation/coreaudio/1580733-audiostreamsetproperty)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AudioStreamSetProperty (     AudioStreamID inStream,     const AudioTimeStamp *inWhen,     UInt32 inChannel,     AudioDevicePropertyID inPropertyID,     UInt32 inPropertyDataSize,     const void *inPropertyData ); ``` |
| To | ``` OSStatus AudioStreamSetProperty (     AudioStreamID inStream,     const AudioTimeStamp * _Nullable inWhen,     UInt32 inChannel,     AudioDevicePropertyID inPropertyID,     UInt32 inPropertyDataSize,     const void * _Nonnull inPropertyData ); ``` |

#### AudioHardwarePlugIn.h

Added #def CoreAudio_AudioHardwarePlugIn_hModified [AudioHardwareClaimAudioDeviceID()](https://developer.apple.com/documentation/coreaudio/1585923-audiohardwareclaimaudiodeviceid)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AudioHardwareClaimAudioDeviceID (     AudioHardwarePlugInRef inOwner,     AudioDeviceID *outAudioDeviceID ); ``` |
| To | ``` OSStatus AudioHardwareClaimAudioDeviceID (     AudioHardwarePlugInRef _Nonnull inOwner,     AudioDeviceID * _Nonnull outAudioDeviceID ); ``` |

Modified [AudioHardwareClaimAudioStreamID()](https://developer.apple.com/documentation/coreaudio/1585933-audiohardwareclaimaudiostreamid)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AudioHardwareClaimAudioStreamID (     AudioHardwarePlugInRef inOwner,     AudioDeviceID inOwningDeviceID,     AudioStreamID *outAudioStreamID ); ``` |
| To | ``` OSStatus AudioHardwareClaimAudioStreamID (     AudioHardwarePlugInRef _Nonnull inOwner,     AudioDeviceID inOwningDeviceID,     AudioStreamID * _Nonnull outAudioStreamID ); ``` |

Modified [AudioHardwareDevicePropertyChanged()](https://developer.apple.com/documentation/coreaudio/1585935-audiohardwaredevicepropertychang)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AudioHardwareDevicePropertyChanged (     AudioHardwarePlugInRef inOwner,     AudioDeviceID inDeviceID,     UInt32 inChannel,     Boolean isInput,     AudioDevicePropertyID inPropertyID ); ``` |
| To | ``` OSStatus AudioHardwareDevicePropertyChanged (     AudioHardwarePlugInRef _Nonnull inOwner,     AudioDeviceID inDeviceID,     UInt32 inChannel,     Boolean isInput,     AudioDevicePropertyID inPropertyID ); ``` |

Modified [AudioHardwareDevicesCreated()](https://developer.apple.com/documentation/coreaudio/1585929-audiohardwaredevicescreated)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AudioHardwareDevicesCreated (     AudioHardwarePlugInRef inOwner,     UInt32 inNumberDevices,     const AudioDeviceID *inAudioDeviceIDs ); ``` |
| To | ``` OSStatus AudioHardwareDevicesCreated (     AudioHardwarePlugInRef _Nonnull inOwner,     UInt32 inNumberDevices,     const AudioDeviceID * _Nonnull inAudioDeviceIDs ); ``` |

Modified [AudioHardwareDevicesDied()](https://developer.apple.com/documentation/coreaudio/1585895-audiohardwaredevicesdied)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AudioHardwareDevicesDied (     AudioHardwarePlugInRef inOwner,     UInt32 inNumberDevices,     const AudioDeviceID *inAudioDeviceIDs ); ``` |
| To | ``` OSStatus AudioHardwareDevicesDied (     AudioHardwarePlugInRef _Nonnull inOwner,     UInt32 inNumberDevices,     const AudioDeviceID * _Nonnull inAudioDeviceIDs ); ``` |

Modified [AudioHardwareStreamPropertyChanged()](https://developer.apple.com/documentation/coreaudio/1585902-audiohardwarestreampropertychang)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AudioHardwareStreamPropertyChanged (     AudioHardwarePlugInRef inOwner,     AudioDeviceID inOwningDeviceID,     AudioStreamID inStreamID,     UInt32 inChannel,     AudioDevicePropertyID inPropertyID ); ``` |
| To | ``` OSStatus AudioHardwareStreamPropertyChanged (     AudioHardwarePlugInRef _Nonnull inOwner,     AudioDeviceID inOwningDeviceID,     AudioStreamID inStreamID,     UInt32 inChannel,     AudioDevicePropertyID inPropertyID ); ``` |

Modified [AudioHardwareStreamsCreated()](https://developer.apple.com/documentation/coreaudio/1585932-audiohardwarestreamscreated)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AudioHardwareStreamsCreated (     AudioHardwarePlugInRef inOwner,     AudioDeviceID inOwningDeviceID,     UInt32 inNumberStreams,     const AudioStreamID *inAudioStreamIDs ); ``` |
| To | ``` OSStatus AudioHardwareStreamsCreated (     AudioHardwarePlugInRef _Nonnull inOwner,     AudioDeviceID inOwningDeviceID,     UInt32 inNumberStreams,     const AudioStreamID * _Nonnull inAudioStreamIDs ); ``` |

Modified [AudioHardwareStreamsDied()](https://developer.apple.com/documentation/coreaudio/1585927-audiohardwarestreamsdied)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AudioHardwareStreamsDied (     AudioHardwarePlugInRef inOwner,     AudioDeviceID inOwningDeviceID,     UInt32 inNumberStreams,     const AudioStreamID *inAudioStreamIDs ); ``` |
| To | ``` OSStatus AudioHardwareStreamsDied (     AudioHardwarePlugInRef _Nonnull inOwner,     AudioDeviceID inOwningDeviceID,     UInt32 inNumberStreams,     const AudioStreamID * _Nonnull inAudioStreamIDs ); ``` |

Modified [AudioObjectCreate()](https://developer.apple.com/documentation/coreaudio/1585905-audioobjectcreate)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AudioObjectCreate (     AudioHardwarePlugInRef inOwningPlugIn,     AudioObjectID inOwningObjectID,     AudioClassID inClassID,     AudioObjectID *outAudioObjectID ); ``` |
| To | ``` OSStatus AudioObjectCreate (     AudioHardwarePlugInRef _Nonnull inOwningPlugIn,     AudioObjectID inOwningObjectID,     AudioClassID inClassID,     AudioObjectID * _Nonnull outAudioObjectID ); ``` |

Modified [AudioObjectPropertiesChanged()](https://developer.apple.com/documentation/coreaudio/1585917-audioobjectpropertieschanged)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AudioObjectPropertiesChanged (     AudioHardwarePlugInRef inOwningPlugIn,     AudioObjectID inObjectID,     UInt32 inNumberAddresses,     const AudioObjectPropertyAddress inAddresses[] ); ``` |
| To | ``` OSStatus AudioObjectPropertiesChanged (     AudioHardwarePlugInRef _Nonnull inOwningPlugIn,     AudioObjectID inObjectID,     UInt32 inNumberAddresses,     const AudioObjectPropertyAddress * _Nonnull inAddresses ); ``` |

Modified [AudioObjectsPublishedAndDied()](https://developer.apple.com/documentation/coreaudio/1585908-audioobjectspublishedanddied)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AudioObjectsPublishedAndDied (     AudioHardwarePlugInRef inOwningPlugIn,     AudioObjectID inOwningObjectID,     UInt32 inNumberPublishedAudioObjects,     const AudioObjectID inPublishedAudioObjects[],     UInt32 inNumberDeadAudioObjects,     const AudioObjectID inDeadAudioObjects[] ); ``` |
| To | ``` OSStatus AudioObjectsPublishedAndDied (     AudioHardwarePlugInRef _Nonnull inOwningPlugIn,     AudioObjectID inOwningObjectID,     UInt32 inNumberPublishedAudioObjects,     const AudioObjectID * _Nullable inPublishedAudioObjects,     UInt32 inNumberDeadAudioObjects,     const AudioObjectID * _Nullable inDeadAudioObjects ); ``` |

#### AudioServerPlugIn.h

Added [AudioDeviceClockAlgorithmSelector](https://developer.apple.com/documentation/coreaudio/audiodeviceclockalgorithmselector)Added [AudioServerPlugInCustomPropertyDataType](https://developer.apple.com/documentation/coreaudio/audioserverplugincustompropertydatatype)Added [AudioServerPlugInIOOperation](https://developer.apple.com/documentation/coreaudio/audioserverpluginiooperation)Added #def CoreAudio_AudioServerPlugIn_h

#### CoreAudio.h

Added #def CoreAudio_CoreAudio_h

#### CoreAudioTypes.h

Removed [#def AudioChannelLayoutTag_GetNumberOfChannels](https://developer.apple.com/documentation/coreaudio/core_audio_data_types/audiochannellayouttag_getnumberofchannels)Removed [kAudioStreamAnyRate](https://developer.apple.com/documentation/coreaudio/core_audio_data_types/kaudiostreamanyrate/kaudiostreamanyrate)Added [AudioChannelBitmap](https://developer.apple.com/documentation/coreaudio/audiochannelbitmap)Added [AudioChannelCoordinateIndex](https://developer.apple.com/documentation/coreaudio/audiochannelcoordinateindex)Added [AudioChannelFlags](https://developer.apple.com/documentation/coreaudio/audiochannelflags)Added [AudioChannelLayoutTag_GetNumberOfChannels()](https://developer.apple.com/documentation/coreaudio/1422032-audiochannellayouttag_getnumbero)Added [AudioTimeStampFlags](https://developer.apple.com/documentation/coreaudio/audiotimestampflags)Added #def CoreAudio_CoreAudioTypes_hAdded [kAudioFormatEnhancedAC3](https://developer.apple.com/documentation/coreaudio/kaudioformatenhancedac3)Added [kAudioStreamAnyRate](https://developer.apple.com/documentation/coreaudio/kaudiostreamanyrate)Added [kAudioTimeStampNothingValid](https://developer.apple.com/documentation/coreaudio/audiotimestampflags/kaudiotimestampnothingvalid)Added [kSMPTETimeUnknown](https://developer.apple.com/documentation/coreaudio/smptetimeflags/ksmptetimeunknown)Added [MPEG4ObjectID](https://developer.apple.com/documentation/coreaudio/mpeg4objectid)Added [SMPTETimeFlags](https://developer.apple.com/documentation/coreaudio/smptetimeflags)Added [SMPTETimeType](https://developer.apple.com/documentation/coreaudio/smptetimetype)

#### HostTime.h

Added #def CoreAudio_HostTime_h

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
