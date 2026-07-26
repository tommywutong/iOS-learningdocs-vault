---
title: 'replaceSubrange(_:with:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/data/replacesubrange(_:with:)-21ouz'
source_url: 'https://developer.apple.com/documentation/foundation/data/replacesubrange(_:with:)-21ouz'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/data/replacesubrange%28_%3Awith%3A%29-21ouz.json'
content_hash: 'sha256:1f43115b4cd3688f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Data](../data.md)

# replaceSubrange(_:with:)

<sub>Instance Method</sub>

Replaces a region of bytes in the data with new bytes from a collection.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func replaceSubrange(_ subrange: Range<Data.Index>, with newElements: some ContiguousBytes & Collection<UInt8>)
```

## Parameters

- `subrange` — The range in the data to replace.

- `newElements` — The replacement bytes.

## Discussion

This will resize the data if required, to fit the entire contents of `newElements`.

> [!info] Precondition
> The bounds of `subrange` must be valid indices of the collection.
