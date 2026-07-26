---
title: 'Revisiting an old post: Streaming and playing an MP3 stream | Cocoa with Love'
source: Cocoa with Love (Matt Gallagher)
source_key: cocoawithlove
source_url: 'https://www.cocoawithlove.com/2009/06/revisiting-old-post-streaming-and.html'
original_language: en
published: ''
status: frozen
license: All rights reserved（页脚明示）→ 严格私有
archived_at: 2026-07-26
content_hash: 'sha256:c2b04e2f31181f1a'
translated: false
---

> 原文：[Revisiting an old post: Streaming and playing an MP3 stream | Cocoa with Love](https://www.cocoawithlove.com/2009/06/revisiting-old-post-streaming-and.html)　·　Cocoa with Love (Matt Gallagher)

Given the attention it received and the number of bugs I know it contained, I wanted to revisit an old post of mine: Streaming and playing an MP3 stream. In this post, I'll talk about the problems the original contained, how I fixed those problems and I'll present the updated result.

## Introduction

Last September, I wrote a post titled "[Streaming and playing an MP3 stream](https://www.cocoawithlove.com/2008/09/streaming-and-playing-live-mp3-stream.html)". The post was largely an experiment — I just wanted to see if I could play a streaming MP3 by quickly adapting Apple's AudioFileStreamExample to accept an HTTP data stream.

Unexpectedly, the post became one of my most popular. The attention quickly revealed the limitations in my approach:

- The blend of Objective-C and C was muddled and led to a situation where neither were being used cleanly.
- The boolean flags I copied from the original example were a bad way to describe the playback state and lots of situations were not covered by these flags.
- Sending notifications to the user-interface on a thread that isn't the main thread causes problems.
- The extra thread I added (the download thread) was never thread-safe.

I've finally decided to take the time to present a solution to these issues and present an approach which is a little more robust and a little easier to extend if needed.

> AudioStreamer project as a zip file
> 
> (around 110kB) which contains Xcode projects for both iPhone and Mac OS. You can also
> 
> browse the source code repository
> 
> .

## Limited scope

One point should be clarified before I continue: this class is intended for _streaming_ audio. By streaming, I don't simply mean "an audio file transferred over HTTP". Instead, I mean a continuous HTTP source without an end that continues indefinitely (like a radio station, not a single song).

Yes, this class will handle fixed-length files transferred over HTTP but it is not ideal for the task.

This class does not handle:

1. Buffering of data to a file
2. Seeking within downloaded data
3. Feedback about the total length of the file
4. Parsing of ID3 metadata

These things often can't be done on streaming data, so this class doesn't try. See the "Adding other functionality" section for hints about how the class could be reorganised to handle some of these features.

## Taking code out of C functions

Since I had borrowed the `AudioFileStream` and `AudioQueue` callback functions from Apple's example, they were Standard C.

My first change was to make these 6 callback functions (7 including the `CFReadStream` callback) little more than wrappers around Objective-C methods:

```objc
void MyPacketsProc(
    void *inClientData,
    UInt32 inNumberBytes,
    UInt32 inNumberPackets,
    const void *inInputData,
    AudioStreamPacketDescription *inPacketDescriptions)
{
    // this is called by audio file stream when it finds packets of audio
    AudioStreamer* streamer = (AudioStreamer *)inClientData;
    [streamer
        handleAudioPackets:inInputData
        numberBytes:inNumberBytes
        numberPackets:inNumberPackets
        packetDescriptions:inPacketDescriptions];
}
```

At a compiled code level, this is a step backwards: all I've done is slowed the program down by an extra Objective-C message send.

Technically, a C function that takes a "context" pointer (like the `inClientData` pointer here) is not significantly different to a method. What a method does is makes data hiding and data abstracted actions easier. Within a method, you can easily access the instance variables of an object and you don't need to explicitly pass context into each function.

This is the cliché argument in favor of object-orientation — but it isn't why I reorganized these functions and methods.

The honest reason why I did it is aesthetics: it is easier to read a class that is implemented using Objective-C methods alone — it's more consistent. I chose to move towards an Objective-C aesthetic and away from the Standard C aesthetic of the CoreAudio sample code to promote consistent formatting, consistent means of accessing state variables, consistent ways of invoking methods and consistent ways of synchronizing access to the class.

## Describing state

With the majority of code now inside the class, I was in a better position to start handling changes through methods rather than direct member access.

My original approach to state came from Apple's original example. This example had just one piece of state: a `bool` named `finished` (which indicated that the run loop should exit).

The problem with this flag is how simple it is. It is unable to distinguish between the following:

1. End of file, normal automatic stop.
2. to stop but the

  thread has not yet responded.
3. thread is created and we must exit.
4. for temporary reasons (clearing it, changing device, seeking to a new point) but we don't want the loop to stop.

For Apple's example, there was no problem: the first case was the only one that ever occurred.

As a hasty solution, I had added `started` and `failed` flags but these really only covered the first and third case adequately.

In the end, I realized that the `AudioStreamer` needed much more descriptive state where every combination of progress within each thread had a different position:

```objc
typedef enum
{
    AS_INITIALIZED = 0,
    AS_STARTING_FILE_THREAD,
    AS_WAITING_FOR_DATA,
    AS_WAITING_FOR_QUEUE_TO_START,
    AS_PLAYING,
    AS_BUFFERING,
    AS_STOPPING,
    AS_STOPPED,
    AS_PAUSED
} AudioStreamerState;
```

and when stopping, one of the following values would also be needed:

```objc
typedef enum
{
    AS_NO_STOP = 0,
    AS_STOPPING_EOF,
    AS_STOPPING_USER_ACTION,
    AS_STOPPING_ERROR,
    AS_STOPPING_TEMPORARILY
} AudioStreamerStopReason;
```

In this way, the state always describes where every thread is and the stop reason explains why a transition is occurring.

Combining this with an error code that replaces the old `failed` flag, I now have a complete desription of the state.

By cleaning up the state of the object, I was able to make the object capable of state transitions that weren't previously possible including pausing/unpausing and returning to the `AS_INITIALIZED` state after a stop (instead of requiring that the class be released after stopping).

## Notifications

In the old version of the project the only way for the user-interface to follow the playback state was to observe the `isPlaying` property on the object which reflected the `kAudioQueueProperty_IsRunning` property of the AudioQueue.

This observing was handled through KeyValueObserving. I'm a big fan of KeyValueObserving for its simplicity and ubiquity but this was not the correct place to use it.

KeyValueObserving always invokes the observer methods in the same thread as the change. Since all changes in AudioStreamer happen in secondary threads, this means that the observer methods were getting invoked in secondary threads.

Why is this bad? A minor drawback is simply the unexpectedness for the observer but the biggest reason was that the sole purpose of observing this property was to update the user-interface and the user-interface on the iPhone cannot be updated from any thread except the main thread. Even on the Mac, performing updates off the main thread can have unexpected and glitchy results.

The solution is to retain the `NSNotificationCenter` of the thread that first calls `start` on the object and use this center to send messages as follows:

```objc
NSNotification *notification =
    [NSNotification
        notificationWithName:ASStatusChangedNotification
        object:self];
[notificationCenter
    performSelector:@selector(postNotification:)
    onThread:[NSThread mainThread]
    withObject:notification
    waitUntilDone:NO];
```

Don't invoke `postNotification:` directly from the secondary thread as, like most methods, it is not thread safe and it could be in use from the main thread.

## Thread safety

Despite adding an extra thread on top of Apple's AudioFileStreamExample, I never really spent any time thinking about thread safety — a reckless approach to stability. In my defence Apple's example wasn't exactly cautious with its threads and would quit while the `AudioQueue`'s thread was still playing the last buffer.

The most efficient approach to threading is to carefully enter `@synchronized` (or `NSLock` or `pthread_mutex_lock`) in a tight region around any use of a shared variable.

Unfortunately for the `AudioStreamer` class, almost everything in the class is shared. Instead, I decided to go for the decidedly less efficient approach of running almost everything in the class within a `@synchronized` section, emerging only at points when control must be yielded to other threads.

The drawback is that the code rarely runs simultaneously on multiple threads (although threading here is for blocking and I/O, not for multi-threaded performance reasons so that's not a probem). The advantage with this heavy-handed locking approach is that the only threading condition that may cause problems are deadlocks.

When do deadlocks occurs? Only when you're waiting for another thread to do something while you're inside the synchronized section needed by that other thread. The simple solution: never wait for another thread inside a synchronized section.

`AudioStreamer` has three situations where 1 thread waits for another:

1. thread waits for any kind of control communication from the main thread or playback finished notification from the

  thread).
2. method (

  thread waits for the

  thread to free up a buffer).
3. invocations (waits for the

  to release all buffers).

The first two points are easy: perform these actions (any any method invocation which invokes them) outside of the `@synchronized` section.

The final point is harder: the synchronous stop must be performed inside the `@synchronized` section to prevent multiple `AudioQueueStop` actions occurring at once. To address this, the release of buffers by the `AudioQueue` (in `handleBufferCompleteForQueue:buffer:`) must perform its work without entering the `@synchronized` section (although it's allowed to use the `queueBuffersMutex` as normal since that isn't used by anything else during a synchronous stop).

Of course, every time the `@sychronized` section is re-entered, a check must be performed to see if "control communication" has occurred (the class checks this by invoking the `isFinishing` method and exiting if it returns `YES`).

## Adding other functionality

### Get metadata

The easiest source of metadata comes from the HTTP headers. Inside the `handleReadFromStream:eventType:` method, use `CFReadStreamCopyProperty` to copy the `kCFStreamPropertyHTTPResponseHeader` property from the `CFReadStreamRef`, then you can use `CFHTTPMessageCopyAllHeaderFields` to copy the header fields out of the response. For many streaming audio servers, the stream name is one of these fields.

The considerably harder source of metadata are the ID3 tags. ID3v1 is always at the end of the file (so is useless when streaming). ID3v2 is located at the start so may be more accessible.

I've never read the ID3 tags but I suspect that if you cache the first few hundred kilobytes of the file somewhere as it loads, open that cache with `AudioFileOpenWithCallbacks` and then read the `kAudioFilePropertyID3Tag` with `AudioFileGetProperty` you may be able to read the ID3 data (if it exists). Like I said though: I've never actually done this so I don't know for certain that it would work.

### Stream fixed-length files

The biggest variation you may want to make to the class is to download fixed-length files, rather than streaming audio.

To handle this, the best approach is to remove the download from the class entirely. Download elsewhere and when "enough" (an amount you should determine on your own) of the file is downloaded, start a variation of the class that plays by streaming from a file on disk.

To adapt the class for streaming from a file on disk, remove the `CFHTTPMessageRef` and `CFReadStreamRef` code from `openFileStream` and replace it with `NSFileHandle` code that uses `waitForDataInBackgroundAndNotify` to asynchronously stream the file in the same way that `CFReadStreamRef` streamed the network data.

Once you're streaming from a file, you'll probably want to permit seeking within the file. I've already put hooks within the file to seek (set the `seekNeeded` flag to true and set the `seekTime` to the time in seconds to which you want to seek) — however, the mechanics of seeking within the file would be dependent on how you access the file.

Incidentally, the `AudioFileStreamSeek` function seems completely broken. If you can't get it to work (as I couldn't) just seek to a new point in the file, set `discontinuous` to `true` and let `AudioFileStream` deal with it.

### Handling data interruptions

At the moment, if the `AudioQueue` has no more buffers to play, the state will transition to `AS_BUFFERING`. At this point, no specific action is taken to resolve this situation — it assumes that the network will eventually resume and requeue enough buffers.

I actually expect there will be cases where this action is insufficient — you may need to ensure that the `AudioQueue` is paused until enough buffers are filled before resuming or even restart the download entirely. I haven't experimented much since it is easiest with streaming audio just to stop and start new.

Incidentally, if you're curious to know how many audio buffers are in use at any given time, uncomment the `NSLog` line in the `handleBufferCompleteForQueue:buffer:` method. This will log how many 1 kilobyte audio buffers are queued waiting for playback (when the queue reaches zero, the `AudioStreamer` enters the `AS_BUFFERING` state).

## Conclusion

> AudioStreamer project as a zip file
> 
> (around 110kB) which contains Xcode projects for both iPhone and Mac OS. You can also
> 
> browse the source code repository
> 
> .

The functionality of this new version has not changed greatly — my purposed was to present a version that is more stable and tolerant of unexpected situations, rather than add new features.

As before, the AudioStreamer class should work on Mac OS X 10.5 and on the iPhone (SDK 2.0 and greater).

The source repository is hosted on github so you can browse, fork or track updates as you choose. I will likely update again in future (I can't imagine I've written this much code without causing more problems) and this way, you can see the changes I've made.

I hope this post has shown you a number of problems that can happen when code is written hastily. This doesn't mean you should always avoid hastily written code (timeliness and proof of concepts are important) but it does mean you should be practised at refactoring code and not simply slap poor fixes onto code that doesn't cleanly solve a problem in the first place.
