---
title: actorSystem
framework: Distributed
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/distributed/distributedactor/actorsystem-swift.property
source_url: 'https://developer.apple.com/documentation/distributed/distributedactor/actorsystem-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/distributed/distributedactor/actorsystem-swift.property.json'
content_hash: 'sha256:82e47a8b53e7fa5f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Distributed](../../distributed.md) · [DistributedActor](../distributedactor.md)

# actorSystem

<sub>Instance Property</sub>

The [DistributedActorSystem](../distributedactorsystem.md) that is managing this distributed actor.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated var actorSystem: Self.ActorSystem { get }
```

## Discussion

It is immutable and equal to the system assigned during the distributed actor’s local initializer (or to the system passed to the [resolve(id:using:)](<resolve(id_using_).md>) static function).

## Synthesized property

In concrete distributed actor declarations, a witness for this protocol requirement is synthesized by the compiler.

It is required to assign an initial value to the `actorSystem` property inside a distributed actor’s designated initializer. Semantically, it can be treated as a `let` declaration, that must be assigned in order to fully-initialize the instance.

If a distributed actor declares no initializer, its default initializer will take the shape of `init(actorSystem:)`, and initialize this property using the passed [DistributedActorSystem](../distributedactorsystem.md). If any user-defined initializer exists, the default initializer is not synthesized, and all the user-defined initializers must take care to initialize this property.
