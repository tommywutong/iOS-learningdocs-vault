---
title: 'lastRange(of:in:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/dataprotocol/lastrange(of:in:)'
source_url: 'https://developer.apple.com/documentation/foundation/dataprotocol/lastrange(of:in:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/dataprotocol/lastrange%28of%3Ain%3A%29.json'
content_hash: 'sha256:01b10fe42771af4f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [DataProtocol](../dataprotocol.md)

# lastRange(of:in:)

<sub>Instance Method</sub>

Returns the last found range of the type’s data buffer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func lastRange<D, R>(of: D, in: R) -> Range<Self.Index>? where D : DataProtocol, R : RangeExpression, Self.Index == R.Bound
```

## Parameters

- `of` — The data sequence to find.

- `in` — A range to limit the scope of the search.

## Return Value

The range, if found, of the last match of the provided data sequence.

## Discussion

An example of searching a constrained range within a data buffer for the last match:

```swift
let data: [UInt8] = [0, 1, 2, 3, 0, 1, 2, 3, 0, 1, 2, 3]
let pattern: [UInt8] = [2, 3]

let match = data.lastRange(of: pattern, in: 0...9)
// match == 6..<8
```

## Default Implementations

### DataProtocol Implementations

- [lastRange(of:in:)](<lastrange(of_in_)-4enyx.md>) — Returns the last found range of the type’s data buffer.

## See Also

### Searching Within Data

- [firstRange(of:)](<firstrange(of_).md>) — Returns the first found range of the type’s data buffer.
- [firstRange(of:in:)](<firstrange(of_in_).md>) — Returns the first found range of the type’s data buffer.
- [lastRange(of:)](<lastrange(of_).md>) — Returns the last found range of the type’s data buffer.
