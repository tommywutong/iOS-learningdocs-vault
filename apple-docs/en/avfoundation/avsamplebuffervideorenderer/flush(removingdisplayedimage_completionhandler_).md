---
title: 'flush(removingDisplayedImage:completionHandler:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+（27.0 起废弃）, iPadOS 17.0+（27.0 起废弃）, Mac Catalyst 17.0+（27.0 起废弃）, macOS 14.0+（27.0 起废弃）, tvOS 17.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/avfoundation/avsamplebuffervideorenderer/flush(removingdisplayedimage:completionhandler:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avsamplebuffervideorenderer/flush(removingdisplayedimage:completionhandler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avsamplebuffervideorenderer/flush%28removingdisplayedimage%3Acompletionhandler%3A%29.json'
content_hash: 'sha256:53d85ca189e2b9b7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVSampleBufferVideoRenderer](../avsamplebuffervideorenderer.md)

# flush(removingDisplayedImage:completionHandler:)

<sub>Instance Method</sub>

Tells the video renderer to discard pending enqueued sample buffers.

> [!warning] Deprecated
> Attach renderer to a render synchronizer with sampleBufferReceiver(adding:) and use the receiver's flush(removingDisplayedImage:) method instead

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func flush(removingDisplayedImage removeDisplayedImage: Bool, completionHandler handler: (@Sendable () -> Void)? = nil)
```

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func flush(removingDisplayedImage removeDisplayedImage: Bool) async
```

## Parameters

- `removeDisplayedImage` — A Boolean value that indicates whether to remove the display image.

- `handler` — A completion handler the system invokes when the flush completes.

## See Also

### Flushing the renderer

- [requiresFlushToResumeDecoding](requiresflushtoresumedecoding.md) — A Boolean value that Indicates whether the renderer requires flushing to continue decoding frames. _(deprecated)_
- [AVSampleBufferVideoRendererRequiresFlushToResumeDecodingDidChangeNotification](requiresflushtoresumedecodingdidchangenotification.md) — A notification that indicates that the video renderer requires flushing to continue rendering sample buffers. _(deprecated)_
- [AVSampleBufferVideoRendererRequiresFlushToResumeDecodingDidChangeNotificationRequiresFlushKey](../avsamplebuffervideorendererrequiresflushtoresumedecodingdidchangenotificationrequiresflushkey.md) _(deprecated)_
