---
title: 'contains(_:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/keyeddecodingcontainerprotocol/contains(_:)'
source_url: 'https://developer.apple.com/documentation/swift/keyeddecodingcontainerprotocol/contains(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/keyeddecodingcontainerprotocol/contains%28_%3A%29.json'
content_hash: 'sha256:cd59c87c29eeac32'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [KeyedDecodingContainerProtocol](../keyeddecodingcontainerprotocol.md)

# contains(_:)

<sub>Instance Method</sub>

Returns a Boolean value indicating whether the decoder contains a value associated with the given key.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func contains(_ key: Self.Key) -> Bool
```

## Parameters

- `key` — The key to search for.

## Return Value

Whether the `Decoder` has an entry for the given key.

## Discussion

The value associated with `key` may be a null value as appropriate for the data format.
