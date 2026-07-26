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
doc_path: /documentation/distributed/distributedactorsystem/serializationrequirement
source_url: 'https://developer.apple.com/documentation/distributed/distributedactorsystem/serializationrequirement'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/distributed/distributedactorsystem/serializationrequirement.json'
content_hash: 'sha256:f782c1d4dd90d762'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Distributed](../../distributed.md) · [DistributedActorSystem](../distributedactorsystem.md)

# SerializationRequirement

<sub>Associated Type</sub>

The serialization requirement that will be applied to all distributed targets used with this system.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
associatedtype SerializationRequirement where Self.SerializationRequirement == Self.InvocationDecoder.SerializationRequirement
```
