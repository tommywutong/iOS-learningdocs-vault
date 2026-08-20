---
title: Always check the result code from AudioUnitGetProperty when used with kAudioUnitProperty_FastDispatch
apple_id: DTS40009556
resource_type: QA
platform: macOS
topic: Audio, Video, & Visual Effects
technology: AudioUnit
published: '2010-02-24'
source_url: https://developer.apple.com/library/archive/qa/qa1646/_index.html
archived_at: '2026-07-18T02:33:14.490141Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1646

# Always check the result code from AudioUnitGetProperty when used with kAudioUnitProperty_FastDispatch

## Q:  I'm using `kAudioUnitProperty_FastDispatch` with `AudioUnitGetProperty` to get function pointers back for some Audio Unit selectors such as `kAudioUnitRenderSelect`, `kAudioUnitSetParameterSelect` and so on. How important is it to check the return code from `AudioUnitGetProperty`?

A: I'm using `kAudioUnitProperty_FastDispatch` with `AudioUnitGetProperty` to get function pointers back for some Audio Unit selectors such as `kAudioUnitRenderSelect`, `kAudioUnitSetParameterSelect` and so on. How important is it to check the return code from `AudioUnitGetProperty`?

While it goes without saying that checking for errors is good programming practice, it is especially important that you __always__ check the return code from `AudioUnitGetProperty` when asking for function pointers from an Audio Unit using the `kAudioUnitProperty_FastDispatch` property.

The normal usage pattern is to check the return code and only assume that a valid function pointer was returned if `AudioUnitGetProperty` returns `noErr`. When `noErr` is returned, there is a guarantee that you have a valid function pointer for the specified selector.

Not checking the return code and assuming a valid function pointer in all instances will lead to crashing since some Audio Units may not implement the `kAudioUnitProperty_FastDispatch` property.

__Listing 1__  Correctly retrieving and using Audio Unit function pointers.

```
AudioUnit myAUnit; ProcPtr myRenderProc, myGetParamProc, mySetParamProc; void *myConnInstanceStorage;  void GetFastDispatchPointers(void) {      UInt32 size = sizeof(AudioUnitRenderProc);     if (AudioUnitGetProperty(myAUnit, kAudioUnitProperty_FastDispatch,                              kAudioUnitScope_Global, kAudioUnitRenderSelect,                              &myRenderProc, &size) != noErr)         myRenderProc = NULL;      if (AudioUnitGetProperty(myAUnit, kAudioUnitProperty_FastDispatch,                              kAudioUnitScope_Global, kAudioUnitGetParameterSelect,                              &myGetParamProc, &size) != noErr)         myGetParamProc = NULL;      if (AudioUnitGetProperty(myAUnit, kAudioUnitProperty_FastDispatch,                              kAudioUnitScope_Global, kAudioUnitSetParameterSelect,                              &mySetParamProc, &size) != noErr)         mySetParamProc = NULL;      if (myRenderProc || myGetParamProc || mySetParamProc) {         myConnInstanceStorage = GetComponentInstanceStorage(myAUnit);     } else {         myConnInstanceStorage = NULL;     } }  ...  OSStatus Render (AudioUnitRenderActionFlags *  ioActionFlags,                  const AudioTimeStamp *        inTimeStamp,                  UInt32                        inOutputBusNumber,                  UInt32                        inNumberFrames,                  AudioBufferList *             ioData)  {      if (myRenderProc != NULL) {         return reinterpret_cast<AudioUnitRenderProc>(myRenderProc) (myConnInstanceStorage,                                                                     ioActionFlags, inTimeStamp,                                                                     inOutputBusNumber, inNumberFrames,                                                                     ioData);     }      return AudioUnitRender(myAUnit, ioActionFlags, inTimeStamp, inOutputBusNumber, inNumberFrames, ioData); }
```


See `CAAudioUnit.cpp` and `CAAudioUnit.h` included with the 10.6 Xcode Tools located in Developer/Extras/CoreAudio/PublicUtility.

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2010-02-24 | New document that describes why you should always check the return code from AudioUnitGetProperty when using the kAudioUnitProperty_FastDispatch property. |

