---
title: Resolvable()
framework: Distributed
symbol_kind: macro
role: symbol
role_heading: Macro
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/distributed/resolvable()
source_url: 'https://developer.apple.com/documentation/distributed/resolvable()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/distributed/resolvable%28%29.json'
content_hash: 'sha256:0e445c0a320c1716'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Distributed](../distributed.md)

# Resolvable()

<sub>Macro</sub>

Enables the attached to protocol to be resolved as remote distributed actor reference.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@attached(peer, names: prefixed(`$`)) @attached(extension, names: arbitrary) macro Resolvable()
```

### Requirements

The attached to type must be a protocol that refines the `DistributedActor` protocol. It must either specify a concrete `ActorSystem` or constrain it in such way that the system’s `SerializationRequirement` is statically known.

## See Also

### Distributed Actors

- [DistributedActor](distributedactor.md) — Common protocol to which all distributed actors conform implicitly.
- [DistributedActorSystem](distributedactorsystem.md) — A distributed actor system underpins and implements all functionality of distributed actors.
- [buildDefaultDistributedRemoteActorExecutor(_:)](<builddefaultdistributedremoteactorexecutor(__).md>) — Obtain the unowned `SerialExecutor` that is used by by remote distributed actor references. The executor is shared between all remote default executor remote distributed actors, and it will crash if any job is enqueued on it.
