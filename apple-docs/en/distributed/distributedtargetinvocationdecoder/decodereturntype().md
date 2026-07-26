---
title: decodeReturnType()
framework: Distributed
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/distributed/distributedtargetinvocationdecoder/decodereturntype()
source_url: 'https://developer.apple.com/documentation/distributed/distributedtargetinvocationdecoder/decodereturntype()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/distributed/distributedtargetinvocationdecoder/decodereturntype%28%29.json'
content_hash: 'sha256:351ff7a05b0f8411'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Distributed](../../distributed.md) · [DistributedTargetInvocationDecoder](../distributedtargetinvocationdecoder.md)

# decodeReturnType()

<sub>Instance Method</sub>

Attempt to decode the known return type of the distributed invocation.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func decodeReturnType() throws -> (any Any.Type)?
```

## Discussion

It is legal to implement this by returning `nil`, and then the system will take the concrete return type from the located function signature.
