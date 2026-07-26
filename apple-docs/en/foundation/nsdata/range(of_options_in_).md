---
title: 'range(of:options:in:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsdata/range(of:options:in:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsdata/range(of:options:in:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsdata/range%28of%3Aoptions%3Ain%3A%29.json'
content_hash: 'sha256:29f36145bb32edaa'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSData](../nsdata.md)

# range(of:options:in:)

<sub>Instance Method</sub>

Finds and returns the range of the first occurrence of the given data, within the given range, subject to given options.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func range(of dataToFind: Data, options mask: NSData.SearchOptions = [], in searchRange: NSRange) -> NSRange
```

## Parameters

- `dataToFind` — The data for which to search.

- `mask` — A mask specifying search options. The [SearchOptions](searchoptions.md) options may be specified singly or by combining them with the C bitwise `OR` operator.

- `searchRange` — The range within the receiver in which to search for `dataToFind`. If this range is not within the data object’s range of bytes, [NSRangeException](../nsexceptionname/rangeexception.md) is raised.

## Return Value

An [NSRange](../nsrange-c.struct.md) structure giving the location and length of `dataToFind` within `searchRange`, modulo the options in `mask`. The range returned is relative to the start of the searched data, not the passed-in search range. Returns `{``NSNotFound``, 0}` if `dataToFind` is not found or is empty.

## See Also

### Finding Data

- [- subdataWithRange:](<subdata(with_).md>) — Returns a new data object containing the data object’s bytes that fall within the limits specified by a given range.
- [SearchOptions](searchoptions.md) — Options for method used to search data objects.
