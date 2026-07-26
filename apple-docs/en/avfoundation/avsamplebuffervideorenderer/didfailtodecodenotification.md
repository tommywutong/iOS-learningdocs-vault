---
title: didFailToDecodeNotification
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 17.0+（27.0 起废弃）, iPadOS 17.0+（27.0 起废弃）, Mac Catalyst 17.0+（27.0 起废弃）, macOS 14.0+（27.0 起废弃）, tvOS 17.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/avfoundation/avsamplebuffervideorenderer/didfailtodecodenotification
source_url: 'https://developer.apple.com/documentation/avfoundation/avsamplebuffervideorenderer/didfailtodecodenotification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avsamplebuffervideorenderer/didfailtodecodenotification.json'
content_hash: 'sha256:490cfc6be75b8c7c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVSampleBufferVideoRenderer](../avsamplebuffervideorenderer.md)

# didFailToDecodeNotification

<sub>Type Property</sub>

A notification that indicates the video renderer fails to decode a sample buffer.

> [!warning] Deprecated
> Use the result of AVSampleBufferVideoRenderer.Receiver enqueue(_:) and enqueueImmediately(_:) for .successWithDecodeFailure instead

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class let didFailToDecodeNotification: NSNotification.Name
```

## See Also

### Handling decode failures

- [AVSampleBufferVideoRendererDidFailToDecodeNotificationErrorKey](didfailtodecodenotificationerrorkey.md) — A key to retrieve an error object that provides the details of the failure. _(deprecated)_
