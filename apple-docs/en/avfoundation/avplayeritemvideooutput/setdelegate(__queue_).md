---
title: 'setDelegate(_:queue:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, macOS 10.8+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avplayeritemvideooutput/setdelegate(_:queue:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayeritemvideooutput/setdelegate(_:queue:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayeritemvideooutput/setdelegate%28_%3Aqueue%3A%29.json'
content_hash: 'sha256:7cd952e983e932cc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayerItemVideoOutput](../avplayeritemvideooutput.md)

# setDelegate(_:queue:)

<sub>Instance Method</sub>

Sets the delegate and dispatch queue for the receiver.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func setDelegate(_ delegate: (any AVPlayerItemOutputPullDelegate)?, queue delegateQueue: dispatch_queue_t?)
```

## Parameters

- `delegate` — The delegate object for the receiver. You may specify `nil` for this parameter.

- `delegateQueue` — The dispatch queue on which to call delegate methods. If you specify `nil` for this parameter, the video output object calls the delegate on the dispatch queue for your app’s main thread.

## See Also

### Configuring the delegate

- [delegate](delegate.md) — The delegate for the video output object.
- [AVPlayerItemOutputPullDelegate](../avplayeritemoutputpulldelegate.md) — Methods you can implement to respond to pixel buffer changes.
- [delegateQueue](delegatequeue.md) — The dispatch queue on which to call delegate methods.
