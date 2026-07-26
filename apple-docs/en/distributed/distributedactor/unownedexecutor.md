---
title: unownedExecutor
framework: Distributed
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/distributed/distributedactor/unownedexecutor
source_url: 'https://developer.apple.com/documentation/distributed/distributedactor/unownedexecutor'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/distributed/distributedactor/unownedexecutor.json'
content_hash: 'sha256:fbd897d55f25a3dd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Distributed](../../distributed.md) · [DistributedActor](../distributedactor.md)

# unownedExecutor

<sub>Instance Property</sub>

Retrieve the executor for this distributed actor as an optimized, unowned reference. This API is equivalent to `Actor/unownedExecutor`, however, by default, it intentionally returns `nil` if this actor is a reference to a remote distributed actor, because the executor for remote references is effectively never g

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated var unownedExecutor: UnownedSerialExecutor { get }
```

## Custom implementation requirements

This property must always evaluate to the same executor for a given actor instance, and holding on to the actor must keep the executor alive.

This property will be implicitly accessed when work needs to be scheduled onto this actor.  These accesses may be merged, eliminated, and rearranged with other work, and they may even be introduced when not strictly required.  Visible side effects are therefore strongly discouraged within this property.
