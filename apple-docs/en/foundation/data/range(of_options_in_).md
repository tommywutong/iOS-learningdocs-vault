---
title: 'range(of:options:in:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/data/range(of:options:in:)'
source_url: 'https://developer.apple.com/documentation/foundation/data/range(of:options:in:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/data/range%28of%3Aoptions%3Ain%3A%29.json'
content_hash: 'sha256:89f4173bea02c20e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Data](../data.md)

# range(of:options:in:)

<sub>Instance Method</sub>

Finds the range of the specified data as a subsequence of this data, if it exists.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func range(of dataToFind: Data, options: Data.SearchOptions = [], in range: Range<Data.Index>? = nil) -> Range<Data.Index>?
```

## Parameters

- `dataToFind` — The data to be searched for.

- `options` — Options for the search. Default value is `[]`.

- `range` — The range of this data in which to perform the search. Default value is `nil`, which means the entire content of this data.

## Return Value

A `Range` specifying the location of the found data, or nil if a match could not be found.

## Discussion

Precondition: `range` must be in the bounds of the Data.

## See Also

### Finding Bytes

- [SearchOptions](searchoptions.md) — Options that control a data search operation.
