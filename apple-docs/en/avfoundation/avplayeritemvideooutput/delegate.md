---
title: delegate
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, macOS 10.8+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avplayeritemvideooutput/delegate
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayeritemvideooutput/delegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayeritemvideooutput/delegate.json'
content_hash: 'sha256:ccfb34cdad9f0925'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayerItemVideoOutput](../avplayeritemvideooutput.md)

# delegate

<sub>Instance Property</sub>

The delegate for the video output object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
weak var delegate: (any AVPlayerItemOutputPullDelegate)? { get }
```

## See Also

### Configuring the delegate

- [- setDelegate:queue:](<setdelegate(__queue_).md>) — Sets the delegate and dispatch queue for the receiver.
- [AVPlayerItemOutputPullDelegate](../avplayeritemoutputpulldelegate.md) — Methods you can implement to respond to pixel buffer changes.
- [delegateQueue](delegatequeue.md) — The dispatch queue on which to call delegate methods.
