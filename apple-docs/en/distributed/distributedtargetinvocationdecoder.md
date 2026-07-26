---
title: DistributedTargetInvocationDecoder
framework: Distributed
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/distributed/distributedtargetinvocationdecoder
source_url: 'https://developer.apple.com/documentation/distributed/distributedtargetinvocationdecoder'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/distributed/distributedtargetinvocationdecoder.json'
content_hash: 'sha256:2e1c2a511366abcd'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Distributed](../distributed.md)

# DistributedTargetInvocationDecoder

<sub>Protocol</sub>

Decoder that must be provided to `executeDistributedTarget` and is used by the Swift runtime to decode arguments of the invocation.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
protocol DistributedTargetInvocationDecoder<SerializationRequirement>
```

### Decoding DistributedActor arguments using Codable

When using an actor system where `ActorID` is `Codable`, every distributed actor using that system is also implicitly `Codable` (see [DistributedActorSystem](distributedactorsystem.md)). Such distributed actors are encoded as their `ActorID` stored in an `Encoder/singleValueContainer`. When `Codable` is being used by such a system, the `decodeNextArgument` method will be using `Decoder` to decode the incoming values, which may themselves be distributed actors.

An actor system must be provided to the `Decoder` in order for a distributed actor’s `Decodable/init(from:)` to be able to return the instance of the actor. Specifically, the decoded`ActorID` is passed to the actor system’s `resolve(id:as:)` method in order to return either a local instance identified by this ID, or creating a remote actor reference. Thus, you must set the actor system the decoding is performed for, on the decoder’s `userInfo`, as follows:

```swift
mutating func decodeNextArgument<Argument: SerializationRequirement>() throws -> Argument {
  let argumentData: Data = /// ...
  // ...
  decoder.userInfo[.actorSystemKey] = self.actorSystem
  return try Argument.decode(
}
```

## Relationships

- **Conforming Types**: [LocalTestingInvocationDecoder](localtestinginvocationdecoder.md)

## Topics

### Associated Types

- [SerializationRequirement](distributedtargetinvocationdecoder/serializationrequirement.md) — The serialization requirement that the types passed to `decodeNextArgument` are required to conform to. The type returned by `decodeReturnType` is also expected to conform to this associated type requirement.

### Instance Methods

- [decodeErrorType()](<distributedtargetinvocationdecoder/decodeerrortype().md>) — Decode the specific error type that the distributed invocation target has recorded. Currently this effectively can only ever be `Error.self`.
- [decodeGenericSubstitutions()](<distributedtargetinvocationdecoder/decodegenericsubstitutions().md>) — Decode all generic substitutions that were recorded for this invocation.
- [decodeNextArgument()](<distributedtargetinvocationdecoder/decodenextargument().md>) — Attempt to decode the next argument from the underlying buffers into pre-allocated storage pointed at by ‘pointer’.
- [decodeReturnType()](<distributedtargetinvocationdecoder/decodereturntype().md>) — Attempt to decode the known return type of the distributed invocation.

## See Also

### Remote Calls

- [RemoteCallTarget](remotecalltarget.md) — Represents a ‘target’ of a distributed call, such as a `distributed func` or `distributed` computed property. Identification schemes may vary between systems, and are subject to evolution.
- [RemoteCallArgument](remotecallargument.md) — Represents an argument passed to a distributed call target.
- [DistributedTargetInvocationEncoder](distributedtargetinvocationencoder.md) — Used to encode an invocation of a distributed target (method or computed property).
- [DistributedTargetInvocationResultHandler](distributedtargetinvocationresulthandler.md) — Protocol a distributed invocation execution’s result handler.
