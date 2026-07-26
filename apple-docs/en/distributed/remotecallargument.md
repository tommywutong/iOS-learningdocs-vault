---
title: RemoteCallArgument
framework: Distributed
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/distributed/remotecallargument
source_url: 'https://developer.apple.com/documentation/distributed/remotecallargument'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/distributed/remotecallargument.json'
content_hash: 'sha256:14b0d33bd5c6e0ae'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Distributed](../distributed.md)

# RemoteCallArgument

<sub>Structure</sub>

Represents an argument passed to a distributed call target.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct RemoteCallArgument<Value>
```

## Topics

### Initializers

- [init(label:name:value:)](<remotecallargument/init(label_name_value_).md>)

### Instance Properties

- [effectiveLabel](remotecallargument/effectivelabel.md) — The effective label of this argument. This reflects the semantics of call sites of function declarations without explicit label definitions in Swift.
- [label](remotecallargument/label.md) — The “argument label” of the argument. The label is the name visible name used in external calls made to this target, e.g. for `func hello(label name: String)` it is `label`.
- [name](remotecallargument/name.md) — The internal name of parameter this argument is accessible as in the function body. It is not part of the functions API and may change without breaking the target identifier.
- [value](remotecallargument/value.md) — The value of the argument being passed to the call. As `RemoteCallArgument` is always used in conjunction with `recordArgument` and populated by the compiler, this Value will generally conform to a distributed actor system’s `SerializationRequirement`.

## See Also

### Remote Calls

- [RemoteCallTarget](remotecalltarget.md) — Represents a ‘target’ of a distributed call, such as a `distributed func` or `distributed` computed property. Identification schemes may vary between systems, and are subject to evolution.
- [DistributedTargetInvocationEncoder](distributedtargetinvocationencoder.md) — Used to encode an invocation of a distributed target (method or computed property).
- [DistributedTargetInvocationDecoder](distributedtargetinvocationdecoder.md) — Decoder that must be provided to `executeDistributedTarget` and is used by the Swift runtime to decode arguments of the invocation.
- [DistributedTargetInvocationResultHandler](distributedtargetinvocationresulthandler.md) — Protocol a distributed invocation execution’s result handler.
