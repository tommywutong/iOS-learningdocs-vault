---
title: Playing a sound file using the Default Output Audio Unit
apple_id: DTS10003287
resource_type: Technical Note
platform: macOS
topic: Audio, Video, & Visual Effects
technology: AudioUnit
published: '2012-10-23'
source_url: https://developer.apple.com/library/archive/technotes/tn2097/_index.html
archived_at: '2026-07-26T19:53:50.697975Z'
---
> 导航：[总目录](../README.md) · [technotes](../_indexes/technotes.md)



Technical Note TN2097

# Playing a sound file using the Default Output Audio Unit

This document discusses how to play a small audio file without using the Public Utility C++ classes available as part of the "Core Audio Utility Classes" sample download. The purpose of this document is to expose the programmer to some essential Core Audio concepts using the Default Output Audio Unit. It covers usage of Audio Units, Audio Converters, and some Core Audio data structures used for holding audio data.

Playing a sound file through Core Audio requires learning a few basic concepts. One of the most important concepts to understand is the role of an AudioUnit within Core Audio.

AudioUnits are a single processing unit that either is a source of audio data (for example, a software synthesizer), a destination of audio data (for example an AudioUnit that wraps an audio device), or both a source and destination, for example a DSP unit, such as a reverb, that takes audio data and processes or transforms this data. For more information on Audio units please refer to [Audio and MIDI on Mac OS X](https://developer.apple.com/audio/pdf/coreaudio.pdf).

This example will use an AudioUnit and an AudioConverter to convert audio data from a file format so it can be played and managed by Core Audio.

[Setting up the Default Output AudioUnit](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgmryg4wugsbrfviecusuj5hek)[Getting information from an Audio File](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgmryg4wugsbrfviecusukrlu6)[Setting up the Audio Converter](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgmryg4wugsbrfvhectkf)[Rendering audio data](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgmryg4wugsbrfviecusugq)[Conclusion](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgmryg4wugsbrfvbu6tsdjrkvgskpjy)[Document Revision History](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgmryg4wvezlwnfzws33ojbuxg5dpoj4s2rdpnz2ey2lonncwyzlnmvxhiskel4yq)

## Setting up the Default Output AudioUnit

AudioUnits are used for a variety of purposes; to generate, process, receive, or otherwise manipulate streams of audio. They can either be a source of data (for example, a software synthesizer), a destination of audio data (for example an AudioUnit serves as an interface to a Audio Device) or both. They are building blocks that may be used singly or connected together to form an audio signal graph. An AudioUnit is also a component, which is a piece of code that provides a defined set of services to one or more clients. A predefined AudioUnit in the AudioUnit framework is the Default Output AudioUnit, which is an interface to the device selected by the user in the sound preference panel. This AudioUnit can easily be constructed by using a `ComponentDescription`.

__Listing 1__  Constructing a DefaultOutputAudioUnit

```
 //An AudioUnit is an OS component.
    //A component description must be setup, then used to
    //initialize an AudioUnit

    ComponentDescription desc;
    Component comp;

    //There are several Different types of AudioUnits.
    //Some audio units serve as Outputs, Mixers, or DSP
    //units. See AUComponent.h for listing

    desc.componentType = kAudioUnitType_Output;

    //Every Component has a subType, which will give a clearer picture
    //of what this components function will be.

    desc.componentSubType = kAudioUnitSubType_DefaultOutput;

    //All AudioUnits in AUComponent.h must use
    //"kAudioUnitManufacturer_Apple" as the Manufacturer

    desc.componentManufacturer = kAudioUnitManufacturer_Apple;
    desc.componentFlags = 0;
    desc.componentFlagsMask = 0;

    //Finds a component that meets the desc spec's
    comp = FindNextComponent(NULL, &desc);
    if (comp == NULL) exit (-1);

    //gains access to the services provided by the component
    err = OpenAComponent(comp, theOutputUnit);
```

Because AudioUnits are used for a variety of audio processing on audio streams, they have many internal properties. The properties of an AudioUnit can easily be modified by using the `AudioUnitGetProperty` and `AudioUnitSetProperty` calls. `AudioUnitGetPropertyInfo` can be used to determine the size of a property and whether or not the property can be modified. `AudioUnitGetPropertyInfo` may be used prior to `AudioUnitGetProperty` and `AudioUnitSetProperty` calls to avoid error.

One of the most important properties of an AudioUnit is its stream format. Stream formats describe the nature of a stream of audio data. They provide formatting information on a stream of data like sample rates, data packet information and encoding types.

Stream formats are stored in structures called AudioStreamBasicDescriptions (ASBD) that are used widely throughout Core Audio. Because AudioUnits can be viewed as having two ends, an input and output, the stream format of the input and output should be set before using the AudioUnit. To obtain the current output stream format selected by a user, a call to `AudioUnitGetProperty()` with the parameters `kAudioUnitScope_Output` and `kAudioUnitProperty_StreamFormat` will return the current ASBD.

__Listing 2__  Using AudioUnit Get and Set routines

```
 //AudioUnit *theUnit - points to the current AudioUnit
 //AudioStreamBasicDescription *theDesc - current ASBD for user output

/***Getting the size of a Property***/
UInt32 size;

//Gets the size of the Stream Format Property and if it is writable
OSStatus result = AudioUnitGetPropertyInfo(*theUnit,
                            kAudioUnitProperty_StreamFormat,
                            kAudioUnitScope_Output,
                            0,
                            &size,
                            &outWritable);

//Get the current stream format of the output
result = AudioUnitGetProperty (*theUnit,
                            kAudioUnitProperty_StreamFormat,
                            kAudioUnitScope_Output,
                            0,
                            theDesc,
                            &size);

//Set the stream format of the output to match the input
result = AudioUnitSetProperty (*theUnit,
                            kAudioUnitProperty_StreamFormat,
                            kAudioUnitScope_Input,
                            theInputBus,
                            theDesc,
                            size);
```

Initialize the AudioUnit with `AudioUnitInitialize` after the stream format property has been established. Initialization of an AudioUnit can be an expensive operation, as it can involve the acquisition of assets (e.g. a sound bank for a MusicDevice), allocation of memory buffers required for the processing involved within the unit, and so forth. Once a unit is initialized it is basically in a state in which it can be largely expected to do work.

We must also specify where this AudioUnit will obtain its input data from by setting up its render callback. This can be done by setting the `kAudioUnitProperty_SetRenderCallback` property with a `AURenderCallbackStruct`.

__Listing 3__  Setting the Rendering Callback for a AudioUnit

```
OSStatus SetupCallbacks(AudioUnit *theOutputUnit,
                                    AURenderCallbackStruct *renderCallback)
{
    OSStatus err= noErr;
    memset(renderCallback, 0, sizeof(AURenderCallbackStruct));

    //inputProc takes a name of a method that will be used as the
    //input procedure when rendering data to the AudioUnit.
    //The input procedure will be called only when the Audio Converter needs
    //more data to process.

    //Set "fileRenderProc" as the name of the input proc
    renderCallback->inputProc = MyFileRenderProc;
    //Can pass ref Con with callback, but this isnt needed in out example
    renderCallback->inputProcRefCon =0;

    //Sets the callback for the AudioUnit to the renderCallback

    err = AudioUnitSetProperty (*theOutputUnit,
                                kAudioUnitProperty_SetRenderCallback,
                                kAudioUnitScope_Input,
                                0,
                                renderCallback,
                                sizeof(AURenderCallbackStruct));
    //Note: Some old V1 examples may use
    //"kAudioUnitProperty_SetInputCallback" which existed in
    //the old API, instead of "kAudioUnitProperty_SetRenderCallback".
    //"kAudioUnitProperty_SetRenderCallback" should
    //be used from now on.

    return err;
}
```

[Back to Top](#)

## Getting information from an Audio File

The AudioFile API provides an interface for creating, opening, modifying and saving audio files. After a sound file is opened, information can be obtained regarding format and size of the file. Before playing an `AudioFile`, a good idea is to obtain the total packet count, the file byte count, and the maximum packet size to use later for grabbing data from the audio file.

__Listing 4__  Getting information from an audio file

```
UInt64 gTotalPacketCount=0;
UInt64 gFileByteCount =0;
UInt32 gMaxPacketSize =0;

...

OSStatus GetFileInfo(FSRef *fileRef,
                               AudioFileID *fileID,
                               AudioStreamBasicDescription *fileASBD,
                               const char *fileName)
{
    OSStatus err= noErr;
    UInt32 size;

    //Obtain filesystem reference to the file using the file path
    FSPathMakeRef ((const UInt8 *)fileName, fileRef, 0);
   //Open an AudioFile and obtain AudioFileID using the file system ref
    err = AudioFileOpen(fileRef, fsRdPerm,0,fileID);

    size = sizeof(AudioStreamBasicDescription);
    memset(fileASBD, 0, size);

    //Fetch the AudioStreamBasicDescription of the audio file. we can
    //skip calling AudioFileGetPropertyInfo because we already know the
    //size of a ASBD
    err = AudioFileGetProperty(*fileID,
                                               kAudioFilePropertyDataFormat,
                                               &size,
                                               fileASBD);
    if(err)
        return err;

    //We need to get the total packet count, byte count, and max packet size
    //Theses values will be used later when grabbing data from the
    //audio file in the input callback procedure.
    size = sizeof(gTotalPacketCount); //type is UInt64
    err = AudioFileGetProperty(*fileID,
                           kAudioFilePropertyAudioDataPacketCount,
                                              &size,
                                              &gTotalPacketCount);
    if(err)
        return err;

    size = sizeof(gFileByteCount); //type is UInt64
    err = AudioFileGetProperty(*fileID,
                                   kAudioFilePropertyAudioDataByteCount,
                                              &size,
                                              &gFileByteCount);
   if(err)
        return err;

    size = sizeof(gMaxPacketSize); //type is UInt32
    err = AudioFileGetProperty(*fileID,
                                      kAudioFilePropertyMaximumPacketSize,
                                      &size,
                                      &gMaxPacketSize);
   if(err)
        return err;

    return err;
}
```

[Back to Top](#)

## Setting up the Audio Converter

Audio Converters should be used when decoding or encoding audio data. AudioConverters can handle changing sample rates and integer <=> float conversions. A very common use of the `AudioConverter` is to converting audio data obtained from a sound file to PCM data so it can be played. The Audio Converter provides an easy way of decoding data from one format to another. An `AudioConverter` requires an audio codec, the source stream format and the destination stream format for creation.

__Listing 5__  Creating a new Audio Converter instance

```
AudioStreamBasicDescription *source_AudioStreamBasicDescription;
AudioStreamBasicDescription *destination_AudioStreamBasicDescription;
AudioConverterRef *converter;

...

AudioConverterNew(source_AudioStreamBasicDescription,
                               destination_AudioStreamBasicDescription ,
                               converter);
```

[Back to Top](#)

## Rendering audio data

Use `AudioFileReadPackets` to read data from an audio file. In our example, we are reading audio data from a very small audio file; therefore, we can this directly into memory before converting the data. When larger files are being read it wouldn't be sensible to read an entire file into memory, the data must be threaded into the `AudioConverter` when it needs more data. In general, reading and processing audio data must be done in separate threads. The AudioFilePlayer in the Public Utility C++ classes included in the Core Audio SDK defers reading the audio data to another thread (See Sample Code: PlayAudioFile). Reading from an audio file in the I/O thread can block, therefore must be implemented in another thread.

__Listing 6__  Reading from an audio file into memory

```
//Reads the entire audio file into memory. No Conversions are done here.
OSStatus ReadFileIntoMem()
{
    OSStatus err = noErr;

    //total bytes read from audio file
    UInt32  bytesReturned = 0;

    //total amount of packets in audio file
    UInt32 packets =gTotalPacketCount;

    //alloc a buffer of memory to hold the data read from disk.
    gEntireFileBuffer = malloc(gFileByteCount);
    memset(gEntireFileBuffer, 0, gFileByteCount);

    //Read in the ENTIRE file into a memory buffer
    err = AudioFileReadPackets (*gSourceAudioFileID,
                                false,
                                &bytesReturned,
                                NULL,
                                0,
                                &packets,
                                gEntireFileBuffer);

    return err;
}
```

To actually begin the conversion of data obtained from the Audio File, the AudioUnit must be started by calling `AudioOutputUnitStart`. The AudioUnit will then "pull" data from wherever its input is set to. Currently in our example, we have only named the input procedure for the AudioUnit (MyFileRenderProc). We have not yet created the input procedure for the AudioUnit. Inside the input proc, we want to obtain converted audio data from the audio file. Calling `AudioConverterFillComplexBuffer` within the rendering callback will return converted data to the AudioUnit. Because this rendering callback is demand driven and will call the method you provided every time the AudioUnit needs more data. The data will be returned in an AudioBufferList, which then can be used for processing. However, `AudioConverterFillComplexBuffer` does require that another input procedure be written to supply data to the Audio Converter.

__Listing 7__  Example Render using AudioConverterFillComplexBuffer

```
OSStatus MyFileRenderProc(void     *inRefCon,
                        AudioUnitRenderActionFlags  *inActionFlags,
                        const AudioTimeStamp *inTimeStamp,
                        UInt32     inBusNumber,
                        UInt32    inNumFrames,
                        AudioBufferList     *ioData)

{
    OSStatus err= noErr;
    //To obtain a data buffer of converted data from a complex input
    //source(compressed files, etc.) use AudioConverterFillComplexBuffer.
    AudioConverterFillComplexBuffer(converter,
                MyACComplexInputProc ,
                0 ,
                &inNumFrames,
                ioData,
                0);

    return err;
}
/*
Parameters for AudioConverterFillComplexBuffer()

converter - the converter being used

MyACComplexInputProc() - input procedure to supply data to the Audio
 Converter.

inNumFrames - The amount of requested data on input. On output, this
number is the amount actually received.

ioData - Buffer of the converted data recieved on return
*/
```

This is an example of an input procedure that supplies data to an Audio Converter. The parameters of this callback are determined by what was included in the `AudioConverterFillComplexBuffer()` call. The new data to be returned is the AudioBufferList given in the parameters (ioData in this example).

__Listing 8__  Example Complex Input Procedure reading from an Audio File

```
OSStatus MyACComplexInputProc (AudioConverterRef        inAudioConverter,
                 UInt32        *ioNumberDataPackets,
                 AudioBufferList             *ioData,
                 AudioStreamPacketDescription    **outDataPacketDescription,
                 void          *inUserData)
{
    OSStatus    err = noErr;
    UInt32  bytesCopied = 0;

    // initialize in case of failure
    ioData->mBuffers[0].mData = NULL;
    ioData->mBuffers[0].mDataByteSize = 0;

    //if there are not enough packets to satisfy request,
    //then read what's left
    if (gPacketOffset + *ioNumberDataPackets > gTotalPacketCount)
        *ioNumberDataPackets = gTotalPacketCount - gPacketOffset;

    // do nothing if there are no packets available
    if (*ioNumberDataPackets)
    {
        if (gSourceBuffer != NULL) {
            free(gSourceBuffer);
            gSourceBuffer = NULL;
        }

        //the total amount of data requested by the AudioConverter
        bytesCopied = *ioNumberDataPackets * gMaxPacketSize;
        //alloc a small buffer for the AudioConverter to use.
        gSourceBuffer = (void *) calloc (1, bytesCopied);

        //copy the amount of data needed (bytesCopied)
        //from buffer of audio file
        memcpy(gSourceBuffer, gEntireFileBuffer + gByteOffset,bytesCopied);

        // keep track of where we want to read from next time
        gByteOffset +=*ioNumberDataPackets * gMaxPacketSize;
        gPacketOffset += *ioNumberDataPackets;

        // tell the Audio Converter where it's source data is
        ioData->mBuffers[0].mData = gSourceBuffer;
        // tell the Audio Converter how much data in each buffer
        ioData->mBuffers[0].mDataByteSize = bytesCopied;
    }
    else
    {
        // there aren't any more packets to read.
        // Set the amount of data read (mDataByteSize) to zero
        // and return noErr to signal the AudioConverter there are
        // no packets left.

        ioData->mBuffers[0].mData = NULL;
        ioData->mBuffers[0].mDataByteSize = 0;
        gIsPlaying=FALSE;
        err = noErr;
    }

    return err;

}
```

[Back to Top](#)

## Conclusion

Core Audio will give you more control over audio in Mac OS X. Audio data processed in Core Audio has greater resolution and performance than the Sound Manager, which enables you to give a better audio experience to customers.

[Back to Top](#)

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2012-10-23 | Editorial |
| 2006-11-15 | New document that playing an Audio File using the Default Output Audio Unit |

