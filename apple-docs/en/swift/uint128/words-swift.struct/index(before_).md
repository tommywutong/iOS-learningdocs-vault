---
title: 'index(before:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/uint128/words-swift.struct/index(before:)'
source_url: 'https://developer.apple.com/documentation/swift/uint128/words-swift.struct/index(before:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/uint128/words-swift.struct/index%28before%3A%29.json'
content_hash: 'sha256:ecc04c169cfd2c2c'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Swift](../../../swift.md) · [UInt128](../../uint128.md) · [Words](../words-swift.struct.md)

# index(before:)

<sub>Instance Method</sub>

Returns the position immediately before the given index.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func index(before i: Int) -> Int
```

## Parameters

- `i` — A valid index of the collection. `i` must be greater than `startIndex`.

## Return Value

The index value immediately before `i`.
