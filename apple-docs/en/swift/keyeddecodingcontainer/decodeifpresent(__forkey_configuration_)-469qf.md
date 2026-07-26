---
title: 'decodeIfPresent(_:forKey:configuration:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/keyeddecodingcontainer/decodeifpresent(_:forkey:configuration:)-469qf'
source_url: 'https://developer.apple.com/documentation/swift/keyeddecodingcontainer/decodeifpresent(_:forkey:configuration:)-469qf'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/keyeddecodingcontainer/decodeifpresent%28_%3Aforkey%3Aconfiguration%3A%29-469qf.json'
content_hash: 'sha256:0344136cdd55d8d2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [KeyedDecodingContainer](../keyeddecodingcontainer.md)

# decodeIfPresent(_:forKey:configuration:)

<sub>Instance Method</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func decodeIfPresent<T>(_: T.Type, forKey key: KeyedDecodingContainer<K>.Key, configuration: T.DecodingConfiguration) throws -> T? where T : DecodableWithConfiguration
```
