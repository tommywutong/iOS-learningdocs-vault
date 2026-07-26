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
doc_path: /documentation/distributed/distributedtargetinvocationdecoder/serializationrequirement
source_url: 'https://developer.apple.com/documentation/distributed/distributedtargetinvocationdecoder/serializationrequirement'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/distributed/distributedtargetinvocationdecoder/serializationrequirement.json'
content_hash: 'sha256:4281e4ee9c1f47ea'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Distributed](../../distributed.md) · [DistributedTargetInvocationDecoder](../distributedtargetinvocationdecoder.md)

# SerializationRequirement

<sub>Associated Type</sub>

The serialization requirement that the types passed to `decodeNextArgument` are required to conform to. The type returned by `decodeReturnType` is also expected to conform to this associated type requirement.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
associatedtype SerializationRequirement
```
