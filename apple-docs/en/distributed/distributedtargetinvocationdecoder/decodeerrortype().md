---
title: decodeErrorType()
framework: Distributed
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/distributed/distributedtargetinvocationdecoder/decodeerrortype()
source_url: 'https://developer.apple.com/documentation/distributed/distributedtargetinvocationdecoder/decodeerrortype()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/distributed/distributedtargetinvocationdecoder/decodeerrortype%28%29.json'
content_hash: 'sha256:0540d7d29894faa9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Distributed](../../distributed.md) · [DistributedTargetInvocationDecoder](../distributedtargetinvocationdecoder.md)

# decodeErrorType()

<sub>Instance Method</sub>

Decode the specific error type that the distributed invocation target has recorded. Currently this effectively can only ever be `Error.self`.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func decodeErrorType() throws -> (any Any.Type)?
```

## Discussion

If the target known to not be throwing, or no error type was recorded, the method should return `nil`.
