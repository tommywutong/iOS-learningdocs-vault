---
title: makeInvocationEncoder()
framework: Distributed
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/distributed/distributedactorsystem/makeinvocationencoder()
source_url: 'https://developer.apple.com/documentation/distributed/distributedactorsystem/makeinvocationencoder()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/distributed/distributedactorsystem/makeinvocationencoder%28%29.json'
content_hash: 'sha256:e6eb484f47b8bd77'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Distributed](../../distributed.md) · [DistributedActorSystem](../distributedactorsystem.md)

# makeInvocationEncoder()

<sub>Instance Method</sub>

Invoked by the Swift runtime when a distributed remote call is about to be made.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func makeInvocationEncoder() -> Self.InvocationEncoder
```

## Discussion

The returned `DistributedTargetInvocation` will be populated with all arguments, generic substitutions, and specific error and return types that are associated with this specific invocation.
