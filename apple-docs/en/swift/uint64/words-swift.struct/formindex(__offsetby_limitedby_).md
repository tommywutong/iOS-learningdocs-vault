---
title: 'formIndex(_:offsetBy:limitedBy:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/uint64/words-swift.struct/formindex(_:offsetby:limitedby:)'
source_url: 'https://developer.apple.com/documentation/swift/uint64/words-swift.struct/formindex(_:offsetby:limitedby:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/uint64/words-swift.struct/formindex%28_%3Aoffsetby%3Alimitedby%3A%29.json'
content_hash: 'sha256:c926f9512c16f235'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Swift](../../../swift.md) · [UInt64](../../uint64.md) · [Words](../words-swift.struct.md)

# formIndex(_:offsetBy:limitedBy:)

<sub>Instance Method</sub>

Offsets the given index by the specified distance, or so that it equals the given limiting index.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func formIndex(_ i: inout Self.Index, offsetBy distance: Int, limitedBy limit: Self.Index) -> Bool
```

## Parameters

- `i` — A valid index of the collection.

- `distance` — The distance to offset `i`. `distance` must not be negative unless the collection conforms to the `BidirectionalCollection` protocol.

- `limit` — A valid index of the collection to use as a limit. If `distance > 0`, a limit that is less than `i` has no effect. Likewise, if `distance < 0`, a limit that is greater than `i` has no effect.

## Return Value

`true` if `i` has been offset by exactly `distance` steps without going beyond `limit`; otherwise, `false`. When the return value is `false`, the value of `i` is equal to `limit`.

## Discussion

The value passed as `distance` must not offset `i` beyond the bounds of the collection, unless the index passed as `limit` prevents offsetting beyond those bounds.

> [!abstract] Complexity
> O(1) if the collection conforms to `RandomAccessCollection`; otherwise, O(_k_), where _k_ is the absolute value of `distance`.
