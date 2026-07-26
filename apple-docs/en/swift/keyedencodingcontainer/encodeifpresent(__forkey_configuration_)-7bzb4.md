---
title: 'encodeIfPresent(_:forKey:configuration:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/keyedencodingcontainer/encodeifpresent(_:forkey:configuration:)-7bzb4'
source_url: 'https://developer.apple.com/documentation/swift/keyedencodingcontainer/encodeifpresent(_:forkey:configuration:)-7bzb4'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/keyedencodingcontainer/encodeifpresent%28_%3Aforkey%3Aconfiguration%3A%29-7bzb4.json'
content_hash: 'sha256:8c86963f7a38a01f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [KeyedEncodingContainer](../keyedencodingcontainer.md)

# encodeIfPresent(_:forKey:configuration:)

<sub>Instance Method</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func encodeIfPresent<T>(_ t: T?, forKey key: KeyedEncodingContainer<K>.Key, configuration: T.EncodingConfiguration) throws where T : EncodableWithConfiguration
```
