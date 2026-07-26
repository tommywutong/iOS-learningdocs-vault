---
title: ResultHandler
framework: Distributed
symbol_kind: associatedtype
role: symbol
role_heading: Associated Type
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/distributed/distributedactorsystem/resulthandler
source_url: 'https://developer.apple.com/documentation/distributed/distributedactorsystem/resulthandler'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/distributed/distributedactorsystem/resulthandler.json'
content_hash: 'sha256:0c26e67f2bdb87ce'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Distributed](../../distributed.md) · [DistributedActorSystem](../distributedactorsystem.md)

# ResultHandler

<sub>Associated Type</sub>

The type of the result handler which will be offered the results returned by a distributed function invocation called via [executeDistributedTarget(on:target:invocationDecoder:handler:)](<executedistributedtarget(on_target_invocationdecoder_handler_).md>).

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
associatedtype ResultHandler : DistributedTargetInvocationResultHandler
```
