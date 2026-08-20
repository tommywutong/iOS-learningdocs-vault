---
title: iOS 10.0 API Diffs
apple_id: TP40017327
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS10APIDiffs/Swift/OpenAL.html
archived_at: '2026-07-18T02:55:35.085927Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 10.0 API Diffs](iOS%209.3%20to%20iOS%2010.0%20API%20Differences.md)


# OpenAL Changes for Swift

### OpenAL

Modified alBufferData(_: ALuint, _: ALenum, _: UnsafeRawPointer!, _: ALsizei, _: ALsizei)

|  | Declaration |
| --- | --- |
| From | ``` func alBufferData(_ bid: ALuint, _ format: ALenum, _ data: UnsafePointer<Void>, _ size: ALsizei, _ freq: ALsizei) ``` |
| To | ``` func alBufferData(_ bid: ALuint, _ format: ALenum, _ data: UnsafeRawPointer!, _ size: ALsizei, _ freq: ALsizei) ``` |

Modified alBufferDataStaticProcPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias alBufferDataStaticProcPtr = (ALint, ALenum, UnsafePointer<Void>, ALsizei, ALsizei) -> Void ``` |
| To | ``` typealias alBufferDataStaticProcPtr = (ALint, ALenum, UnsafeRawPointer, ALsizei, ALsizei) -> Swift.Void ``` |

Modified alBufferfv(_: ALuint, _: ALenum, _: UnsafePointer<ALfloat>!)

|  | Declaration |
| --- | --- |
| From | ``` func alBufferfv(_ bid: ALuint, _ param: ALenum, _ values: UnsafePointer<ALfloat>) ``` |
| To | ``` func alBufferfv(_ bid: ALuint, _ param: ALenum, _ values: UnsafePointer<ALfloat>!) ``` |

Modified alBufferiv(_: ALuint, _: ALenum, _: UnsafePointer<ALint>!)

|  | Declaration |
| --- | --- |
| From | ``` func alBufferiv(_ bid: ALuint, _ param: ALenum, _ values: UnsafePointer<ALint>) ``` |
| To | ``` func alBufferiv(_ bid: ALuint, _ param: ALenum, _ values: UnsafePointer<ALint>!) ``` |

Modified alcASAGetListenerProcPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias alcASAGetListenerProcPtr = (ALuint, UnsafeMutablePointer<Void>, UnsafeMutablePointer<ALuint>) -> ALenum ``` |
| To | ``` typealias alcASAGetListenerProcPtr = (ALuint, UnsafeMutableRawPointer, UnsafeMutablePointer<ALuint>) -> ALenum ``` |

Modified alcASAGetSourceProcPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias alcASAGetSourceProcPtr = (ALuint, ALuint, UnsafeMutablePointer<Void>, UnsafeMutablePointer<ALuint>) -> ALenum ``` |
| To | ``` typealias alcASAGetSourceProcPtr = (ALuint, ALuint, UnsafeMutableRawPointer, UnsafeMutablePointer<ALuint>) -> ALenum ``` |

Modified alcASASetListenerProcPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias alcASASetListenerProcPtr = (ALuint, UnsafeMutablePointer<Void>, ALuint) -> ALenum ``` |
| To | ``` typealias alcASASetListenerProcPtr = (ALuint, UnsafeMutableRawPointer, ALuint) -> ALenum ``` |

Modified alcASASetSourceProcPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias alcASASetSourceProcPtr = (ALuint, ALuint, UnsafeMutablePointer<Void>, ALuint) -> ALenum ``` |
| To | ``` typealias alcASASetSourceProcPtr = (ALuint, ALuint, UnsafeMutableRawPointer, ALuint) -> ALenum ``` |

Modified alcCaptureCloseDevice(_: OpaquePointer!) -> ALCboolean

|  | Declaration |
| --- | --- |
| From | ``` func alcCaptureCloseDevice(_ device: COpaquePointer) -> ALCboolean ``` |
| To | ``` func alcCaptureCloseDevice(_ device: OpaquePointer!) -> ALCboolean ``` |

Modified alcCaptureOpenDevice(_: UnsafePointer<ALCchar>!, _: ALCuint, _: ALCenum, _: ALCsizei) -> OpaquePointer!

|  | Declaration |
| --- | --- |
| From | ``` func alcCaptureOpenDevice(_ devicename: UnsafePointer<ALCchar>, _ frequency: ALCuint, _ format: ALCenum, _ buffersize: ALCsizei) -> COpaquePointer ``` |
| To | ``` func alcCaptureOpenDevice(_ devicename: UnsafePointer<ALCchar>!, _ frequency: ALCuint, _ format: ALCenum, _ buffersize: ALCsizei) -> OpaquePointer! ``` |

Modified alcCaptureSamples(_: OpaquePointer!, _: UnsafeMutableRawPointer!, _: ALCsizei)

|  | Declaration |
| --- | --- |
| From | ``` func alcCaptureSamples(_ device: COpaquePointer, _ buffer: UnsafeMutablePointer<Void>, _ samples: ALCsizei) ``` |
| To | ``` func alcCaptureSamples(_ device: OpaquePointer!, _ buffer: UnsafeMutableRawPointer!, _ samples: ALCsizei) ``` |

Modified alcCaptureStart(_: OpaquePointer!)

|  | Declaration |
| --- | --- |
| From | ``` func alcCaptureStart(_ device: COpaquePointer) ``` |
| To | ``` func alcCaptureStart(_ device: OpaquePointer!) ``` |

Modified alcCaptureStop(_: OpaquePointer!)

|  | Declaration |
| --- | --- |
| From | ``` func alcCaptureStop(_ device: COpaquePointer) ``` |
| To | ``` func alcCaptureStop(_ device: OpaquePointer!) ``` |

Modified alcCloseDevice(_: OpaquePointer!) -> ALCboolean

|  | Declaration |
| --- | --- |
| From | ``` func alcCloseDevice(_ device: COpaquePointer) -> ALCboolean ``` |
| To | ``` func alcCloseDevice(_ device: OpaquePointer!) -> ALCboolean ``` |

Modified alcCreateContext(_: OpaquePointer!, _: UnsafePointer<ALCint>!) -> OpaquePointer!

|  | Declaration |
| --- | --- |
| From | ``` func alcCreateContext(_ device: COpaquePointer, _ attrlist: UnsafePointer<ALCint>) -> COpaquePointer ``` |
| To | ``` func alcCreateContext(_ device: OpaquePointer!, _ attrlist: UnsafePointer<ALCint>!) -> OpaquePointer! ``` |

Modified alcDestroyContext(_: OpaquePointer!)

|  | Declaration |
| --- | --- |
| From | ``` func alcDestroyContext(_ context: COpaquePointer) ``` |
| To | ``` func alcDestroyContext(_ context: OpaquePointer!) ``` |

Modified alcGetContextsDevice(_: OpaquePointer!) -> OpaquePointer!

|  | Declaration |
| --- | --- |
| From | ``` func alcGetContextsDevice(_ context: COpaquePointer) -> COpaquePointer ``` |
| To | ``` func alcGetContextsDevice(_ context: OpaquePointer!) -> OpaquePointer! ``` |

Modified alcGetCurrentContext() -> OpaquePointer!

|  | Declaration |
| --- | --- |
| From | ``` func alcGetCurrentContext() -> COpaquePointer ``` |
| To | ``` func alcGetCurrentContext() -> OpaquePointer! ``` |

Modified alcGetEnumValue(_: OpaquePointer!, _: UnsafePointer<ALCchar>!) -> ALCenum

|  | Declaration |
| --- | --- |
| From | ``` func alcGetEnumValue(_ device: COpaquePointer, _ enumname: UnsafePointer<ALCchar>) -> ALCenum ``` |
| To | ``` func alcGetEnumValue(_ device: OpaquePointer!, _ enumname: UnsafePointer<ALCchar>!) -> ALCenum ``` |

Modified alcGetError(_: OpaquePointer!) -> ALCenum

|  | Declaration |
| --- | --- |
| From | ``` func alcGetError(_ device: COpaquePointer) -> ALCenum ``` |
| To | ``` func alcGetError(_ device: OpaquePointer!) -> ALCenum ``` |

Modified alcGetIntegerv(_: OpaquePointer!, _: ALCenum, _: ALCsizei, _: UnsafeMutablePointer<ALCint>!)

|  | Declaration |
| --- | --- |
| From | ``` func alcGetIntegerv(_ device: COpaquePointer, _ param: ALCenum, _ size: ALCsizei, _ data: UnsafeMutablePointer<ALCint>) ``` |
| To | ``` func alcGetIntegerv(_ device: OpaquePointer!, _ param: ALCenum, _ size: ALCsizei, _ data: UnsafeMutablePointer<ALCint>!) ``` |

Modified alcGetProcAddress(_: OpaquePointer!, _: UnsafePointer<ALCchar>!) -> UnsafeMutableRawPointer!

|  | Declaration |
| --- | --- |
| From | ``` func alcGetProcAddress(_ device: COpaquePointer, _ funcname: UnsafePointer<ALCchar>) -> UnsafeMutablePointer<Void> ``` |
| To | ``` func alcGetProcAddress(_ device: OpaquePointer!, _ funcname: UnsafePointer<ALCchar>!) -> UnsafeMutableRawPointer! ``` |

Modified alcGetString(_: OpaquePointer!, _: ALCenum) -> UnsafePointer<ALCchar>!

|  | Declaration |
| --- | --- |
| From | ``` func alcGetString(_ device: COpaquePointer, _ param: ALCenum) -> UnsafePointer<ALCchar> ``` |
| To | ``` func alcGetString(_ device: OpaquePointer!, _ param: ALCenum) -> UnsafePointer<ALCchar>! ``` |

Modified alcIsExtensionPresent(_: OpaquePointer!, _: UnsafePointer<ALCchar>!) -> ALCboolean

|  | Declaration |
| --- | --- |
| From | ``` func alcIsExtensionPresent(_ device: COpaquePointer, _ extname: UnsafePointer<ALCchar>) -> ALCboolean ``` |
| To | ``` func alcIsExtensionPresent(_ device: OpaquePointer!, _ extname: UnsafePointer<ALCchar>!) -> ALCboolean ``` |

Modified alcMacOSXMixerMaxiumumBussesProcPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias alcMacOSXMixerMaxiumumBussesProcPtr = (ALint) -> Void ``` |
| To | ``` typealias alcMacOSXMixerMaxiumumBussesProcPtr = (ALint) -> Swift.Void ``` |

Modified alcMacOSXMixerOutputRateProcPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias alcMacOSXMixerOutputRateProcPtr = (ALdouble) -> Void ``` |
| To | ``` typealias alcMacOSXMixerOutputRateProcPtr = (ALdouble) -> Swift.Void ``` |

Modified alcMacOSXRenderingQualityProcPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias alcMacOSXRenderingQualityProcPtr = (ALint) -> Void ``` |
| To | ``` typealias alcMacOSXRenderingQualityProcPtr = (ALint) -> Swift.Void ``` |

Modified alcMakeContextCurrent(_: OpaquePointer!) -> ALCboolean

|  | Declaration |
| --- | --- |
| From | ``` func alcMakeContextCurrent(_ context: COpaquePointer) -> ALCboolean ``` |
| To | ``` func alcMakeContextCurrent(_ context: OpaquePointer!) -> ALCboolean ``` |

Modified alcOpenDevice(_: UnsafePointer<ALCchar>!) -> OpaquePointer!

|  | Declaration |
| --- | --- |
| From | ``` func alcOpenDevice(_ devicename: UnsafePointer<ALCchar>) -> COpaquePointer ``` |
| To | ``` func alcOpenDevice(_ devicename: UnsafePointer<ALCchar>!) -> OpaquePointer! ``` |

Modified alcOutputCapturerPrepareProcPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias alcOutputCapturerPrepareProcPtr = (ALCuint, ALCenum, ALCsizei) -> Void ``` |
| To | ``` typealias alcOutputCapturerPrepareProcPtr = (ALCuint, ALCenum, ALCsizei) -> Swift.Void ``` |

Modified alcOutputCapturerSamplesProcPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias alcOutputCapturerSamplesProcPtr = (UnsafeMutablePointer<Void>, ALCsizei) -> Void ``` |
| To | ``` typealias alcOutputCapturerSamplesProcPtr = (UnsafeMutableRawPointer, ALCsizei) -> Swift.Void ``` |

Modified alcOutputCapturerStartProcPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias alcOutputCapturerStartProcPtr = () -> Void ``` |
| To | ``` typealias alcOutputCapturerStartProcPtr = () -> Swift.Void ``` |

Modified alcOutputCapturerStopProcPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias alcOutputCapturerStopProcPtr = () -> Void ``` |
| To | ``` typealias alcOutputCapturerStopProcPtr = () -> Swift.Void ``` |

Modified alcProcessContext(_: OpaquePointer!)

|  | Declaration |
| --- | --- |
| From | ``` func alcProcessContext(_ context: COpaquePointer) ``` |
| To | ``` func alcProcessContext(_ context: OpaquePointer!) ``` |

Modified alcSuspendContext(_: OpaquePointer!)

|  | Declaration |
| --- | --- |
| From | ``` func alcSuspendContext(_ context: COpaquePointer) ``` |
| To | ``` func alcSuspendContext(_ context: OpaquePointer!) ``` |

Modified alDeleteBuffers(_: ALsizei, _: UnsafePointer<ALuint>!)

|  | Declaration |
| --- | --- |
| From | ``` func alDeleteBuffers(_ n: ALsizei, _ buffers: UnsafePointer<ALuint>) ``` |
| To | ``` func alDeleteBuffers(_ n: ALsizei, _ buffers: UnsafePointer<ALuint>!) ``` |

Modified alDeleteSources(_: ALsizei, _: UnsafePointer<ALuint>!)

|  | Declaration |
| --- | --- |
| From | ``` func alDeleteSources(_ n: ALsizei, _ sources: UnsafePointer<ALuint>) ``` |
| To | ``` func alDeleteSources(_ n: ALsizei, _ sources: UnsafePointer<ALuint>!) ``` |

Modified alGenBuffers(_: ALsizei, _: UnsafeMutablePointer<ALuint>!)

|  | Declaration |
| --- | --- |
| From | ``` func alGenBuffers(_ n: ALsizei, _ buffers: UnsafeMutablePointer<ALuint>) ``` |
| To | ``` func alGenBuffers(_ n: ALsizei, _ buffers: UnsafeMutablePointer<ALuint>!) ``` |

Modified alGenSources(_: ALsizei, _: UnsafeMutablePointer<ALuint>!)

|  | Declaration |
| --- | --- |
| From | ``` func alGenSources(_ n: ALsizei, _ sources: UnsafeMutablePointer<ALuint>) ``` |
| To | ``` func alGenSources(_ n: ALsizei, _ sources: UnsafeMutablePointer<ALuint>!) ``` |

Modified alGetBooleanv(_: ALenum, _: UnsafeMutablePointer<ALboolean>!)

|  | Declaration |
| --- | --- |
| From | ``` func alGetBooleanv(_ param: ALenum, _ data: UnsafeMutablePointer<ALboolean>) ``` |
| To | ``` func alGetBooleanv(_ param: ALenum, _ data: UnsafeMutablePointer<ALboolean>!) ``` |

Modified alGetBuffer3f(_: ALuint, _: ALenum, _: UnsafeMutablePointer<ALfloat>!, _: UnsafeMutablePointer<ALfloat>!, _: UnsafeMutablePointer<ALfloat>!)

|  | Declaration |
| --- | --- |
| From | ``` func alGetBuffer3f(_ bid: ALuint, _ param: ALenum, _ value1: UnsafeMutablePointer<ALfloat>, _ value2: UnsafeMutablePointer<ALfloat>, _ value3: UnsafeMutablePointer<ALfloat>) ``` |
| To | ``` func alGetBuffer3f(_ bid: ALuint, _ param: ALenum, _ value1: UnsafeMutablePointer<ALfloat>!, _ value2: UnsafeMutablePointer<ALfloat>!, _ value3: UnsafeMutablePointer<ALfloat>!) ``` |

Modified alGetBuffer3i(_: ALuint, _: ALenum, _: UnsafeMutablePointer<ALint>!, _: UnsafeMutablePointer<ALint>!, _: UnsafeMutablePointer<ALint>!)

|  | Declaration |
| --- | --- |
| From | ``` func alGetBuffer3i(_ bid: ALuint, _ param: ALenum, _ value1: UnsafeMutablePointer<ALint>, _ value2: UnsafeMutablePointer<ALint>, _ value3: UnsafeMutablePointer<ALint>) ``` |
| To | ``` func alGetBuffer3i(_ bid: ALuint, _ param: ALenum, _ value1: UnsafeMutablePointer<ALint>!, _ value2: UnsafeMutablePointer<ALint>!, _ value3: UnsafeMutablePointer<ALint>!) ``` |

Modified alGetBufferf(_: ALuint, _: ALenum, _: UnsafeMutablePointer<ALfloat>!)

|  | Declaration |
| --- | --- |
| From | ``` func alGetBufferf(_ bid: ALuint, _ param: ALenum, _ value: UnsafeMutablePointer<ALfloat>) ``` |
| To | ``` func alGetBufferf(_ bid: ALuint, _ param: ALenum, _ value: UnsafeMutablePointer<ALfloat>!) ``` |

Modified alGetBufferfv(_: ALuint, _: ALenum, _: UnsafeMutablePointer<ALfloat>!)

|  | Declaration |
| --- | --- |
| From | ``` func alGetBufferfv(_ bid: ALuint, _ param: ALenum, _ values: UnsafeMutablePointer<ALfloat>) ``` |
| To | ``` func alGetBufferfv(_ bid: ALuint, _ param: ALenum, _ values: UnsafeMutablePointer<ALfloat>!) ``` |

Modified alGetBufferi(_: ALuint, _: ALenum, _: UnsafeMutablePointer<ALint>!)

|  | Declaration |
| --- | --- |
| From | ``` func alGetBufferi(_ bid: ALuint, _ param: ALenum, _ value: UnsafeMutablePointer<ALint>) ``` |
| To | ``` func alGetBufferi(_ bid: ALuint, _ param: ALenum, _ value: UnsafeMutablePointer<ALint>!) ``` |

Modified alGetBufferiv(_: ALuint, _: ALenum, _: UnsafeMutablePointer<ALint>!)

|  | Declaration |
| --- | --- |
| From | ``` func alGetBufferiv(_ bid: ALuint, _ param: ALenum, _ values: UnsafeMutablePointer<ALint>) ``` |
| To | ``` func alGetBufferiv(_ bid: ALuint, _ param: ALenum, _ values: UnsafeMutablePointer<ALint>!) ``` |

Modified alGetDoublev(_: ALenum, _: UnsafeMutablePointer<ALdouble>!)

|  | Declaration |
| --- | --- |
| From | ``` func alGetDoublev(_ param: ALenum, _ data: UnsafeMutablePointer<ALdouble>) ``` |
| To | ``` func alGetDoublev(_ param: ALenum, _ data: UnsafeMutablePointer<ALdouble>!) ``` |

Modified alGetEnumValue(_: UnsafePointer<ALchar>!) -> ALenum

|  | Declaration |
| --- | --- |
| From | ``` func alGetEnumValue(_ ename: UnsafePointer<ALchar>) -> ALenum ``` |
| To | ``` func alGetEnumValue(_ ename: UnsafePointer<ALchar>!) -> ALenum ``` |

Modified alGetFloatv(_: ALenum, _: UnsafeMutablePointer<ALfloat>!)

|  | Declaration |
| --- | --- |
| From | ``` func alGetFloatv(_ param: ALenum, _ data: UnsafeMutablePointer<ALfloat>) ``` |
| To | ``` func alGetFloatv(_ param: ALenum, _ data: UnsafeMutablePointer<ALfloat>!) ``` |

Modified alGetIntegerv(_: ALenum, _: UnsafeMutablePointer<ALint>!)

|  | Declaration |
| --- | --- |
| From | ``` func alGetIntegerv(_ param: ALenum, _ data: UnsafeMutablePointer<ALint>) ``` |
| To | ``` func alGetIntegerv(_ param: ALenum, _ data: UnsafeMutablePointer<ALint>!) ``` |

Modified alGetListener3f(_: ALenum, _: UnsafeMutablePointer<ALfloat>!, _: UnsafeMutablePointer<ALfloat>!, _: UnsafeMutablePointer<ALfloat>!)

|  | Declaration |
| --- | --- |
| From | ``` func alGetListener3f(_ param: ALenum, _ value1: UnsafeMutablePointer<ALfloat>, _ value2: UnsafeMutablePointer<ALfloat>, _ value3: UnsafeMutablePointer<ALfloat>) ``` |
| To | ``` func alGetListener3f(_ param: ALenum, _ value1: UnsafeMutablePointer<ALfloat>!, _ value2: UnsafeMutablePointer<ALfloat>!, _ value3: UnsafeMutablePointer<ALfloat>!) ``` |

Modified alGetListener3i(_: ALenum, _: UnsafeMutablePointer<ALint>!, _: UnsafeMutablePointer<ALint>!, _: UnsafeMutablePointer<ALint>!)

|  | Declaration |
| --- | --- |
| From | ``` func alGetListener3i(_ param: ALenum, _ value1: UnsafeMutablePointer<ALint>, _ value2: UnsafeMutablePointer<ALint>, _ value3: UnsafeMutablePointer<ALint>) ``` |
| To | ``` func alGetListener3i(_ param: ALenum, _ value1: UnsafeMutablePointer<ALint>!, _ value2: UnsafeMutablePointer<ALint>!, _ value3: UnsafeMutablePointer<ALint>!) ``` |

Modified alGetListenerf(_: ALenum, _: UnsafeMutablePointer<ALfloat>!)

|  | Declaration |
| --- | --- |
| From | ``` func alGetListenerf(_ param: ALenum, _ value: UnsafeMutablePointer<ALfloat>) ``` |
| To | ``` func alGetListenerf(_ param: ALenum, _ value: UnsafeMutablePointer<ALfloat>!) ``` |

Modified alGetListenerfv(_: ALenum, _: UnsafeMutablePointer<ALfloat>!)

|  | Declaration |
| --- | --- |
| From | ``` func alGetListenerfv(_ param: ALenum, _ values: UnsafeMutablePointer<ALfloat>) ``` |
| To | ``` func alGetListenerfv(_ param: ALenum, _ values: UnsafeMutablePointer<ALfloat>!) ``` |

Modified alGetListeneri(_: ALenum, _: UnsafeMutablePointer<ALint>!)

|  | Declaration |
| --- | --- |
| From | ``` func alGetListeneri(_ param: ALenum, _ value: UnsafeMutablePointer<ALint>) ``` |
| To | ``` func alGetListeneri(_ param: ALenum, _ value: UnsafeMutablePointer<ALint>!) ``` |

Modified alGetListeneriv(_: ALenum, _: UnsafeMutablePointer<ALint>!)

|  | Declaration |
| --- | --- |
| From | ``` func alGetListeneriv(_ param: ALenum, _ values: UnsafeMutablePointer<ALint>) ``` |
| To | ``` func alGetListeneriv(_ param: ALenum, _ values: UnsafeMutablePointer<ALint>!) ``` |

Modified alGetProcAddress(_: UnsafePointer<ALchar>!) -> UnsafeMutableRawPointer!

|  | Declaration |
| --- | --- |
| From | ``` func alGetProcAddress(_ fname: UnsafePointer<ALchar>) -> UnsafeMutablePointer<Void> ``` |
| To | ``` func alGetProcAddress(_ fname: UnsafePointer<ALchar>!) -> UnsafeMutableRawPointer! ``` |

Modified alGetSource3f(_: ALuint, _: ALenum, _: UnsafeMutablePointer<ALfloat>!, _: UnsafeMutablePointer<ALfloat>!, _: UnsafeMutablePointer<ALfloat>!)

|  | Declaration |
| --- | --- |
| From | ``` func alGetSource3f(_ sid: ALuint, _ param: ALenum, _ value1: UnsafeMutablePointer<ALfloat>, _ value2: UnsafeMutablePointer<ALfloat>, _ value3: UnsafeMutablePointer<ALfloat>) ``` |
| To | ``` func alGetSource3f(_ sid: ALuint, _ param: ALenum, _ value1: UnsafeMutablePointer<ALfloat>!, _ value2: UnsafeMutablePointer<ALfloat>!, _ value3: UnsafeMutablePointer<ALfloat>!) ``` |

Modified alGetSource3i(_: ALuint, _: ALenum, _: UnsafeMutablePointer<ALint>!, _: UnsafeMutablePointer<ALint>!, _: UnsafeMutablePointer<ALint>!)

|  | Declaration |
| --- | --- |
| From | ``` func alGetSource3i(_ sid: ALuint, _ param: ALenum, _ value1: UnsafeMutablePointer<ALint>, _ value2: UnsafeMutablePointer<ALint>, _ value3: UnsafeMutablePointer<ALint>) ``` |
| To | ``` func alGetSource3i(_ sid: ALuint, _ param: ALenum, _ value1: UnsafeMutablePointer<ALint>!, _ value2: UnsafeMutablePointer<ALint>!, _ value3: UnsafeMutablePointer<ALint>!) ``` |

Modified alGetSourcef(_: ALuint, _: ALenum, _: UnsafeMutablePointer<ALfloat>!)

|  | Declaration |
| --- | --- |
| From | ``` func alGetSourcef(_ sid: ALuint, _ param: ALenum, _ value: UnsafeMutablePointer<ALfloat>) ``` |
| To | ``` func alGetSourcef(_ sid: ALuint, _ param: ALenum, _ value: UnsafeMutablePointer<ALfloat>!) ``` |

Modified alGetSourcefv(_: ALuint, _: ALenum, _: UnsafeMutablePointer<ALfloat>!)

|  | Declaration |
| --- | --- |
| From | ``` func alGetSourcefv(_ sid: ALuint, _ param: ALenum, _ values: UnsafeMutablePointer<ALfloat>) ``` |
| To | ``` func alGetSourcefv(_ sid: ALuint, _ param: ALenum, _ values: UnsafeMutablePointer<ALfloat>!) ``` |

Modified alGetSourcei(_: ALuint, _: ALenum, _: UnsafeMutablePointer<ALint>!)

|  | Declaration |
| --- | --- |
| From | ``` func alGetSourcei(_ sid: ALuint, _ param: ALenum, _ value: UnsafeMutablePointer<ALint>) ``` |
| To | ``` func alGetSourcei(_ sid: ALuint, _ param: ALenum, _ value: UnsafeMutablePointer<ALint>!) ``` |

Modified alGetSourceiv(_: ALuint, _: ALenum, _: UnsafeMutablePointer<ALint>!)

|  | Declaration |
| --- | --- |
| From | ``` func alGetSourceiv(_ sid: ALuint, _ param: ALenum, _ values: UnsafeMutablePointer<ALint>) ``` |
| To | ``` func alGetSourceiv(_ sid: ALuint, _ param: ALenum, _ values: UnsafeMutablePointer<ALint>!) ``` |

Modified alGetString(_: ALenum) -> UnsafePointer<ALchar>!

|  | Declaration |
| --- | --- |
| From | ``` func alGetString(_ param: ALenum) -> UnsafePointer<ALchar> ``` |
| To | ``` func alGetString(_ param: ALenum) -> UnsafePointer<ALchar>! ``` |

Modified alIsExtensionPresent(_: UnsafePointer<ALchar>!) -> ALboolean

|  | Declaration |
| --- | --- |
| From | ``` func alIsExtensionPresent(_ extname: UnsafePointer<ALchar>) -> ALboolean ``` |
| To | ``` func alIsExtensionPresent(_ extname: UnsafePointer<ALchar>!) -> ALboolean ``` |

Modified alListenerfv(_: ALenum, _: UnsafePointer<ALfloat>!)

|  | Declaration |
| --- | --- |
| From | ``` func alListenerfv(_ param: ALenum, _ values: UnsafePointer<ALfloat>) ``` |
| To | ``` func alListenerfv(_ param: ALenum, _ values: UnsafePointer<ALfloat>!) ``` |

Modified alListeneriv(_: ALenum, _: UnsafePointer<ALint>!)

|  | Declaration |
| --- | --- |
| From | ``` func alListeneriv(_ param: ALenum, _ values: UnsafePointer<ALint>) ``` |
| To | ``` func alListeneriv(_ param: ALenum, _ values: UnsafePointer<ALint>!) ``` |

Modified alMacOSXRenderChannelCountProcPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias alMacOSXRenderChannelCountProcPtr = (ALint) -> Void ``` |
| To | ``` typealias alMacOSXRenderChannelCountProcPtr = (ALint) -> Swift.Void ``` |

Modified alSourceAddNotificationProcPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias alSourceAddNotificationProcPtr = (ALuint, ALuint, alSourceNotificationProc, UnsafeMutablePointer<Void>) -> ALenum ``` |
| To | ``` typealias alSourceAddNotificationProcPtr = (ALuint, ALuint, OpenAL.alSourceNotificationProc, UnsafeMutableRawPointer?) -> ALenum ``` |

Modified alSourcefv(_: ALuint, _: ALenum, _: UnsafePointer<ALfloat>!)

|  | Declaration |
| --- | --- |
| From | ``` func alSourcefv(_ sid: ALuint, _ param: ALenum, _ values: UnsafePointer<ALfloat>) ``` |
| To | ``` func alSourcefv(_ sid: ALuint, _ param: ALenum, _ values: UnsafePointer<ALfloat>!) ``` |

Modified alSourceiv(_: ALuint, _: ALenum, _: UnsafePointer<ALint>!)

|  | Declaration |
| --- | --- |
| From | ``` func alSourceiv(_ sid: ALuint, _ param: ALenum, _ values: UnsafePointer<ALint>) ``` |
| To | ``` func alSourceiv(_ sid: ALuint, _ param: ALenum, _ values: UnsafePointer<ALint>!) ``` |

Modified alSourceNotificationProc

|  | Declaration |
| --- | --- |
| From | ``` typealias alSourceNotificationProc = (ALuint, ALuint, UnsafeMutablePointer<Void>) -> Void ``` |
| To | ``` typealias alSourceNotificationProc = (ALuint, ALuint, UnsafeMutableRawPointer?) -> Swift.Void ``` |

Modified alSourcePausev(_: ALsizei, _: UnsafePointer<ALuint>!)

|  | Declaration |
| --- | --- |
| From | ``` func alSourcePausev(_ ns: ALsizei, _ sids: UnsafePointer<ALuint>) ``` |
| To | ``` func alSourcePausev(_ ns: ALsizei, _ sids: UnsafePointer<ALuint>!) ``` |

Modified alSourcePlayv(_: ALsizei, _: UnsafePointer<ALuint>!)

|  | Declaration |
| --- | --- |
| From | ``` func alSourcePlayv(_ ns: ALsizei, _ sids: UnsafePointer<ALuint>) ``` |
| To | ``` func alSourcePlayv(_ ns: ALsizei, _ sids: UnsafePointer<ALuint>!) ``` |

Modified alSourceQueueBuffers(_: ALuint, _: ALsizei, _: UnsafePointer<ALuint>!)

|  | Declaration |
| --- | --- |
| From | ``` func alSourceQueueBuffers(_ sid: ALuint, _ numEntries: ALsizei, _ bids: UnsafePointer<ALuint>) ``` |
| To | ``` func alSourceQueueBuffers(_ sid: ALuint, _ numEntries: ALsizei, _ bids: UnsafePointer<ALuint>!) ``` |

Modified alSourceRemoveNotificationProcPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias alSourceRemoveNotificationProcPtr = (ALuint, ALuint, alSourceNotificationProc, UnsafeMutablePointer<Void>) -> Void ``` |
| To | ``` typealias alSourceRemoveNotificationProcPtr = (ALuint, ALuint, OpenAL.alSourceNotificationProc, UnsafeMutableRawPointer?) -> Swift.Void ``` |

Modified alSourceRenderingQualityProcPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias alSourceRenderingQualityProcPtr = (ALuint, ALint) -> Void ``` |
| To | ``` typealias alSourceRenderingQualityProcPtr = (ALuint, ALint) -> Swift.Void ``` |

Modified alSourceRewindv(_: ALsizei, _: UnsafePointer<ALuint>!)

|  | Declaration |
| --- | --- |
| From | ``` func alSourceRewindv(_ ns: ALsizei, _ sids: UnsafePointer<ALuint>) ``` |
| To | ``` func alSourceRewindv(_ ns: ALsizei, _ sids: UnsafePointer<ALuint>!) ``` |

Modified alSourceStopv(_: ALsizei, _: UnsafePointer<ALuint>!)

|  | Declaration |
| --- | --- |
| From | ``` func alSourceStopv(_ ns: ALsizei, _ sids: UnsafePointer<ALuint>) ``` |
| To | ``` func alSourceStopv(_ ns: ALsizei, _ sids: UnsafePointer<ALuint>!) ``` |

Modified alSourceUnqueueBuffers(_: ALuint, _: ALsizei, _: UnsafeMutablePointer<ALuint>!)

|  | Declaration |
| --- | --- |
| From | ``` func alSourceUnqueueBuffers(_ sid: ALuint, _ numEntries: ALsizei, _ bids: UnsafeMutablePointer<ALuint>) ``` |
| To | ``` func alSourceUnqueueBuffers(_ sid: ALuint, _ numEntries: ALsizei, _ bids: UnsafeMutablePointer<ALuint>!) ``` |

Modified LPALBUFFER3F

|  | Declaration |
| --- | --- |
| From | ``` typealias LPALBUFFER3F = (ALuint, ALenum, ALfloat, ALfloat, ALfloat) -> Void ``` |
| To | ``` typealias LPALBUFFER3F = (ALuint, ALenum, ALfloat, ALfloat, ALfloat) -> Swift.Void ``` |

Modified LPALBUFFER3I

|  | Declaration |
| --- | --- |
| From | ``` typealias LPALBUFFER3I = (ALuint, ALenum, ALint, ALint, ALint) -> Void ``` |
| To | ``` typealias LPALBUFFER3I = (ALuint, ALenum, ALint, ALint, ALint) -> Swift.Void ``` |

Modified LPALBUFFERDATA

|  | Declaration |
| --- | --- |
| From | ``` typealias LPALBUFFERDATA = (ALuint, ALenum, UnsafePointer<Void>, ALsizei, ALsizei) -> Void ``` |
| To | ``` typealias LPALBUFFERDATA = (ALuint, ALenum, UnsafeRawPointer?, ALsizei, ALsizei) -> Swift.Void ``` |

Modified LPALBUFFERF

|  | Declaration |
| --- | --- |
| From | ``` typealias LPALBUFFERF = (ALuint, ALenum, ALfloat) -> Void ``` |
| To | ``` typealias LPALBUFFERF = (ALuint, ALenum, ALfloat) -> Swift.Void ``` |

Modified LPALBUFFERFV

|  | Declaration |
| --- | --- |
| From | ``` typealias LPALBUFFERFV = (ALuint, ALenum, UnsafePointer<ALfloat>) -> Void ``` |
| To | ``` typealias LPALBUFFERFV = (ALuint, ALenum, UnsafePointer<ALfloat>?) -> Swift.Void ``` |

Modified LPALBUFFERI

|  | Declaration |
| --- | --- |
| From | ``` typealias LPALBUFFERI = (ALuint, ALenum, ALint) -> Void ``` |
| To | ``` typealias LPALBUFFERI = (ALuint, ALenum, ALint) -> Swift.Void ``` |

Modified LPALBUFFERIV

|  | Declaration |
| --- | --- |
| From | ``` typealias LPALBUFFERIV = (ALuint, ALenum, UnsafePointer<ALint>) -> Void ``` |
| To | ``` typealias LPALBUFFERIV = (ALuint, ALenum, UnsafePointer<ALint>?) -> Swift.Void ``` |

Modified LPALCCAPTURECLOSEDEVICE

|  | Declaration |
| --- | --- |
| From | ``` typealias LPALCCAPTURECLOSEDEVICE = (COpaquePointer) -> ALCboolean ``` |
| To | ``` typealias LPALCCAPTURECLOSEDEVICE = (OpaquePointer?) -> ALCboolean ``` |

Modified LPALCCAPTUREOPENDEVICE

|  | Declaration |
| --- | --- |
| From | ``` typealias LPALCCAPTUREOPENDEVICE = (UnsafePointer<ALCchar>, ALCuint, ALCenum, ALCsizei) -> COpaquePointer ``` |
| To | ``` typealias LPALCCAPTUREOPENDEVICE = (UnsafePointer<ALCchar>?, ALCuint, ALCenum, ALCsizei) -> OpaquePointer? ``` |

Modified LPALCCAPTURESAMPLES

|  | Declaration |
| --- | --- |
| From | ``` typealias LPALCCAPTURESAMPLES = (COpaquePointer, UnsafeMutablePointer<Void>, ALCsizei) -> Void ``` |
| To | ``` typealias LPALCCAPTURESAMPLES = (OpaquePointer?, UnsafeMutableRawPointer?, ALCsizei) -> Swift.Void ``` |

Modified LPALCCAPTURESTART

|  | Declaration |
| --- | --- |
| From | ``` typealias LPALCCAPTURESTART = (COpaquePointer) -> Void ``` |
| To | ``` typealias LPALCCAPTURESTART = (OpaquePointer?) -> Swift.Void ``` |

Modified LPALCCAPTURESTOP

|  | Declaration |
| --- | --- |
| From | ``` typealias LPALCCAPTURESTOP = (COpaquePointer) -> Void ``` |
| To | ``` typealias LPALCCAPTURESTOP = (OpaquePointer?) -> Swift.Void ``` |

Modified LPALCCLOSEDEVICE

|  | Declaration |
| --- | --- |
| From | ``` typealias LPALCCLOSEDEVICE = (COpaquePointer) -> ALCboolean ``` |
| To | ``` typealias LPALCCLOSEDEVICE = (OpaquePointer?) -> ALCboolean ``` |

Modified LPALCCREATECONTEXT

|  | Declaration |
| --- | --- |
| From | ``` typealias LPALCCREATECONTEXT = (COpaquePointer, UnsafePointer<ALCint>) -> COpaquePointer ``` |
| To | ``` typealias LPALCCREATECONTEXT = (OpaquePointer?, UnsafePointer<ALCint>?) -> OpaquePointer? ``` |

Modified LPALCDESTROYCONTEXT

|  | Declaration |
| --- | --- |
| From | ``` typealias LPALCDESTROYCONTEXT = (COpaquePointer) -> Void ``` |
| To | ``` typealias LPALCDESTROYCONTEXT = (OpaquePointer?) -> Swift.Void ``` |

Modified LPALCGETCONTEXTSDEVICE

|  | Declaration |
| --- | --- |
| From | ``` typealias LPALCGETCONTEXTSDEVICE = (COpaquePointer) -> COpaquePointer ``` |
| To | ``` typealias LPALCGETCONTEXTSDEVICE = (OpaquePointer?) -> OpaquePointer? ``` |

Modified LPALCGETCURRENTCONTEXT

|  | Declaration |
| --- | --- |
| From | ``` typealias LPALCGETCURRENTCONTEXT = () -> COpaquePointer ``` |
| To | ``` typealias LPALCGETCURRENTCONTEXT = () -> OpaquePointer? ``` |

Modified LPALCGETENUMVALUE

|  | Declaration |
| --- | --- |
| From | ``` typealias LPALCGETENUMVALUE = (COpaquePointer, UnsafePointer<ALCchar>) -> ALCenum ``` |
| To | ``` typealias LPALCGETENUMVALUE = (OpaquePointer?, UnsafePointer<ALCchar>?) -> ALCenum ``` |

Modified LPALCGETERROR

|  | Declaration |
| --- | --- |
| From | ``` typealias LPALCGETERROR = (COpaquePointer) -> ALCenum ``` |
| To | ``` typealias LPALCGETERROR = (OpaquePointer?) -> ALCenum ``` |

Modified LPALCGETINTEGERV

|  | Declaration |
| --- | --- |
| From | ``` typealias LPALCGETINTEGERV = (COpaquePointer, ALCenum, ALCsizei, UnsafeMutablePointer<ALCint>) -> Void ``` |
| To | ``` typealias LPALCGETINTEGERV = (OpaquePointer?, ALCenum, ALCsizei, UnsafeMutablePointer<ALCint>?) -> Swift.Void ``` |

Modified LPALCGETPROCADDRESS

|  | Declaration |
| --- | --- |
| From | ``` typealias LPALCGETPROCADDRESS = (COpaquePointer, UnsafePointer<ALCchar>) -> UnsafeMutablePointer<Void> ``` |
| To | ``` typealias LPALCGETPROCADDRESS = (OpaquePointer?, UnsafePointer<ALCchar>?) -> UnsafeMutableRawPointer? ``` |

Modified LPALCGETSTRING

|  | Declaration |
| --- | --- |
| From | ``` typealias LPALCGETSTRING = (COpaquePointer, ALCenum) -> UnsafePointer<ALCchar> ``` |
| To | ``` typealias LPALCGETSTRING = (OpaquePointer?, ALCenum) -> UnsafePointer<ALCchar>? ``` |

Modified LPALCISEXTENSIONPRESENT

|  | Declaration |
| --- | --- |
| From | ``` typealias LPALCISEXTENSIONPRESENT = (COpaquePointer, UnsafePointer<ALCchar>) -> ALCboolean ``` |
| To | ``` typealias LPALCISEXTENSIONPRESENT = (OpaquePointer?, UnsafePointer<ALCchar>?) -> ALCboolean ``` |

Modified LPALCMAKECONTEXTCURRENT

|  | Declaration |
| --- | --- |
| From | ``` typealias LPALCMAKECONTEXTCURRENT = (COpaquePointer) -> ALCboolean ``` |
| To | ``` typealias LPALCMAKECONTEXTCURRENT = (OpaquePointer?) -> ALCboolean ``` |

Modified LPALCOPENDEVICE

|  | Declaration |
| --- | --- |
| From | ``` typealias LPALCOPENDEVICE = (UnsafePointer<ALCchar>) -> COpaquePointer ``` |
| To | ``` typealias LPALCOPENDEVICE = (UnsafePointer<ALCchar>?) -> OpaquePointer? ``` |

Modified LPALCPROCESSCONTEXT

|  | Declaration |
| --- | --- |
| From | ``` typealias LPALCPROCESSCONTEXT = (COpaquePointer) -> Void ``` |
| To | ``` typealias LPALCPROCESSCONTEXT = (OpaquePointer?) -> Swift.Void ``` |

Modified LPALCSUSPENDCONTEXT

|  | Declaration |
| --- | --- |
| From | ``` typealias LPALCSUSPENDCONTEXT = (COpaquePointer) -> Void ``` |
| To | ``` typealias LPALCSUSPENDCONTEXT = (OpaquePointer?) -> Swift.Void ``` |

Modified LPALDELETEBUFFERS

|  | Declaration |
| --- | --- |
| From | ``` typealias LPALDELETEBUFFERS = (ALsizei, UnsafePointer<ALuint>) -> Void ``` |
| To | ``` typealias LPALDELETEBUFFERS = (ALsizei, UnsafePointer<ALuint>?) -> Swift.Void ``` |

Modified LPALDELETESOURCES

|  | Declaration |
| --- | --- |
| From | ``` typealias LPALDELETESOURCES = (ALsizei, UnsafePointer<ALuint>) -> Void ``` |
| To | ``` typealias LPALDELETESOURCES = (ALsizei, UnsafePointer<ALuint>?) -> Swift.Void ``` |

Modified LPALDISABLE

|  | Declaration |
| --- | --- |
| From | ``` typealias LPALDISABLE = (ALenum) -> Void ``` |
| To | ``` typealias LPALDISABLE = (ALenum) -> Swift.Void ``` |

Modified LPALDISTANCEMODEL

|  | Declaration |
| --- | --- |
| From | ``` typealias LPALDISTANCEMODEL = (ALenum) -> Void ``` |
| To | ``` typealias LPALDISTANCEMODEL = (ALenum) -> Swift.Void ``` |

Modified LPALDOPPLERFACTOR

|  | Declaration |
| --- | --- |
| From | ``` typealias LPALDOPPLERFACTOR = (ALfloat) -> Void ``` |
| To | ``` typealias LPALDOPPLERFACTOR = (ALfloat) -> Swift.Void ``` |

Modified LPALDOPPLERVELOCITY

|  | Declaration |
| --- | --- |
| From | ``` typealias LPALDOPPLERVELOCITY = (ALfloat) -> Void ``` |
| To | ``` typealias LPALDOPPLERVELOCITY = (ALfloat) -> Swift.Void ``` |

Modified LPALENABLE

|  | Declaration |
| --- | --- |
| From | ``` typealias LPALENABLE = (ALenum) -> Void ``` |
| To | ``` typealias LPALENABLE = (ALenum) -> Swift.Void ``` |

Modified LPALGENBUFFERS

|  | Declaration |
| --- | --- |
| From | ``` typealias LPALGENBUFFERS = (ALsizei, UnsafeMutablePointer<ALuint>) -> Void ``` |
| To | ``` typealias LPALGENBUFFERS = (ALsizei, UnsafeMutablePointer<ALuint>?) -> Swift.Void ``` |

Modified LPALGENSOURCES

|  | Declaration |
| --- | --- |
| From | ``` typealias LPALGENSOURCES = (ALsizei, UnsafeMutablePointer<ALuint>) -> Void ``` |
| To | ``` typealias LPALGENSOURCES = (ALsizei, UnsafeMutablePointer<ALuint>?) -> Swift.Void ``` |

Modified LPALGETBOOLEANV

|  | Declaration |
| --- | --- |
| From | ``` typealias LPALGETBOOLEANV = (ALenum, UnsafeMutablePointer<ALboolean>) -> Void ``` |
| To | ``` typealias LPALGETBOOLEANV = (ALenum, UnsafeMutablePointer<ALboolean>?) -> Swift.Void ``` |

Modified LPALGETBUFFER3F

|  | Declaration |
| --- | --- |
| From | ``` typealias LPALGETBUFFER3F = (ALuint, ALenum, UnsafeMutablePointer<ALfloat>, UnsafeMutablePointer<ALfloat>, UnsafeMutablePointer<ALfloat>) -> Void ``` |
| To | ``` typealias LPALGETBUFFER3F = (ALuint, ALenum, UnsafeMutablePointer<ALfloat>?, UnsafeMutablePointer<ALfloat>?, UnsafeMutablePointer<ALfloat>?) -> Swift.Void ``` |

Modified LPALGETBUFFER3I

|  | Declaration |
| --- | --- |
| From | ``` typealias LPALGETBUFFER3I = (ALuint, ALenum, UnsafeMutablePointer<ALint>, UnsafeMutablePointer<ALint>, UnsafeMutablePointer<ALint>) -> Void ``` |
| To | ``` typealias LPALGETBUFFER3I = (ALuint, ALenum, UnsafeMutablePointer<ALint>?, UnsafeMutablePointer<ALint>?, UnsafeMutablePointer<ALint>?) -> Swift.Void ``` |

Modified LPALGETBUFFERF

|  | Declaration |
| --- | --- |
| From | ``` typealias LPALGETBUFFERF = (ALuint, ALenum, UnsafeMutablePointer<ALfloat>) -> Void ``` |
| To | ``` typealias LPALGETBUFFERF = (ALuint, ALenum, UnsafeMutablePointer<ALfloat>?) -> Swift.Void ``` |

Modified LPALGETBUFFERFV

|  | Declaration |
| --- | --- |
| From | ``` typealias LPALGETBUFFERFV = (ALuint, ALenum, UnsafeMutablePointer<ALfloat>) -> Void ``` |
| To | ``` typealias LPALGETBUFFERFV = (ALuint, ALenum, UnsafeMutablePointer<ALfloat>?) -> Swift.Void ``` |

Modified LPALGETBUFFERI

|  | Declaration |
| --- | --- |
| From | ``` typealias LPALGETBUFFERI = (ALuint, ALenum, UnsafeMutablePointer<ALint>) -> Void ``` |
| To | ``` typealias LPALGETBUFFERI = (ALuint, ALenum, UnsafeMutablePointer<ALint>?) -> Swift.Void ``` |

Modified LPALGETBUFFERIV

|  | Declaration |
| --- | --- |
| From | ``` typealias LPALGETBUFFERIV = (ALuint, ALenum, UnsafeMutablePointer<ALint>) -> Void ``` |
| To | ``` typealias LPALGETBUFFERIV = (ALuint, ALenum, UnsafeMutablePointer<ALint>?) -> Swift.Void ``` |

Modified LPALGETDOUBLEV

|  | Declaration |
| --- | --- |
| From | ``` typealias LPALGETDOUBLEV = (ALenum, UnsafeMutablePointer<ALdouble>) -> Void ``` |
| To | ``` typealias LPALGETDOUBLEV = (ALenum, UnsafeMutablePointer<ALdouble>?) -> Swift.Void ``` |

Modified LPALGETENUMVALUE

|  | Declaration |
| --- | --- |
| From | ``` typealias LPALGETENUMVALUE = (UnsafePointer<ALchar>) -> ALenum ``` |
| To | ``` typealias LPALGETENUMVALUE = (UnsafePointer<ALchar>?) -> ALenum ``` |

Modified LPALGETFLOATV

|  | Declaration |
| --- | --- |
| From | ``` typealias LPALGETFLOATV = (ALenum, UnsafeMutablePointer<ALfloat>) -> Void ``` |
| To | ``` typealias LPALGETFLOATV = (ALenum, UnsafeMutablePointer<ALfloat>?) -> Swift.Void ``` |

Modified LPALGETINTEGERV

|  | Declaration |
| --- | --- |
| From | ``` typealias LPALGETINTEGERV = (ALenum, UnsafeMutablePointer<ALint>) -> Void ``` |
| To | ``` typealias LPALGETINTEGERV = (ALenum, UnsafeMutablePointer<ALint>?) -> Swift.Void ``` |

Modified LPALGETLISTENER3F

|  | Declaration |
| --- | --- |
| From | ``` typealias LPALGETLISTENER3F = (ALenum, UnsafeMutablePointer<ALfloat>, UnsafeMutablePointer<ALfloat>, UnsafeMutablePointer<ALfloat>) -> Void ``` |
| To | ``` typealias LPALGETLISTENER3F = (ALenum, UnsafeMutablePointer<ALfloat>?, UnsafeMutablePointer<ALfloat>?, UnsafeMutablePointer<ALfloat>?) -> Swift.Void ``` |

Modified LPALGETLISTENER3I

|  | Declaration |
| --- | --- |
| From | ``` typealias LPALGETLISTENER3I = (ALenum, UnsafeMutablePointer<ALint>, UnsafeMutablePointer<ALint>, UnsafeMutablePointer<ALint>) -> Void ``` |
| To | ``` typealias LPALGETLISTENER3I = (ALenum, UnsafeMutablePointer<ALint>?, UnsafeMutablePointer<ALint>?, UnsafeMutablePointer<ALint>?) -> Swift.Void ``` |

Modified LPALGETLISTENERF

|  | Declaration |
| --- | --- |
| From | ``` typealias LPALGETLISTENERF = (ALenum, UnsafeMutablePointer<ALfloat>) -> Void ``` |
| To | ``` typealias LPALGETLISTENERF = (ALenum, UnsafeMutablePointer<ALfloat>?) -> Swift.Void ``` |

Modified LPALGETLISTENERFV

|  | Declaration |
| --- | --- |
| From | ``` typealias LPALGETLISTENERFV = (ALenum, UnsafeMutablePointer<ALfloat>) -> Void ``` |
| To | ``` typealias LPALGETLISTENERFV = (ALenum, UnsafeMutablePointer<ALfloat>?) -> Swift.Void ``` |

Modified LPALGETLISTENERI

|  | Declaration |
| --- | --- |
| From | ``` typealias LPALGETLISTENERI = (ALenum, UnsafeMutablePointer<ALint>) -> Void ``` |
| To | ``` typealias LPALGETLISTENERI = (ALenum, UnsafeMutablePointer<ALint>?) -> Swift.Void ``` |

Modified LPALGETLISTENERIV

|  | Declaration |
| --- | --- |
| From | ``` typealias LPALGETLISTENERIV = (ALenum, UnsafeMutablePointer<ALint>) -> Void ``` |
| To | ``` typealias LPALGETLISTENERIV = (ALenum, UnsafeMutablePointer<ALint>?) -> Swift.Void ``` |

Modified LPALGETPROCADDRESS

|  | Declaration |
| --- | --- |
| From | ``` typealias LPALGETPROCADDRESS = (UnsafePointer<ALchar>) -> UnsafeMutablePointer<Void> ``` |
| To | ``` typealias LPALGETPROCADDRESS = (UnsafePointer<ALchar>?) -> UnsafeMutableRawPointer? ``` |

Modified LPALGETSOURCE3F

|  | Declaration |
| --- | --- |
| From | ``` typealias LPALGETSOURCE3F = (ALuint, ALenum, UnsafeMutablePointer<ALfloat>, UnsafeMutablePointer<ALfloat>, UnsafeMutablePointer<ALfloat>) -> Void ``` |
| To | ``` typealias LPALGETSOURCE3F = (ALuint, ALenum, UnsafeMutablePointer<ALfloat>?, UnsafeMutablePointer<ALfloat>?, UnsafeMutablePointer<ALfloat>?) -> Swift.Void ``` |

Modified LPALGETSOURCE3I

|  | Declaration |
| --- | --- |
| From | ``` typealias LPALGETSOURCE3I = (ALuint, ALenum, UnsafeMutablePointer<ALint>, UnsafeMutablePointer<ALint>, UnsafeMutablePointer<ALint>) -> Void ``` |
| To | ``` typealias LPALGETSOURCE3I = (ALuint, ALenum, UnsafeMutablePointer<ALint>?, UnsafeMutablePointer<ALint>?, UnsafeMutablePointer<ALint>?) -> Swift.Void ``` |

Modified LPALGETSOURCEF

|  | Declaration |
| --- | --- |
| From | ``` typealias LPALGETSOURCEF = (ALuint, ALenum, UnsafeMutablePointer<ALfloat>) -> Void ``` |
| To | ``` typealias LPALGETSOURCEF = (ALuint, ALenum, UnsafeMutablePointer<ALfloat>?) -> Swift.Void ``` |

Modified LPALGETSOURCEFV

|  | Declaration |
| --- | --- |
| From | ``` typealias LPALGETSOURCEFV = (ALuint, ALenum, UnsafeMutablePointer<ALfloat>) -> Void ``` |
| To | ``` typealias LPALGETSOURCEFV = (ALuint, ALenum, UnsafeMutablePointer<ALfloat>?) -> Swift.Void ``` |

Modified LPALGETSOURCEI

|  | Declaration |
| --- | --- |
| From | ``` typealias LPALGETSOURCEI = (ALuint, ALenum, UnsafeMutablePointer<ALint>) -> Void ``` |
| To | ``` typealias LPALGETSOURCEI = (ALuint, ALenum, UnsafeMutablePointer<ALint>?) -> Swift.Void ``` |

Modified LPALGETSOURCEIV

|  | Declaration |
| --- | --- |
| From | ``` typealias LPALGETSOURCEIV = (ALuint, ALenum, UnsafeMutablePointer<ALint>) -> Void ``` |
| To | ``` typealias LPALGETSOURCEIV = (ALuint, ALenum, UnsafeMutablePointer<ALint>?) -> Swift.Void ``` |

Modified LPALGETSTRING

|  | Declaration |
| --- | --- |
| From | ``` typealias LPALGETSTRING = (ALenum) -> UnsafePointer<ALchar> ``` |
| To | ``` typealias LPALGETSTRING = (ALenum) -> UnsafePointer<ALchar>? ``` |

Modified LPALISEXTENSIONPRESENT

|  | Declaration |
| --- | --- |
| From | ``` typealias LPALISEXTENSIONPRESENT = (UnsafePointer<ALchar>) -> ALboolean ``` |
| To | ``` typealias LPALISEXTENSIONPRESENT = (UnsafePointer<ALchar>?) -> ALboolean ``` |

Modified LPALLISTENER3F

|  | Declaration |
| --- | --- |
| From | ``` typealias LPALLISTENER3F = (ALenum, ALfloat, ALfloat, ALfloat) -> Void ``` |
| To | ``` typealias LPALLISTENER3F = (ALenum, ALfloat, ALfloat, ALfloat) -> Swift.Void ``` |

Modified LPALLISTENER3I

|  | Declaration |
| --- | --- |
| From | ``` typealias LPALLISTENER3I = (ALenum, ALint, ALint, ALint) -> Void ``` |
| To | ``` typealias LPALLISTENER3I = (ALenum, ALint, ALint, ALint) -> Swift.Void ``` |

Modified LPALLISTENERF

|  | Declaration |
| --- | --- |
| From | ``` typealias LPALLISTENERF = (ALenum, ALfloat) -> Void ``` |
| To | ``` typealias LPALLISTENERF = (ALenum, ALfloat) -> Swift.Void ``` |

Modified LPALLISTENERFV

|  | Declaration |
| --- | --- |
| From | ``` typealias LPALLISTENERFV = (ALenum, UnsafePointer<ALfloat>) -> Void ``` |
| To | ``` typealias LPALLISTENERFV = (ALenum, UnsafePointer<ALfloat>?) -> Swift.Void ``` |

Modified LPALLISTENERI

|  | Declaration |
| --- | --- |
| From | ``` typealias LPALLISTENERI = (ALenum, ALint) -> Void ``` |
| To | ``` typealias LPALLISTENERI = (ALenum, ALint) -> Swift.Void ``` |

Modified LPALLISTENERIV

|  | Declaration |
| --- | --- |
| From | ``` typealias LPALLISTENERIV = (ALenum, UnsafePointer<ALint>) -> Void ``` |
| To | ``` typealias LPALLISTENERIV = (ALenum, UnsafePointer<ALint>?) -> Swift.Void ``` |

Modified LPALSOURCE3F

|  | Declaration |
| --- | --- |
| From | ``` typealias LPALSOURCE3F = (ALuint, ALenum, ALfloat, ALfloat, ALfloat) -> Void ``` |
| To | ``` typealias LPALSOURCE3F = (ALuint, ALenum, ALfloat, ALfloat, ALfloat) -> Swift.Void ``` |

Modified LPALSOURCE3I

|  | Declaration |
| --- | --- |
| From | ``` typealias LPALSOURCE3I = (ALuint, ALenum, ALint, ALint, ALint) -> Void ``` |
| To | ``` typealias LPALSOURCE3I = (ALuint, ALenum, ALint, ALint, ALint) -> Swift.Void ``` |

Modified LPALSOURCEF

|  | Declaration |
| --- | --- |
| From | ``` typealias LPALSOURCEF = (ALuint, ALenum, ALfloat) -> Void ``` |
| To | ``` typealias LPALSOURCEF = (ALuint, ALenum, ALfloat) -> Swift.Void ``` |

Modified LPALSOURCEFV

|  | Declaration |
| --- | --- |
| From | ``` typealias LPALSOURCEFV = (ALuint, ALenum, UnsafePointer<ALfloat>) -> Void ``` |
| To | ``` typealias LPALSOURCEFV = (ALuint, ALenum, UnsafePointer<ALfloat>?) -> Swift.Void ``` |

Modified LPALSOURCEI

|  | Declaration |
| --- | --- |
| From | ``` typealias LPALSOURCEI = (ALuint, ALenum, ALint) -> Void ``` |
| To | ``` typealias LPALSOURCEI = (ALuint, ALenum, ALint) -> Swift.Void ``` |

Modified LPALSOURCEIV

|  | Declaration |
| --- | --- |
| From | ``` typealias LPALSOURCEIV = (ALuint, ALenum, UnsafePointer<ALint>) -> Void ``` |
| To | ``` typealias LPALSOURCEIV = (ALuint, ALenum, UnsafePointer<ALint>?) -> Swift.Void ``` |

Modified LPALSOURCEPAUSE

|  | Declaration |
| --- | --- |
| From | ``` typealias LPALSOURCEPAUSE = (ALuint) -> Void ``` |
| To | ``` typealias LPALSOURCEPAUSE = (ALuint) -> Swift.Void ``` |

Modified LPALSOURCEPAUSEV

|  | Declaration |
| --- | --- |
| From | ``` typealias LPALSOURCEPAUSEV = (ALsizei, UnsafePointer<ALuint>) -> Void ``` |
| To | ``` typealias LPALSOURCEPAUSEV = (ALsizei, UnsafePointer<ALuint>?) -> Swift.Void ``` |

Modified LPALSOURCEPLAY

|  | Declaration |
| --- | --- |
| From | ``` typealias LPALSOURCEPLAY = (ALuint) -> Void ``` |
| To | ``` typealias LPALSOURCEPLAY = (ALuint) -> Swift.Void ``` |

Modified LPALSOURCEPLAYV

|  | Declaration |
| --- | --- |
| From | ``` typealias LPALSOURCEPLAYV = (ALsizei, UnsafePointer<ALuint>) -> Void ``` |
| To | ``` typealias LPALSOURCEPLAYV = (ALsizei, UnsafePointer<ALuint>?) -> Swift.Void ``` |

Modified LPALSOURCEQUEUEBUFFERS

|  | Declaration |
| --- | --- |
| From | ``` typealias LPALSOURCEQUEUEBUFFERS = (ALuint, ALsizei, UnsafePointer<ALuint>) -> Void ``` |
| To | ``` typealias LPALSOURCEQUEUEBUFFERS = (ALuint, ALsizei, UnsafePointer<ALuint>?) -> Swift.Void ``` |

Modified LPALSOURCEREWIND

|  | Declaration |
| --- | --- |
| From | ``` typealias LPALSOURCEREWIND = (ALuint) -> Void ``` |
| To | ``` typealias LPALSOURCEREWIND = (ALuint) -> Swift.Void ``` |

Modified LPALSOURCEREWINDV

|  | Declaration |
| --- | --- |
| From | ``` typealias LPALSOURCEREWINDV = (ALsizei, UnsafePointer<ALuint>) -> Void ``` |
| To | ``` typealias LPALSOURCEREWINDV = (ALsizei, UnsafePointer<ALuint>?) -> Swift.Void ``` |

Modified LPALSOURCESTOP

|  | Declaration |
| --- | --- |
| From | ``` typealias LPALSOURCESTOP = (ALuint) -> Void ``` |
| To | ``` typealias LPALSOURCESTOP = (ALuint) -> Swift.Void ``` |

Modified LPALSOURCESTOPV

|  | Declaration |
| --- | --- |
| From | ``` typealias LPALSOURCESTOPV = (ALsizei, UnsafePointer<ALuint>) -> Void ``` |
| To | ``` typealias LPALSOURCESTOPV = (ALsizei, UnsafePointer<ALuint>?) -> Swift.Void ``` |

Modified LPALSOURCEUNQUEUEBUFFERS

|  | Declaration |
| --- | --- |
| From | ``` typealias LPALSOURCEUNQUEUEBUFFERS = (ALuint, ALsizei, UnsafeMutablePointer<ALuint>) -> Void ``` |
| To | ``` typealias LPALSOURCEUNQUEUEBUFFERS = (ALuint, ALsizei, UnsafeMutablePointer<ALuint>?) -> Swift.Void ``` |

Modified LPALSPEEDOFSOUND

|  | Declaration |
| --- | --- |
| From | ``` typealias LPALSPEEDOFSOUND = (ALfloat) -> Void ``` |
| To | ``` typealias LPALSPEEDOFSOUND = (ALfloat) -> Swift.Void ``` |

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
