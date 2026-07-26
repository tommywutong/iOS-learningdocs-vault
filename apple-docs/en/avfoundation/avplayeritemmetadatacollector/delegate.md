---
title: delegate
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 9.3+, iPadOS 9.3+, Mac Catalyst 13.1+, macOS 10.11.3+, tvOS 9.2+, visionOS 1.0+, watchOS 2.3+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avplayeritemmetadatacollector/delegate
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayeritemmetadatacollector/delegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayeritemmetadatacollector/delegate.json'
content_hash: 'sha256:2416ac42d5db5d7e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayerItemMetadataCollector](../avplayeritemmetadatacollector.md)

# delegate

<sub>Instance Property</sub>

Accesses the metadata collector’s delegate object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
weak var delegate: (any AVPlayerItemMetadataCollectorPushDelegate)? { get }
```

## Discussion

The delegate is held using a zeroing-weak reference, so this property will have a value of `nil` after a delegate that was previously set has been deallocated.

This property is not key-value observable.

## See Also

### Accessing the delegate and callback queue

- [- setDelegate:queue:](<setdelegate(__queue_).md>) — Sets the delegate and a dispatch queue on which the delegate will be called.
- [AVPlayerItemMetadataCollectorPushDelegate](../avplayeritemmetadatacollectorpushdelegate.md) — A protocol you implement to receive metadata callbacks from a player item metadata collector.
- [delegateQueue](delegatequeue.md) — The dispatch queue on which the delegate’s methods are called.
