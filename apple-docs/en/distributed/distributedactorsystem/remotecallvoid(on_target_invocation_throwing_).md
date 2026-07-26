---
title: 'remoteCallVoid(on:target:invocation:throwing:)'
framework: Distributed
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/distributed/distributedactorsystem/remotecallvoid(on:target:invocation:throwing:)'
source_url: 'https://developer.apple.com/documentation/distributed/distributedactorsystem/remotecallvoid(on:target:invocation:throwing:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/distributed/distributedactorsystem/remotecallvoid%28on%3Atarget%3Ainvocation%3Athrowing%3A%29.json'
content_hash: 'sha256:fb1742f07ee39cbd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Distributed](../../distributed.md) · [DistributedActorSystem](../distributedactorsystem.md)

# remoteCallVoid(on:target:invocation:throwing:)

<sub>Instance Method</sub>

Invoked by the Swift runtime when making a remote call.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func remoteCallVoid<Act, Err>(on actor: Act, target: RemoteCallTarget, invocation: inout Self.InvocationEncoder, throwing: Err.Type) async throws where Act : DistributedActor, Err : Error, Self.ActorID == Act.ID
```

## Discussion

The `arguments` are the arguments container that was previously created by `makeInvocationEncoder` and has been populated with all arguments.

This method should perform the actual remote function call, and await for its response.

## Errors

This method is allowed to throw because of underlying transport or serialization errors, as well as by re-throwing the error received from the remote callee (if able to).
