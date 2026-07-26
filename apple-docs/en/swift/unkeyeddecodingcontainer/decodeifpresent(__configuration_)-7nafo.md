---
title: 'decodeIfPresent(_:configuration:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/unkeyeddecodingcontainer/decodeifpresent(_:configuration:)-7nafo'
source_url: 'https://developer.apple.com/documentation/swift/unkeyeddecodingcontainer/decodeifpresent(_:configuration:)-7nafo'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/unkeyeddecodingcontainer/decodeifpresent%28_%3Aconfiguration%3A%29-7nafo.json'
content_hash: 'sha256:2b5bd4c3f2307d9d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [UnkeyedDecodingContainer](../unkeyeddecodingcontainer.md)

# decodeIfPresent(_:configuration:)

<sub>Instance Method</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func decodeIfPresent<T>(_: T.Type, configuration: T.DecodingConfiguration) throws -> T? where T : DecodableWithConfiguration
```
