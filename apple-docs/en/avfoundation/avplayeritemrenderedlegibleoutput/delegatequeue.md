---
title: delegateQueue
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avplayeritemrenderedlegibleoutput/delegatequeue
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayeritemrenderedlegibleoutput/delegatequeue'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayeritemrenderedlegibleoutput/delegatequeue.json'
content_hash: 'sha256:a3bd025a2dd2bfb9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayerItemRenderedLegibleOutput](../avplayeritemrenderedlegibleoutput.md)

# delegateQueue

<sub>Instance Property</sub>

The dispatch queue on which the output calls the delegate object.

<sub>iOS, iPadOS, Mac Catalyst, macOS</sub>

```swift
var delegateQueue: dispatch_queue_t? { get }
```

## See Also

### Setting a delegate

- [delegate](delegate.md) — A delegate object for this output.
- [- setDelegate:queue:](<setdelegate(__queue_).md>) — Sets the delegate object and the queue on which it’s invoked.
- [AVPlayerItemRenderedLegibleOutputPushDelegate](../avplayeritemrenderedlegibleoutputpushdelegate.md) — A delegate that handles the rendered pixel buffers produced by a rendered legible output object.
