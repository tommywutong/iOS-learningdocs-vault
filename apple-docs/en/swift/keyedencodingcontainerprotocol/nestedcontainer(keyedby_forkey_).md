---
title: 'nestedContainer(keyedBy:forKey:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/keyedencodingcontainerprotocol/nestedcontainer(keyedby:forkey:)'
source_url: 'https://developer.apple.com/documentation/swift/keyedencodingcontainerprotocol/nestedcontainer(keyedby:forkey:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/keyedencodingcontainerprotocol/nestedcontainer%28keyedby%3Aforkey%3A%29.json'
content_hash: 'sha256:7119118e383bc32b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [KeyedEncodingContainerProtocol](../keyedencodingcontainerprotocol.md)

# nestedContainer(keyedBy:forKey:)

<sub>Instance Method</sub>

Stores a keyed encoding container for the given key and returns it.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func nestedContainer<NestedKey>(keyedBy keyType: NestedKey.Type, forKey key: Self.Key) -> KeyedEncodingContainer<NestedKey> where NestedKey : CodingKey
```

## Parameters

- `keyType` — The key type to use for the container.

- `key` — The key to encode the container for.

## Return Value

A new keyed encoding container.
