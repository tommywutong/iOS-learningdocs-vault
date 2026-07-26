---
title: 'Streaming MP3/AAC audio again | Cocoa with Love'
source: Cocoa with Love (Matt Gallagher)
source_key: cocoawithlove
source_url: 'https://www.cocoawithlove.com/2010/03/streaming-mp3aac-audio-again.html'
original_language: en
published: ''
status: frozen
license: All rights reserved（页脚明示）→ 严格私有
archived_at: 2026-07-26
content_hash: 'sha256:a474c7ceac789871'
translated: false
---

> 原文：[Streaming MP3/AAC audio again | Cocoa with Love](https://www.cocoawithlove.com/2010/03/streaming-mp3aac-audio-again.html)　·　Cocoa with Love (Matt Gallagher)

This week I present some further additions to AudioStreamer, a class I first presented in [Streaming and playing an MP3 stream](https://www.cocoawithlove.com/2008/09/streaming-and-playing-live-mp3-stream.html) and revisited with bug fixes in [Revisiting an old post: Streaming and playing an MP3 stream](https://www.cocoawithlove.com/2009/06/revisiting-old-post-streaming-and.html). This time, I'll add the two of the most requested features: seeking and HE-AAC audio support.

## Introduction

The `AudioFileStream` and `AudioQueue` APIs on the Mac and iPhone are useful but tricky. They are much lower level than `AVAudioPlayer` and `MPMoviePlayer` (iPhone) or `QTMovieView` (Mac) but are not as low level as the `AudioUnits` and `AUGraph`.

As the only Apple-provided way of streaming audio to the iPhone without a fullscreen movie player, these APIs are important.

> AudioStreamer
> 
> (you can also
> 
> browse the source code repository
> 
> ).

## HE-AAC

HE-AAC is actually very simple to use on the iPhone but I never took the time to add support for it to `AudioStreamer` before now because I had no personal need for it.

While it is simple to add, there is one complicating issue: the iPhone Simulator does not support HE-AAC. I'm sure this has confused a number of people who otherwise implemented HE-AAC correctly.

Enabling HE-AAC support for a file is as simple as sending the right `AudioStreamBasicDescription` to the `AudioQueueNewOutput` (which creates the playback queue).

```objc
err = AudioQueueNewOutput(&asbd, MyAudioQueueOutputCallback, self, NULL, NULL, 0, &audioQueue);
```

If `asbd.mFormatID == kAudioFormatMPEG4AAC_HE`, then the `AudioQueue` will parse the required SBR data.

Of course, there's some added trickiness in knowing whether a given AAC file contains SBR data.

We can get this information from our `AudioFileStream` when it notifies us that the `kAudioFileStreamProperty_FormatList` is available. This property contains the list of formats that the stream may be interpreted as.

```objc
if (inPropertyID == kAudioFileStreamProperty_FormatList)
{
    Boolean outWriteable;
    UInt32 formatListSize;

    // Get the size of the format list
    err = AudioFileStreamGetPropertyInfo(inAudioFileStream,
        kAudioFileStreamProperty_FormatList, &formatListSize, &outWriteable);
    if (err) { // handle error }
    
    // Get the list of formats itself
    AudioFormatListItem *formatList = malloc(formatListSize);
    err = AudioFileStreamGetProperty(inAudioFileStream, kAudioFileStreamProperty_FormatList, &formatListSize, formatList);
    if (err) { // handle error }

    // Look through the list of formats to find HE-AAC if present
    for (int i = 0;
        i * sizeof(AudioFormatListItem) < formatListSize;
        i += sizeof(AudioFormatListItem))
    {
        AudioStreamBasicDescription pasbd = formatList[i].mASBD;
        if (pasbd.mFormatID == kAudioFormatMPEG4AAC_HE)
        {
            // We've found HE-AAC, remember this to tell the audio queue
            // when we construct it.
#if !TARGET_IPHONE_SIMULATOR
            asbd = pasbd;
#endif
            break;
        }                                
    }
    free(formatList);
}
```

By default, we get the `AudioStreamBasicDescription` from the AudioFileStream's `kAudioFileStreamProperty_DataFormat`. This additional code changes to a different `AudioStreamBasicDescription` in the case of HE-AAC. Since HE-AAC is the only file format that works in this manner, it is the only special case that appears here.

## Seeking in an audio file downloaded via HTTP

Seeking requires three steps:

1. Know the duration of the file to seek within
2. Know where you can safely seek
3. Perform the seek itself

### Duration of the file

The first might seem easy but unfortunately, `AudioFileStream` does not give us the duration. We can get the nominal bitrate (only accurate for CBR data), byte counts, packet durations, packet counts and sample rates but none of these give the duration of the file unless you have an accurate bitrate, which we don't.

Instead, I've added a running average bitrate to AudioStreamer. Between `BitRateEstimationMinPackets` and `BitRateEstimationMaxPackets` (these constants are defined at the top of _AudioStreamer.m_), the bitrate is calculated from the packet sizes:

```objc
double averagePacketByteSize = processedPacketsSizeTotal / processedPacketsCount;
return 8.0 * averagePacketByteSize / packetDuration;
```

Unfortunately, since this average changes over time in all VBR streams, this means that the estimated duration of the file may change by 10% or so for the first 20-30 seconds of playback. In a proper application, you may want to consider an appropriate way to present or conceal this uncertainty for the user.

### Seek offset in bytes

The seek offset for a given time can be obtained from the file's duration and the bitrate.

However, it is not safe (particularly in an AAC) to seek to an arbitrary location. You must seek to a packet boundary.

If we want to seek to `newSeekTime` (a value in seconds), the initial guess at the byte offset for this time might look like this:

```objc
seekByteOffset = dataOffset + (newSeekTime / self.duration) * (fileLength - dataOffset);
```

In this calculation, `dataOffset` is the start of audio packets within the file, `fileLength` is the byte size of the whole file and `self.duration` is the duration in seconds (calculated from the average bitrate and `fileLength`.

Now we must round this to the nearest packet boundary.

```objc
double calculatedBitRate = [self calculatedBitRate];
if (packetDuration > 0 &&
    calculatedBitRate > 0)
{
    UInt32 ioFlags = 0;
    SInt64 packetAlignedByteOffset;
    SInt64 seekPacket = floor(newSeekTime / packetDuration);

    // Ask the file stream for the boundary for the appropriate packet
    err = AudioFileStreamSeek(
        audioFileStream, seekPacket, &packetAlignedByteOffset, &ioFlags);

    // Only use the boundary if it is NOT estimated
    // -- otherwise, stay with our first guess
    if (!err && !(ioFlags & kAudioFileStreamSeekFlag_OffsetIsEstimated))
    {
        seekTime -= ((seekByteOffset - dataOffset) - packetAlignedByteOffset) * 8.0
            / calculatedBitRate;
        seekByteOffset = packetAlignedByteOffset + dataOffset;
    }
}
```

Notice that we still need to add the `dataOffset` (the starting offset for audio packets in the stream) to the `packetAlignedByteOffset` to get a seek-safe byte offset. In my previous post, I mentioned that `AudioFileStreamSeek `wasn't working for me: it was because I wasn't adding this `dataOffset` (that you get from the `AudioFileStream`).

### Perform the seek

With the rounding to a packet boundary, the seek is now done at a byte-level on the HTTP connection itself. By this, I mean I close the existing `CFReadStreamRef` and reopen a new one with a new `CFHTTPMessageRef`. With `seekByteOffset` set to a non-zero value, my code for starting the HTTP connection now enters the following conditional:

```objc
if (fileLength > 0 && seekByteOffset > 0)
{
    // Set the byte range in the HTTP header for the request
    CFHTTPMessageSetHeaderFieldValue(message, CFSTR("Range"),
        (CFStringRef)[NSString stringWithFormat:
            @"bytes=%ld-%ld", seekByteOffset, fileLength]);

    // flag used to tell the AudioFileStream that I've skipped to a new
    // location when I next call AudioFileStreamParseBytes
    discontinuous = YES;
}
```

Obviously, integrating this required a little bit of massaging so that I could restart the HTTP connection without restarting the AudioFileStream or AudioQueue. I do stop the AudioQueue during seeking and restart it when the first new packet is ready to be queued.

## Limitations

### Different formats

I have tested this code with exactly 1 MP3 file, 1 AAC file and 1 HE-AAC file. There are thousands of variations of these formats which may still break the code. You will need to test your own files and ensure they work.

> If you get an error in
> 
> , set a breakpoint in
> 
> — all errors in AudioStreamer should go through this method so you should be able to look at the previous frame in the stack and see what line caused the error.

### Progressive download

This class does not cache anything to disk. If you want progressive download instead of live streaming, you'd need to save the data from the `CFReadStreamRef` or better yet, download the file separately and open the still-downloading file as a `CFReadStreamRef` and feed it into AudioStreamer.

### Multiple audio files at once

The iPhone can only decode 1 MP3 or AAC file at a time. That's a hardware limitation.

The Mac can decode as many as the CPU will allow. Go crazy.

### Metadata

There is still no support for ID3 metdata in `AudioStreamer`, since `AudioFileStream` does not support it.

If you absolutely need metadata from the file, then the only possible way to get it is to save all the data downloaded up until the first packet and use a different library (like FFmpeg's libavformat) to parse the metadata. It's not an easy task — if at all possible, it would be better to get the metadata another way.

## Conclusion

> AudioStreamer
> 
> (you can also
> 
> browse the source code repository
> 
> ).

While the code I've added this time is fairly brief, some of it is very hard to find elsewhere (I was unable to find anyone using `AudioFileStreamSeek` correctly anywhere).

My original goal with AudioStreamer was to handle live streams — MP3 sources without a beginning or an end — so seeking and HE-AAC files were not my priority. However, it appears that lots of people are using the `AudioStreamer` code as a starting point for their iPhone applications with fixed length files, so I've taken the time here to add the most requested features for these people.

None of these changes should affect files with indeterminate length which should continue to function as before.
