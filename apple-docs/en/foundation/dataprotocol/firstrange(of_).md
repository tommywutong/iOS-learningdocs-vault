---
title: 'firstRange(of:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/dataprotocol/firstrange(of:)'
source_url: 'https://developer.apple.com/documentation/foundation/dataprotocol/firstrange(of:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/dataprotocol/firstrange%28of%3A%29.json'
content_hash: 'sha256:a171587627ccda8d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [DataProtocol](../dataprotocol.md)

# firstRange(of:)

<sub>Instance Method</sub>

Returns the first found range of the type’s data buffer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func firstRange<D>(of data: D) -> Range<Self.Index>? where D : DataProtocol
```

## Parameters

- `data` — The data sequence to find.

## Return Value

The range, if found, of the first match of the provided data sequence.

## Discussion

An example of searching a data buffer converted from a string:

```swift
let data = "0123456789".data(using: .utf8)!
let pattern = "456".data(using: .utf8)!
let foundRange = data.firstRange(of: pattern)

// foundRange == Range(4..<7)
```

## See Also

### Searching Within Data

- [firstRange(of:in:)](<firstrange(of_in_).md>) — Returns the first found range of the type’s data buffer.
- [lastRange(of:)](<lastrange(of_).md>) — Returns the last found range of the type’s data buffer.
- [lastRange(of:in:)](<lastrange(of_in_).md>) — Returns the last found range of the type’s data buffer.
