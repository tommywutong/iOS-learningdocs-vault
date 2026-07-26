---
title: delegateQueue
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 9.3+, iPadOS 9.3+, Mac Catalyst 13.1+, macOS 10.11.3+, tvOS 9.2+, visionOS 1.0+, watchOS 2.3+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avplayeritemmetadatacollector/delegatequeue
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayeritemmetadatacollector/delegatequeue'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayeritemmetadatacollector/delegatequeue.json'
content_hash: 'sha256:48285f3a1ec77450'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayerItemMetadataCollector](../avplayeritemmetadatacollector.md)

# delegateQueue

<sub>Instance Property</sub>

The dispatch queue on which the delegate’s methods are called.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var delegateQueue: dispatch_queue_t? { get }
```

## Discussion

This property is not key-value observable.

## See Also

### Accessing the delegate and callback queue

- [- setDelegate:queue:](<setdelegate(__queue_).md>) — Sets the delegate and a dispatch queue on which the delegate will be called.
- [delegate](delegate.md) — Accesses the metadata collector’s delegate object.
- [AVPlayerItemMetadataCollectorPushDelegate](../avplayeritemmetadatacollectorpushdelegate.md) — A protocol you implement to receive metadata callbacks from a player item metadata collector.
