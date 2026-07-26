---
title: 'setDelegate(_:queue:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 9.3+, iPadOS 9.3+, Mac Catalyst 13.1+, macOS 10.11.3+, tvOS 9.2+, visionOS 1.0+, watchOS 2.3+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avplayeritemmetadatacollector/setdelegate(_:queue:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayeritemmetadatacollector/setdelegate(_:queue:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayeritemmetadatacollector/setdelegate%28_%3Aqueue%3A%29.json'
content_hash: 'sha256:0d5df31cb2fe8ae8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayerItemMetadataCollector](../avplayeritemmetadatacollector.md)

# setDelegate(_:queue:)

<sub>Instance Method</sub>

Sets the delegate and a dispatch queue on which the delegate will be called.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func setDelegate(_ delegate: (any AVPlayerItemMetadataCollectorPushDelegate)?, queue delegateQueue: dispatch_queue_t?)
```

## Parameters

- `delegate` — An object conforming to [AVPlayerItemMetadataCollectorPushDelegate](../avplayeritemmetadatacollectorpushdelegate.md) protocol.

- `delegateQueue` — A dispatch queue on which all delegate methods will be called.

## See Also

### Accessing the delegate and callback queue

- [delegate](delegate.md) — Accesses the metadata collector’s delegate object.
- [AVPlayerItemMetadataCollectorPushDelegate](../avplayeritemmetadatacollectorpushdelegate.md) — A protocol you implement to receive metadata callbacks from a player item metadata collector.
- [delegateQueue](delegatequeue.md) — The dispatch queue on which the delegate’s methods are called.
