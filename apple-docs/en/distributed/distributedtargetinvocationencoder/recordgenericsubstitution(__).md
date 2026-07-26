---
title: 'recordGenericSubstitution(_:)'
framework: Distributed
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/distributed/distributedtargetinvocationencoder/recordgenericsubstitution(_:)'
source_url: 'https://developer.apple.com/documentation/distributed/distributedtargetinvocationencoder/recordgenericsubstitution(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/distributed/distributedtargetinvocationencoder/recordgenericsubstitution%28_%3A%29.json'
content_hash: 'sha256:d330a9b3428471d4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Distributed](../../distributed.md) · [DistributedTargetInvocationEncoder](../distributedtargetinvocationencoder.md)

# recordGenericSubstitution(_:)

<sub>Instance Method</sub>

The arguments must be encoded order-preserving, and once `decodeGenericSubstitutions` is called, the substitutions must be returned in the same order in which they were recorded.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func recordGenericSubstitution<T>(_ type: T.Type) throws
```

## Parameters

- `type` — A generic substitution type to be recorded for this invocation.
