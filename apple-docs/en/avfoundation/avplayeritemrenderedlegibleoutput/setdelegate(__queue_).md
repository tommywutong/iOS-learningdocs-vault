---
title: 'setDelegate(_:queue:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avplayeritemrenderedlegibleoutput/setdelegate(_:queue:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayeritemrenderedlegibleoutput/setdelegate(_:queue:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayeritemrenderedlegibleoutput/setdelegate%28_%3Aqueue%3A%29.json'
content_hash: 'sha256:90eddc315d9c705e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayerItemRenderedLegibleOutput](../avplayeritemrenderedlegibleoutput.md)

# setDelegate(_:queue:)

<sub>Instance Method</sub>

Sets the delegate object and the queue on which it’s invoked.

<sub>iOS, iPadOS, Mac Catalyst, macOS</sub>

```swift
func setDelegate(_ delegate: (any AVPlayerItemRenderedLegibleOutputPushDelegate)?, queue delegateQueue: dispatch_queue_t?)
```

## Parameters

- `delegate` — A delegate object for this output.

- `delegateQueue` — A dispatch queue on which the system calls all delegate methods.

## See Also

### Setting a delegate

- [delegate](delegate.md) — A delegate object for this output.
- [delegateQueue](delegatequeue.md) — The dispatch queue on which the output calls the delegate object.
- [AVPlayerItemRenderedLegibleOutputPushDelegate](../avplayeritemrenderedlegibleoutputpushdelegate.md) — A delegate that handles the rendered pixel buffers produced by a rendered legible output object.
