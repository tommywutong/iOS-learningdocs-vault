---
title: ActorID
framework: Distributed
symbol_kind: associatedtype
role: symbol
role_heading: Associated Type
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/distributed/distributedactorsystem/actorid
source_url: 'https://developer.apple.com/documentation/distributed/distributedactorsystem/actorid'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/distributed/distributedactorsystem/actorid.json'
content_hash: 'sha256:bec2ad8ce36f8dda'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Distributed](../../distributed.md) · [DistributedActorSystem](../distributedactorsystem.md)

# ActorID

<sub>Associated Type</sub>

The type ID that will be assigned to any distributed actor managed by this actor system.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
associatedtype ActorID : Hashable, Sendable
```

### A note on Codable IDs

If this type is `Codable`, then any `distributed actor` using this `ActorID` as its `DistributedActor/ID` will gain a synthesized `Codable` conformance which is implemented by encoding the `ID`. The decoding counter part of the `Codable` conformance is implemented by decoding the `ID` and passing it to the [resolve(id:using:)](<../distributedactor/resolve(id_using_).md>) method.
