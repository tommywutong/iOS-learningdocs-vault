---
title: delegate
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avplayeritemrenderedlegibleoutput/delegate
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayeritemrenderedlegibleoutput/delegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayeritemrenderedlegibleoutput/delegate.json'
content_hash: 'sha256:b97a97c5a3f69543'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayerItemRenderedLegibleOutput](../avplayeritemrenderedlegibleoutput.md)

# delegate

<sub>Instance Property</sub>

A delegate object for this output.

<sub>iOS, iPadOS, Mac Catalyst, macOS</sub>

```swift
weak var delegate: (any AVPlayerItemRenderedLegibleOutputPushDelegate)? { get }
```

## See Also

### Setting a delegate

- [- setDelegate:queue:](<setdelegate(__queue_).md>) — Sets the delegate object and the queue on which it’s invoked.
- [delegateQueue](delegatequeue.md) — The dispatch queue on which the output calls the delegate object.
- [AVPlayerItemRenderedLegibleOutputPushDelegate](../avplayeritemrenderedlegibleoutputpushdelegate.md) — A delegate that handles the rendered pixel buffers produced by a rendered legible output object.
