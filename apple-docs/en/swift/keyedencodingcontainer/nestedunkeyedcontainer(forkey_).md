---
title: 'nestedUnkeyedContainer(forKey:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/keyedencodingcontainer/nestedunkeyedcontainer(forkey:)'
source_url: 'https://developer.apple.com/documentation/swift/keyedencodingcontainer/nestedunkeyedcontainer(forkey:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/keyedencodingcontainer/nestedunkeyedcontainer%28forkey%3A%29.json'
content_hash: 'sha256:5ad27d3e73a154a3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [KeyedEncodingContainer](../keyedencodingcontainer.md)

# nestedUnkeyedContainer(forKey:)

<sub>Instance Method</sub>

Stores an unkeyed encoding container for the given key and returns it.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func nestedUnkeyedContainer(forKey key: KeyedEncodingContainer<K>.Key) -> any UnkeyedEncodingContainer
```

## Parameters

- `key` — The key to encode the container for.

## Return Value

A new unkeyed encoding container.
