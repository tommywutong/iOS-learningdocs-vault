---
title: Using AudioDeviceRead in Mac OS 10.4
apple_id: DTS10003582
resource_type: Technical Note
platform: macOS
topic: Audio, Video, & Visual Effects
technology: CoreAudio
published: '2006-11-29'
source_url: https://developer.apple.com/library/archive/technotes/tn2113/_index.html
archived_at: '2026-07-26T19:53:51.230477Z'
---
> 导航：[总目录](../README.md) · [technotes](../_indexes/technotes.md)



# Retired Document

__Important:__
This document may not represent best practices for current development. Links to downloads and other resources may no longer be valid.

Technical Note TN2113

# Using AudioDeviceRead in Mac OS 10.4

__Important:__ This document may not represent best practices for current development. Links to downloads and other resources may no longer be valid.

In order to support a wider variety of data formats, the structure of the data buffers used by the HAL (Hardware Abstraction Layer) and IOAudio-based drivers has changed. As a consequence, code that used the HAL API, `AudioDeviceRead`(), and the property `kAudioDevicePropertyRegisterBufferList`, needs to be updated to work correctly on Mac OS X Tiger.

__Note:__ These changes are only required for Tiger and later systems (10.4+). These changes will not work for previous releases.

[Introduction](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgnjygiwugsbrfvke4vcbi4yq)[Creating a AudioBufferList to use with AudioDeviceRead](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgnjygiwugsbrfvke4vcbi4za)[Preparing AudioBufferList for AudioDeviceRead](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgnjygiwugsbrfvke4vcbi43q)[Unregistering an AudioBufferList](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgnjygiwugsbrfvke4vcbi42q)[Document Revision History](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgnjygiwvezlwnfzws33ojbuxg5dpoj4s2rdpnz2ey2lonncwyzlnmvxhiskel4yq)

## Introduction

Prior to Tiger, the `AudioBufferList` used with these APIs consisted of AudioBuffers that point to a block of unstructured memory to be used for reading the data. Starting with Tiger, this changes such that each `AudioBuffer` in the `AudioBufferList` points at an `IOAudioBufferDataDescriptor` structure. This structure is defined in <IOKit/audio/IOAudioTypes.h> as follows:

__Listing 1__  `IOAudioBufferDataDescriptor` structure as defined in <IOKit/audio/IOAudioTypes.h>

```c
 typedef struct _IOAudioBufferDataDescriptor {
        UInt32	fActualDataByteSize;
        UInt32	fActualNumSampleFrames;
        UInt32	fTotalDataByteSize;
        UInt32	fNominalDataByteSize;
        Byte		fData[kVariableLengthArray];
    } IOAudioBufferDataDescriptor;
```

This change impacts registering the `AudioBufferList` to be used with an AudioDevice. To register an `AudioBufferList` to be used with an AudioDevice, the property `kAudioDevicePropertyRegisterBufferList` must be used with the `AudioDeviceSetProperty` method. The `kAudioDevicePropertyRegisterBufferList` property allows clients to register a fully populated `AudioBufferList` that matches the topology described by stream configuration of the audio device.

In addition to setting up the `AudioBufferList`, each `IOAudioBufferDataDescriptor` has to be fully filled out prior to calling `AudioDeviceSetProperty`(..., `kAudioDevicePropertyRegisterBufferList`, ...). The `fActualDataByteSize` field is set to the number of bytes out of fData that are used for a typical read. The `fActualNumSampleFrames` field is set to the number of sample frames used for a typical read. The `fTotalDataByteSize` field is set to the total number of bytes in the fData field. The `fNominalDataByteSize` field is set to the number of bytes out of fData that are used for a typical read. Note that `fActualDataByteSize` and `fNominalDataByteSize` are always the same value here. Typically, `fTotalDataByteSize` is also the same as `fActualDataByteSize` and `fNominalDataByteSize`, but can be larger. This is useful in situations where the application wants to read more or less data than typical to facilitate synchronization or reading variable sized data, such as a packet of compressed data.

[Back to Top](#)

## Creating a AudioBufferList to use with AudioDeviceRead

__Listing 2__  Registering an `AudioBufferList` for `AudioDeviceRead`

```c
//	HAL's main header
#include <CoreAudio/AudioHardware.h>

//	need this for IOAudioBufferDataDescriptor
#include <IOKit/audio/IOAudioTypes.h>

//	from /Developer/Examples/CoreAudio/PublicUtility
#include "CAAudioBufferList.h"
#include "CADebugMacros.h"

//	need this for memset
#include <string.h>

//	need to this to use vm_allocate
#include <mach/mach.h>

AudioBufferList* MakeABLForAudioDeviceRead(AudioDeviceID inDevice,
UInt32 inNumberFramesToRead, UInt32 inNumberStreams,
AudioStreamBasicDescription inStreamFormats[])
{
    //	allocate the ABL
    AudioBufferList* theABL = CAAudioBufferList::Create(inNumberStreams);
    theABL->mNumberBuffers = inNumberStreams;
    UInt32 theABLSize = CAAudioBufferList::CalculateByteSize(inNumberStreams);

    //	initialize each AudioBuffer in theABL
    for(UInt32 theIndex = 0; theIndex < inNumberStreams; ++theIndex)
    {
        //	we have to calculate how big the fData part of
                //     the IOAudioBufferDataDescriptor is
                // (note that this code assumes linear PCM data)
        UInt32 theDataByteSize = inNumberFramesToRead * inStreamFormats[theIndex].mBytesPerPacket;

        //	we can now calculate how much memory we need to
                //    allocate to hold the entire IOAudioBufferDataDescriptor
        UInt32 theAllocationByteSize = offsetof(IOAudioBufferDataDescriptor, fData) + theDataByteSize;

        //	allocate the IOAudioBufferDataDescriptor
        IOAudioBufferDataDescriptor* theDescriptor = NULL;
        kern_return_t theKernelError = vm_allocate(mach_task_self(),
                                                              vm_address_t*)&theDescriptor,
                                                              theAllocationByteSize,
                                                              VM_FLAGS_ANYWHERE);
        AssertNoKernelError(theKernelError, "vm_allocate failed");

        //	the three byte size fields of the IOAudioBufferDataDescriptor
                //     refer to the size of the fData field
        theDescriptor->fActualDataByteSize = theDataByteSize;
        theDescriptor->fTotalDataByteSize = theDataByteSize;
        theDescriptor->fNominalDataByteSize = theDataByteSize;

        //	the actual number of frames field is the number of frames to read
        theDescriptor->fActualNumSampleFrames = inNumberFramesToRead;

        //	clear out fData
        memset(&(theDescriptor->fData[0]), 0, theDataByteSize);

        //	start filling the AudioBuffer out with the number of channels
        theABL->mBuffers[theIndex].mNumberChannels = inStreamFormats[theIndex].mChannelsPerFrame;

        //	note that the data byte size in the AudioBuffer refers to
                //     the entire size of the IOAudioBufferDataDescriptor
        theABL->mBuffers[theIndex].mDataByteSize = theAllocationByteSize;

        //	and the data pointer points at the IOAudioBufferDataDescriptor
        theABL->mBuffers[theIndex].mData = theDescriptor;
    }

    //	register the ABL with the device
    OSStatus theError = AudioDeviceSetProperty(inDevice,
                                                    NULL,
                                                    0,
                                                    true,
                                                    kAudioDevicePropertyRegisterBufferList,
                                                    theABLSize,
                                                    theABL);

    AssertNoError(theError, "couldn't register the ABL");

    return theABL;
}
```

[Back to Top](#)

## Preparing AudioBufferList for AudioDeviceRead

The `AudioBufferList` needs to be prepared prior to passing it to `AudioDeviceRead`(). Each `IOAudioBufferDataDescriptor` in the `AudioBufferList` must have its fields properly filled out to indicate how much data is to be read. The `fActualDataByteSize` field is set to the number of bytes out of fData that are to be read. The `fActualNumSampleFrames` field is set to the number of sample frames that are to be read. The `fTotalDataByteSize` field is set to the total number of bytes in the fData field. The `fNominalDataByteSize` field is set to the number of bytes out of fData that are used for a typical read (the same as was used for registering the `AudioBufferList`). Note that an application can use the `fActualDataByteSize` and `fActualNumSampleFrames` can be used to vary the amount of data that gets read. When `AudioDeviceRead` returns, the data that was read will be in the fData field of each `IOAudioBufferDataDescriptor` in the `AudioBufferList`.

__Listing 3__  Preparing `AudioBufferList` for `AudioDeviceRead`

```c
//	HAL's main header
#include <CoreAudio/AudioHardware.h>

//	need this for IOAudioBufferDataDescriptor
#include <IOKit/audio/IOAudioTypes.h>

//	from /Developer/Examples/CoreAudio/PublicUtility
#include "CADebugMacros.h"

OSStatus	PrepareABLAndCallAudioDeviceRead(AudioBufferList* inABL,
                                                             AudioTimeStamp* inTimeToReadFrom,
                                                             AudioDeviceID inDevice,
                                                             UInt32 inNumberFramesToRead,
                                                             UInt32 inNumberStreams,
                                                             AudioStreamBasicDescription inStreamFormats[])
{
    //	go through each AudioBuffer and update the
        //     values in its IOAudioBufferDataDescriptor
    for(UInt32 theIndex = 0; theIndex < inNumberStreams; ++theIndex)
    {
        //	get the IOAudioBufferDataDescriptor
        IOAudioBufferDataDescriptor* theDescriptor =
                       (IOAudioBufferDataDescriptor*)inABL->mBuffers[theIndex].mData;

        //	adjust the actual size fields
        // (note that this code assumes that the other fields were
                //     filled out previously since they don't change)
        theDescriptor->fActualDataByteSize = inNumberFramesToRead * inStreamFormats[theIndex].mBytesPerFrame;
        theDescriptor->fActualNumSampleFrames = inNumberFramesToRead;
    }

    return AudioDeviceRead(inDevice, inTimeToReadFrom, inABL);
}
```

[Back to Top](#)

## Unregistering an AudioBufferList

To unregister an `AudioBufferList` that will no longer be used with `AudioDeviceRead`, you must deallocate the `IOAudioBufferDataDescriptor` as well at the `AudioBufferList`.

__Listing 4__  Unregistering an `AudioBufferList`

```
void	DestroyABLForAudioDeviceRead(AudioBufferList* inABL,
 AudioDeviceID inDevice,
UInt32 inNumberFramesToRead,
UInt32 inNumberStreams,
AudioStreamBasicDescription inStreamFormats[])
{
    //	this routine assumes that inABL is already filled out
        //    with the same values as when it was returned from MakeABLForAudioDeviceRead()

    //	unregister the ABL with the HAL
    UInt32 theABLSize = CAAudioBufferList::CalculateByteSize(inNumberStreams);
    OSStatus theError = AudioDeviceGetProperty(inDevice,
                                                             0,
                                                             true,
                                                             kAudioDevicePropertyRegisterBufferList,
                                                             &theABLSize,
                                                             inABL);
    AssertNoError(theError, "couldn't unregister the ABL");

    //	go through each AudioBuffer in theABL
    for(UInt32 theIndex = 0; theIndex < inNumberStreams; ++theIndex)
    {
        //	deallocate the IOAudioBufferDataDescriptor
        vm_deallocate(mach_task_self(),
                                       (vm_address_t) inABL->mBuffers[theIndex].mData,
                                       inABL->mBuffers[theIndex].mDataByteSize);
    }

    //	deallocate the ABL
    CAAudioBufferList::Destroy(inABL);
}
```

[Back to Top](#)

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2006-11-29 | fixed syntax error in example code |
| 2005-05-18 | New document that how to use AudioBufferLists with AudioDeviceRead in Tiger and beyond. |

