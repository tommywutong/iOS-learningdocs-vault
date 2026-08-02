---
title: Audio Queue Services Programming Guide
apple_id: TP40005343
resource_type: Guide
platform: tvOS|iOS|macOS
topic: Audio, Video, & Visual Effects
technology: AudioToolbox
published: '2013-12-19'
source_url: https://developer.apple.com/library/archive/documentation/MusicAudio/Conceptual/AudioQueueProgrammingGuide/AQPlayback/PlayingAudio.html
archived_at: '2026-07-15T08:17:10.504234Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Audio Queue Services Programming Guide](Introduction.md)


[Next](Document%20Revision%20History.md)[Previous](Recording%20Audio.md)

# Playing Audio

When you play audio using Audio Queue Services, the source can be just about anything—an on-disk file, a software-based audio synthesizer, an object in memory, and so on. This chapter describes the most common scenario: playing back an on-disk file.

To add playback functionality to your application, you typically perform the following steps:

1. Define a custom structure to manage state, format, and path information.
2. Write an audio queue callback function to perform the actual playback.
3. Write code to determine a good size for the audio queue buffers.
4. Open an audio file for playback and determine its audio data format.
5. Create a playback audio queue and configure it for playback.
6. Allocate and enqueue audio queue buffers. Tell the audio queue to start playing. When done, the playback callback tells the audio queue to stop.
7. Dispose of the audio queue. Release resources.

The remainder of this chapter describes each of these steps in detail.

To start, define a custom structure that you’ll use to manage audio format and audio queue state information. Listing 3-1 illustrates such a structure:

__Listing 3-1__  A custom structure for a playback audio queue

```
static const int kNumberBuffers = 3;                              // 1
struct AQPlayerState {
    AudioStreamBasicDescription   mDataFormat;                    // 2
    AudioQueueRef                 mQueue;                         // 3
    AudioQueueBufferRef           mBuffers[kNumberBuffers];       // 4
    AudioFileID                   mAudioFile;                     // 5
    UInt32                        bufferByteSize;                 // 6
    SInt64                        mCurrentPacket;                 // 7
    UInt32                        mNumPacketsToRead;              // 8
    AudioStreamPacketDescription  *mPacketDescs;                  // 9
    bool                          mIsRunning;                     // 10
};
```

Most fields in this structure are identical (or nearly so) to those in the custom structure used for recording, as described in the Recording Audio chapter in [Define a Custom Structure to Manage State](Recording%20Audio.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tgnbtfvbuqnbnknltcni). For example, the `mDataFormat` field is used here to hold the format of the file being played. When recording, the analogous field holds the format of the file being written to disk.

Here’s a description of the fields in this structure:

1. Sets the number of audio queue buffers to use. Three is typically a good number, as described in [Audio Queue Buffers](About%20Audio%20Queues.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tgnbtfvbuqnjnknltcmy).
2. An `AudioStreamBasicDescription` structure (from `CoreAudioTypes.h`) representing the audio data format of the file being played. This format gets used by the audio queue specified in the `mQueue` field.

   The `mDataFormat` field gets filled by querying an audio file's `kAudioFilePropertyDataFormat` property, as described in [Obtaining a File’s Audio Data Format](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tgnbtfvbuqmznknlteni).

   For details on the `AudioStreamBasicDescription` structure, see _[Core Audio Data Types Reference](https://developer.apple.com/documentation/coreaudio/core_audio_data_types)_.
3. The playback audio queue created by your application.
4. An array holding pointers to the audio queue buffers managed by the audio queue.
5. An audio file object that represents the audio file your program plays.
6. The size, in bytes, for each audio queue buffer. This value is calculated in these examples in the `DeriveBufferSize` function, after the audio queue is created and before it is started. See [Write a Function to Derive Playback Audio Queue Buffer Size](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tgnbtfvbuqmznknltemy).
7. The packet index for the next packet to play from the audio file.
8. The number of packets to read on each invocation of the audio queue’s playback callback. Like the `bufferByteSize` field, this value is calculated in these examples in the `DeriveBufferSize` function, after the audio queue is created and before it is started.
9. For VBR audio data, the array of packet descriptions for the file being played. For CBR data, the value of this field is `NULL`.
10. A Boolean value indicating whether or not the audio queue is running.

Next, write a playback audio queue callback function. This callback does three main things:

- Reads a specified amount of data from an audio file and puts it into an audio queue buffer
- Enqueues the audio queue buffer to the buffer queue
- When there’s no more data to read from the audio file, tells the audio queue to stop

This section shows an example callback declaration, describes each of these tasks separately, and finally presents an entire playback callback. For an illustration of the role of a playback callback, you can refer back to [Figure 1-4](About%20Audio%20Queues.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tgnbtfvbuqnjnknltg).

Listing 3-2 shows an example declaration for a playback audio queue callback function, declared as `AudioQueueOutputCallback` in the `AudioQueue.h` header file:

__Listing 3-2__  The playback audio queue callback declaration

```
static void HandleOutputBuffer (
    void                 *aqData,                 // 1
    AudioQueueRef        inAQ,                    // 2
    AudioQueueBufferRef  inBuffer                 // 3
)
```

Here’s how this code works:

1. Typically, `aqData` is the custom structure that contains state information for the audio queue, as described in [Define a Custom Structure to Manage State](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tgnbtfvbuqmznknltcni).
2. The audio queue that owns this callback.
3. An audio queue buffer that the callback is to fill with data by reading from an audio file.

The first action of a playback audio queue callback is to read data from an audio file and place it in an audio queue buffer. Listing 3-3 shows how to do this.

__Listing 3-3__  Reading from an audio file into an audio queue buffer

```swift
AudioFileReadPackets (                        // 1
    pAqData->mAudioFile,                      // 2
    false,                                    // 3
    &numBytesReadFromFile,                    // 4
    pAqData->mPacketDescs,                    // 5
    pAqData->mCurrentPacket,                  // 6
    &numPackets,                              // 7
    inBuffer->mAudioData                      // 8
);
```

Here’s how this code works:

1. The `AudioFileReadPackets` function, declared in the `AudioFile.h` header file, reads data from an audio file and places it into a buffer.
2. The audio file to read from.
3. Uses a value of `false` to indicate that the function should not cache the data when reading.
4. On output, the number of bytes of audio data that were read from the audio file.
5. On output, an array of packet descriptions for the data that was read from the audio file. For CBR data, the input value of this parameter is `NULL`.
6. The packet index for the first packet to read from the audio file.
7. On input, the number of packets to read from the audio file. On output, the number of packets actually read.
8. On output, the filled audio queue buffer containing data that was read from the audio file.

Now that data has been read from an audio file and placed in an audio queue buffer, the callback enqueues the buffer, as shown in Listing 3-4. Once in the buffer queue, the audio data in the buffer is available for the audio queue to send to the output device.

__Listing 3-4__  Enqueuing an audio queue buffer after reading from disk

```swift
AudioQueueEnqueueBuffer (                      // 1
    pAqData->mQueue,                           // 2
    inBuffer,                                  // 3
    (pAqData->mPacketDescs ? numPackets : 0),  // 4
    pAqData->mPacketDescs                      // 5
);
```

Here’s how this code works:

1. The `AudioQueueEnqueueBuffer` function adds an audio queue buffer to a buffer queue.
2. The audio queue that owns the buffer queue.
3. The audio queue buffer to enqueue
4. The number of packets represented in the audio queue buffer’s data. For CBR data, which uses no packet descriptions, uses `0`.
5. For compressed audio data formats that use packet descriptions, the packet descriptions for the packets in the buffer. .

The last thing your callback does is to check if there’s no more data to read from the audio file that you’re playing. Upon discovering the end of the file, your callback tells the playback audio queue to stop. Listing 3-5 illustrates this.

__Listing 3-5__  Stopping an audio queue

```swift
if (numPackets == 0) {                          // 1
    AudioQueueStop (                            // 2
        pAqData->mQueue,                        // 3
        false                                   // 4
    );
    pAqData->mIsRunning = false;                // 5
}
```

Here’s how this code works:

1. Checks if the number of packets read by the `AudioFileReadPackets` function (invoked earlier by the callback) is `0`.
2. The `AudioQueueStop` function stops the audio queue.
3. The audio queue to stop.
4. Stops the audio queue asynchronously, when all queued buffers have been played. See [Audio Queue Control and State](About%20Audio%20Queues.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tgnbtfvbuqnjnknltcny).
5. Sets a flag in the custom structure to indicate that playback is finished.

Listing 3-6 shows a basic version of a full playback audio queue callback. As with the rest of the code examples in this document, this listing excludes error handling.

__Listing 3-6__  A playback audio queue callback function

```swift
static void HandleOutputBuffer (     void                *aqData,     AudioQueueRef       inAQ,     AudioQueueBufferRef inBuffer ) {     AQPlayerState *pAqData = (AQPlayerState *) aqData;        // 1     if (pAqData->mIsRunning == 0) return;                     // 2     UInt32 numBytesReadFromFile;                              // 3     UInt32 numPackets = pAqData->mNumPacketsToRead;           // 4     AudioFileReadPackets (         pAqData->mAudioFile,         false,         &numBytesReadFromFile,         pAqData->mPacketDescs,          pAqData->mCurrentPacket,         &numPackets,         inBuffer->mAudioData      );     if (numPackets > 0) {                                     // 5         inBuffer->mAudioDataByteSize = numBytesReadFromFile;  // 6        AudioQueueEnqueueBuffer (              pAqData->mQueue,             inBuffer,             (pAqData->mPacketDescs ? numPackets : 0),             pAqData->mPacketDescs         );         pAqData->mCurrentPacket += numPackets;                // 7      } else {         AudioQueueStop (             pAqData->mQueue,             false         );         pAqData->mIsRunning = false;      } }
```

Here’s how this code works:

1. The custom data supplied to the audio queue upon instantiation, including the audio file object (of type `AudioFileID`) representing the file to play as well as a variety of state data. See [Define a Custom Structure to Manage State](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tgnbtfvbuqmznknltcni).
2. If the audio queue is stopped, returns immediately.
3. A variable to hold the number of bytes of audio data read from the file being played.
4. Initializes the `numPackets` variable with the number of packets to read from the file being played.
5. Tests whether some audio data was retrieved from the file. If so, enqueues the newly-filled buffer. If not, stops the audio queue.
6. Tells the audio queue buffer structure the number of bytes of data that were read.
7. Increments the packet index according to the number of packets that were read.

Audio Queue Services expects your application to specify a size for the audio queue buffers you use. Listing 3-7 shows one way to do this. It derives a buffer size large enough to hold a given duration of audio data.

You’ll call this `DeriveBufferSize` function in your application, after creating a playback audio queue, as a prerequisite to asking the audio queue to allocate buffers. See [Set Sizes for a Playback Audio Queue](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tgnbtfvbuqmznknlts).

The code here does two additional things compared to the analogous function you saw in [Write a Function to Derive Recording Audio Queue Buffer Size](Recording%20Audio.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tgnbtfvbuqnbnknltcna). For playback you also:

- Derive the number of packets to read each time your callback invokes the `AudioFileReadPackets` function
- Set a lower bound on buffer size, to avoid overly frequent disk access

The calculation here takes into account the audio data format you’re reading from disk. The format includes all the factors that might affect buffer size, such as the number of audio channels.

__Listing 3-7__  Deriving a playback audio queue buffer size

```
void DeriveBufferSize (
    AudioStreamBasicDescription &ASBDesc,                            // 1
    UInt32                      maxPacketSize,                       // 2
    Float64                     seconds,                             // 3
    UInt32                      *outBufferSize,                      // 4
    UInt32                      *outNumPacketsToRead                 // 5
) {
    static const int maxBufferSize = 0x50000;                        // 6
    static const int minBufferSize = 0x4000;                         // 7

    if (ASBDesc.mFramesPerPacket != 0) {                             // 8
        Float64 numPacketsForTime =
            ASBDesc.mSampleRate / ASBDesc.mFramesPerPacket * seconds;
        *outBufferSize = numPacketsForTime * maxPacketSize;
    } else {                                                         // 9
        *outBufferSize =
            maxBufferSize > maxPacketSize ?
                maxBufferSize : maxPacketSize;
    }

    if (                                                             // 10
        *outBufferSize > maxBufferSize &&
        *outBufferSize > maxPacketSize
    )
        *outBufferSize = maxBufferSize;
    else {                                                           // 11
        if (*outBufferSize < minBufferSize)
            *outBufferSize = minBufferSize;
    }

    *outNumPacketsToRead = *outBufferSize / maxPacketSize;           // 12
}
```

Here’s how this code works:

1. The `AudioStreamBasicDescription` structure for the audio queue.
2. The estimated maximum packet size for the data in the audio file you’re playing. You can determine this value by invoking the `AudioFileGetProperty` function (declared in the `AudioFile.h` header file) with a property ID of `kAudioFilePropertyPacketSizeUpperBound`. See [Set Sizes for a Playback Audio Queue](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tgnbtfvbuqmznknlts).
3. The size you are specifying for each audio queue buffer, in terms of seconds of audio.
4. On output, the size for each audio queue buffer, in bytes.
5. On output, the number of packets of audio data to read from the file on each invocation of the playback audio queue callback.
6. An upper bound for the audio queue buffer size, in bytes. In this example, the upper bound is set to 320 KB. This corresponds to approximately five seconds of stereo, 24 bit audio at a sample rate of 96 kHz.
7. A lower bound for the audio queue buffer size, in bytes. In this example, the lower bound is set to 16 KB.
8. For audio data formats that define a fixed number of frames per packet, derives the audio queue buffer size.
9. For audio data formats that do not define a fixed number of frames per packet, derives a reasonable audio queue buffer size based on the maximum packet size and the upper bound you’ve set.
10. If the derived buffer size is above the upper bound you’ve set, adjusts it the bound—taking into account the estimated maximum packet size.
11. If the derived buffer size is below the lower bound you’ve set, adjusts it to the bound.
12. Calculates the number of packets to read from the audio file on each invocation of the callback.

Now you open an audio file for playback, using these three steps:

1. Obtain a CFURL object representing the audio file you want to play.
2. Open the file.
3. Obtain the file’s audio data format.

Listing 3-8 demonstrates how to obtain a CFURL object for the audio file you want to play. You use the CFURL object in the next step, opening the file..

__Listing 3-8__  Obtaining a CFURL object for an audio file

```
CFURLRef audioFileURL =
    CFURLCreateFromFileSystemRepresentation (           // 1
        NULL,                                           // 2
        (const UInt8 *) filePath,                       // 3
        strlen (filePath),                              // 4
        false                                           // 5
    );
```

Here’s how this code works:

1. The `CFURLCreateFromFileSystemRepresentation` function, declared in the `CFURL.h` header file, creates a CFURL object representing the file to play.
2. Uses `NULL` (or `kCFAllocatorDefault`) to use the current default memory allocator.
3. The file-system path you want to convert to a CFURL object. In production code, you would typically obtain a value for `filePath` from the user.
4. The number of bytes in the file-system path.
5. A value of `false` indicates that `filePath` represents a file, not a directory.

Listing 3-9 demonstrates how to open an audio file for playback.

__Listing 3-9__  Opening an audio file for playback

```
AQPlayerState aqData;                                   // 1

OSStatus result =
    AudioFileOpenURL (                                  // 2
        audioFileURL,                                   // 3
        fsRdPerm,                                       // 4
        0,                                              // 5
        &aqData.mAudioFile                              // 6
    );

CFRelease (audioFileURL);                               // 7
```

Here’s how this code works:

1. Creates an instance of the `AQPlayerState` custom structure (see [Define a Custom Structure to Manage State](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tgnbtfvbuqmznknltcni)). You use this instance when you open an audio file for playback, as a place to hold the audio file object (of type `AudioFileID`) that represents the audio file.
2. The `AudioFileOpenURL` function, declared in the `AudioFile.h` header file, opens the file you want to play.
3. A reference to the file to play.
4. The file permissions you want to use with the file you’re playing. The available permissions are defined in the File Manager’s `File Access Permission Constants` enumeration. In this example you request permission to read the file.
5. An optional file type hint. A value of `0` here indicates that the example does not use this facility.
6. On output, a reference to the audio file is placed in the custom structure’s `mAudioFile` field.
7. Releases the CFURL object that was created in step 1.

Listing 3-10 shows how to obtain a file’s audio data format.

__Listing 3-10__  Obtaining a file’s audio data format

```
UInt32 dataFormatSize = sizeof (aqData.mDataFormat);    // 1

AudioFileGetProperty (                                  // 2
    aqData.mAudioFile,                                  // 3
    kAudioFilePropertyDataFormat,                       // 4
    &dataFormatSize,                                    // 5
    &aqData.mDataFormat                                 // 6
);
```

Here’s how this code works:

1. Gets an expected property value size to use when querying the audio file about its audio data format.
2. The `AudioFileGetProperty` function, declared in the `AudioFile.h` header file, obtains the value for a specified property in an audio file.
3. An audio file object (of type `AudioFileID`) representing the file whose audio data format you want to obtain.
4. The property ID for obtaining the value of the audio file’s data format.
5. On input, the expected size of the `AudioStreamBasicDescription` structure that describes the audio file’s data format. On output, the actual size. Your playback application does not need to make use of this value.
6. On output, the full audio data format, in the form of an `AudioStreamBasicDescription` structure, obtained from the audio file. This line applies the file’s audio data format to the audio queue by storing it in the audio queue’s custom structure.

Listing 3-11 shows how to create a playback audio queue. Notice that the `AudioQueueNewOutput` function uses the custom structure and the callback that were configured in previous steps, as well as the audio data format of the file to be played.

__Listing 3-11__  Creating a playback audio queue

```
AudioQueueNewOutput (                                // 1     &aqData.mDataFormat,                             // 2     HandleOutputBuffer,                              // 3     &aqData,                                         // 4     CFRunLoopGetCurrent (),                          // 5     kCFRunLoopCommonModes,                           // 6     0,                                               // 7     &aqData.mQueue                                   // 8 );
```

Here’s how this code works:

1. The `AudioQueueNewOutput` function creates a new playback audio queue.
2. The audio data format of the file that the audio queue is being set up to play. See [Obtaining a File’s Audio Data Format](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tgnbtfvbuqmznknlteni).
3. The callback function to use with the playback audio queue. See [Write a Playback Audio Queue Callback](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tgnbtfvbuqmznknlte).
4. The custom data structure for the playback audio queue. See [Define a Custom Structure to Manage State](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tgnbtfvbuqmznknltcni).
5. The current run loop, and the one on which the audio queue playback callback will be invoked.
6. The run loop modes in which the callback can be invoked. Normally, use the `kCFRunLoopCommonModes` constant here.
7. Reserved. Must be `0`.
8. On output, the newly allocated playback audio queue.

Next, you set some sizes for the playback audio queue. You use these sizes when you allocate buffers for an audio queue and before you start reading an audio file.

The code listings in this section show how to set:

- Audio queue buffer size
- Number of packets to read for each invocation of the playback audio queue callback
- Array size for holding the packet descriptions for one buffer’s worth of audio data

Listing 3-12 demonstrates how to use the `DeriveBufferSize` function you wrote earlier (see [Write a Function to Derive Playback Audio Queue Buffer Size](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tgnbtfvbuqmznknltemy)). The goal here is to set a size, in bytes, for each audio queue buffer, and to determine the number of packets to read for each invocation of the playback audio queue callback.

This code uses a conservative estimate of maximum packet size, which Core Audio provides by way of the `kAudioFilePropertyPacketSizeUpperBound` property. In most cases, it is better to use this technique—which is approximate but fast—than to take the time to read an entire audio file to obtain the actual maximum packet size.

__Listing 3-12__  Setting playback audio queue buffer size and number of packets to read

```
UInt32 maxPacketSize;
UInt32 propertySize = sizeof (maxPacketSize);
AudioFileGetProperty (                               // 1
    aqData.mAudioFile,                               // 2
    kAudioFilePropertyPacketSizeUpperBound,          // 3
    &propertySize,                                   // 4
    &maxPacketSize                                   // 5
);

DeriveBufferSize (                                   // 6
    aqData.mDataFormat,                              // 7
    maxPacketSize,                                   // 8
    0.5,                                             // 9
    &aqData.bufferByteSize,                          // 10
    &aqData.mNumPacketsToRead                        // 11
);
```

Here’s how this code works:

1. The `AudioFileGetProperty` function, declared in the `AudioFile.h` header file, obtains the value of a specified property for an audio file. Here you use it to get a conservative upper bound, in bytes, for the size of the audio data packets in the file you want to play.
2. An audio file object (of type `AudioFileID`) representing the file you want to play. See [Opening an Audio File](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tgnbtfvbuqmznknltena).
3. The property ID for obtaining a conservative upper bound for packet size in an audio file.
4. On output, the size, in bytes, for the `kAudioFilePropertyPacketSizeUpperBound` property.
5. On output, a conservative upper bound for packet size, in bytes, for the file you want to play.
6. The `DeriveBufferSize` function, described in [Write a Function to Derive Playback Audio Queue Buffer Size](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tgnbtfvbuqmznknltemy), sets a buffer size and a number of packets to read on each invocation of the playback audio queue callback.
7. The audio data format of the file you want to play. See [Obtaining a File’s Audio Data Format](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tgnbtfvbuqmznknlteni).
8. The estimated maximum packet size in the audio file, from line 5 of this listing.
9. The number of seconds of audio that each audio queue buffer should hold. One half second, as set here, is typically a good choice.
10. On output, the size for each audio queue buffer, in bytes. This value is placed in the custom structure for the audio queue.
11. On output, the number of packets to read on each invocation of the playback audio queue callback. This value is also placed in the custom structure for the audio queue.

Now you allocate memory for an array to hold the packet descriptions for one buffer’s worth of audio data. Constant bitrate data does not use packet descriptions, so the CBR case—step 3 in Listing 3-13—is very simple.

__Listing 3-13__  Allocating memory for a packet descriptions array

```
bool isFormatVBR = (                                       // 1
    aqData.mDataFormat.mBytesPerPacket == 0 ||
    aqData.mDataFormat.mFramesPerPacket == 0
);

if (isFormatVBR) {                                         // 2
    aqData.mPacketDescs =
      (AudioStreamPacketDescription*) malloc (
        aqData.mNumPacketsToRead * sizeof (AudioStreamPacketDescription)
      );
} else {                                                   // 3
    aqData.mPacketDescs = NULL;
}
```

Here’s how this code works:

1. Determines if the audio file’s data format is VBR or CBR. In VBR data, one or both of the bytes-per-packet or frames-per-packet values is variable, and so will be listed as `0` in the audio queue’s `AudioStreamBasicDescription` structure.
2. For an audio file that contains VBR data, allocates memory for the packet descriptions array. Calculates the memory needed based on the number of audio data packets to be read on each invocation of the playback callback. See [Setting Buffer Size and Number of Packets to Read](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tgnbtfvbuqmznknltenq).
3. For an audio file that contains CBR data, such as linear PCM, the audio queue does not use a packet descriptions array.

Some compressed audio formats, such as MPEG 4 AAC, make use of structures to contain audio metadata. These structures are called __magic cookies__. When you play a file in such a format using Audio Queue Services, you get the magic cookie from the audio file and add it to the audio queue before you start playing.

Listing 3-14 shows how to obtain a magic cookie from a file and apply it to an audio queue. Your code would call this function before starting playback.

__Listing 3-14__  Setting a magic cookie for a playback audio queue

```
UInt32 cookieSize = sizeof (UInt32);                   // 1
bool couldNotGetProperty =                             // 2
    AudioFileGetPropertyInfo (                         // 3
        aqData.mAudioFile,                             // 4
        kAudioFilePropertyMagicCookieData,             // 5
        &cookieSize,                                   // 6
        NULL                                           // 7
    );

if (!couldNotGetProperty && cookieSize) {              // 8
    char* magicCookie =
        (char *) malloc (cookieSize);

    AudioFileGetProperty (                             // 9
        aqData.mAudioFile,                             // 10
        kAudioFilePropertyMagicCookieData,             // 11
        &cookieSize,                                   // 12
        magicCookie                                    // 13
    );

    AudioQueueSetProperty (                            // 14
        aqData.mQueue,                                 // 15
        kAudioQueueProperty_MagicCookie,               // 16
        magicCookie,                                   // 17
        cookieSize                                     // 18
    );

    free (magicCookie);                                // 19
}
```

Here’s how this code works:

1. Sets an estimated size for the magic cookie data.
2. Captures the result of the `AudioFileGetPropertyInfo` function. If successful, this function returns a value of `NoErr`, equivalent to Boolean `false`.
3. The `AudioFileGetPropertyInfo` function, declared in the `AudioFile.h` header file, gets the size of the value of a specified property. You use this to set the size of the variable that holds the property value.
4. An audio file object (of type `AudioFileID`) that represents the audio file you want to play.
5. The property ID representing an audio file’s magic cookie data.
6. On input, an estimated size for the magic cookie data. On output, the actual size.
7. Uses `NULL` to indicate that you don’t care about the read/write access for the property.
8. If the audio file does contain a magic cookie, allocate memory to hold it.
9. The `AudioFileGetProperty` function, declared in the `AudioFile.h` header file, gets the value of a specified property. In this case, it gets the audio file’s magic cookie.
10. An audio file object (of type `AudioFileID`) that represents the audio file you want to play, and whose magic cookie you are getting.
11. The property ID representing the audio file’s magic cookie data.
12. On input, the size of the `magicCookie` variable obtained using the `AudioFileGetPropertyInfo` function. On output, the actual size of the magic cookie in terms of the number of bytes written to the `magicCookie` variable.
13. On output, the audio file’s magic cookie.
14. The `AudioQueueSetProperty` function sets a property in an audio queue. In this case, it sets a magic cookie for the audio queue, matching the magic cookie in the audio file to be played.
15. The audio queue that you want to set a magic cookie for.
16. The property ID representing an audio queue’s magic cookie.
17. The magic cookie from the audio file that you want to play.
18. The size, in bytes, of the magic cookie.
19. Releases the memory that was allocated for the magic cookie.

You now ask the audio queue that you’ve created (in [Create a Playback Audio Queue](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tgnbtfvbuqmznknltk)) to prepare a set of audio queue buffers. Listing 3-15 demonstrates how to do this.

__Listing 3-15__  Allocating and priming audio queue buffers for playback

```
aqData.mCurrentPacket = 0;                                // 1

for (int i = 0; i < kNumberBuffers; ++i) {                // 2
    AudioQueueAllocateBuffer (                            // 3
        aqData.mQueue,                                    // 4
        aqData.bufferByteSize,                            // 5
        &aqData.mBuffers[i]                               // 6
    );

    HandleOutputBuffer (                                  // 7
        &aqData,                                          // 8
        aqData.mQueue,                                    // 9
        aqData.mBuffers[i]                                // 10
    );
}
```

Here’s how this code works:

1. Sets the packet index to `0`, so that when the audio queue callback starts filling buffers (step 7) it starts at the beginning of the audio file.
2. Allocates and primes a set of audio queue buffers. (You set this number, `kNumberBuffers`, to `3` in [Define a Custom Structure to Manage State](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tgnbtfvbuqmznknltcni).)
3. The `AudioQueueAllocateBuffer` function creates an audio queue buffer by allocating memory for it.
4. The audio queue that is allocating the audio queue buffer.
5. The size, in bytes, for the new audio queue buffer.
6. On output, adds the new audio queue buffer to the `mBuffers` array in the custom structure.
7. The `HandleOutputBuffer` function is the playback audio queue callback you wrote. See [Write a Playback Audio Queue Callback](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tgnbtfvbuqmznknlte).
8. The custom structure for the audio queue.
9. The audio queue whose callback you’re invoking.
10. The audio queue buffer that you’re passing to the audio queue callback.

Before you tell an audio queue to begin playing, you set its gain by way of the audio queue parameter mechanism. Listing 3-16 shows how to do this. For more on the parameter mechanism, see [Audio Queue Parameters](About%20Audio%20Queues.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tgnbtfvbuqnjnknltcni).

__Listing 3-16__  Setting an audio queue’s playback gain

```
Float32 gain = 1.0;                                       // 1
    // Optionally, allow user to override gain setting here
AudioQueueSetParameter (                                  // 2
    aqData.mQueue,                                        // 3
    kAudioQueueParam_Volume,                              // 4
    gain                                                  // 5
);
```

Here’s how this code works:

1. Sets a gain to use with the audio queue, between `0` (for silence) and `1` (for unity gain).
2. The `AudioQueueSetParameter` function sets the value of a parameter for an audio queue.
3. The audio queue that you are setting a parameter on.
4. The ID of the parameter you are setting. The `kAudioQueueParam_Volume` constant lets you set an audio queue’s gain.
5. The gain setting that you are applying to the audio queue.

All of the preceding code has led up to the process of playing a file. This includes starting an audio queue and maintaining a run loop while a file is playing, as shown in Listing 3-17.

__Listing 3-17__  Starting and running an audio queue

```
aqData.mIsRunning = true;                          // 1

AudioQueueStart (                                  // 2
    aqData.mQueue,                                 // 3
    NULL                                           // 4
);

do {                                               // 5
    CFRunLoopRunInMode (                           // 6
        kCFRunLoopDefaultMode,                     // 7
        0.25,                                      // 8
        false                                      // 9
    );
} while (aqData.mIsRunning);

CFRunLoopRunInMode (                               // 10
    kCFRunLoopDefaultMode,
    1,
    false
);
```

Here’s how this code works:

1. Sets a flag in the custom structure to indicate that the audio queue is running.
2. The `AudioQueueStart` function starts the audio queue, on its own thread.
3. The audio queue to start.
4. Uses `NULL` to indicate that the audio queue should start playing immediately.
5. Polls the custom structure’s `mIsRunning` field regularly to check if the audio queue has stopped.
6. The `CFRunLoopRunInMode` function runs the run loop that contains the audio queue’s thread.
7. Uses the default mode for the run loop.
8. Sets the run loop’s running time to `0.25` seconds.
9. Uses `false` to indicate that the run loop should continue for the full time specified.
10. After the audio queue has stopped, runs the run loop a bit longer to ensure that the audio queue buffer currently playing has time to finish.

When you’re finished playing a file, dispose of the audio queue, close the audio file, and free any remaining resources. Listing 3-18 illustrates these steps.

__Listing 3-18__  Cleaning up after playing an audio file

```
AudioQueueDispose (                            // 1
    aqData.mQueue,                             // 2
    true                                       // 3
);

AudioFileClose (aqData.mAudioFile);            // 4

free (aqData.mPacketDescs);                    // 5
```

Here’s how this code works:

1. The `AudioQueueDispose` function disposes of the audio queue and all of its resources, including its buffers.
2. The audio queue you want to dispose of.
3. Use `true` to dispose of the audio queue synchronously.
4. Closes the audio file that was played. The `AudioFileClose` function is declared in the `AudioFile.h` header file.
5. Releases the memory that was used to hold the packet descriptions.

[Next](Document%20Revision%20History.md)[Previous](Recording%20Audio.md)

