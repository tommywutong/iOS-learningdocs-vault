---
title: Audio Queue - Looping Compressed Audio
apple_id: DTS40008277
resource_type: QA
platform: iOS|macOS
topic: Audio, Video, & Visual Effects
technology: AudioToolbox
published: '2013-08-09'
source_url: https://developer.apple.com/library/archive/qa/qa1636/_index.html
archived_at: '2026-07-18T02:33:02.738418Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1636

# Audio Queue - Looping Compressed Audio

## Q:  How do I seamlessly loop AAC compressed audio using Audio Queue?

A: Summary

Seamlessly looping a compressed audio file requires three pieces of information related to how the audio media was compressed:

1. The number of silent sample frames (known as priming frames) added to the front of the encoded audio data.
2. The number of padding samples frames (known as remainder frames) added to the end of the encoded audio data.
3. The audio data packet count indicating the total number of audio data packets contained in the file.

Use `AudioQueueEnqueueBufferWithParameters` to enqueue all of the packets you have to the audio queue, trim off the priming sample frames from the start, trim off remainder sample frames from the last packet and reset the current packet count to start reading data from the beginning of the file creating the loop.

To analyze what this information looks like in a compressed audio file create an AAC encoded [Apple Core Audio Format](../documentation/Music%20Audio/Apple%20Core%20Audio%20Format%20Specification%201.0.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytqnrsfvbuqmrqgmwviucykjcummjqge) (.caf) file with `afconvert`, then use `afinfo` to print out some details about the file.


```shell
% afconvert -d aac -f caff /System/Library/Sounds/Submarine.aiff /tmp/output.caf

% afinfo /tmp/output.caf

File: /tmp/output.caf
File type ID: caff
Data format: 2 ch,  44100 Hz, 'aac ' (0x00000000) 0 bits/channel, 0 bytes/packet, 1024 frames/packet, 0 bytes/frame
                no channel layout.
estimated duration: 0.975 sec
audio bytes: 10541
audio packets: 45
audio 42998 valid frames + 2112 priming + 970 remainder = 46080
```

What do the numbers mean?

- To encode the `Submarine.aiff` file using AAC requires 45 Audio Packets. This is the Audio Data Packet Count.
- These 45 Audio Packets contain 1024 frames per packet which is 46080 sample frames long (45 \* 1024 = 46080).
- The first 2112 sample frames are silence. These silent sample frames are the encoder priming frames; Essentially empty AAC packets and packets containing information used to correctly decode the first samples.
- The last Audio Packet has 970 remainder sample frames of silence added to it, rounding up the Audio Packet size to 1024. In other words, of the 1024 sample frames represented in the last packet, only 54 sample frames are actually valid samples we want to decode (1024 - 970 = 54).

Now that we know the encoder latencies and padding, we can completely understand (and represent in the file) these pads and therefore derive the actual number of samples in the bitstream.

If you take the total number of samples (46080), subtract the priming and padding sample frames (2112 and 970 respectively) you are left with 42998 valid samples (46080 - 2112 - 970 = 42998). You can confirm that 42998 is the original length of `Submarine.aiff` by using `afinfo` again.


```
% afinfo /System/Library/Sounds/Submarine.aiff

File: /System/Library/Sounds/Submarine.aiff
File type ID: AIFF
Data format: 2 ch,  44100 Hz, 'lpcm' (0x0000000E) 16-bit big-endian signed integer
                no channel layout.
estimated duration: 0.975 sec
audio bytes: 171992
audio packets: 42998
```

Once you have the accurate number of priming and remainder frames along with the packet count for the encoded bitstream, and keep this information in mind when enqueuing buffers, gapless looping with the Audio Queue becomes a fairly straight forward endeavor.

To decode the above AAC compressed bitstream and get the same number of samples out; Enqueue all of the packets you have to the audio queue, trim off 2112 sample frames from the start, trim off 970 sample frames from the last packet and you will have completely decoded the compressed bitstream accurately to the last sample. Once you've enqueued all of the packets, reset your current packet count and start again thereby looping the audio.

With all the numbers out of the way and since we now know about priming frames, remainder frames and packet count -- where do we get these values from?

Retrieve the Priming Frames and Remainder Frames values by calling `AudioFileGetProperty` asking for the `kAudioFilePropertyPacketTableInfo` property as shown in Listing 1. Store them away for use in the output callback.


```
<AudioToolbox/AudioFile.h>

/*!
    @struct     AudioFilePacketTableInfo
    @abstract   This contains information about the number of valid frames in a file and where they begin and
                end.
    @discussion Some data formats may have packets whose contents are not completely valid, but represent
                priming or remainder frames that are not meant to be played. For example a file with 100
                packets of AAC is nominally 1024 * 100 = 102400 frames of data. However the first 2112 frames
                of that may be priming frames and there may be some number of remainder frames added to pad
                out to a full packet of 1024 frames. The priming and remainder frames should be discarded. The
                total number of packets in the file times the frames per packet (or counting each packet's
                frames individually for a variable frames per packet format) minus mPrimingFrames, minus
                mRemainderFrames, should equal mNumberValidFrames.
    @field      mNumberValidFrames the number of valid frames in the file.
    @field      mPrimingFrames the number of invalid frames at the beginning of the file.
    @field      mRemainderFrames the number of invalid frames at the end of the file.
*/
struct AudioFilePacketTableInfo
{
        SInt64  mNumberValidFrames;
        SInt32  mPrimingFrames;
        SInt32  mRemainderFrames;
};
typedef struct AudioFilePacketTableInfo AudioFilePacketTableInfo;
```


__Listing 1__

```swift
AudioFilePacketTableInfo thePacketTableInfo;

UInt32 size = sizeof(thePacketTableInfo);
AudioFileGetProperty(myAudioFileID, kAudioFilePropertyPacketTableInfo, &size, &thePacketTableInfo);

myAudioLooper->mPrimingFrames = thePacketTableInfo.mPrimingFrames;
myAudioLooper->mRemainderFrames = thePacketTableInfo.mRemainderFrames;
```


As mentioned, knowing when to loop the file requires retrieving how many total packets are in the file. Retrieve this value from the audio file by calling `AudioFileGetProperty` asking for the `kAudioFileStreamProperty_AudioDataPacketCount`  property as shown in Listing 2.

The Audio Data Packet Count is a `UInt64` value indicating the number of packets of audio data in the file. Store this away for use in the output callback.

__Listing 2__

```swift
UInt32 size = sizeof(myAudioLooper->mAudioFilePacketCount);

AudioFileGetProperty(myAudioFileID, kAudioFileStreamProperty_AudioDataPacketCount,
                                    &size, &myAudioLooper->mAudioFilePacketCount);
```


Enqueuing is done using the `AudioQueueEnqueueBufferWithParameters` API which conveniently provides trimming capability. Use the priming frames value for the `inTrimFramesAtStart` parameter as required and use the remainder frames value for the `inTrimFramesAtEnd` parameter as required.


```
AudioQueueEnqueueBufferWithParameters(AudioQueueRef                        inAQ,
                                      AudioQueueBufferRef                  inBuffer,
                                      UInt32                               inNumPacketDescs,
                                      const AudioStreamPacketDescription * inPacketDescs,
                                      UInt32                               inTrimFramesAtStart,
                                      UInt32                               inTrimFramesAtEnd,
                                      UInt32                               inNumParamValues,
                                      const AudioQueueParameterEvent *     inParamValues,
                                      const AudioTimeStamp *               inStartTime,
                                      AudioTimeStamp *                     outActualStartTime)

Assigns a buffer to an audio queue for playback, providing parameters and start time information.

You can exert some control of the buffer queue by using this function. You can assign audio queue settings that are in effect carried by an audio queue buffer as you enqueue it. Hence, these changes only take effect when an audio queue buffer begins playing.

This function queues a buffer for playback only, not for recording. Audio queues for recording have no parameters, do not support variable-bit-rate (VBR) formats (which might require trimming), and have a different way to handle timing. When queued for playback, the buffer must contain the audio data to be played back. See AudioQueueEnqueueBuffer for details on queuing a buffer for recording.

Parameters:

inAQ - The audio queue associated with the buffer.

inBuffer - The buffer to be played from.

inNumPacketDescs - The number of packet descriptions pointed to by the inPacketDescs parameter. Required only
                   for variable-bit-rate (VBR) audio formats. Pass 0 if no packet descriptions are required.

inPacketDescs - A pointer to an array of audio stream packet descriptions. Required only for VBR audio
                formats. Pass NULL if no packet descriptions are required.

inTrimFramesAtStart - The number of priming frames to skip at the start of the buffer.

inTrimFramesAtEnd - The number of frames to skip at the end of the buffer.

inNumParamValues - The number of parameter values pointed to by the inParamValues parameter.

inParamValues - An array of parameter values(In Mac OS X v10.5, there is only one parameter,
                kAudioQueueParam_Volume.) These values are set before buffer playback and cannot be
                changed while the buffer is playing. How accurately changes in parameters can be
                scheduled depends on the size of the buffer. If there are no parameters to set
                (inNumParamValues = 0), pass NULL.

inStartTime - A pointer to a structure containing the desired start time for playing the buffer. If
               you specify the time using the mSampleTime field of the AudioTimeStamp structure, the
               sample time is relative to the time the queue started. If you pass NULL for the start
               time, the buffer starts immediately after the previously queued buffer, or as soon as
               possible if no buffers are queued ahead of it. Buffers are played in the order they are
               queued. If multiple buffers are queued, their times must be in ascending order or NULL;
               otherwise, an error occurs. The start time indicates when the actual audio data in the
               buffer is to be played (that is, the trim frames are not counted).

outActualStartTime - On return, points to an AudioTimeStamp structure indicating when the buffer will
                     actually play.
```


Put it all together in the Audio Queue Output Callback. Also called a playback buffer callback, this function is invoked when the audio queue has finished with the data to be played and a buffer is available to the application for reuse. Applications generally immediately refill and enqueue the completed buffer at this time.

Respect the trimming information and reset the packet count to loop the audio.

__Listing 3__  Example Of A Looping Output Callback

```swift
void AQLooper::AQBufferCallback(void *inUserData, AudioQueueRef inAQ, AudioQueueBufferRef inCompleteAQBuffer)
{
    AQLooper *THIS = (AQLooper *)inUserData;

    if (THIS->mIsDone) return;

    UInt32 numBytes;
    UInt32 nPackets = THIS->GetNumPacketsToRead(); // generally enough for a half second of audio based on the
                                                   // format -- see CalculateBytesForTime() from aqplay.cpp

    OSStatus result = AudioFileReadPackets(THIS->GetAudioFileID(),
                                           false,
                                           &numBytes,
                                           inCompleteAQBuffer->mPacketDescriptions,
                                           THIS->GetCurrentPacket(),
                                           &nPackets,
                                           inCompleteAQBuffer->mAudioData);
    if (result) printf("AudioFileReadPackets failed: %d", result);

    if (nPackets > 0) {
        UInt32 trimFramesAtStart = 0;
        UInt32 trimFramesAtEnd = 0;

        inCompleteAQBuffer->mAudioDataByteSize = numBytes;
        inCompleteAQBuffer->mPacketDescriptionCount = nPackets;

        if (THIS->mCurrentPacket == 0) {
            // at the beginning -- need to trim priming frames
            trimFramesAtStart = THIS->mPrimingFrames;
        }

        THIS->mCurrentPacket = (THIS->GetCurrentPacket() + nPackets);

        if (THIS->mCurrentPacket == THIS->mAudioFilePacketCount) {
            // at the end -- need to trim remainder frames
            inTrimFramesAtEnd = THIS->mRemainderFrames;

            // reset read from the beginning again
            THIS->mCurrentPacket = 0;
        }

        result = AudioQueueEnqueueBufferWithParameters(inAQ,
                                                       inCompleteAQBuffer,
                                                       0,
                                                       NULL,
                                                       trimFramesAtStart,
                                                       trimFramesAtEnd,
                                                       0, NULL, NULL, NULL);
        if (result) printf("AudioQueueEnqueueBufferWithParameters failed: %d", result);
    }
}
```


- [Audio Queue Programming Guide](https://developer.apple.com/library/archive/documentation/MusicAudio/Conceptual/AudioQueueProgrammingGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40005343-CH1)
- _[Audio Queue Services Reference](https://developer.apple.com/documentation/audiotoolbox/audio_queue_services)_
- _[Audio File Services Reference](https://developer.apple.com/documentation/audiotoolbox/audio_file_services)_
- [Apple Core Audio Format](../documentation/Music%20Audio/Apple%20Core%20Audio%20Format%20Specification%201.0.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytqnrsfvbuqmrqgmwviucykjcummjqge)
- _[Creating Core Audio Format (.caf) Files](https://developer.apple.com/library/archive/qa/qa1534/_index.html#//apple_ref/doc/uid/DTS40008152)_

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2013-08-09 | Editorial |
| 2009-02-20 | New document that discusses the format information required to seamlessly loop compressed audio using Audio Queue. |

