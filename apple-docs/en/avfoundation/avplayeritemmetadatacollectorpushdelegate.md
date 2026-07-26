---
title: AVPlayerItemMetadataCollectorPushDelegate
framework: AVFoundation
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avplayeritemmetadatacollectorpushdelegate
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayeritemmetadatacollectorpushdelegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayeritemmetadatacollectorpushdelegate.json'
content_hash: 'sha256:d51e77c92cbb78c9'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVPlayerItemMetadataCollectorPushDelegate

<sub>Protocol</sub>

A protocol you implement to receive metadata callbacks from a player item metadata collector.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
protocol AVPlayerItemMetadataCollectorPushDelegate : NSObjectProtocol, Sendable
```

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Accessing HLS date range metadata

- [- metadataCollector:didCollectDateRangeMetadataGroups:indexesOfNewGroups:indexesOfModifiedGroups:](<avplayeritemmetadatacollectorpushdelegate/metadatacollector(__didcollect_indexesofnewgroups_indexesofmodifiedgroups_).md>) — Tells the delegate the collected metadata group information has changed and needs to be updated.

## See Also

### Accessing the delegate and callback queue

- [- setDelegate:queue:](<avplayeritemmetadatacollector/setdelegate(__queue_).md>) — Sets the delegate and a dispatch queue on which the delegate will be called.
- [delegate](avplayeritemmetadatacollector/delegate.md) — Accesses the metadata collector’s delegate object.
- [delegateQueue](avplayeritemmetadatacollector/delegatequeue.md) — The dispatch queue on which the delegate’s methods are called.
