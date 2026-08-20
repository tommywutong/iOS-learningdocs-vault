---
title: GLAirplay
apple_id: DTS40013259
resource_type: Sample Code
platform: iOS
topic: User Experience
technology: null
published: '2016-08-12'
source_url: https://developer.apple.com/library/archive/samplecode/GLAirplay/Listings/GLAirPlay_MyOpenALSupport_h.html
archived_at: '2026-07-18T03:09:50.412917Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [GLAirplay](GLAirplay.md)


[Next](GLAirPlay-UserInterfaceViewController.m.md)[Previous](GLAirPlay-CubePlayback.m.md)

# GLAirPlay/MyOpenALSupport.h

```objc
/*
 Copyright (C) 2016 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 OpenAL-related support functions
 */

#import <OpenAL/al.h>
#import <OpenAL/alc.h>
#import <AudioToolbox/AudioToolbox.h>
#import <AVFoundation/AVAudioSession.h>

typedef ALvoid  AL_APIENTRY (*alBufferDataStaticProcPtr) (const ALint bid, ALenum format, ALvoid* data, ALsizei size, ALsizei freq);
ALvoid  alBufferDataStaticProc(const ALint bid, ALenum format, ALvoid* data, ALsizei size, ALsizei freq)
{
    static  alBufferDataStaticProcPtr   proc = NULL;

    if (proc == NULL) {
        proc = (alBufferDataStaticProcPtr) alcGetProcAddress(NULL, (const ALCchar*) "alBufferDataStatic");
    }

    if (proc)
        proc(bid, format, data, size, freq);

    return;
}

void* MyGetOpenALAudioData(CFURLRef inFileURL, ALsizei *outDataSize, ALenum *outDataFormat, ALsizei*    outSampleRate)
{
    OSStatus                        err = noErr;    
    UInt64                          fileDataSize = 0;
    AudioStreamBasicDescription     theFileFormat;
    UInt32                          thePropertySize = sizeof(theFileFormat);
    AudioFileID                     afid = 0;
    void*                           theData = NULL;

    // Open a file with ExtAudioFileOpen()
    err = AudioFileOpenURL(inFileURL, kAudioFileReadPermission, 0, &afid);
    if(err) { printf("MyGetOpenALAudioData: AudioFileOpenURL FAILED, Error = %d\n", (int)err); goto Exit; }

    // Get the audio data format
    err = AudioFileGetProperty(afid, kAudioFilePropertyDataFormat, &thePropertySize, &theFileFormat);
    if(err) { printf("MyGetOpenALAudioData: AudioFileGetProperty(kAudioFileProperty_DataFormat) FAILED, Error = %d\n", (int)err); goto Exit; }

    if (theFileFormat.mChannelsPerFrame > 2)  { 
        printf("MyGetOpenALAudioData - Unsupported Format, channel count is greater than stereo\n"); goto Exit;
    }

    if ((theFileFormat.mFormatID != kAudioFormatLinearPCM) || (!TestAudioFormatNativeEndian(theFileFormat))) { 
        printf("MyGetOpenALAudioData - Unsupported Format, must be little-endian PCM\n"); goto Exit;
    }

    if ((theFileFormat.mBitsPerChannel != 8) && (theFileFormat.mBitsPerChannel != 16)) { 
        printf("MyGetOpenALAudioData - Unsupported Format, must be 8 or 16 bit PCM\n"); goto Exit;
    }


    thePropertySize = sizeof(fileDataSize);
    err = AudioFileGetProperty(afid, kAudioFilePropertyAudioDataByteCount, &thePropertySize, &fileDataSize);
    if(err) { printf("MyGetOpenALAudioData: AudioFileGetProperty(kAudioFilePropertyAudioDataByteCount) FAILED, Error = %d\n", (int)err); goto Exit; }

    // Read all the data into memory
    UInt32      dataSize = (UInt32)fileDataSize;
    theData = malloc(dataSize);
    if (theData)
    {
        AudioFileReadBytes(afid, false, 0, &dataSize, theData);
        if(err == noErr)
        {
            // success
            *outDataSize = (ALsizei)dataSize;
            *outDataFormat = (theFileFormat.mChannelsPerFrame > 1) ? AL_FORMAT_STEREO16 : AL_FORMAT_MONO16;
            *outSampleRate = (ALsizei)theFileFormat.mSampleRate;
        }
        else 
        { 
            // failure
            free (theData);
            theData = NULL; // make sure to return NULL
            printf("MyGetOpenALAudioData: ExtAudioFileRead FAILED, Error = %d\n", (int)err); goto Exit;
        }   
    }

Exit:
    // Dispose the ExtAudioFileRef, it is no longer needed
    if (afid) AudioFileClose(afid);
    return theData;
}

void TeardownOpenAL()
{
    ALCcontext  *context = NULL;
    ALCdevice   *device = NULL;
    ALuint      returnedName;

    // Delete the Sources
    alDeleteSources(1, &returnedName);
    // Delete the Buffers
    alDeleteBuffers(1, &returnedName);

    //Get active context
    context = alcGetCurrentContext();
    //Get device for active context
    device = alcGetContextsDevice(context);
    //Release context
    alcDestroyContext(context);
    //Close device
    alcCloseDevice(device);
}
```

[Next](GLAirPlay-UserInterfaceViewController.m.md)[Previous](GLAirPlay-CubePlayback.m.md)

