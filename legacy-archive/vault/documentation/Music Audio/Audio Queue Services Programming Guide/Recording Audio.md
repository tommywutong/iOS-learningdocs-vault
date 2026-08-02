---
title: Audio Queue Services Programming Guide
apple_id: TP40005343
resource_type: Guide
platform: tvOS|iOS|macOS
topic: Audio, Video, & Visual Effects
technology: AudioToolbox
published: '2013-12-19'
source_url: https://developer.apple.com/library/archive/documentation/MusicAudio/Conceptual/AudioQueueProgrammingGuide/AQRecord/RecordingAudio.html
archived_at: '2026-07-15T08:17:10.532351Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Audio Queue Services Programming Guide](Introduction.md)


[Next](Playing%20Audio.md)[Previous](About%20Audio%20Queues.md)

# Recording Audio

When you record using Audio Queue Services, the destination can be just about anything—an on-disk file, a network connection, an object in memory, and so on. This chapter describes the most common scenario: basic recording to an on-disk file.

To add recording functionality to your application, you typically perform the following steps:

1. Define a custom structure to manage state, format, and path information.
2. Write an audio queue callback function to perform the actual recording.
3. Optionally write code to determine a good size for the audio queue buffers. Write code to work with magic cookies, if you’ll be recording in a format that uses cookies.
4. Fill the fields of the custom structure. This includes specifying the data stream that the audio queue sends to the file it’s recording into, as well as the path to that file.
5. Create a recording audio queue and ask it to create a set of audio queue buffers. Also create a file to record into.
6. Tell the audio queue to start recording.
7. When done, tell the audio queue to stop and then dispose of it. The audio queue disposes of its buffers.

The remainder of this chapter describes each of these steps in detail.

The first step in developing a recording solution using Audio Queue Services is to define a custom structure. You’ll use this structure to manage the audio format and audio queue state information. Listing 2-1 illustrates such a structure:

__Listing 2-1__  A custom structure for a recording audio queue

```
static const int kNumberBuffers = 3;                            // 1
struct AQRecorderState {
    AudioStreamBasicDescription  mDataFormat;                   // 2
    AudioQueueRef                mQueue;                        // 3
    AudioQueueBufferRef          mBuffers[kNumberBuffers];      // 4
    AudioFileID                  mAudioFile;                    // 5
    UInt32                       bufferByteSize;                // 6
    SInt64                       mCurrentPacket;                // 7
    bool                         mIsRunning;                    // 8
};
```

Here’s a description of the fields in this structure:

1. Sets the number of audio queue buffers to use.
2. An `AudioStreamBasicDescription` structure (from `CoreAudioTypes.h`) representing the audio data format to write to disk. This format gets used by the audio queue specified in the `mQueue` field.

   The `mDataFormat` field gets filled initially by code in your program, as described in [Set Up an Audio Format for Recording](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tgnbtfvbuqnbnknlti). It is good practice to then update the value of this field by querying the audio queue's `kAudioQueueProperty_StreamDescription` property, as described in [Getting the Full Audio Format from an Audio Queue](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tgnbtfvbuqnbnknltemy). On Mac OS X v10.5, use the `kAudioConverterCurrentInputStreamDescription` property instead.

   For details on the `AudioStreamBasicDescription` structure, see _[Core Audio Data Types Reference](https://developer.apple.com/documentation/coreaudio/core_audio_data_types)_.
3. The recording audio queue created by your application.
4. An array holding pointers to the audio queue buffers managed by the audio queue.
5. An audio file object representing the file into which your program records audio data.
6. The size, in bytes, for each audio queue buffer. This value is calculated in these examples in the `DeriveBufferSize` function, after the audio queue is created and before it is started. See [Write a Function to Derive Recording Audio Queue Buffer Size](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tgnbtfvbuqnbnknltcna).
7. The packet index for the first packet to be written from the current audio queue buffer.
8. A Boolean value indicating whether or not the audio queue is running.

Next, write a recording audio queue callback function. This callback does two main things:

- Writes the contents of a newly filled audio queue buffer to the audio file you’re recording into
- Enqueues the audio queue buffer (whose contents were just written to disk) to the buffer queue

This section shows an example callback declaration, then describes these two tasks separately, and finally presents an entire recording callback. For an illustration of the role of a recording audio queue callback, you can refer back to [Figure 1-3](About%20Audio%20Queues.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tgnbtfvbuqnjnknlte).

Listing 2-2 shows an example declaration for a recording audio queue callback function, declared as `AudioQueueInputCallback` in the `AudioQueue.h` header file:

__Listing 2-2__  The recording audio queue callback declaration

```
static void HandleInputBuffer (
    void                                *aqData,             // 1
    AudioQueueRef                       inAQ,                // 2
    AudioQueueBufferRef                 inBuffer,            // 3
    const AudioTimeStamp                *inStartTime,        // 4
    UInt32                              inNumPackets,        // 5
    const AudioStreamPacketDescription  *inPacketDesc        // 6
)
```

Here’s how this code works:

1. Typically, `aqData` is a custom structure that contains state data for the audio queue, as described in [Define a Custom Structure to Manage State](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tgnbtfvbuqnbnknltcni).
2. The audio queue that owns this callback.
3. The audio queue buffer containing the incoming audio data to record.
4. The sample time of the first sample in the audio queue buffer (not needed for simple recording).
5. The number of packet descriptions in the inPacketDesc parameter. A value of `0` indicates CBR data.
6. For compressed audio data formats that require packet descriptions, the packet descriptions produced by the encoder for the packets in the buffer.

The first task of a recording audio queue callback is to write an audio queue buffer to disk. This buffer is the one the callback’s audio queue has just finished filling with new audio data from an input device. The callback uses the `AudioFileWritePackets` function from the `AudioFile.h` header file, as shown in Listing 2-3.

__Listing 2-3__  Writing an audio queue buffer to disk

```swift
AudioFileWritePackets (                     // 1
    pAqData->mAudioFile,                    // 2
    false,                                  // 3
    inBuffer->mAudioDataByteSize,           // 4
    inPacketDesc,                           // 5
    pAqData->mCurrentPacket,                // 6
    &inNumPackets,                          // 7
    inBuffer->mAudioData                    // 8
);
```

Here’s how this code works:

1. The `AudioFileWritePackets` function, declared in the `AudioFile.h` header file, writes the contents of a buffer to an audio data file.
2. The audio file object (of type `AudioFileID`) that represents the audio file to write to. The `pAqData` variable is a pointer to the data structure described in [Listing 2-1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tgnbtfvbuqnbnknltk).
3. Uses a value of `false` to indicate that the function should not cache the data when writing.
4. The number of bytes of audio data being written. The `inBuffer` variable represents the audio queue buffer handed to the callback by the audio queue.
5. An array of packet descriptions for the audio data. A value of `NULL` indicates no packet descriptions are required (such as for CBR audio data).
6. The packet index for the first packet to be written.
7. On input, the number of packets to write. On output, the number of packets actually written.
8. The new audio data to write to the audio file.

Now that the audio data from an audio queue buffer has been written to the audio file, the callback enqueues the buffer, as shown in Listing 2-4. Once back in the buffer queue, the buffer is in line and ready to accept more incoming audio data.

__Listing 2-4__  Enqueuing an audio queue buffer after writing to disk

```swift
AudioQueueEnqueueBuffer (                    // 1
    pAqData->mQueue,                         // 2
    inBuffer,                                // 3
    0,                                       // 4
    NULL                                     // 5
);
```

Here’s how this code works:

1. The `AudioQueueEnqueueBuffer` function adds an audio queue buffer to an audio queue’s buffer queue.
2. The audio queue to add the designated audio queue buffer to. The `pAqData` variable is a pointer to the data structure described in Listing 2-1.
3. The audio queue buffer to enqueue.
4. The number of packet descriptions in the audio queue buffer's data. Set to `0` because this parameter is unused for recording.
5. The array of packet descriptions describing the audio queue buffer’s data. Set to `NULL` because this parameter is unused for recording.

Listing 2-5 shows a basic version of a full recording audio queue callback. As with the rest of the code examples in this document, this listing excludes error handling.

__Listing 2-5__  A recording audio queue callback function

```swift

static void HandleInputBuffer (
    void                                 *aqData,
    AudioQueueRef                        inAQ,
    AudioQueueBufferRef                  inBuffer,
    const AudioTimeStamp                 *inStartTime,
    UInt32                               inNumPackets,
    const AudioStreamPacketDescription   *inPacketDesc
) {
    AQRecorderState *pAqData = (AQRecorderState *) aqData;               // 1

    if (inNumPackets == 0 &&                                             // 2
          pAqData->mDataFormat.mBytesPerPacket != 0)
       inNumPackets =
           inBuffer->mAudioDataByteSize / pAqData->mDataFormat.mBytesPerPacket;

    if (AudioFileWritePackets (                                          // 3
            pAqData->mAudioFile,
            false,
            inBuffer->mAudioDataByteSize,
            inPacketDesc,
            pAqData->mCurrentPacket,
            &inNumPackets,
            inBuffer->mAudioData
        ) == noErr) {
            pAqData->mCurrentPacket += inNumPackets;                     // 4
    }
   if (pAqData->mIsRunning == 0)                                         // 5
      return;

    AudioQueueEnqueueBuffer (                                            // 6
        pAqData->mQueue,
        inBuffer,
        0,
        NULL
    );
}
```

Here’s how this code works:

1. The custom structure supplied to the audio queue object upon instantiation, including an audio file object representing the audio file to record into as well as a variety of state data. See [Define a Custom Structure to Manage State](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tgnbtfvbuqnbnknltcni).
2. If the audio queue buffer contains CBR data, calculate the number of packets in the buffer. This number equals the total bytes of data in the buffer divided by the (constant) number of bytes per packet. For VBR data, the audio queue supplies the number of packets in the buffer when it invokes the callback.
3. Writes the contents of the buffer to the audio data file. For a detailed description , see [Writing an Audio Queue Buffer to Disk](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tgnbtfvbuqnbnknltg).
4. If successful in writing the audio data, increment the audio data file’s packet index to be ready for writing the next buffer's worth of audio data.
5. If the audio queue has stopped, return.
6. Enqueues the audio queue buffer whose contents have just been written to the audio file. For a detailed description, see [Enqueuing an Audio Queue Buffer](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tgnbtfvbuqnbnknltq).

Audio Queue Services expects your application to specify a size for the audio queue buffers you use. Listing 2-6 shows one way to do this. It derives a buffer size large enough to hold a given duration of audio data.

The calculation here takes into account the audio data format you’re recording to. The format includes all the factors that might affect buffer size, such as the number of audio channels.

__Listing 2-6__  Deriving a recording audio queue buffer size

```
void DeriveBufferSize (
    AudioQueueRef                audioQueue,                  // 1
    AudioStreamBasicDescription  &ASBDescription,             // 2
    Float64                      seconds,                     // 3
    UInt32                       *outBufferSize               // 4
) {
    static const int maxBufferSize = 0x50000;                 // 5

    int maxPacketSize = ASBDescription.mBytesPerPacket;       // 6
    if (maxPacketSize == 0) {                                 // 7
        UInt32 maxVBRPacketSize = sizeof(maxPacketSize);
        AudioQueueGetProperty (
                audioQueue,
                kAudioQueueProperty_MaximumOutputPacketSize,
                // in Mac OS X v10.5, instead use
                //   kAudioConverterPropertyMaximumOutputPacketSize
                &maxPacketSize,
                &maxVBRPacketSize
        );
    }

    Float64 numBytesForTime =
        ASBDescription.mSampleRate * maxPacketSize * seconds; // 8
    *outBufferSize =
    UInt32 (numBytesForTime < maxBufferSize ?
        numBytesForTime : maxBufferSize);                     // 9
}
```

Here’s how this code works:

1. The audio queue that owns the buffers whose size you want to specify.
2. The `AudioStreamBasicDescription` structure for the audio queue.
3. The size you are specifying for each audio queue buffer, in terms of seconds of audio.
4. On output, the size for each audio queue buffer, in terms of bytes.
5. An upper bound for the audio queue buffer size, in bytes. In this example, the upper bound is set to 320 KB. This corresponds to approximately five seconds of stereo, 24 bit audio at a sample rate of 96 kHz.
6. For CBR audio data, get the (constant) packet size from the `AudioStreamBasicDescription` structure. Use this value as the maximum packet size.

   This assignment has the side effect of determining if the audio data to be recorded is CBR or VBR. If it is VBR, the audio queue’s `AudioStreamBasicDescription` structure lists the value of bytes-per-packet as `0`.
7. For VBR audio data, query the audio queue to get the estimated maximum packet size.
8. Derive the buffer size, in bytes.
9. Limit the buffer size, if needed, to the previously set upper bound.

Some compressed audio formats, such as MPEG 4 AAC, make use of structures that contain audio metadata. These structures are called __magic cookies__. When you record to such a format using Audio Queue Services, you must get the magic cookie from the audio queue and add it to the audio file before you start recording.

Listing 2-7 shows how to obtain a magic cookie from an audio queue and apply it to an audio file. Your code would call a function like this before recording, and then again after recording—some codecs update magic cookie data when recording has stopped.

__Listing 2-7__  Setting a magic cookie for an audio file

```
OSStatus SetMagicCookieForFile (
    AudioQueueRef inQueue,                                      // 1
    AudioFileID   inFile                                        // 2
) {
    OSStatus result = noErr;                                    // 3
    UInt32 cookieSize;                                          // 4

    if (
            AudioQueueGetPropertySize (                         // 5
                inQueue,
                kAudioQueueProperty_MagicCookie,
                &cookieSize
            ) == noErr
    ) {
        char* magicCookie =
            (char *) malloc (cookieSize);                       // 6
        if (
                AudioQueueGetProperty (                         // 7
                    inQueue,
                    kAudioQueueProperty_MagicCookie,
                    magicCookie,
                    &cookieSize
                ) == noErr
        )
            result =    AudioFileSetProperty (                  // 8
                            inFile,
                            kAudioFilePropertyMagicCookieData,
                            cookieSize,
                            magicCookie
                        );
        free (magicCookie);                                     // 9
    }
    return result;                                              // 10
}
```

Here’s how this code works:

1. The audio queue you’re using for recording.
2. The audio file you’re recording into.
3. A result variable that indicates the success or failure of this function.
4. A variable to hold the magic cookie data size.
5. Gets the data size of the magic cookie from the audio queue and stores it in the `cookieSize` variable.
6. Allocates an array of bytes to hold the magic cookie information.
7. Gets the magic cookie by querying the audio queue’s `kAudioQueueProperty_MagicCookie` property.
8. Sets the magic cookie for the audio file you’re recording into. The `AudioFileSetProperty` function is declared in the `AudioFile.h` header file.
9. Frees the memory for the temporary cookie variable.
10. Returns the success or failure of this function.

This section describes how you set up an audio data format for the audio queue. The audio queue uses this format for recording to a file.

To set up an audio data format, you specify:

- Audio data format type (such as linear PCM, AAC, etc.)
- Sample rate (such as 44.1 kHz)
- Number of audio channels (such as 2, for stereo)
- Bit depth (such as 16 bits)
- Frames per packet (linear PCM, for example, uses one frame per packet)
- Audio file type (such as CAF, AIFF, etc.)
- Details of the audio data format required for the file type

Listing 2-8 illustrates setting up an audio format for recording, using a fixed choice for each attribute. In production code, you’d typically allow the user to specify some or all aspects of the audio format. With either approach, the goal is to fill the `mDataFormat` field of the `AQRecorderState` custom structure, described in [Define a Custom Structure to Manage State](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tgnbtfvbuqnbnknltcni).

__Listing 2-8__  Specifying an audio queue’s audio data format

```
AQRecorderState aqData;                                       // 1

aqData.mDataFormat.mFormatID         = kAudioFormatLinearPCM; // 2
aqData.mDataFormat.mSampleRate       = 44100.0;               // 3
aqData.mDataFormat.mChannelsPerFrame = 2;                     // 4
aqData.mDataFormat.mBitsPerChannel   = 16;                    // 5
aqData.mDataFormat.mBytesPerPacket   =                        // 6
   aqData.mDataFormat.mBytesPerFrame =
      aqData.mDataFormat.mChannelsPerFrame * sizeof (SInt16);
aqData.mDataFormat.mFramesPerPacket  = 1;                     // 7

AudioFileTypeID fileType             = kAudioFileAIFFType;    // 8
aqData.mDataFormat.mFormatFlags =                             // 9
    kLinearPCMFormatFlagIsBigEndian
    | kLinearPCMFormatFlagIsSignedInteger
    | kLinearPCMFormatFlagIsPacked;
```

Here’s how this code works:

1. Creates an instance of the `AQRecorderState` custom structure. The structure’s `mDataFormat` field contains an `AudioStreamBasicDescription` structure. The values set in the `mDataFormat` field provide an initial definition of the audio format for the audio queue—which is also the audio format for the file you record into. In [Listing 2-10](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tgnbtfvbuqnbnknlts), you obtain a more complete specification of the audio format, which Core Audio provides to you based on the format type and file type.
2. Defines the audio data format type as linear PCM. See _[Core Audio Data Types Reference](https://developer.apple.com/documentation/coreaudio/core_audio_data_types)_ for a complete listing of the available data formats.
3. Defines the sample rate as 44.1 kHz.
4. Defines the number of channels as 2.
5. Defines the bit depth per channel as 16.
6. Defines the number of bytes per packet, and the number of bytes per frame, to 4 (that is, 2 channels times 2 bytes per sample).
7. Defines the number of frames per packet as 1.
8. Defines the file type as AIFF. See the audio file types enumeration in the `AudioFile.h` header file for a complete listing of the available file types. You can specify any file type for which there is an installed codec, as described in [Using Codecs and Audio Data Formats](About%20Audio%20Queues.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tgnbtfvbuqnjnknltcna).
9. Sets the format flags needed for the specified file type.

Now, with the recording callback and audio data format set up, you create and configure an audio queue for recording.

Listing 2-9 illustrates how to create a recording audio queue. Notice that the `AudioQueueNewInput` function uses the callback, the custom structure, and the audio data format that were configured in previous steps.

__Listing 2-9__  Creating a recording audio queue

```
AudioQueueNewInput (                              // 1
    &aqData.mDataFormat,                          // 2
    HandleInputBuffer,                            // 3
    &aqData,                                      // 4
    NULL,                                         // 5
    kCFRunLoopCommonModes,                        // 6
    0,                                            // 7
    &aqData.mQueue                                // 8
);
```

Here’s how this code works:

1. The `AudioQueueNewInput` function creates a new recording audio queue.
2. The audio data format to use for the recording. See [Set Up an Audio Format for Recording](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tgnbtfvbuqnbnknlti).
3. The callback function to use with the recording audio queue. See [Write a Recording Audio Queue Callback](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tgnbtfvbuqnbnknltena).
4. The custom data structure for the recording audio queue. See [Define a Custom Structure to Manage State](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tgnbtfvbuqnbnknltcni).
5. The run loop on which the callback will be invoked. Use `NULL` to specify default behavior, in which the callback will be invoked on a thread internal to the audio queue. This is typical use—it allows the audio queue to record while your application’s user interface thread waits for user input to stop the recording.
6. The run loop modes in which the callback can be invoked. Normally, use the `kCFRunLoopCommonModes` constant here.
7. Reserved. Must be `0`.
8. On output, the newly allocated recording audio queue.

When the audio queue came into existence (see [Creating a Recording Audio Queue](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tgnbtfvbuqnbnknlteni)), it may have filled out the `AudioStreamBasicDescription` structure more completely than you have, particularly for compressed formats. To obtain the complete format description, call the `AudioQueueGetProperty` function as shown in Listing 2-10. You use the complete audio format when you create an audio file to record into (see [Create an Audio File](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tgnbtfvbuqnbnknltenq)).

__Listing 2-10__  Getting the audio format from an audio queue

```
UInt32 dataFormatSize = sizeof (aqData.mDataFormat);       // 1

AudioQueueGetProperty (                                    // 2
    aqData.mQueue,                                         // 3
    kAudioQueueProperty_StreamDescription,                 // 4
    // in Mac OS X, instead use
    //    kAudioConverterCurrentInputStreamDescription
    &aqData.mDataFormat,                                   // 5
    &dataFormatSize                                        // 6
);
```

Here’s how this code works:

1. Gets an expected property value size to use when querying the audio queue about its audio data format.
2. The `AudioQueueGetProperty` function obtains the value for a specified property in an audio queue.
3. The audio queue to obtain the audio data format from.
4. The property ID for obtaining the value of the audio queue’s data format.
5. On output, the full audio data format, in the form of an `AudioStreamBasicDescription` structure, obtained from the audio queue.
6. On input, the expected size of the `AudioStreamBasicDescription` structure. On output, the actual size. Your recording application does not need to make use of this value.

With an audio queue created and configured, you create the audio file that you’ll record audio data into, as shown in Listing 2-11. The audio file uses the data format and file format specifications previously stored in the audio queue’s custom structure.

__Listing 2-11__  Creating an audio file for recording

```
CFURLRef audioFileURL =
    CFURLCreateFromFileSystemRepresentation (            // 1
        NULL,                                            // 2
        (const UInt8 *) filePath,                        // 3
        strlen (filePath),                               // 4
        false                                            // 5
    );

AudioFileCreateWithURL (                                 // 6
    audioFileURL,                                        // 7
    fileType,                                            // 8
    &aqData.mDataFormat,                                 // 9
    kAudioFileFlags_EraseFile,                           // 10
    &aqData.mAudioFile                                   // 11
);
```

Here’s how this code works:

1. The `CFURLCreateFromFileSystemRepresentation` function, declared in the `CFURL.h` header file, creates a CFURL object representing a file to record into.
2. Use `NULL` (or `kCFAllocatorDefault`) to use the current default memory allocator.
3. The file-system path you want to convert to a CFURL object. In production code, you would typically obtain a value for `filePath` from the user.
4. The number of bytes in the file-system path.
5. A value of `false` indicates that `filePath` represents a file, not a directory.
6. The `AudioFileCreateWithURL` function, from the `AudioFile.h` header file, creates a new audio file or initializes an existing file.
7. The URL at which to create the new audio file, or to initialize in the case of an existing file. The URL was derived from the `CFURLCreateFromFileSystemRepresentation` in step 1.
8. The file type for the new file. In the example code in this chapter, this was previously set to AIFF by way of the `kAudioFileAIFFType` file type constant. See [Set Up an Audio Format for Recording](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tgnbtfvbuqnbnknlti).
9. The data format of the audio that will be recorded into the file, specified as an `AudioStreamBasicDescription` structure. In the example code for this chapter, this was also set in [Set Up an Audio Format for Recording](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tgnbtfvbuqnbnknlti).
10. Erases the file, in the case that the file already exists.
11. On output, an audio file object (of type `AudioFileID`) representing the audio file to record into.

Before you prepare a set of audio queue buffers that you’ll use while recording, you make use of the `DeriveBufferSize` function you wrote earlier (see [Write a Function to Derive Recording Audio Queue Buffer Size](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tgnbtfvbuqnbnknltcna)). You assign this size to the recording audio queue you are using. Listing 2-12 illustrates this:

__Listing 2-12__  Setting an audio queue buffer size

```
DeriveBufferSize (                               // 1
    aqData.mQueue,                               // 2
    aqData.mDataFormat,                          // 3
    0.5,                                         // 4
    &aqData.bufferByteSize                       // 5
);
```

Here’s how this code works:

1. The `DeriveBufferSize` function, described in [Write a Function to Derive Recording Audio Queue Buffer Size](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tgnbtfvbuqnbnknltcna), sets an appropriate audio queue buffer size.
2. The audio queue that you’re setting buffer size for.
3. The audio data format for the file you are recording. See [Set Up an Audio Format for Recording](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tgnbtfvbuqnbnknlti).
4. The number of seconds of audio that each audio queue buffer should hold. One half second, as set here, is typically a good choice.
5. On output, the size for each audio queue buffer, in bytes. This value is placed in the custom structure for the audio queue.

You now ask the audio queue that you’ve created (in [Create a Recording Audio Queue](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tgnbtfvbuqnbnknlte)) to prepare a set of audio queue buffers. Listing 2-13 demonstrates how to do this.

__Listing 2-13__  Preparing a set of audio queue buffers

```
for (int i = 0; i < kNumberBuffers; ++i) {           // 1
    AudioQueueAllocateBuffer (                       // 2
        aqData.mQueue,                               // 3
        aqData.bufferByteSize,                       // 4
        &aqData.mBuffers[i]                          // 5
    );

    AudioQueueEnqueueBuffer (                        // 6
        aqData.mQueue,                               // 7
        aqData.mBuffers[i],                          // 8
        0,                                           // 9
        NULL                                         // 10
    );
}
```

Here’s how this code works:

1. Iterates to allocate and enqueue each audio queue buffer.
2. The `AudioQueueAllocateBuffer` function asks an audio queue to allocate an audio queue buffer.
3. The audio queue that performs the allocation and that will own the buffer.
4. The size, in bytes, for the new audio queue buffer being allocated. See [Write a Function to Derive Recording Audio Queue Buffer Size](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tgnbtfvbuqnbnknltcna).
5. On output, the newly allocated audio queue buffer. The pointer to the buffer is placed in the custom structure you’re using with the audio queue.
6. The `AudioQueueEnqueueBuffer` function adds an audio queue buffer to the end of a buffer queue.
7. The audio queue whose buffer queue you are adding the buffer to.
8. The audio queue buffer you are enqueuing.
9. This parameter is unused when enqueuing a buffer for recording.
10. This parameter is unused when enqueuing a buffer for recording.

All of the preceding code has led up to the very simple process of recording, as shown in Listing 2-14.

__Listing 2-14__  Recording audio

```
aqData.mCurrentPacket = 0;                           // 1
aqData.mIsRunning = true;                            // 2

AudioQueueStart (                                    // 3
    aqData.mQueue,                                   // 4
    NULL                                             // 5
);
// Wait, on user interface thread, until user stops the recording
AudioQueueStop (                                     // 6
    aqData.mQueue,                                   // 7
    true                                             // 8
);

aqData.mIsRunning = false;                           // 9
```

Here’s how this code works:

1. Initializes the packet index to `0` to begin recording at the start of the audio file.
2. Sets a flag in the custom structure to indicate that the audio queue is running. This flag is used by the recording audio queue callback.
3. The `AudioQueueStart` function starts the audio queue, on its own thread.
4. The audio queue to start.
5. Uses `NULL` to indicate that the audio queue should start recording immediately.
6. The `AudioQueueStop` function stops and resets the recording audio queue.
7. The audio queue to stop.
8. Use `true` to use synchronous stopping. See [Audio Queue Control and State](About%20Audio%20Queues.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tgnbtfvbuqnjnknltcny) for an explanation of synchronous and asynchronous stopping.
9. Sets a flag in the custom structure to indicate that the audio queue is not running.

When you’re finished with recording, dispose of the audio queue and close the audio file. Listing 2-15 illustrates these steps.

__Listing 2-15__  Cleaning up after recording

```
AudioQueueDispose (                                 // 1
    aqData.mQueue,                                  // 2
    true                                            // 3
);

AudioFileClose (aqData.mAudioFile);                 // 4
```

Here’s how this code works:

1. The `AudioQueueDispose` function disposes of the audio queue and all of its resources, including its buffers.
2. The audio queue you want to dispose of.
3. Use `true` to dispose of the audio queue synchronously (that is, immediately).
4. Closes the audio file that was used for recording. The `AudioFileClose` function is declared in the `AudioFile.h` header file.

[Next](Playing%20Audio.md)[Previous](About%20Audio%20Queues.md)

