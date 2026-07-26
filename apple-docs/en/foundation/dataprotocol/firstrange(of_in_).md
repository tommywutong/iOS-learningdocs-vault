---
title: 'firstRange(of:in:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/dataprotocol/firstrange(of:in:)'
source_url: 'https://developer.apple.com/documentation/foundation/dataprotocol/firstrange(of:in:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/dataprotocol/firstrange%28of%3Ain%3A%29.json'
content_hash: 'sha256:8e835a8200b41488'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [DataProtocol](../dataprotocol.md)

# firstRange(of:in:)

<sub>Instance Method</sub>

Returns the first found range of the type’s data buffer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func firstRange<D, R>(of: D, in: R) -> Range<Self.Index>? where D : DataProtocol, R : RangeExpression, Self.Index == R.Bound
```

## Parameters

- `of` — The data sequence to find.

- `in` — A range to limit the scope of the search.

## Return Value

The range, if found, of the first match of the provided data sequence.

## Discussion

An example of searching a constrained range within a data buffer for the first match:

```swift
let data: [UInt8] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
let pattern: [UInt8] = [2, 3, 4]

let possibleMatch = data.firstRange(of: pattern, in: 5...9)
// possibleMatch == nil

let match = data.firstRange(of: pattern, in: 2...9)
// match == 2..<5
```

## Default Implementations

### DataProtocol Implementations

- [firstRange(of:in:)](<firstrange(of_in_)-52f13.md>) — Returns the first found range of the type’s data buffer.

## See Also

### Searching Within Data

- [firstRange(of:)](<firstrange(of_).md>) — Returns the first found range of the type’s data buffer.
- [lastRange(of:)](<lastrange(of_).md>) — Returns the last found range of the type’s data buffer.
- [lastRange(of:in:)](<lastrange(of_in_).md>) — Returns the last found range of the type’s data buffer.
