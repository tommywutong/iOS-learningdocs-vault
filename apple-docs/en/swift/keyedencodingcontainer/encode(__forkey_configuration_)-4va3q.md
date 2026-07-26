---
title: 'encode(_:forKey:configuration:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/keyedencodingcontainer/encode(_:forkey:configuration:)-4va3q'
source_url: 'https://developer.apple.com/documentation/swift/keyedencodingcontainer/encode(_:forkey:configuration:)-4va3q'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/keyedencodingcontainer/encode%28_%3Aforkey%3Aconfiguration%3A%29-4va3q.json'
content_hash: 'sha256:c8e8a888ec86d336'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [KeyedEncodingContainer](../keyedencodingcontainer.md)

# encode(_:forKey:configuration:)

<sub>Instance Method</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func encode<T>(_ t: T, forKey key: KeyedEncodingContainer<K>.Key, configuration: T.EncodingConfiguration) throws where T : EncodableWithConfiguration
```
