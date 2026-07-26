---
title: delegateQueue
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, macOS 10.8+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avplayeritemvideooutput/delegatequeue
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayeritemvideooutput/delegatequeue'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayeritemvideooutput/delegatequeue.json'
content_hash: 'sha256:0598793fce922d0f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayerItemVideoOutput](../avplayeritemvideooutput.md)

# delegateQueue

<sub>Instance Property</sub>

The dispatch queue on which to call delegate methods.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var delegateQueue: dispatch_queue_t? { get }
```

## See Also

### Configuring the delegate

- [- setDelegate:queue:](<setdelegate(__queue_).md>) — Sets the delegate and dispatch queue for the receiver.
- [delegate](delegate.md) — The delegate for the video output object.
- [AVPlayerItemOutputPullDelegate](../avplayeritemoutputpulldelegate.md) — Methods you can implement to respond to pixel buffer changes.
