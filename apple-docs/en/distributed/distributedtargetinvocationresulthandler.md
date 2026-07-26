---
title: DistributedTargetInvocationResultHandler
framework: Distributed
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/distributed/distributedtargetinvocationresulthandler
source_url: 'https://developer.apple.com/documentation/distributed/distributedtargetinvocationresulthandler'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/distributed/distributedtargetinvocationresulthandler.json'
content_hash: 'sha256:98b4da6e2d3cb611'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Distributed](../distributed.md)

# DistributedTargetInvocationResultHandler

<sub>Protocol</sub>

Protocol a distributed invocation execution’s result handler.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
protocol DistributedTargetInvocationResultHandler<SerializationRequirement>
```

## Overview

An instance conforming to this type must be passed when invoking `executeDistributedTarget(on:target:invocationDecoder:handler:)` while handling an incoming distributed call.

The handler will then be invoked with the return value (or error) that the invoked target returned (or threw).

## Relationships

- **Conforming Types**: [LocalTestingInvocationResultHandler](localtestinginvocationresulthandler.md)

## Topics

### Associated Types

- [SerializationRequirement](distributedtargetinvocationresulthandler/serializationrequirement.md) — The serialization requirement that the value passed to `onReturn` is required to conform to.

### Instance Methods

- [onReturn(value:)](<distributedtargetinvocationresulthandler/onreturn(value_).md>) — Invoked when the distributed target execution returns successfully. The `value` is the return value of the executed distributed invocation target.
- [onReturnVoid()](<distributedtargetinvocationresulthandler/onreturnvoid().md>) — Invoked when the distributed target execution of a `Void` returning function has completed successfully.
- [onThrow(error:)](<distributedtargetinvocationresulthandler/onthrow(error_).md>) — Invoked when the distributed target execution of a target has thrown an error.

## See Also

### Remote Calls

- [RemoteCallTarget](remotecalltarget.md) — Represents a ‘target’ of a distributed call, such as a `distributed func` or `distributed` computed property. Identification schemes may vary between systems, and are subject to evolution.
- [RemoteCallArgument](remotecallargument.md) — Represents an argument passed to a distributed call target.
- [DistributedTargetInvocationEncoder](distributedtargetinvocationencoder.md) — Used to encode an invocation of a distributed target (method or computed property).
- [DistributedTargetInvocationDecoder](distributedtargetinvocationdecoder.md) — Decoder that must be provided to `executeDistributedTarget` and is used by the Swift runtime to decode arguments of the invocation.
