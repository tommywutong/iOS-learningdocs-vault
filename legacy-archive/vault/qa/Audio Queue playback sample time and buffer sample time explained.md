---
title: Audio Queue playback sample time and buffer sample time explained
apple_id: DTS40010356
resource_type: QA
platform: iOS|macOS
topic: Audio, Video, & Visual Effects
technology: AudioToolbox
published: '2010-09-20'
source_url: https://developer.apple.com/library/archive/qa/qa1718/_index.html
archived_at: '2026-07-18T02:34:27.385355Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1718

# Audio Queue playback sample time and buffer sample time explained

## Q:  Can you explain how the timeline an audio queue object is using relates to a buffer being queued for playback at a given time?

A: Can you explain how the timeline an audio queue object is using relates to a buffer being queued for playback at a given time?

An audio queue object uses what is referred to as the playback timeline, this is __the number of samples that have elapsed since the audio queue was started__. When an audio queue object is first started, the playback timeline value is always 0.

To understand how the audio queue timeline relates to the buffers being queued, let's imagine a simple scenario using a single audio buffer containing 10,000 samples. An application enqueues this buffer and starts an audio queue. As the queue plays the buffer a first time, the audio queue timeline value directly reflects where the audio queue object is in relation to the audio buffer being played. For example, if the queue is halfway though the buffer, the audio queue timeline value is 5,000 because the queue would be at sample 5,000 in the buffer.

As the queue continues to play, the application enqueues the buffer a second time via the `AudioQueueOutputCallback` callback. The audio queue timeline continues to increment. The timeline for example, may now have a value of 15,000, indicating it is halfway though the second enqueued buffer of 10,000 samples and therefore is at sample 5,000 in the second audio buffer.

Let's now assume the `AudioQueueOutputCallback` is invoked again but this time the application would like to wait 100,000 samples before having the audio buffer play again, creating a gap in the playback. To do so you must use the `AudioQueueEnqueueBufferWithParameters` function with a `AudioTimeStamp` value of 120,000 provided for the `inStartTime` parameter.

Where does the sample time of 120,000 come from?

- 10,000 - Duration of the first buffer.
- + 10,000 - Duration of the second buffer.
- + 100,000 - Gap the application wanted.
- = 120,000 - Audio queue timeline value at this moment in the queue.

This works because the audio queue is still playing and still incrementing the playback timeline, but won't actually play the enqueued buffer until the "playback head" gets to the sample time that was provided when enqueuing the buffer (120,000). When the audio queue reaches this sample time, it plays the first sample (0) of the new 10,000 sample audio buffer. When the audio queue playback timeline value reaches 125,000 it is once again halfway (5,000 samples) through the audio buffer.

Applications may also pass trimming parameters such as `inTrimFramesAtStart` to the `AudioQueueEnqueueBufferWithParameters` function, further controlling playback. The `inTrimFramesAtStart` parameter tells the audio queue to trim a specific amount of samples off the beginning of the audio buffer that is being enqueued. To trim samples off the end of a buffer, use the `inTrimFramesAtEnd` parameter instead. Both parameters may also be used together.

Let's assume that the next time the `AudioQueueOutputCallback` callback is invoked the applications wants to skip over the first 5,000 samples in the audio buffer. It would use the `AudioQueueEnqueueBufferWithParameters` function with the `inStartTime` parameter set to `NULL`. This tell the audio queue object to play back the buffer immediately after the previous buffer finishes. The application would also provide the value of 5,000 for the `inTrimFramesAtStart` parameter, informing the audio queue to not play the first 5,000 samples in the buffer.

This invocation of the `AudioQueueEnqueueBufferWithParameters` function changes the buffer sample duration for the enqueuing operation. The 10,000 sample audio buffer is now effectively trimmed to 5,000 samples. The buffer plays back immediately from the trimmed offset from the start of the audio buffer as soon as the audio queue finishes playing the previously enqueued buffer. There is no gap.

What will the audio queue's timeline value be after this trimmed buffer is played?

- 120,000 - Our previous queue timeline value.
- + 10,000 - Previous queued buffer with the gap before it.
- + 5,000 - Duration of the trimmed buffer.
- = 135,000 - Sample time at this moment in the queue.

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2010-09-20 | New document that describes how the audio queue playback sample time relates to an enqueued buffers sample time and discusses AudioQueueEnqueueBufferWithParameters. |

