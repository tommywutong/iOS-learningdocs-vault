---
title: 'recordArgument(_:)'
framework: Distributed
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/distributed/distributedtargetinvocationencoder/recordargument(_:)'
source_url: 'https://developer.apple.com/documentation/distributed/distributedtargetinvocationencoder/recordargument(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/distributed/distributedtargetinvocationencoder/recordargument%28_%3A%29.json'
content_hash: 'sha256:04f60a903d1a61ff'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Distributed](../../distributed.md) · [DistributedTargetInvocationEncoder](../distributedtargetinvocationencoder.md)

# recordArgument(_:)

<sub>Instance Method</sub>

Record an argument of `Argument` type. This will be invoked for every argument of the target, in declaration order.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func recordArgument<Value>(_ argument: RemoteCallArgument<Value>) throws
```

### Serialization Requirement

Implementations of this method must ensure that the `Value` type parameter conforms to the types’ `SerializationRequirement`.
