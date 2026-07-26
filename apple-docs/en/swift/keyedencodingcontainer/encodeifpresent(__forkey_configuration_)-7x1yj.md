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
doc_path: '/documentation/swift/keyedencodingcontainer/encodeifpresent(_:forkey:configuration:)-7x1yj'
source_url: 'https://developer.apple.com/documentation/swift/keyedencodingcontainer/encodeifpresent(_:forkey:configuration:)-7x1yj'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/keyedencodingcontainer/encodeifpresent%28_%3Aforkey%3Aconfiguration%3A%29-7x1yj.json'
content_hash: 'sha256:6b6c2e3c9f4dbdbe'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [KeyedEncodingContainer](../keyedencodingcontainer.md)

# encodeIfPresent(_:forKey:configuration:)

<sub>Instance Method</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func encodeIfPresent<T, C>(_ t: T?, forKey key: KeyedEncodingContainer<K>.Key, configuration: C.Type) throws where T : EncodableWithConfiguration, C : EncodingConfigurationProviding, T.EncodingConfiguration == C.EncodingConfiguration
```
