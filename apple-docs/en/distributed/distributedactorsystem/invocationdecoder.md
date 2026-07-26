---
title: InvocationDecoder
framework: Distributed
symbol_kind: associatedtype
role: symbol
role_heading: Associated Type
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/distributed/distributedactorsystem/invocationdecoder
source_url: 'https://developer.apple.com/documentation/distributed/distributedactorsystem/invocationdecoder'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/distributed/distributedactorsystem/invocationdecoder.json'
content_hash: 'sha256:3b82918c0f9ba39f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Distributed](../../distributed.md) · [DistributedActorSystem](../distributedactorsystem.md)

# InvocationDecoder

<sub>Associated Type</sub>

Type of [DistributedTargetInvocationDecoder](../distributedtargetinvocationdecoder.md) that should be used when decoding invocations during [executeDistributedTarget(on:target:invocationDecoder:handler:)](<executedistributedtarget(on_target_invocationdecoder_handler_).md>) calls.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
associatedtype InvocationDecoder : DistributedTargetInvocationDecoder where Self.InvocationDecoder.SerializationRequirement == Self.InvocationEncoder.SerializationRequirement
```
