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
doc_path: '/documentation/foundation/data/replacesubrange(_:with:)-9u7ry'
source_url: 'https://developer.apple.com/documentation/foundation/data/replacesubrange(_:with:)-9u7ry'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/data/replacesubrange%28_%3Awith%3A%29-9u7ry.json'
content_hash: 'sha256:e98b6056b1ab224e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Data](../data.md)

# replaceSubrange(_:with:)

<sub>Instance Method</sub>

Replaces a region of bytes in the data with new bytes from a collection.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@abi(func repalceSubrangeFast(_ subrange: Range<Data.Index>, with newElements: some Collection<UInt8>)) mutating func replaceSubrange(_ subrange: Range<Data.Index>, with newElements: some Collection<UInt8>)
```

## Parameters

- `subrange` — The range in the data to replace.

- `newElements` — The replacement bytes.

## Discussion

This will resize the data if required, to fit the entire contents of `newElements`.

Precondition: The bounds of `subrange` must be valid indices of the collection.

## See Also

### Replacing a Range of Bytes

- [replaceSubrange(_:with:)](<replacesubrange(__with_)-9nzh.md>) — Replaces a region of bytes in the data with new bytes from a buffer.
- [replaceSubrange(_:with:count:)](<replacesubrange(__with_count_).md>) — Replaces a region of bytes in the data with bytes from memory.
