---
title: delegate
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta, watchOS 27.0+ beta]
languages: [occ]
beta: true
deprecated: false
doc_path: /documentation/avfoundation/avplayeritemsamplebufferoutput/delegate
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayeritemsamplebufferoutput/delegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayeritemsamplebufferoutput/delegate.json'
content_hash: 'sha256:55100a4e7e7d6c72'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayerItemSampleBufferOutput](../avplayeritemsamplebufferoutput.md)

# delegate

<sub>Instance Property</sub>

The receiver’s delegate.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
@property (weak, readonly) id<AVPlayerItemSampleBufferOutputDelegate> delegate;
```

## See Also

### Configuring the delegate

- [delegateQueue](delegatequeue.md) — The dispatch queue where the delegate is messaged. _(beta)_
- [setDelegate:queue:](setdelegate_queue_.md) — Sets the receiver’s delegate and a dispatch queue on which the delegate will be called. _(beta)_
