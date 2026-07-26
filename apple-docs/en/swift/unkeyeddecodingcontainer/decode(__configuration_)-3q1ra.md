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
doc_path: '/documentation/swift/unkeyeddecodingcontainer/decode(_:configuration:)-3q1ra'
source_url: 'https://developer.apple.com/documentation/swift/unkeyeddecodingcontainer/decode(_:configuration:)-3q1ra'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/unkeyeddecodingcontainer/decode%28_%3Aconfiguration%3A%29-3q1ra.json'
content_hash: 'sha256:42650074ccd3504f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [UnkeyedDecodingContainer](../unkeyeddecodingcontainer.md)

# decode(_:configuration:)

<sub>Instance Method</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func decode<T>(_: T.Type, configuration: T.DecodingConfiguration) throws -> T where T : DecodableWithConfiguration
```
