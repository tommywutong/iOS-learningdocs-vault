---
title: requiresFlushToResumeDecoding
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 17.0+（27.0 起废弃）, iPadOS 17.0+（27.0 起废弃）, Mac Catalyst 17.0+（27.0 起废弃）, macOS 14.0+（27.0 起废弃）, tvOS 17.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/avfoundation/avsamplebuffervideorenderer/requiresflushtoresumedecoding
source_url: 'https://developer.apple.com/documentation/avfoundation/avsamplebuffervideorenderer/requiresflushtoresumedecoding'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avsamplebuffervideorenderer/requiresflushtoresumedecoding.json'
content_hash: 'sha256:f837e04ac4f6e054'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVSampleBufferVideoRenderer](../avsamplebuffervideorenderer.md)

# requiresFlushToResumeDecoding

<sub>Instance Property</sub>

A Boolean value that Indicates whether the renderer requires flushing to continue decoding frames.

> [!warning] Deprecated
> Use the result of AVSampleBufferVideoRenderer.Receiver enqueue(_:) and enqueueImmediately(_:) for .requiresFlushToResumeDecoding instead

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var requiresFlushToResumeDecoding: Bool { get }
```

## Discussion

When your app enters a state where using a video decoder resources is not permissible, the value of this property changes to [true](../../swift/true.md) along with the video renderer’s status changing to [AVQueuedSampleBufferRenderingStatusFailed](../avqueuedsamplebufferrenderingstatus/failed.md). To resume rendering sample buffers, you must first reset the video renderer by calling [- flush](<../avqueuedsamplebufferrendering/flush().md>) or [- flushWithRemovalOfDisplayedImage:completionHandler:](<flush(removingdisplayedimage_completionhandler_).md>).

This property is not key-value observable. Instead, track changes to this property by observing notifications of type [AVSampleBufferVideoRendererRequiresFlushToResumeDecodingDidChangeNotification](requiresflushtoresumedecodingdidchangenotification.md).

## See Also

### Flushing the renderer

- [AVSampleBufferVideoRendererRequiresFlushToResumeDecodingDidChangeNotification](requiresflushtoresumedecodingdidchangenotification.md) — A notification that indicates that the video renderer requires flushing to continue rendering sample buffers. _(deprecated)_
- [AVSampleBufferVideoRendererRequiresFlushToResumeDecodingDidChangeNotificationRequiresFlushKey](../avsamplebuffervideorendererrequiresflushtoresumedecodingdidchangenotificationrequiresflushkey.md) _(deprecated)_
- [- flushWithRemovalOfDisplayedImage:completionHandler:](<flush(removingdisplayedimage_completionhandler_).md>) — Tells the video renderer to discard pending enqueued sample buffers. _(deprecated)_
