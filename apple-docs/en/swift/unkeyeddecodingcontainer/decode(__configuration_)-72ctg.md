---
title: 'decode(_:configuration:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/unkeyeddecodingcontainer/decode(_:configuration:)-72ctg'
source_url: 'https://developer.apple.com/documentation/swift/unkeyeddecodingcontainer/decode(_:configuration:)-72ctg'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/unkeyeddecodingcontainer/decode%28_%3Aconfiguration%3A%29-72ctg.json'
content_hash: 'sha256:04d2670a61ca3beb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [UnkeyedDecodingContainer](../unkeyeddecodingcontainer.md)

# decode(_:configuration:)

<sub>Instance Method</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func decode<T, C>(_: T.Type, configuration: C.Type) throws -> T where T : DecodableWithConfiguration, C : DecodingConfigurationProviding, T.DecodingConfiguration == C.DecodingConfiguration
```
