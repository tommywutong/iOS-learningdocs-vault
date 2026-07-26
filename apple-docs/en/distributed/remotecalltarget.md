---
title: RemoteCallTarget
framework: Distributed
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/distributed/remotecalltarget
source_url: 'https://developer.apple.com/documentation/distributed/remotecalltarget'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/distributed/remotecalltarget.json'
content_hash: 'sha256:c0d5f9ef553bbcd1'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Distributed](../distributed.md)

# RemoteCallTarget

<sub>Structure</sub>

Represents a ‘target’ of a distributed call, such as a `distributed func` or `distributed` computed property. Identification schemes may vary between systems, and are subject to evolution.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct RemoteCallTarget
```

## Overview

Actor systems generally should treat the `identifier` as an opaque string, and pass it along to the remote system for in their `remoteCall` implementation. Alternative approaches are possible, where the identifiers are either compressed, cached, or represented in other ways, as long as the recipient system is able to determine which target was intended to be invoked.

The string representation will attempt to pretty print the target identifier, however its exact format is not specified and may change in future versions.

## Relationships

- **Conforms To**: [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md)

## Topics

### Initializers

- [init(_:)](<remotecalltarget/init(__).md>)

### Instance Properties

- [description](remotecalltarget/description.md) — Attempts to pretty format the underlying target identifier. If unable to, returns the raw underlying identifier.
- [identifier](remotecalltarget/identifier.md) — The underlying identifier of the target, returned as-is.

## See Also

### Remote Calls

- [RemoteCallArgument](remotecallargument.md) — Represents an argument passed to a distributed call target.
- [DistributedTargetInvocationEncoder](distributedtargetinvocationencoder.md) — Used to encode an invocation of a distributed target (method or computed property).
- [DistributedTargetInvocationDecoder](distributedtargetinvocationdecoder.md) — Decoder that must be provided to `executeDistributedTarget` and is used by the Swift runtime to decode arguments of the invocation.
- [DistributedTargetInvocationResultHandler](distributedtargetinvocationresulthandler.md) — Protocol a distributed invocation execution’s result handler.
