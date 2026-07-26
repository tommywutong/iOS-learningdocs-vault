---
title: AVSampleBufferVideoRendererRequiresFlushToResumeDecodingDidChangeNotificationRequiresFlushKey
framework: AVFoundation
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 27.0+ beta（27.0 起废弃）, iPadOS 27.0+ beta（27.0 起废弃）, Mac Catalyst 27.0+ beta（27.0 起废弃）, macOS 27.0+ beta（27.0 起废弃）, tvOS 27.0+ beta（27.0 起废弃）, visionOS 27.0+ beta（27.0 起废弃）]
languages: [swift, occ]
beta: true
deprecated: true
doc_path: /documentation/avfoundation/avsamplebuffervideorendererrequiresflushtoresumedecodingdidchangenotificationrequiresflushkey
source_url: 'https://developer.apple.com/documentation/avfoundation/avsamplebuffervideorendererrequiresflushtoresumedecodingdidchangenotificationrequiresflushkey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avsamplebuffervideorendererrequiresflushtoresumedecodingdidchangenotificationrequiresflushkey.json'
content_hash: 'sha256:61cad98b3e3c3555'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVSampleBufferVideoRendererRequiresFlushToResumeDecodingDidChangeNotificationRequiresFlushKey

<sub>Global Variable</sub>

> [!warning] Deprecated
> Use the result of AVSampleBufferVideoRenderer.Receiver enqueue(_:) and enqueueImmediately(_:) for .requiresFlushToResumeDecoding instead

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
let AVSampleBufferVideoRendererRequiresFlushToResumeDecodingDidChangeNotificationRequiresFlushKey: String
```

## See Also

### Flushing the renderer

- [requiresFlushToResumeDecoding](avsamplebuffervideorenderer/requiresflushtoresumedecoding.md) — A Boolean value that Indicates whether the renderer requires flushing to continue decoding frames. _(deprecated)_
- [AVSampleBufferVideoRendererRequiresFlushToResumeDecodingDidChangeNotification](avsamplebuffervideorenderer/requiresflushtoresumedecodingdidchangenotification.md) — A notification that indicates that the video renderer requires flushing to continue rendering sample buffers. _(deprecated)_
- [- flushWithRemovalOfDisplayedImage:completionHandler:](<avsamplebuffervideorenderer/flush(removingdisplayedimage_completionhandler_).md>) — Tells the video renderer to discard pending enqueued sample buffers. _(deprecated)_
