---
title: 'setDelegate:queue:'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta, watchOS 27.0+ beta]
languages: [occ]
beta: true
deprecated: false
doc_path: '/documentation/avfoundation/avplayeritemsamplebufferoutput/setdelegate:queue:'
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayeritemsamplebufferoutput/setdelegate:queue:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayeritemsamplebufferoutput/setdelegate%3Aqueue%3A.json'
content_hash: 'sha256:32a941985f44c46e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayerItemSampleBufferOutput](../avplayeritemsamplebufferoutput.md)

# setDelegate:queue:

<sub>Instance Method</sub>

Sets the receiver’s delegate and a dispatch queue on which the delegate will be called.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
- (void) setDelegate:(id<AVPlayerItemSampleBufferOutputDelegate>) delegate queue:(dispatch_queue_t) delegateQueue;
```

## Parameters

- `delegate` — An object conforming to AVPlayerItemSampleBufferOutputDelegate protocol.

- `delegateQueue` — A dispatch queue on which all delegate methods will be called.

## See Also

### Configuring the delegate

- [delegate](delegate.md) — The receiver’s delegate. _(beta)_
- [delegateQueue](delegatequeue.md) — The dispatch queue where the delegate is messaged. _(beta)_
