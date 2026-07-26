---
title: Distributed
framework: Distributed
symbol_kind: module
role: collection
role_heading: Framework
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/distributed
source_url: 'https://developer.apple.com/documentation/distributed'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/distributed.json'
content_hash: 'sha256:095e8dfb16b90f53'
translated: false
---

> Navigation: [Technologies](technologies.md)

# Distributed

<sub>Framework</sub>

Build systems that run distributed code across multiple processes and devices.

## Overview

Distributed actors share many characteristics with Swift actors, and include additional isolation checks to ensure location transparency and safety in a distributed environment. Similar to how actors make it easier to write concurrent code that’s safe and correct to run on a single computer, distributed actors make it easier to write code that runs across multiple computers.

![](../../attachments/2bf6622bede5876c3f4d6d1a4e1f1089/distributed-module@2x.png)

<sub>A diagram showing two columns of actors. The left column includes a remote actor reference. The right column includes a local distributed actor. An arrow points from the remote actor reference to the local distributed actor that it refers to.</sub>

You use three main parts when writing code with distributed actors:

- Swift language support for actors and distributed actors. For more information, see [Concurrency](https://docs.swift.org/swift-book/LanguageGuide/Concurrency.html) in [The Swift Programming Language](https://docs.swift.org/swift-book/).
- The Distributed module, which includes the types and protocols you need to declare and use distribute actors. For example, it has protocols to which distributed actors and distributed actor systems conform, and structures that encapsulate information about calls to a distributed actor.
- A _distributed actor system_, also called a cluster runtime, provides an implementation of the [DistributedActorSystem](distributed/distributedactorsystem.md) protocol and coordinates between the cluster’s nodes. A distributed actor is always part of some distributed actor system; that distributed actor system handles the serialization and networking necessary to perform remote method calls. For local testing, you can use [LocalTestingDistributedActorSystem](distributed/localtestingdistributedactorsystem.md). For production, you can use the distributed actor system from the [Swift Distributed Actors](https://github.com/apple/swift-distributed-actors/) library, use another library, or write your own distributed actor system.

## Topics

### Essentials

- [TicTacFish: Implementing a game using distributed actors](swift/tictacfish_implementing_a_game_using_distributed_actors.md) — Use distributed actors to take your Swift concurrency and actor-based apps beyond a single process.

### Distributed Actors

- [DistributedActor](distributed/distributedactor.md) — Common protocol to which all distributed actors conform implicitly.
- [DistributedActorSystem](distributed/distributedactorsystem.md) — A distributed actor system underpins and implements all functionality of distributed actors.
- [Resolvable()](<distributed/resolvable().md>) — Enables the attached to protocol to be resolved as remote distributed actor reference.
- [buildDefaultDistributedRemoteActorExecutor(_:)](<distributed/builddefaultdistributedremoteactorexecutor(__).md>) — Obtain the unowned `SerialExecutor` that is used by by remote distributed actor references. The executor is shared between all remote default executor remote distributed actors, and it will crash if any job is enqueued on it.

### Remote Calls

- [RemoteCallTarget](distributed/remotecalltarget.md) — Represents a ‘target’ of a distributed call, such as a `distributed func` or `distributed` computed property. Identification schemes may vary between systems, and are subject to evolution.
- [RemoteCallArgument](distributed/remotecallargument.md) — Represents an argument passed to a distributed call target.
- [DistributedTargetInvocationEncoder](distributed/distributedtargetinvocationencoder.md) — Used to encode an invocation of a distributed target (method or computed property).
- [DistributedTargetInvocationDecoder](distributed/distributedtargetinvocationdecoder.md) — Decoder that must be provided to `executeDistributedTarget` and is used by the Swift runtime to decode arguments of the invocation.
- [DistributedTargetInvocationResultHandler](distributed/distributedtargetinvocationresulthandler.md) — Protocol a distributed invocation execution’s result handler.

### Local Testing

- [LocalTestingDistributedActorSystem](distributed/localtestingdistributedactorsystem.md) — A `DistributedActorSystem` designed for local only testing.
- [LocalTestingActorID](distributed/localtestingactorid.md)
- [LocalTestingActorAddress](distributed/localtestingactoraddress.md) _(deprecated)_
- [LocalTestingInvocationEncoder](distributed/localtestinginvocationencoder.md)
- [LocalTestingInvocationDecoder](distributed/localtestinginvocationdecoder.md)
- [LocalTestingInvocationResultHandler](distributed/localtestinginvocationresulthandler.md)

### Errors

- [DistributedActorCodingError](distributed/distributedactorcodingerror.md) — Error thrown by distributed actor systems while encountering encoding/decoding issues.
- [DistributedActorSystemError](distributed/distributedactorsystemerror.md) — Error protocol to which errors thrown by any `DistributedActorSystem` should conform.
- [ExecuteDistributedTargetError](distributed/executedistributedtargeterror.md) — Error thrown by [executeDistributedTarget(on:target:invocationDecoder:handler:)](<distributed/distributedactorsystem/executedistributedtarget(on_target_invocationdecoder_handler_).md>).
- [LocalTestingDistributedActorSystemError](distributed/localtestingdistributedactorsystemerror.md)
