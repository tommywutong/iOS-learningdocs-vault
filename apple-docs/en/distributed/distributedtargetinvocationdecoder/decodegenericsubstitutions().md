---
title: decodeGenericSubstitutions()
framework: Distributed
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/distributed/distributedtargetinvocationdecoder/decodegenericsubstitutions()
source_url: 'https://developer.apple.com/documentation/distributed/distributedtargetinvocationdecoder/decodegenericsubstitutions()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/distributed/distributedtargetinvocationdecoder/decodegenericsubstitutions%28%29.json'
content_hash: 'sha256:e309f5e53d584e79'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Distributed](../../distributed.md) · [DistributedTargetInvocationDecoder](../distributedtargetinvocationdecoder.md)

# decodeGenericSubstitutions()

<sub>Instance Method</sub>

Decode all generic substitutions that were recorded for this invocation.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func decodeGenericSubstitutions() throws -> [any Any.Type]
```

## Return Value

Array of all generic substitutions necessary to execute this invocation target.

## Discussion

The values retrieved from here must be in the same order as they were recorded by [recordGenericSubstitution(_:)](<../distributedtargetinvocationencoder/recordgenericsubstitution(__).md>).

> [!danger] Throws
> If decoding substitutions fails.
