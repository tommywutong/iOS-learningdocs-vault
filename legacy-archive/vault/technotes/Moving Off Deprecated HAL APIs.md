---
title: Moving Off Deprecated HAL APIs
apple_id: DTS40009453
resource_type: Technical Note
platform: macOS
topic: Audio, Video, & Visual Effects
technology: CoreAudio
published: '2010-04-14'
source_url: https://developer.apple.com/library/archive/technotes/tn2223/_index.html
archived_at: '2026-07-26T19:54:09.744135Z'
---
> 导航：[总目录](../README.md) · [technotes](../_indexes/technotes.md)



Technical Note TN2223

# Moving Off Deprecated HAL APIs

This Technical Note discusses transitioning to the newer `AudioDevice` and `AudioObject` APIs available since the release of Mac OS X 10.5.

[Introduction](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydsnbvgmwugsbrfvjukq2ujfhu4mi)[IOProc Registration Changes](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydsnbvgmwugsbrfvjukq2ujfhu4mq)[Examples](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydsnbvgmwugsbrfvjvkqstivbviskpjyza)[Property Accessor Changes](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydsnbvgmwugsbrfvjukq2ujfhu4na)[Examples](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydsnbvgmwugsbrfvjvkqstivbviskpjy2a)[Reference](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydsnbvgmwugsbrfvjukq2ujfhu4nq)[Document Revision History](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydsnbvgmwvezlwnfzws33ojbuxg5dpoj4s2rdpnz2ey2lonncwyzlnmvxhiskel4yq)

## Introduction

The `AudioHardware.h` header file contains APIs used to work with the audio HAL. The audio HAL provides the abstraction through which applications can access audio hardware. There are a set of HAL APIs which have been deprecated since the release of Mac OS X 10.5 and should no longer be used.

There are two types of deprecated APIs. The first type are the `AudioDeviceIOProc` registration calls, these include `AudioDeviceAddIOProc` and `AudioDeviceRemoveIOProc`. The second type are the property accessors such as `AudioHardwareGetProperty`, `AudioDeviceSetProperty` and related APIs.

Transitioning to the newer APIs is straight forward and recommended for all applications currently using the older deprecated APIs.

[Back to Top](#)

## IOProc Registration Changes

The `AudioDeviceIOProc` registration change introduces the `AudioDeviceIOProcID` type and remaps `AudioDeviceAddIOProc` and `AudioDeviceRemoveIOProc` to `AudioDeviceCreateIOProcID` and `AudioDeviceDestroyIOProcID` respectively.

An `AudioDeviceIOProcID` represents both an IOProc and the client data that goes with it. Once created, an `AudioDeviceIOProcID` can be used everywhere one would use a regular IOProc. The purpose for an `AudioDeviceIOProcID` is to allow a client to register the same function pointer as an IOProc with a device multiple times (as long as the user client data pointer is different each time).

When using these new registration APIs, you pass the `AudioDeviceIOProcID` returned from `AudioDeviceCreateIOProcID` to `AudioDeviceStart` and `AudioDeviceStop` rather than the IOProc itself.

### Examples

__Listing 1__  Deprecated - `AudioDeviceIOProc` Registration.

```
OSStatus MyIOProc(AudioDeviceID           inDevice,                   const AudioTimeStamp*   inNow,                   const AudioBufferList*  inInputData,                   const AudioTimeStamp*   inInputTime,                   AudioBufferList*        outOutputData,                   const AudioTimeStamp*   inOutputTime,                   void*                   inClientData) {     // your IOProc here     ... }  // Deprecated void DeprecatedFakePlay(AudioObjectID inDevice, void* inClientData) {     //  register the IOProc     OSStatus theError = AudioDeviceAddIOProc(inDevice, MyIOProc, inClientData);     // handle errors      //  start IO     theError = AudioDeviceStart(inDevice, MyIOProc);      ...      //  stop IO     theError = AudioDeviceStop(inDevice, MyIOProc);      //  unregister the IOProc     theError = AudioDeviceRemoveIOProc(inDevice, MyIOProc); }
```

__Listing 2__  New - `AudioDeviceIOProc` Registration.

```
OSStatus MyIOProc(AudioDeviceID           inDevice,                   const AudioTimeStamp*   inNow,                   const AudioBufferList*  inInputData,                   const AudioTimeStamp*   inInputTime,                   AudioBufferList*        outOutputData,                   const AudioTimeStamp*   inOutputTime,                   void*                   inClientData) {     // your IOProc here     ... }  // New Mac OS X 10.5+ void NewFakePlay(AudioObjectID inDevice, void* inClientData) {     //  register the IOProc     AudioDeviceIOProcID theIOProcID = NULL;      OSStatus theError = AudioDeviceCreateIOProcID(inDevice, MyIOProc, inClientData, &theIOProcID);     // handle errors     // ensure theIOProcID != NULL      //  start IO     theError = AudioDeviceStart(inDevice, theIOProcID);      ...      //  stop IO     theError = AudioDeviceStop(inDevice, theIOProcID);      //  unregister the IOProc     theError = AudioDeviceDestroyIOProcID(inDevice, theIOProcID); }
```

[Back to Top](#)

## Property Accessor Changes

The Property Accessor changes are a little different but can be summed up like this -- All the individual class property access functions have been replaced by a similarly named `AudioObject`-prefixed function.

The table below illustrates the basic mapping where 'XXX' in the older API name can be replaced by 'Hardware', 'Device' or 'Stream':

__Table 1__

| Deprecated API | New API |
| AudioXXXGetPropertyInfo | AudioObjectHasProperty, AudioObjectIsPropertySettable, AudioObjectGetPropertyDataSize |
| AudioXXXGetProperty | AudioObjectGetPropertyData |
| AudioXXXSetProperty | AudioObjectSetPropertyData |
| AudioXXXAddPropertyListener | AudioObjectAddPropertyListener |
| AudioXXXRemovePropertyListener | AudioObjectRemovePropertyListener |

The key difference between the deprecated and new API is the use of the `AudioObjectPropertyAddress` structure.

```
struct  AudioObjectPropertyAddress {     AudioObjectPropertySelector mSelector;     AudioObjectPropertyScope    mScope;     AudioObjectPropertyElement  mElement; }; typedef struct AudioObjectPropertyAddress   AudioObjectPropertyAddress;
```

The `AudioObjectPropertyAddress` structure is used with the new APIs to encapsulate the distinguishing information for a specific property; the selector ID (`mSelector`), the scope (`mScope`) and the element (`mElement`). The HAL uses the terms scope and element in the same way that the AudioUnit API does.

Most objects have only one scope and one element, for example the System Object, Stream Object and Control Object have only one scope, `kAudioObjectPropertyScopeGlobal` and one element, `kAudioObjectPropertyElementMaster`.

Device Objects are different and may have three other scopes beside `kAudioObjectPropertyScopeGlobal`. These are `kAudioDevicePropertyScopeInput`, `kAudioDevicePropertyScopeOutput`, and `kAudioDevicePropertyScopePlayThrough`.

For a Device Object, the element (`mElement`) of the `AudioObjectPropertyAddress` structure refers to the channel number on the device.

### Examples

__Listing 3__  Deprecated - Getting the default Input device.

```
AudioDeviceID DeprecatedGetDefaultInputDevice() {     AudioDeviceID theAnswer = 0;     UInt32 theSize = sizeof(AudioDeviceID);     OSStatus theError = AudioHardwareGetProperty(kAudioHardwarePropertyDefaultInputDevice,                                                  &theSize,                                                  &theAnswer);      // handle errors      return theAnswer; }
```

__Listing 4__  New - Getting the default input device.

```
AudioDeviceID NewGetDefaultInputDevice() {     AudioDeviceID theAnswer = 0;     UInt32 theSize = sizeof(AudioDeviceID);     AudioObjectPropertyAddress theAddress = { kAudioHardwarePropertyDefaultInputDevice,                                               kAudioObjectPropertyScopeGlobal,                                               kAudioObjectPropertyElementMaster };      OSStatus theError = AudioObjectGetPropertyData(kAudioObjectSystemObject,                                                    &theAddress,                                                    0,                                                    NULL,                                                    &theSize,                                                    &theAnswer);     // handle errors      return theAnswer; }
```

__Listing 5__  Deprecated - Getting the current volume scalar.

```
Float32 DeprecatedGetVolumeScalar(AudioDeviceID inDevice, bool inIsInput, UInt32 inChannel) {     Float32 theAnswer = 0;     UInt32 theSize = sizeof(Float32);     OSStatus theError = AudioDeviceGetProperty(inDevice,                                                inChannel,                                                inIsInput,                                                kAudioDevicePropertyVolumeScalar,                                                &theSize,                                                &theAnswer);     // handle errors      return theAnswer; }
```

__Listing 6__  New - Getting the current volume scalar.

```
Float32 NewGetVolumeScalar(AudioDeviceID inDevice, bool inIsInput, UInt32 inChannel) {     Float32 theAnswer = 0;     UInt32 theSize = sizeof(Float32);     AudioObjectPropertyScope theScope = inIsInput ? kAudioDevicePropertyScopeInput :                                                     kAudioDevicePropertyScopeOutput     AudioObjectPropertyAddress theAddress = { kAudioDevicePropertyVolumeScalar,                                               theScope,                                               inChannel };      OSStatus theError = AudioObjectGetPropertyData(inDevice,                                                    &theAddress,                                                    0,                                                    NULL,                                                    &theSize,                                                    &theAnswer);     // handle errors      return theAnswer; }
```

Note the usage of `kAudioObjectSystemObject` when replacing the old APIs. `kAudioObjectSystemObject` is an `AudioObjectID` that always refers to the one and only instance of the Audio System Object.

[Back to Top](#)

## Reference

See `CoreAudio/AudioHardware.h` for further details.

[Back to Top](#)

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2010-04-14 | Editorial |
| 2010-04-08 | Editorial |
| 2010-01-09 | New document that discusses transitioning to the newer AudioDevice and AudioObject APIs available on Mac OS X 10.5+ |

