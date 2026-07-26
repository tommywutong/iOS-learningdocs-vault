---
title: 'AVSampleBufferAudioRenderer.Receiver.SuggestedFlushReason.wasFlushedAutomatically(at:)'
framework: AVFoundation
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta, watchOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: '/documentation/avfoundation/avsamplebufferaudiorenderer/receiver/suggestedflushreason/wasflushedautomatically(at:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avsamplebufferaudiorenderer/receiver/suggestedflushreason/wasflushedautomatically(at:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avsamplebufferaudiorenderer/receiver/suggestedflushreason/wasflushedautomatically%28at%3A%29.json'
content_hash: 'sha256:b7ed57a0d89162ac'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [AVFoundation](../../../../avfoundation.md) · [AVSampleBufferAudioRenderer](../../../avsamplebufferaudiorenderer.md) · [Receiver](../../receiver.md) · [SuggestedFlushReason](../suggestedflushreason.md)

# AVSampleBufferAudioRenderer.Receiver.SuggestedFlushReason.wasFlushedAutomatically(at:)

<sub>Case</sub>

The enqueued media data has been flushed for a reason other than a call to the `flush()` method.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case wasFlushedAutomatically(at: CMTime)
```

## Discussion

The renderer may flush enqueued media data when the user routes playback to a new destination.  The renderer may also flush enqueued media data when the playback rate of the attached render synchronizer is changed (e.g. 1.0 -\> 2.0 or 1.0 -\> 0.0 -\> 2.0), however no flush will occur for normal pauses (non-zero -\> 0.0) and resumes (0.0 -\> same non-zero rate as before).

When an automatic flush occurs, the attached render synchronizer’s timebase will remain running at its current rate.  It is typically best to respond to this event by enqueueing media data with timestamps starting at the timebase’s current time.  To the listener, this will sound similar to muting the audio for a short period of time.  If it is more desirable to ensure that all audio is played than to keep the timeline moving, you may also stop the synchronizer, set the synchronizer’s current time to the associated CMTime value of this event, start reenqueueing sample buffers with timestamps starting at that time, and restart the synchronizer.  To the listener, this will sound similar to pausing the audio for a short period of time.

The best practice is to invoke the `flush()` method, in a manner that is serialized with enqueueing sample buffers, after receiving this event and before resuming the enqueueing of sample buffers.

## See Also

### Flush reasons

- [AVSampleBufferAudioRenderer.Receiver.SuggestedFlushReason.outputConfigurationChanged](outputconfigurationchanged.md) — The audio output configuration has changed.
