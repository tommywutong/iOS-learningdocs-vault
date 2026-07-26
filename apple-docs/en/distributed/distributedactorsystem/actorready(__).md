---
title: 'actorReady(_:)'
framework: Distributed
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/distributed/distributedactorsystem/actorready(_:)'
source_url: 'https://developer.apple.com/documentation/distributed/distributedactorsystem/actorready(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/distributed/distributedactorsystem/actorready%28_%3A%29.json'
content_hash: 'sha256:ee8e8d8d7311b8e4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Distributed](../../distributed.md) · [DistributedActorSystem](../distributedactorsystem.md)

# actorReady(_:)

<sub>Instance Method</sub>

Invoked during a distributed actor’s initialization, as soon as it becomes fully initialized.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func actorReady<Act>(_ actor: Act) where Act : DistributedActor, Self.ActorID == Act.ID
```

## Parameters

- `actor` — Reference to the (local) actor that was just fully initialized.

## Discussion

The system is expected to store the reference to this actor, and maintain an `ActorID: DistributedActor` mapping for the purpose of implementing the `resolve(id:as:)` method.

The system usually should NOT retain the passed reference, and it will be informed via [resignID(_:)](<resignid(__).md>) when the actor has been deallocated so it can remove the stale reference from its internal `ActorID: DistributedActor` mapping.

The [id](../distributedactor/id.md) of the passed actor must be an [ActorID](actorid.md) that this system previously has assigned.

If `actorReady` gets called with some unknown ID, it should crash immediately as it signifies some very unexpected use of the system.
