---
title: 'encode(_:configuration:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/unkeyedencodingcontainer/encode(_:configuration:)-85f4v'
source_url: 'https://developer.apple.com/documentation/swift/unkeyedencodingcontainer/encode(_:configuration:)-85f4v'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/unkeyedencodingcontainer/encode%28_%3Aconfiguration%3A%29-85f4v.json'
content_hash: 'sha256:50c660bfc30ff603'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [UnkeyedEncodingContainer](../unkeyedencodingcontainer.md)

# encode(_:configuration:)

<sub>Instance Method</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func encode<T>(_ t: T, configuration: T.EncodingConfiguration) throws where T : EncodableWithConfiguration
```
