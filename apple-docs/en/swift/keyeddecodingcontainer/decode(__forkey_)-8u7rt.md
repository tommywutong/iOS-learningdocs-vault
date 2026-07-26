---
title: 'decode(_:forKey:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/keyeddecodingcontainer/decode(_:forkey:)-8u7rt'
source_url: 'https://developer.apple.com/documentation/swift/keyeddecodingcontainer/decode(_:forkey:)-8u7rt'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/keyeddecodingcontainer/decode%28_%3Aforkey%3A%29-8u7rt.json'
content_hash: 'sha256:953b3d257e40ac12'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [KeyedDecodingContainer](../keyeddecodingcontainer.md)

# decode(_:forKey:)

<sub>Instance Method</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func decode<T, C>(_: CodableConfiguration<T?, C>.Type, forKey key: KeyedDecodingContainer<K>.Key) throws -> CodableConfiguration<T?, C> where T : DecodableWithConfiguration, T : EncodableWithConfiguration, C : DecodingConfigurationProviding, C : EncodingConfigurationProviding, T.DecodingConfiguration == C.DecodingConfiguration, T.EncodingConfiguration == C.EncodingConfiguration
```
