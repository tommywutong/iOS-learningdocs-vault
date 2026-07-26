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
doc_path: '/documentation/swift/keyeddecodingcontainer/decodeifpresent(_:forkey:configuration:)-5g1cl'
source_url: 'https://developer.apple.com/documentation/swift/keyeddecodingcontainer/decodeifpresent(_:forkey:configuration:)-5g1cl'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/keyeddecodingcontainer/decodeifpresent%28_%3Aforkey%3Aconfiguration%3A%29-5g1cl.json'
content_hash: 'sha256:6127de5a84622467'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [KeyedDecodingContainer](../keyeddecodingcontainer.md)

# decodeIfPresent(_:forKey:configuration:)

<sub>Instance Method</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func decodeIfPresent<T, C>(_: T.Type, forKey key: KeyedDecodingContainer<K>.Key, configuration: C.Type) throws -> T? where T : DecodableWithConfiguration, C : DecodingConfigurationProviding, T.DecodingConfiguration == C.DecodingConfiguration
```
