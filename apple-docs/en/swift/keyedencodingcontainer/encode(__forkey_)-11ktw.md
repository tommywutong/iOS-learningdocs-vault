---
title: 'encode(_:forKey:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/keyedencodingcontainer/encode(_:forkey:)-11ktw'
source_url: 'https://developer.apple.com/documentation/swift/keyedencodingcontainer/encode(_:forkey:)-11ktw'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/keyedencodingcontainer/encode%28_%3Aforkey%3A%29-11ktw.json'
content_hash: 'sha256:8323db4904d0b72f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [KeyedEncodingContainer](../keyedencodingcontainer.md)

# encode(_:forKey:)

<sub>Instance Method</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func encode<T, C>(_ wrapper: CodableConfiguration<T?, C>, forKey key: KeyedEncodingContainer<K>.Key) throws where T : DecodableWithConfiguration, T : EncodableWithConfiguration, C : DecodingConfigurationProviding, C : EncodingConfigurationProviding, T.DecodingConfiguration == C.DecodingConfiguration, T.EncodingConfiguration == C.EncodingConfiguration
```
