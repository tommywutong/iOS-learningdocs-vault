---
title: iOS 9.0 API Diffs
apple_id: TP40016222
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS90APIDiffs/Swift/OpenAL.html
archived_at: '2026-07-18T02:56:56.497724Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 9.0 API Diffs](iOS%208.3%20to%20iOS%209.0%20API%20Differences.md)


# OpenAL Changes for Swift

### OpenAL

Added AL_BITSAdded AL_BUFFERAdded AL_BUFFERS_PROCESSEDAdded AL_BUFFERS_QUEUEDAdded AL_BYTE_OFFSETAdded AL_CHANNELSAdded AL_CONE_INNER_ANGLEAdded AL_CONE_OUTER_ANGLEAdded AL_CONE_OUTER_GAINAdded AL_DIRECTIONAdded AL_DISTANCE_MODELAdded AL_DOPPLER_FACTORAdded AL_DOPPLER_VELOCITYAdded AL_EXPONENT_DISTANCEAdded AL_EXPONENT_DISTANCE_CLAMPEDAdded AL_EXTENSIONSAdded AL_FALSEAdded AL_FORMAT_MONO16Added AL_FORMAT_MONO8Added AL_FORMAT_STEREO16Added AL_FORMAT_STEREO8Added AL_FREQUENCYAdded AL_GAINAdded AL_ILLEGAL_COMMANDAdded AL_ILLEGAL_ENUMAdded AL_INITIALAdded AL_INVALIDAdded AL_INVALID_ENUMAdded AL_INVALID_NAMEAdded AL_INVALID_OPERATIONAdded AL_INVALID_VALUEAdded AL_INVERSE_DISTANCEAdded AL_INVERSE_DISTANCE_CLAMPEDAdded AL_LINEAR_DISTANCEAdded AL_LINEAR_DISTANCE_CLAMPEDAdded AL_LOOPINGAdded AL_MAX_DISTANCEAdded AL_MAX_GAINAdded AL_MIN_GAINAdded AL_NO_ERRORAdded AL_NONEAdded AL_ORIENTATIONAdded AL_OUT_OF_MEMORYAdded AL_PAUSEDAdded AL_PENDINGAdded AL_PITCHAdded AL_PLAYINGAdded AL_POSITIONAdded AL_PROCESSEDAdded AL_QUEUE_HAS_LOOPEDAdded AL_REFERENCE_DISTANCEAdded AL_RENDERERAdded AL_ROLLOFF_FACTORAdded AL_SAMPLE_OFFSETAdded AL_SEC_OFFSETAdded AL_SIZEAdded AL_SOURCE_RELATIVEAdded AL_SOURCE_STATEAdded AL_SOURCE_TYPEAdded AL_SPEED_OF_SOUNDAdded AL_STATICAdded AL_STOPPEDAdded AL_STREAMINGAdded AL_TRUEAdded AL_UNDETERMINEDAdded AL_UNUSEDAdded AL_VELOCITYAdded AL_VENDORAdded AL_VERSIONAdded ALbooleanAdded alBuffer3f(_: ALuint, _: ALenum, _: ALfloat, _: ALfloat, _: ALfloat)Added alBuffer3i(_: ALuint, _: ALenum, _: ALint, _: ALint, _: ALint)Added alBufferData(_: ALuint, _: ALenum, _: UnsafePointer<Void>, _: ALsizei, _: ALsizei)Added alBufferDataStaticProcPtrAdded alBufferf(_: ALuint, _: ALenum, _: ALfloat)Added alBufferfv(_: ALuint, _: ALenum, _: UnsafePointer<ALfloat>)Added alBufferi(_: ALuint, _: ALenum, _: ALint)Added alBufferiv(_: ALuint, _: ALenum, _: UnsafePointer<ALint>)Added ALbyteAdded ALC_ALL_ATTRIBUTESAdded ALC_ALL_DEVICES_SPECIFIERAdded ALC_ASA_REVERB_ROOM_TYPE_CathedralAdded ALC_ASA_REVERB_ROOM_TYPE_LargeChamberAdded ALC_ASA_REVERB_ROOM_TYPE_LargeHallAdded ALC_ASA_REVERB_ROOM_TYPE_LargeHall2Added ALC_ASA_REVERB_ROOM_TYPE_LargeRoomAdded ALC_ASA_REVERB_ROOM_TYPE_LargeRoom2Added ALC_ASA_REVERB_ROOM_TYPE_MediumChamberAdded ALC_ASA_REVERB_ROOM_TYPE_MediumHallAdded ALC_ASA_REVERB_ROOM_TYPE_MediumHall2Added ALC_ASA_REVERB_ROOM_TYPE_MediumHall3Added ALC_ASA_REVERB_ROOM_TYPE_MediumRoomAdded ALC_ASA_REVERB_ROOM_TYPE_PlateAdded ALC_ASA_REVERB_ROOM_TYPE_SmallRoomAdded ALC_ATTRIBUTES_SIZEAdded ALC_CAPTURE_DEFAULT_DEVICE_SPECIFIERAdded ALC_CAPTURE_DEVICE_SPECIFIERAdded ALC_CAPTURE_SAMPLESAdded ALC_DEFAULT_ALL_DEVICES_SPECIFIERAdded ALC_DEFAULT_DEVICE_SPECIFIERAdded ALC_DEVICE_SPECIFIERAdded ALC_EXTENSIONSAdded ALC_FALSEAdded ALC_FREQUENCYAdded ALC_INVALIDAdded ALC_INVALID_CONTEXTAdded ALC_INVALID_DEVICEAdded ALC_INVALID_ENUMAdded ALC_INVALID_VALUEAdded ALC_MAJOR_VERSIONAdded ALC_MINOR_VERSIONAdded ALC_MONO_SOURCESAdded ALC_NO_ERRORAdded ALC_OUT_OF_MEMORYAdded ALC_REFRESHAdded ALC_STEREO_SOURCESAdded ALC_SYNCAdded ALC_TRUEAdded ALC_VERSION_0_1Added alcASAGetListenerProcPtrAdded alcASAGetSourceProcPtrAdded alcASASetListenerProcPtrAdded alcASASetSourceProcPtrAdded ALCbooleanAdded ALCbyteAdded alcCaptureCloseDevice(_: COpaquePointer) -> ALCbooleanAdded alcCaptureOpenDevice(_: UnsafePointer<ALCchar>, _: ALCuint, _: ALCenum, _: ALCsizei) -> COpaquePointerAdded alcCaptureSamples(_: COpaquePointer, _: UnsafeMutablePointer<Void>, _: ALCsizei)Added alcCaptureStart(_: COpaquePointer)Added alcCaptureStop(_: COpaquePointer)Added ALCcharAdded alcCloseDevice(_: COpaquePointer) -> ALCbooleanAdded alcCreateContext(_: COpaquePointer, _: UnsafePointer<ALCint>) -> COpaquePointerAdded alcDestroyContext(_: COpaquePointer)Added ALCdoubleAdded ALCenumAdded ALCfloatAdded alcGetContextsDevice(_: COpaquePointer) -> COpaquePointerAdded alcGetCurrentContext() -> COpaquePointerAdded alcGetEnumValue(_: COpaquePointer, _: UnsafePointer<ALCchar>) -> ALCenumAdded alcGetError(_: COpaquePointer) -> ALCenumAdded alcGetIntegerv(_: COpaquePointer, _: ALCenum, _: ALCsizei, _: UnsafeMutablePointer<ALCint>)Added alcGetProcAddress(_: COpaquePointer, _: UnsafePointer<ALCchar>) -> UnsafeMutablePointer<Void>Added alcGetString(_: COpaquePointer, _: ALCenum) -> UnsafePointer<ALCchar>Added ALcharAdded ALCintAdded alcIsExtensionPresent(_: COpaquePointer, _: UnsafePointer<ALCchar>) -> ALCbooleanAdded alcMacOSXGetMixerMaxiumumBussesProcPtrAdded alcMacOSXGetMixerOutputRateProcPtrAdded alcMacOSXGetRenderingQualityProcPtrAdded alcMacOSXMixerMaxiumumBussesProcPtrAdded alcMacOSXMixerOutputRateProcPtrAdded alcMacOSXRenderingQualityProcPtrAdded alcMakeContextCurrent(_: COpaquePointer) -> ALCbooleanAdded alcOpenDevice(_: UnsafePointer<ALCchar>) -> COpaquePointerAdded alcOutputCapturerAvailableSamplesProcPtrAdded alcOutputCapturerPrepareProcPtrAdded alcOutputCapturerSamplesProcPtrAdded alcOutputCapturerStartProcPtrAdded alcOutputCapturerStopProcPtrAdded alcProcessContext(_: COpaquePointer)Added ALCshortAdded ALCsizeiAdded alcSuspendContext(_: COpaquePointer)Added ALCubyteAdded ALCuintAdded ALCushortAdded alDeleteBuffers(_: ALsizei, _: UnsafePointer<ALuint>)Added alDeleteSources(_: ALsizei, _: UnsafePointer<ALuint>)Added alDisable(_: ALenum)Added alDistanceModel(_: ALenum)Added alDopplerFactor(_: ALfloat)Added alDopplerVelocity(_: ALfloat)Added ALdoubleAdded alEnable(_: ALenum)Added ALenumAdded ALfloatAdded alGenBuffers(_: ALsizei, _: UnsafeMutablePointer<ALuint>)Added alGenSources(_: ALsizei, _: UnsafeMutablePointer<ALuint>)Added alGetBoolean(_: ALenum) -> ALbooleanAdded alGetBooleanv(_: ALenum, _: UnsafeMutablePointer<ALboolean>)Added alGetBuffer3f(_: ALuint, _: ALenum, _: UnsafeMutablePointer<ALfloat>, _: UnsafeMutablePointer<ALfloat>, _: UnsafeMutablePointer<ALfloat>)Added alGetBuffer3i(_: ALuint, _: ALenum, _: UnsafeMutablePointer<ALint>, _: UnsafeMutablePointer<ALint>, _: UnsafeMutablePointer<ALint>)Added alGetBufferf(_: ALuint, _: ALenum, _: UnsafeMutablePointer<ALfloat>)Added alGetBufferfv(_: ALuint, _: ALenum, _: UnsafeMutablePointer<ALfloat>)Added alGetBufferi(_: ALuint, _: ALenum, _: UnsafeMutablePointer<ALint>)Added alGetBufferiv(_: ALuint, _: ALenum, _: UnsafeMutablePointer<ALint>)Added alGetDouble(_: ALenum) -> ALdoubleAdded alGetDoublev(_: ALenum, _: UnsafeMutablePointer<ALdouble>)Added alGetEnumValue(_: UnsafePointer<ALchar>) -> ALenumAdded alGetError() -> ALenumAdded alGetFloat(_: ALenum) -> ALfloatAdded alGetFloatv(_: ALenum, _: UnsafeMutablePointer<ALfloat>)Added alGetInteger(_: ALenum) -> ALintAdded alGetIntegerv(_: ALenum, _: UnsafeMutablePointer<ALint>)Added alGetListener3f(_: ALenum, _: UnsafeMutablePointer<ALfloat>, _: UnsafeMutablePointer<ALfloat>, _: UnsafeMutablePointer<ALfloat>)Added alGetListener3i(_: ALenum, _: UnsafeMutablePointer<ALint>, _: UnsafeMutablePointer<ALint>, _: UnsafeMutablePointer<ALint>)Added alGetListenerf(_: ALenum, _: UnsafeMutablePointer<ALfloat>)Added alGetListenerfv(_: ALenum, _: UnsafeMutablePointer<ALfloat>)Added alGetListeneri(_: ALenum, _: UnsafeMutablePointer<ALint>)Added alGetListeneriv(_: ALenum, _: UnsafeMutablePointer<ALint>)Added alGetProcAddress(_: UnsafePointer<ALchar>) -> UnsafeMutablePointer<Void>Added alGetSource3f(_: ALuint, _: ALenum, _: UnsafeMutablePointer<ALfloat>, _: UnsafeMutablePointer<ALfloat>, _: UnsafeMutablePointer<ALfloat>)Added alGetSource3i(_: ALuint, _: ALenum, _: UnsafeMutablePointer<ALint>, _: UnsafeMutablePointer<ALint>, _: UnsafeMutablePointer<ALint>)Added alGetSourcef(_: ALuint, _: ALenum, _: UnsafeMutablePointer<ALfloat>)Added alGetSourcefv(_: ALuint, _: ALenum, _: UnsafeMutablePointer<ALfloat>)Added alGetSourcei(_: ALuint, _: ALenum, _: UnsafeMutablePointer<ALint>)Added alGetSourceiv(_: ALuint, _: ALenum, _: UnsafeMutablePointer<ALint>)Added alGetString(_: ALenum) -> UnsafePointer<ALchar>Added ALintAdded alIsBuffer(_: ALuint) -> ALbooleanAdded alIsEnabled(_: ALenum) -> ALbooleanAdded alIsExtensionPresent(_: UnsafePointer<ALchar>) -> ALbooleanAdded alIsSource(_: ALuint) -> ALbooleanAdded alListener3f(_: ALenum, _: ALfloat, _: ALfloat, _: ALfloat)Added alListener3i(_: ALenum, _: ALint, _: ALint, _: ALint)Added alListenerf(_: ALenum, _: ALfloat)Added alListenerfv(_: ALenum, _: UnsafePointer<ALfloat>)Added alListeneri(_: ALenum, _: ALint)Added alListeneriv(_: ALenum, _: UnsafePointer<ALint>)Added alMacOSXGetRenderChannelCountProcPtrAdded alMacOSXRenderChannelCountProcPtrAdded ALshortAdded ALsizeiAdded alSource3f(_: ALuint, _: ALenum, _: ALfloat, _: ALfloat, _: ALfloat)Added alSource3i(_: ALuint, _: ALenum, _: ALint, _: ALint, _: ALint)Added alSourceAddNotificationProcPtrAdded alSourcef(_: ALuint, _: ALenum, _: ALfloat)Added alSourcefv(_: ALuint, _: ALenum, _: UnsafePointer<ALfloat>)Added alSourceGetRenderingQualityProcPtrAdded alSourcei(_: ALuint, _: ALenum, _: ALint)Added alSourceiv(_: ALuint, _: ALenum, _: UnsafePointer<ALint>)Added alSourceNotificationProcAdded alSourcePause(_: ALuint)Added alSourcePausev(_: ALsizei, _: UnsafePointer<ALuint>)Added alSourcePlay(_: ALuint)Added alSourcePlayv(_: ALsizei, _: UnsafePointer<ALuint>)Added alSourceQueueBuffers(_: ALuint, _: ALsizei, _: UnsafePointer<ALuint>)Added alSourceRemoveNotificationProcPtrAdded alSourceRenderingQualityProcPtrAdded alSourceRewind(_: ALuint)Added alSourceRewindv(_: ALsizei, _: UnsafePointer<ALuint>)Added alSourceStop(_: ALuint)Added alSourceStopv(_: ALsizei, _: UnsafePointer<ALuint>)Added alSourceUnqueueBuffers(_: ALuint, _: ALsizei, _: UnsafeMutablePointer<ALuint>)Added alSpeedOfSound(_: ALfloat)Added ALubyteAdded ALuintAdded ALushortAdded LPALBUFFER3FAdded LPALBUFFER3IAdded LPALBUFFERDATAAdded LPALBUFFERFAdded LPALBUFFERFVAdded LPALBUFFERIAdded LPALBUFFERIVAdded LPALCCAPTURECLOSEDEVICEAdded LPALCCAPTUREOPENDEVICEAdded LPALCCAPTURESAMPLESAdded LPALCCAPTURESTARTAdded LPALCCAPTURESTOPAdded LPALCCLOSEDEVICEAdded LPALCCREATECONTEXTAdded LPALCDESTROYCONTEXTAdded LPALCGETCONTEXTSDEVICEAdded LPALCGETCURRENTCONTEXTAdded LPALCGETENUMVALUEAdded LPALCGETERRORAdded LPALCGETINTEGERVAdded LPALCGETPROCADDRESSAdded LPALCGETSTRINGAdded LPALCISEXTENSIONPRESENTAdded LPALCMAKECONTEXTCURRENTAdded LPALCOPENDEVICEAdded LPALCPROCESSCONTEXTAdded LPALCSUSPENDCONTEXTAdded LPALDELETEBUFFERSAdded LPALDELETESOURCESAdded LPALDISABLEAdded LPALDISTANCEMODELAdded LPALDOPPLERFACTORAdded LPALDOPPLERVELOCITYAdded LPALENABLEAdded LPALGENBUFFERSAdded LPALGENSOURCESAdded LPALGETBOOLEANAdded LPALGETBOOLEANVAdded LPALGETBUFFER3FAdded LPALGETBUFFER3IAdded LPALGETBUFFERFAdded LPALGETBUFFERFVAdded LPALGETBUFFERIAdded LPALGETBUFFERIVAdded LPALGETDOUBLEAdded LPALGETDOUBLEVAdded LPALGETENUMVALUEAdded LPALGETERRORAdded LPALGETFLOATAdded LPALGETFLOATVAdded LPALGETINTEGERAdded LPALGETINTEGERVAdded LPALGETLISTENER3FAdded LPALGETLISTENER3IAdded LPALGETLISTENERFAdded LPALGETLISTENERFVAdded LPALGETLISTENERIAdded LPALGETLISTENERIVAdded LPALGETPROCADDRESSAdded LPALGETSOURCE3FAdded LPALGETSOURCE3IAdded LPALGETSOURCEFAdded LPALGETSOURCEFVAdded LPALGETSOURCEIAdded LPALGETSOURCEIVAdded LPALGETSTRINGAdded LPALISBUFFERAdded LPALISENABLEDAdded LPALISEXTENSIONPRESENTAdded LPALISSOURCEAdded LPALLISTENER3FAdded LPALLISTENER3IAdded LPALLISTENERFAdded LPALLISTENERFVAdded LPALLISTENERIAdded LPALLISTENERIVAdded LPALSOURCE3FAdded LPALSOURCE3IAdded LPALSOURCEFAdded LPALSOURCEFVAdded LPALSOURCEIAdded LPALSOURCEIVAdded LPALSOURCEPAUSEAdded LPALSOURCEPAUSEVAdded LPALSOURCEPLAYAdded LPALSOURCEPLAYVAdded LPALSOURCEQUEUEBUFFERSAdded LPALSOURCEREWINDAdded LPALSOURCEREWINDVAdded LPALSOURCESTOPAdded LPALSOURCESTOPVAdded LPALSOURCEUNQUEUEBUFFERSAdded LPALSPEEDOFSOUND

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
