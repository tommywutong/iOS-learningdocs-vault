---
title: 'distance(from:to:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/uint8/words-swift.struct/distance(from:to:)'
source_url: 'https://developer.apple.com/documentation/swift/uint8/words-swift.struct/distance(from:to:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/uint8/words-swift.struct/distance%28from%3Ato%3A%29.json'
content_hash: 'sha256:a8917625f2fa2a57'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Swift](../../../swift.md) · [UInt8](../../uint8.md) · [Words](../words-swift.struct.md)

# distance(from:to:)

<sub>Instance Method</sub>

Returns the distance between two indices.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func distance(from start: Self.Index, to end: Self.Index) -> Self.Index.Stride
```

## Parameters

- `start` — A valid index of the collection.

- `end` — Another valid index of the collection. If `end` is equal to `start`, the result is zero.

## Return Value

The distance between `start` and `end`.

## Discussion

> [!abstract] Complexity
> O(1)
