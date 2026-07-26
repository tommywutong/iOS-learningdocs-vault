---
title: 'lastRange(of:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/dataprotocol/lastrange(of:)'
source_url: 'https://developer.apple.com/documentation/foundation/dataprotocol/lastrange(of:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/dataprotocol/lastrange%28of%3A%29.json'
content_hash: 'sha256:9a39530d90cbf503'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [DataProtocol](../dataprotocol.md)

# lastRange(of:)

<sub>Instance Method</sub>

Returns the last found range of the type’s data buffer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func lastRange<D>(of data: D) -> Range<Self.Index>? where D : DataProtocol
```

## Parameters

- `data` — The data sequence to find.

## Return Value

The range, if found, of the last match of the provided data sequence.

## Discussion

An example of searching a data buffer for the last match:

```swift
let data: [UInt8] = [0, 1, 2, 3, 0, 1, 2, 3]
let pattern: [UInt8] = [2, 3]

let match = data.lastRange(of: pattern)
// match == 6..<8

```

## See Also

### Searching Within Data

- [firstRange(of:)](<firstrange(of_).md>) — Returns the first found range of the type’s data buffer.
- [firstRange(of:in:)](<firstrange(of_in_).md>) — Returns the first found range of the type’s data buffer.
- [lastRange(of:in:)](<lastrange(of_in_).md>) — Returns the last found range of the type’s data buffer.
