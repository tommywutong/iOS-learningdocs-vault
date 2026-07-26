---
title: AVPlayerItemRenderedLegibleOutputPushDelegate
framework: AVFoundation
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avplayeritemrenderedlegibleoutputpushdelegate
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayeritemrenderedlegibleoutputpushdelegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayeritemrenderedlegibleoutputpushdelegate.json'
content_hash: 'sha256:01776561e55eb39f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVPlayerItemRenderedLegibleOutputPushDelegate

<sub>Protocol</sub>

A delegate that handles the rendered pixel buffers produced by a rendered legible output object.

<sub>iOS, iPadOS, Mac Catalyst, macOS</sub>

```swift
protocol AVPlayerItemRenderedLegibleOutputPushDelegate : AVPlayerItemOutputPushDelegate
```

## Relationships

- **Inherits From**: [AVPlayerItemOutputPushDelegate](avplayeritemoutputpushdelegate.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Handling rendered pixel buffers

- [- renderedLegibleOutput:didOutputRenderedCaptionImages:forItemTime:](<avplayeritemrenderedlegibleoutputpushdelegate/renderedlegibleoutput(__didoutputrenderedcaptionimages_foritemtime_).md>) — Tells the delegate that new rendered caption images are available.

## See Also

### Setting a delegate

- [delegate](avplayeritemrenderedlegibleoutput/delegate.md) — A delegate object for this output.
- [- setDelegate:queue:](<avplayeritemrenderedlegibleoutput/setdelegate(__queue_).md>) — Sets the delegate object and the queue on which it’s invoked.
- [delegateQueue](avplayeritemrenderedlegibleoutput/delegatequeue.md) — The dispatch queue on which the output calls the delegate object.
