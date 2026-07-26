---
title: delegateQueue
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta, watchOS 27.0+ beta]
languages: [occ]
beta: true
deprecated: false
doc_path: /documentation/avfoundation/avplayeritemsamplebufferoutput/delegatequeue
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayeritemsamplebufferoutput/delegatequeue'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayeritemsamplebufferoutput/delegatequeue.json'
content_hash: 'sha256:3d4e37ce3748dc28'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayerItemSampleBufferOutput](../avplayeritemsamplebufferoutput.md)

# delegateQueue

<sub>Instance Property</sub>

The dispatch queue where the delegate is messaged.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
@property (nonatomic, readonly, nullable) dispatch_queue_t delegateQueue;
```

## See Also

### Configuring the delegate

- [delegate](delegate.md) — The receiver’s delegate. _(beta)_
- [setDelegate:queue:](setdelegate_queue_.md) — Sets the receiver’s delegate and a dispatch queue on which the delegate will be called. _(beta)_
