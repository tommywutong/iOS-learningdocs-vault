---
title: 'flush(fromSourceTime:completionHandler:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+（27.0 起废弃）, iPadOS 11.0+（27.0 起废弃）, Mac Catalyst 13.1+（27.0 起废弃）, macOS 10.13+（27.0 起废弃）, tvOS 11.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）, watchOS 4.0+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/avfoundation/avsamplebufferaudiorenderer/flush(fromsourcetime:completionhandler:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avsamplebufferaudiorenderer/flush(fromsourcetime:completionhandler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avsamplebufferaudiorenderer/flush%28fromsourcetime%3Acompletionhandler%3A%29.json'
content_hash: 'sha256:de54adb95fde8adf'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVSampleBufferAudioRenderer](../avsamplebufferaudiorenderer.md)

# flush(fromSourceTime:completionHandler:)

<sub>Instance Method</sub>

Flushes queued sample buffers with presentation time stamps later than or equal to the specified time.

> [!warning] Deprecated
> Attach renderer to a render synchronizer with sampleBufferReceiver(adding:) and use the receiver's flush(fromSourceTime:) method instead

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func flush(fromSourceTime time: CMTime, completionHandler: @escaping @Sendable (Bool) -> Void)
```

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func flush(fromSourceTime time: CMTime) async -> Bool
```

## Parameters

- `time` — The time used to flush all later sample buffers.

- `completionHandler` — The block to invoke when the flush operation has either been completed or been interrupted. The block takes one argument: - **flushSucceeded** — A Boolean value indicating whether the sample buffers were flushed.

## Discussion

This method can be used to replace media data scheduled to be rendered in the future, without interrupting playback. One example of this is when the data that has already been enqueued is from a sequence of two songs and the second song is swapped for a new song. In this case, this method would be called with the timestamp of the first sample buffer from the second song. After the completion handler is executed with a `YES` parameter, media data may again be enqueued with time stamps at the specified time.

If `NO` is provided to the completion handler, the flush did not succeed and the set of enqueued sample buffers remains unchanged. A flush can fail because the source time was too close to (or earlier than) the current time or because the current configuration of the receiver does not support flushing at a particular time. In these cases, the caller can choose to flush all enqueued media data by invoking [- flush](<../avsamplebufferdisplaylayer/flush().md>).

## See Also

### Removing queued buffers

- [AVSampleBufferAudioRendererFlushTimeKey](../avsamplebufferaudiorendererflushtimekey.md) — The key that indicates the presentation timestamp of the first queued sample that was flushed. _(deprecated)_
