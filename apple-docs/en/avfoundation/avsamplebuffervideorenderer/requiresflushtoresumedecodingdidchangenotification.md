---
title: requiresFlushToResumeDecodingDidChangeNotification
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 17.0+（27.0 起废弃）, iPadOS 17.0+（27.0 起废弃）, Mac Catalyst 17.0+（27.0 起废弃）, macOS 14.0+（27.0 起废弃）, tvOS 17.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/avfoundation/avsamplebuffervideorenderer/requiresflushtoresumedecodingdidchangenotification
source_url: 'https://developer.apple.com/documentation/avfoundation/avsamplebuffervideorenderer/requiresflushtoresumedecodingdidchangenotification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avsamplebuffervideorenderer/requiresflushtoresumedecodingdidchangenotification.json'
content_hash: 'sha256:5ebf0b4f4cb4d9aa'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVSampleBufferVideoRenderer](../avsamplebuffervideorenderer.md)

# requiresFlushToResumeDecodingDidChangeNotification

<sub>Type Property</sub>

A notification that indicates that the video renderer requires flushing to continue rendering sample buffers.

> [!warning] Deprecated
> Use the result of AVSampleBufferVideoRenderer.Receiver enqueue(_:) and enqueueImmediately(_:) for .requiresFlushToResumeDecoding instead

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class let requiresFlushToResumeDecodingDidChangeNotification: NSNotification.Name
```

## See Also

### Flushing the renderer

- [requiresFlushToResumeDecoding](requiresflushtoresumedecoding.md) — A Boolean value that Indicates whether the renderer requires flushing to continue decoding frames. _(deprecated)_
- [AVSampleBufferVideoRendererRequiresFlushToResumeDecodingDidChangeNotificationRequiresFlushKey](../avsamplebuffervideorendererrequiresflushtoresumedecodingdidchangenotificationrequiresflushkey.md) _(deprecated)_
- [- flushWithRemovalOfDisplayedImage:completionHandler:](<flush(removingdisplayedimage_completionhandler_).md>) — Tells the video renderer to discard pending enqueued sample buffers. _(deprecated)_
