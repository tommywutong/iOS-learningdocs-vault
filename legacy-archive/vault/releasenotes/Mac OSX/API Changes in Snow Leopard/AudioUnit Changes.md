---
title: API Changes in Snow Leopard
apple_id: TP40007673
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2008-06-09'
source_url: https://developer.apple.com/library/archive/releasenotes/MacOSX/SnowLeopard_API_ReleaseNote/AudioUnit.html
archived_at: '2026-07-18T02:58:42.162514Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [API Changes in Snow Leopard](API%20Changes%20in%20Snow%20Leopard.md)


[ADC Home](https://developer.apple.com/) >
[Reference Library](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30000943) >
Release Notes >
OS X >
[API Changes in Snow Leopard Developer Preview](API%20Changes%20in%20Snow%20Leopard.md) >

# AudioUnit Changes

## AudioUnit

AUComponent.hAdded [kAudioUnitSubType_RemoteIO](https://developer.apple.com/documentation/audiotoolbox/1619485-anonymous/kaudiounitsubtype_remoteio) (no architecture available)Modified [AudioUnitSetParameter()](https://developer.apple.com/documentation/audiotoolbox/1438454-audiounitsetparameter)

|  | Declaration |
| --- | --- |
| Old | ComponentResult AudioUnitSetParameter ( AudioUnit ci, AudioUnitParameterID inID, AudioUnitScope inScope, AudioUnitElement inElement, AudioUnitParameterValue inValue, UInt32 inBufferOffsetInFrames); |
| New | OSStatus AudioUnitSetParameter ( AudioUnit ci, AudioUnitParameterID inID, AudioUnitScope inScope, AudioUnitElement inElement, AudioUnitParameterValue inValue, UInt32 inBufferOffsetInFrames); |

Modified [AudioUnitAddPropertyListener()](https://developer.apple.com/documentation/audiotoolbox/1440111-audiounitaddpropertylistener)

|  | Declaration |
| --- | --- |
| Old | ComponentResult AudioUnitAddPropertyListener ( AudioUnit ci, AudioUnitPropertyID inID, AudioUnitPropertyListenerProc inProc, void \*inProcUserData); |
| New | OSStatus AudioUnitAddPropertyListener ( AudioUnit ci, AudioUnitPropertyID inID, AudioUnitPropertyListenerProc inProc, void \*inProcUserData); |

Modified [AudioUnitGetProperty()](https://developer.apple.com/documentation/audiotoolbox/1439840-audiounitgetproperty)

|  | Declaration |
| --- | --- |
| Old | ComponentResult AudioUnitGetProperty ( AudioUnit ci, AudioUnitPropertyID inID, AudioUnitScope inScope, AudioUnitElement inElement, void \*outData, UInt32 \*ioDataSize); |
| New | OSStatus AudioUnitGetProperty ( AudioUnit ci, AudioUnitPropertyID inID, AudioUnitScope inScope, AudioUnitElement inElement, void \*outData, UInt32 \*ioDataSize); |

Modified [AudioUnitSetProperty()](https://developer.apple.com/documentation/audiotoolbox/1440371-audiounitsetproperty)

|  | Declaration |
| --- | --- |
| Old | ComponentResult AudioUnitSetProperty ( AudioUnit ci, AudioUnitPropertyID inID, AudioUnitScope inScope, AudioUnitElement inElement, const void \*inData, UInt32 inDataSize); |
| New | OSStatus AudioUnitSetProperty ( AudioUnit ci, AudioUnitPropertyID inID, AudioUnitScope inScope, AudioUnitElement inElement, const void \*inData, UInt32 inDataSize); |

Modified [AudioUnitRemoveRenderNotify()](https://developer.apple.com/documentation/audiotoolbox/1440547-audiounitremoverendernotify)

|  | Declaration |
| --- | --- |
| Old | ComponentResult AudioUnitRemoveRenderNotify ( AudioUnit ci, AURenderCallback inProc, void \*inProcUserData); |
| New | OSStatus AudioUnitRemoveRenderNotify ( AudioUnit ci, AURenderCallback inProc, void \*inProcUserData); |

Modified [AudioUnitReset()](https://developer.apple.com/documentation/audiotoolbox/1439607-audiounitreset)

|  | Declaration |
| --- | --- |
| Old | ComponentResult AudioUnitReset ( AudioUnit ci, AudioUnitScope inScope, AudioUnitElement inElement); |
| New | OSStatus AudioUnitReset ( AudioUnit ci, AudioUnitScope inScope, AudioUnitElement inElement); |

Modified [AudioUnitScheduleParameters()](https://developer.apple.com/documentation/audiotoolbox/1439670-audiounitscheduleparameters)

|  | Declaration |
| --- | --- |
| Old | ComponentResult AudioUnitScheduleParameters ( AudioUnit ci, const AudioUnitParameterEvent \*inParameterEvent, UInt32 inNumParamEvents); |
| New | OSStatus AudioUnitScheduleParameters ( AudioUnit ci, const AudioUnitParameterEvent \*inParameterEvent, UInt32 inNumParamEvents); |

Modified [AudioUnitInitialize()](https://developer.apple.com/documentation/audiotoolbox/1439851-audiounitinitialize)

|  | Declaration |
| --- | --- |
| Old | ComponentResult AudioUnitInitialize ( AudioUnit ci); |
| New | OSStatus AudioUnitInitialize ( AudioUnit ci); |

Modified [AudioUnitUninitialize()](https://developer.apple.com/documentation/audiotoolbox/1438415-audiounituninitialize)

|  | Declaration |
| --- | --- |
| Old | ComponentResult AudioUnitUninitialize ( AudioUnit ci); |
| New | OSStatus AudioUnitUninitialize ( AudioUnit ci); |

Modified [AudioUnitGetParameter()](https://developer.apple.com/documentation/audiotoolbox/1440055-audiounitgetparameter)

|  | Declaration |
| --- | --- |
| Old | ComponentResult AudioUnitGetParameter ( AudioUnit ci, AudioUnitParameterID inID, AudioUnitScope inScope, AudioUnitElement inElement, AudioUnitParameterValue \*outValue); |
| New | OSStatus AudioUnitGetParameter ( AudioUnit ci, AudioUnitParameterID inID, AudioUnitScope inScope, AudioUnitElement inElement, AudioUnitParameterValue \*outValue); |

Modified [AudioUnitRender()](https://developer.apple.com/documentation/audiotoolbox/1438430-audiounitrender)

|  | Declaration |
| --- | --- |
| Old | ComponentResult AudioUnitRender ( AudioUnit ci, AudioUnitRenderActionFlags \*ioActionFlags, const AudioTimeStamp \*inTimeStamp, UInt32 inOutputBusNumber, UInt32 inNumberFrames, AudioBufferList \*ioData); |
| New | OSStatus AudioUnitRender ( AudioUnit ci, AudioUnitRenderActionFlags \*ioActionFlags, const AudioTimeStamp \*inTimeStamp, UInt32 inOutputBusNumber, UInt32 inNumberFrames, AudioBufferList \*ioData); |

Modified [AudioUnitAddRenderNotify()](https://developer.apple.com/documentation/audiotoolbox/1440259-audiounitaddrendernotify)

|  | Declaration |
| --- | --- |
| Old | ComponentResult AudioUnitAddRenderNotify ( AudioUnit ci, AURenderCallback inProc, void \*inProcUserData); |
| New | OSStatus AudioUnitAddRenderNotify ( AudioUnit ci, AURenderCallback inProc, void \*inProcUserData); |

Modified AudioUnitRemovePropertyListener()

|  | Deprecation | Declaration |
| --- | --- | --- |
| Old | 10.5 | ComponentResult AudioUnitRemovePropertyListener ( AudioUnit ci, AudioUnitPropertyID inID, AudioUnitPropertyListenerProc inProc); |
| New |  | OSStatus AudioUnitRemovePropertyListener ( AudioUnit ci, AudioUnitPropertyID inID, AudioUnitPropertyListenerProc inProc); |

Modified [AudioUnitGetPropertyInfo()](https://developer.apple.com/documentation/audiotoolbox/1440663-audiounitgetpropertyinfo)

|  | Declaration |
| --- | --- |
| Old | ComponentResult AudioUnitGetPropertyInfo ( AudioUnit ci, AudioUnitPropertyID inID, AudioUnitScope inScope, AudioUnitElement inElement, UInt32 \*outDataSize, Boolean \*outWritable); |
| New | OSStatus AudioUnitGetPropertyInfo ( AudioUnit ci, AudioUnitPropertyID inID, AudioUnitScope inScope, AudioUnitElement inElement, UInt32 \*outDataSize, Boolean \*outWritable); |

Modified [AudioUnitRemovePropertyListenerWithUserData()](https://developer.apple.com/documentation/audiotoolbox/1441010-audiounitremovepropertylistenerw)

|  | Declaration |
| --- | --- |
| Old | ComponentResult AudioUnitRemovePropertyListenerWithUserData ( AudioUnit ci, AudioUnitPropertyID inID, AudioUnitPropertyListenerProc inProc, void \*inProcUserData); |
| New | OSStatus AudioUnitRemovePropertyListenerWithUserData ( AudioUnit ci, AudioUnitPropertyID inID, AudioUnitPropertyListenerProc inProc, void \*inProcUserData); |

AUNTComponent.hModified AudioUnitRemoveRenderNotification()

|  | Deprecation | Declaration |
| --- | --- | --- |
| Old | 10.3 | ComponentResult AudioUnitRemoveRenderNotification ( AudioUnit ci, AudioUnitRenderCallback inProc, void \*inProcRefCon); |
| New |  | OSStatus AudioUnitRemoveRenderNotification ( AudioUnit ci, AudioUnitRenderCallback inProc, void \*inProcRefCon); |

Modified AudioUnitSetRenderNotification()

|  | Deprecation | Declaration |
| --- | --- | --- |
| Old | 10.3 | ComponentResult AudioUnitSetRenderNotification ( AudioUnit ci, AudioUnitRenderCallback inProc, void \*inProcRefCon); |
| New |  | OSStatus AudioUnitSetRenderNotification ( AudioUnit ci, AudioUnitRenderCallback inProc, void \*inProcRefCon); |

Modified AudioUnitRenderSlice()

|  | Deprecation | Declaration |
| --- | --- | --- |
| Old | 10.3 | ComponentResult AudioUnitRenderSlice ( AudioUnit ci, AudioUnitRenderActionFlags inActionFlags, const AudioTimeStamp \*inTimeStamp, UInt32 inOutputBusNumber, AudioBuffer \*ioData); |
| New |  | OSStatus AudioUnitRenderSlice ( AudioUnit ci, AudioUnitRenderActionFlags inActionFlags, const AudioTimeStamp \*inTimeStamp, UInt32 inOutputBusNumber, AudioBuffer \*ioData); |

AudioCodec.hModified [AudioCodecInitialize()](https://developer.apple.com/documentation/audiotoolbox/1440177-audiocodecinitialize)

|  | Declaration |
| --- | --- |
| Old | ComponentResult AudioCodecInitialize ( AudioCodec inCodec, const AudioStreamBasicDescription \*inInputFormat, const AudioStreamBasicDescription \*inOutputFormat, const void \*inMagicCookie, UInt32 inMagicCookieByteSize); |
| New | OSStatus AudioCodecInitialize ( AudioCodec inCodec, const AudioStreamBasicDescription \*inInputFormat, const AudioStreamBasicDescription \*inOutputFormat, const void \*inMagicCookie, UInt32 inMagicCookieByteSize); |

Modified [AudioCodecGetPropertyInfo()](https://developer.apple.com/documentation/audiotoolbox/1439602-audiocodecgetpropertyinfo)

|  | Declaration |
| --- | --- |
| Old | ComponentResult AudioCodecGetPropertyInfo ( AudioCodec inCodec, AudioCodecPropertyID inPropertyID, UInt32 \*outSize, Boolean \*outWritable); |
| New | OSStatus AudioCodecGetPropertyInfo ( AudioCodec inCodec, AudioCodecPropertyID inPropertyID, UInt32 \*outSize, Boolean \*outWritable); |

Modified [AudioCodecReset()](https://developer.apple.com/documentation/audiotoolbox/1439087-audiocodecreset)

|  | Declaration |
| --- | --- |
| Old | ComponentResult AudioCodecReset ( AudioCodec inCodec); |
| New | OSStatus AudioCodecReset ( AudioCodec inCodec); |

Modified [AudioCodecProduceOutputPackets()](https://developer.apple.com/documentation/audiotoolbox/1440558-audiocodecproduceoutputpackets)

|  | Declaration |
| --- | --- |
| Old | ComponentResult AudioCodecProduceOutputPackets ( AudioCodec inCodec, void \*outOutputData, UInt32 \*ioOutputDataByteSize, UInt32 \*ioNumberPackets, AudioStreamPacketDescription \*outPacketDescription, UInt32 \*outStatus); |
| New | OSStatus AudioCodecProduceOutputPackets ( AudioCodec inCodec, void \*outOutputData, UInt32 \*ioOutputDataByteSize, UInt32 \*ioNumberPackets, AudioStreamPacketDescription \*outPacketDescription, UInt32 \*outStatus); |

Modified [AudioCodecSetProperty()](https://developer.apple.com/documentation/audiotoolbox/1439355-audiocodecsetproperty)

|  | Declaration |
| --- | --- |
| Old | ComponentResult AudioCodecSetProperty ( AudioCodec inCodec, AudioCodecPropertyID inPropertyID, UInt32 inPropertyDataSize, const void \*inPropertyData); |
| New | OSStatus AudioCodecSetProperty ( AudioCodec inCodec, AudioCodecPropertyID inPropertyID, UInt32 inPropertyDataSize, const void \*inPropertyData); |

Modified [AudioCodecAppendInputData()](https://developer.apple.com/documentation/audiotoolbox/1438536-audiocodecappendinputdata)

|  | Declaration |
| --- | --- |
| Old | ComponentResult AudioCodecAppendInputData ( AudioCodec inCodec, const void \*inInputData, UInt32 \*ioInputDataByteSize, UInt32 \*ioNumberPackets, const AudioStreamPacketDescription \*inPacketDescription); |
| New | OSStatus AudioCodecAppendInputData ( AudioCodec inCodec, const void \*inInputData, UInt32 \*ioInputDataByteSize, UInt32 \*ioNumberPackets, const AudioStreamPacketDescription \*inPacketDescription); |

Modified [AudioCodecUninitialize()](https://developer.apple.com/documentation/audiotoolbox/1439079-audiocodecuninitialize)

|  | Declaration |
| --- | --- |
| Old | ComponentResult AudioCodecUninitialize ( AudioCodec inCodec); |
| New | OSStatus AudioCodecUninitialize ( AudioCodec inCodec); |

Modified [AudioCodecGetProperty()](https://developer.apple.com/documentation/audiotoolbox/1439429-audiocodecgetproperty)

|  | Declaration |
| --- | --- |
| Old | ComponentResult AudioCodecGetProperty ( AudioCodec inCodec, AudioCodecPropertyID inPropertyID, UInt32 \*ioPropertyDataSize, void \*outPropertyData); |
| New | OSStatus AudioCodecGetProperty ( AudioCodec inCodec, AudioCodecPropertyID inPropertyID, UInt32 \*ioPropertyDataSize, void \*outPropertyData); |

AudioComponent.hAdded [AudioComponent](https://developer.apple.com/documentation/audiotoolbox/audiocomponent)Added [AudioComponentCopyName()](https://developer.apple.com/documentation/audiotoolbox/1410519-audiocomponentcopyname)Added [AudioComponentCount()](https://developer.apple.com/documentation/audiotoolbox/1410476-audiocomponentcount)Added [AudioComponentDescription](https://developer.apple.com/documentation/audiotoolbox/audiocomponentdescription)Added [AudioComponentFindNext()](https://developer.apple.com/documentation/audiotoolbox/1410445-audiocomponentfindnext)Added [AudioComponentGetDescription()](https://developer.apple.com/documentation/audiotoolbox/1410523-audiocomponentgetdescription)Added [AudioComponentGetVersion()](https://developer.apple.com/documentation/audiotoolbox/1410441-audiocomponentgetversion)Added [AudioComponentInstance](https://developer.apple.com/documentation/audiotoolbox/audiocomponentinstance)Added [AudioComponentInstanceDispose()](https://developer.apple.com/documentation/audiotoolbox/1410508-audiocomponentinstancedispose)Added [AudioComponentInstanceGetComponent()](https://developer.apple.com/documentation/audiotoolbox/1410447-audiocomponentinstancegetcompone)Added [AudioComponentInstanceNew()](https://developer.apple.com/documentation/audiotoolbox/1410465-audiocomponentinstancenew)AudioOutputUnit.hModified [AudioOutputUnitStop()](https://developer.apple.com/documentation/audiotoolbox/1440513-audiooutputunitstop)

|  | Declaration |
| --- | --- |
| Old | ComponentResult AudioOutputUnitStop ( AudioUnit ci); |
| New | OSStatus AudioOutputUnitStop ( AudioUnit ci); |

Modified [AudioOutputUnitStart()](https://developer.apple.com/documentation/audiotoolbox/1439763-audiooutputunitstart)

|  | Declaration |
| --- | --- |
| Old | ComponentResult AudioOutputUnitStart ( AudioUnit ci); |
| New | OSStatus AudioOutputUnitStart ( AudioUnit ci); |

AudioUnit.hAdded [#def AUDIO_UNIT_VERSION](https://developer.apple.com/documentation/audiotoolbox/audio_unit_version)AudioUnitCarbonView.hModified AudioUnitCarbonViewSetEventListener()

|  | Deprecation | Declaration |
| --- | --- | --- |
| Old | 10.4 | ComponentResult AudioUnitCarbonViewSetEventListener ( AudioUnitCarbonView inView, AudioUnitCarbonViewEventListener inCallback, void \*inUserData); |
| New |  | OSStatus AudioUnitCarbonViewSetEventListener ( AudioUnitCarbonView inView, AudioUnitCarbonViewEventListener inCallback, void \*inUserData); |

Modified AudioUnitCarbonViewCreate()

|  | Declaration |
| --- | --- |
| Old | ComponentResult AudioUnitCarbonViewCreate ( AudioUnitCarbonView inView, AudioUnit inAudioUnit, WindowRef inWindow, ControlRef inParentControl, const Float32Point \*inLocation, const Float32Point \*inSize, ControlRef \*outControl); |
| New | OSStatus AudioUnitCarbonViewCreate ( AudioUnitCarbonView inView, AudioUnit inAudioUnit, WindowRef inWindow, ControlRef inParentControl, const Float32Point \*inLocation, const Float32Point \*inSize, ControlRef \*outControl); |

AudioUnitProperties.hAdded [kAudioUnitProperty_ShouldAllocateBuffer](https://developer.apple.com/documentation/audiotoolbox/1534199-generic_audio_unit_properties/kaudiounitproperty_shouldallocatebuffer)MusicDevice.hModified [MusicDeviceReleaseInstrument()](https://developer.apple.com/documentation/audiotoolbox/1473475-musicdevicereleaseinstrument)

|  | Deprecation | Declaration |
| --- | --- | --- |
| Old | 10.5 | ComponentResult MusicDeviceReleaseInstrument ( MusicDeviceComponent ci, MusicDeviceInstrumentID inInstrument); |
| New |  | OSStatus MusicDeviceReleaseInstrument ( MusicDeviceComponent ci, MusicDeviceInstrumentID inInstrument); |

Modified [MusicDevicePrepareInstrument()](https://developer.apple.com/documentation/audiotoolbox/1473487-musicdeviceprepareinstrument)

|  | Deprecation | Declaration |
| --- | --- | --- |
| Old | 10.5 | ComponentResult MusicDevicePrepareInstrument ( MusicDeviceComponent ci, MusicDeviceInstrumentID inInstrument); |
| New |  | OSStatus MusicDevicePrepareInstrument ( MusicDeviceComponent ci, MusicDeviceInstrumentID inInstrument); |

Modified [MusicDeviceMIDIEvent()](https://developer.apple.com/documentation/audiotoolbox/1439861-musicdevicemidievent)

|  | Declaration |
| --- | --- |
| Old | ComponentResult MusicDeviceMIDIEvent ( MusicDeviceComponent ci, UInt32 inStatus, UInt32 inData1, UInt32 inData2, UInt32 inOffsetSampleFrame); |
| New | OSStatus MusicDeviceMIDIEvent ( MusicDeviceComponent ci, UInt32 inStatus, UInt32 inData1, UInt32 inData2, UInt32 inOffsetSampleFrame); |

Modified [MusicDeviceStartNote()](https://developer.apple.com/documentation/audiotoolbox/1440960-musicdevicestartnote)

|  | Declaration |
| --- | --- |
| Old | ComponentResult MusicDeviceStartNote ( MusicDeviceComponent ci, MusicDeviceInstrumentID inInstrument, MusicDeviceGroupID inGroupID, NoteInstanceID \*outNoteInstanceID, UInt32 inOffsetSampleFrame, const MusicDeviceNoteParams \*inParams); |
| New | OSStatus MusicDeviceStartNote ( MusicDeviceComponent ci, MusicDeviceInstrumentID inInstrument, MusicDeviceGroupID inGroupID, NoteInstanceID \*outNoteInstanceID, UInt32 inOffsetSampleFrame, const MusicDeviceNoteParams \*inParams); |

Modified [MusicDeviceStopNote()](https://developer.apple.com/documentation/audiotoolbox/1440390-musicdevicestopnote)

|  | Declaration |
| --- | --- |
| Old | ComponentResult MusicDeviceStopNote ( MusicDeviceComponent ci, MusicDeviceGroupID inGroupID, NoteInstanceID inNoteInstanceID, UInt32 inOffsetSampleFrame); |
| New | OSStatus MusicDeviceStopNote ( MusicDeviceComponent ci, MusicDeviceGroupID inGroupID, NoteInstanceID inNoteInstanceID, UInt32 inOffsetSampleFrame); |

Modified [MusicDeviceSysEx()](https://developer.apple.com/documentation/audiotoolbox/1438996-musicdevicesysex)

|  | Declaration |
| --- | --- |
| Old | ComponentResult MusicDeviceSysEx ( MusicDeviceComponent ci, const UInt8 \*inData, UInt32 inLength); |
| New | OSStatus MusicDeviceSysEx ( MusicDeviceComponent ci, const UInt8 \*inData, UInt32 inLength); |

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
