---
title: 'decode(_:forKey:configuration:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/keyeddecodingcontainer/decode(_:forkey:configuration:)-2rk0t'
source_url: 'https://developer.apple.com/documentation/swift/keyeddecodingcontainer/decode(_:forkey:configuration:)-2rk0t'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/keyeddecodingcontainer/decode%28_%3Aforkey%3Aconfiguration%3A%29-2rk0t.json'
content_hash: 'sha256:6e92d9d755c2521b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [KeyedDecodingContainer](../keyeddecodingcontainer.md)

# decode(_:forKey:configuration:)

<sub>Instance Method</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func decode<T>(_: T.Type, forKey key: KeyedDecodingContainer<K>.Key, configuration: T.DecodingConfiguration) throws -> T where T : DecodableWithConfiguration
```
