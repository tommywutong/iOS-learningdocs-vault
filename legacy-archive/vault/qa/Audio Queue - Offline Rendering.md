---
title: Audio Queue - Offline Rendering
apple_id: DTS40008247
resource_type: QA
platform: iOS
topic: Audio, Video, & Visual Effects
technology: AudioToolbox
published: '2013-01-02'
source_url: https://developer.apple.com/library/archive/qa/qa1562/_index.html
archived_at: '2026-07-18T02:32:18.414736Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1562

# Audio Queue - Offline Rendering

## Q:  Are there any guidelines I need to follow when attempting to render offline using Audio Queue?

A: Offline rendering with an audio queue output allows applications to render audio to a buffer instead of directly to an output device. This is especially useful with the iPhone OS, since the Audio Converter and Extended Audio File APIs do not currently (up to iPhone OS 2.2) support decompressing AAC, ALAC or MP3 encoded audio to LPCM if further processing is desired.

If you need to generate buffers of LPCM data from AAC, ALAC or MP3 encoded audio, using audio queue offline rendering is the recommended approach.

When setting up an audio queue output object for offline rendering, follow these few simple guidelines for successful use of the `AudioQueueOfflineRender` function.

When performing offline render an input buffer queue along with an output buffer is used.

The buffer queue used for input (pushing data into the audio queue), is the standard playback buffer queue as described in [The Playback Process](../documentation/Music%20Audio/Audio%20Queue%20Services%20Programming%20Guide/About%20Audio%20Queues.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tgnbtfvbuqnjnknltg) section of the [Audio Queue Services Programming Guide](https://developer.apple.com/library/archive/documentation/MusicAudio/Conceptual/AudioQueueProgrammingGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40005343-CH1).

Your `AudioQueueOutputCallback` function will receive an `AudioQueueBufferRef` to a free buffer from this input buffer queue; this is how input data is supplied to the audio queue output object. Buffer allocation is performed by calling `AudioQueueAllocateBuffer` with a buffer size calculated to represent some amount of input audio data based on the source audio format, generally between 16k and 64k.

__Listing 1__  Input buffer allocation.

```
AudioQueueAllocateBuffer(myInfo.mQueue, bufferByteSize, &myInfo.mBuffer);
```

The output buffer(s) is the destination buffer for the offline render operation (pulling data out of the audio queue). This is the `AudioQueueBufferRef` you pass to `AudioQueueOfflineRender`. Allocating one or more of these buffers is also done using `AudioQueueAllocateBuffer`.

The rule of thumb for output buffer size is to use a value which ensures you don't pull data out any faster than you push data in for render.

While you normally need multiple input buffers, one output buffer will almost always be sufficient.

__Listing 2__  Output buffer allocation.

```swift
/*
    Allocate the output (capture) buffer keeping it at half the size of the enqueue (input) buffer.
    This ensures we don't pull data out any faster than we can push data in for render,
    and keeps the Audio Queue Offline Render happy.
*/

const UInt32 captureBufferByteSize = bufferByteSize / 2;
AudioQueueBufferRef captureBuffer;
AudioBufferList captureABL;

AudioQueueAllocateBuffer(myInfo.mQueue, captureBufferByteSize, &captureBuffer);
captureABL.mNumberBuffers = 1;
captureABL.mBuffers[0].mData = captureBuffer->mAudioData;
captureABL.mBuffers[0].mNumberChannels = captureFormat.mChannelsPerFrame;
```


One of the current requirements for the offline render mechanism is a single initial call to `AudioQueueOfflineRender` asking for `0` frames. This should be done as soon as the audio queue has been started, in other words, immediately after calling `AudioQueueStart`.

__Listing 3__  Call `AudioQueueOfflineRender` once for 0 frames.

```
/*
    Lets start the queue - stop is called in the input buffer callback when there is no more data to read.
*/
AudioQueueStart(myInfo.mQueue, NULL);

AudioTimeStamp theTimeStamp;
theTimeStamp.mFlags = kAudioTimeStampSampleTimeValid;
theTimeStamp.mSampleTime = 0;

/*
    Important - We need to call this once asking for 0 frames!
*/
AudioQueueOfflineRender(myInfo.mQueue, &theTimeStamp, captureBuffer, 0);

...
```


Once `AudioQueueOfflineRender` has been called initially, you may then enqueue one or more input buffers with relatively large numbers of frames, for example 16K or greater. This is usually done by directly calling your `AudioQueueOutputCallback` function.

__Listing 4__  Initially enqueue input buffers

```
/*
    We need to enqueue a buffer after the queue has started.
*/
AQEnqueueBufferCallback(&myInfo, myInfo.mQueue, myInfo.mBuffer);

...
```


You can now call `AudioQueueOfflineRender` requesting a relatively small number of of output frames, generally between 4k and 8k.

Beyond the size of the input buffer pushes and the size of the output pulls, it matters how many input buffers are kept in the queue. In particular, you must take care not to pull (by calling `AudioQueueOfflineRender`) for more frames than you have pushed via the `AudioQueueEnqueueBuffer` function. You may also want to keep track of how many frames you expect to decode so that you know when to stop calling `AudioQueueOfflineRender`.

The rule is if at any given time you have pushed N number of frames, you __must not__ pull for more than N number of frames.

__Listing 5__  Rendering output.

```swift
/* Start Rendering Offline */
while (true) {
    UInt32 reqFrames = captureBufferByteSize / captureFormat.mBytesPerFrame;

    AudioQueueOfflineRender(myInfo.mQueue, &theTimeStamp, captureBuffer, reqFrames);

    captureABL.mBuffers[0].mData = captureBuffer->mAudioData;
    captureABL.mBuffers[0].mDataByteSize = captureBuffer->mAudioDataByteSize;

    UInt32 writeFrames = captureABL.mBuffers[0].mDataByteSize / captureFormat.mBytesPerFrame;

    /* We may not get any frames so check this here - are we done? */
    if (writeFrames == 0) break;

    /* Do Something With The Returned Audio Data - Maybe Write it to a file, ok let's do that. */
    ExtAudioFileWrite(captureFile, writeFrames, &captureABL);

    /* This flag ensures that the Audio Queue was flushed by a call to AudioQueueFlush in the
       AudioQueueOutputCallback just before the call to AudioQueueStop and ensures we get all the data out.
       If the queue has been flushed we are done. */
    if (myInfo.mFlushed) break;

    theTimeStamp.mSampleTime += writeFrames;
}
```


Setup for audio queue offline rendering is very similar to how you would normally set up an audio queue output object for playback. Keep buffer allocation in mind and make sure to call `AudioQueueOfflineRender` asking for `0` frames immediately after the call to `AudioQueueStart`. Never pull for more data than you have pushed into the queue and call `AudioQueueFlush` before `AudioQueueStop` to ensure you get all the data out.


```
main:
    AudioQueueNewOutput
    AudioQueueSetProperty(kAudioQueueProperty_MagicCookie) // as required
    AudioQueueSetProperty(kAudioQueueProperty_ChannelLayout) // as required
    AudioQueueAllocateBuffer    // input buffer(s)
    AudioQueueSetOfflineRenderFormat
    AudioQueueAllocateBuffer    // output buffer
    AudioQueueStart
    AudioQueueOfflineRender(0) // mandatory call asking for 0 frames
    myAQEnqueueBufferCallback  // enqueue some input buffers

    loop:
        AudioQueueOfflineRender(n)
        ...

AudioQueueOutputCallback function:
    myAQEnqueueBufferCallback
```

See the aqrender.cpp file for further reference.

[Audio Queue Services Programming Guide](https://developer.apple.com/library/archive/documentation/MusicAudio/Conceptual/AudioQueueProgrammingGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40005343-CH1)

- aqrender.cpp ("qa1562_aqrender.zip", 6.2K)

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2013-01-02 | Editorial |
| 2009-02-13 | New document that describes how to set up the Audio Queue for Offline Rendering |

