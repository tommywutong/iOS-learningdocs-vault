---
title: ActorSystem
framework: Distributed
symbol_kind: associatedtype
role: symbol
role_heading: Associated Type
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/distributed/distributedactor/actorsystem-swift.associatedtype
source_url: 'https://developer.apple.com/documentation/distributed/distributedactor/actorsystem-swift.associatedtype'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/distributed/distributedactor/actorsystem-swift.associatedtype.json'
content_hash: 'sha256:5fe7d749856fa150'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Distributed](../../distributed.md) · [DistributedActor](../distributedactor.md)

# ActorSystem

<sub>Associated Type</sub>

The type of transport used to communicate with actors of this type.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
associatedtype ActorSystem : DistributedActorSystem where Self.ID == Self.ActorSystem.ActorID
```
