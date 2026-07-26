---
title: 'nestedContainer(keyedBy:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/unkeyedencodingcontainer/nestedcontainer(keyedby:)'
source_url: 'https://developer.apple.com/documentation/swift/unkeyedencodingcontainer/nestedcontainer(keyedby:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/unkeyedencodingcontainer/nestedcontainer%28keyedby%3A%29.json'
content_hash: 'sha256:cbd7607d276931bb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [UnkeyedEncodingContainer](../unkeyedencodingcontainer.md)

# nestedContainer(keyedBy:)

<sub>Instance Method</sub>

Encodes a nested container keyed by the given type and returns it.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func nestedContainer<NestedKey>(keyedBy keyType: NestedKey.Type) -> KeyedEncodingContainer<NestedKey> where NestedKey : CodingKey
```

## Parameters

- `keyType` — The key type to use for the container.

## Return Value

A new keyed encoding container.
