---
title: SerializationRequirement
framework: Distributed
symbol_kind: associatedtype
role: symbol
role_heading: Associated Type
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/distributed/distributedactor/serializationrequirement
source_url: 'https://developer.apple.com/documentation/distributed/distributedactor/serializationrequirement'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/distributed/distributedactor/serializationrequirement.json'
content_hash: 'sha256:b1e0c19e6714b477'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Distributed](../../distributed.md) · [DistributedActor](../distributedactor.md)

# SerializationRequirement

<sub>Associated Type</sub>

The serialization requirement to apply to all distributed declarations inside the actor.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
associatedtype SerializationRequirement where Self.SerializationRequirement == Self.ActorSystem.SerializationRequirement
```
