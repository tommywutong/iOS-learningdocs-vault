---
title: InvocationEncoder
framework: Distributed
symbol_kind: associatedtype
role: symbol
role_heading: Associated Type
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/distributed/distributedactorsystem/invocationencoder
source_url: 'https://developer.apple.com/documentation/distributed/distributedactorsystem/invocationencoder'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/distributed/distributedactorsystem/invocationencoder.json'
content_hash: 'sha256:156e768c61ecf9fc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Distributed](../../distributed.md) · [DistributedActorSystem](../distributedactorsystem.md)

# InvocationEncoder

<sub>Associated Type</sub>

Type of [DistributedTargetInvocationEncoder](../distributedtargetinvocationencoder.md) that should be used when the Swift runtime needs to encode a distributed target call into an encoder, before passing it off to `remoteCall(...)`.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
associatedtype InvocationEncoder : DistributedTargetInvocationEncoder where Self.InvocationEncoder.SerializationRequirement == Self.ResultHandler.SerializationRequirement
```
