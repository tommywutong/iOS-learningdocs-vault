---
title: 'recordReturnType(_:)'
framework: Distributed
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/distributed/distributedtargetinvocationencoder/recordreturntype(_:)'
source_url: 'https://developer.apple.com/documentation/distributed/distributedtargetinvocationencoder/recordreturntype(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/distributed/distributedtargetinvocationencoder/recordreturntype%28_%3A%29.json'
content_hash: 'sha256:95c8adf92dbcfd6a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Distributed](../../distributed.md) · [DistributedTargetInvocationEncoder](../distributedtargetinvocationencoder.md)

# recordReturnType(_:)

<sub>Instance Method</sub>

Record the return type of the distributed method. This method will not be invoked if the target is returning `Void`.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func recordReturnType<R>(_ type: R.Type) throws
```

### Serialization Requirement

Implementations of this method must ensure that the `R` type parameter conforms to the types’ `SerializationRequirement`.
