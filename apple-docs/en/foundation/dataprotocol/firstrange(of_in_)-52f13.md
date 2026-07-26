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
doc_path: '/documentation/foundation/dataprotocol/firstrange(of:in:)-52f13'
source_url: 'https://developer.apple.com/documentation/foundation/dataprotocol/firstrange(of:in:)-52f13'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/dataprotocol/firstrange%28of%3Ain%3A%29-52f13.json'
content_hash: 'sha256:16f8cc15ab31a904'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [DataProtocol](../dataprotocol.md)

# firstRange(of:in:)

<sub>Instance Method</sub>

Returns the first found range of the type’s data buffer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func firstRange<D, R>(of data: D, in range: R) -> Range<Self.Index>? where D : DataProtocol, R : RangeExpression, Self.Index == R.Bound
```

## Parameters

- `data` — The data sequence to find.

- `range` — A range to limit the scope of the search.

## Return Value

The range, if found, of the first match of the provided data sequence.
