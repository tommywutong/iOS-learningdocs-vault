---
title: 'buildDefaultDistributedRemoteActorExecutor(_:)'
framework: Distributed
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/distributed/builddefaultdistributedremoteactorexecutor(_:)'
source_url: 'https://developer.apple.com/documentation/distributed/builddefaultdistributedremoteactorexecutor(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/distributed/builddefaultdistributedremoteactorexecutor%28_%3A%29.json'
content_hash: 'sha256:7713c7e8ecc18604'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Distributed](../distributed.md)

# buildDefaultDistributedRemoteActorExecutor(_:)

<sub>Function</sub>

Obtain the unowned `SerialExecutor` that is used by by remote distributed actor references. The executor is shared between all remote default executor remote distributed actors, and it will crash if any job is enqueued on it.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func buildDefaultDistributedRemoteActorExecutor<Act>(_ actor: Act) -> UnownedSerialExecutor where Act : DistributedActor
```

## Discussion

It is possible to obtain the executor e.g. for logging or general debugging, however attempting to enqueue work on what might potentially be a remote actor is a programming error and therefore will crash if the actor is potentially.

If one intends to use a distributed actor’s executor to schedule work on it, one should programmatically ensure that that actor is local, e.g. using the `whenLocal` functionality of distributed actors, or by other means (e.g. “knowing that it definitely must be local”)

## See Also

### Distributed Actors

- [DistributedActor](distributedactor.md) — Common protocol to which all distributed actors conform implicitly.
- [DistributedActorSystem](distributedactorsystem.md) — A distributed actor system underpins and implements all functionality of distributed actors.
- [Resolvable()](<resolvable().md>) — Enables the attached to protocol to be resolved as remote distributed actor reference.
