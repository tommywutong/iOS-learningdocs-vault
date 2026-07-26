---
title: 'subdata(with:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsdata/subdata(with:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsdata/subdata(with:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsdata/subdata%28with%3A%29.json'
content_hash: 'sha256:14113f15d3fd80ce'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSData](../nsdata.md)

# subdata(with:)

<sub>Instance Method</sub>

Returns a new data object containing the data object’s bytes that fall within the limits specified by a given range.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func subdata(with range: NSRange) -> Data
```

## Parameters

- `range` — The range in the receiver from which to get the data. If this range is not within the data object’s range of bytes, [NSRangeException](../nsexceptionname/rangeexception.md) is raised.

## Return Value

A data object containing the receiver’s bytes that fall within the limits specified by `range`.

## Discussion

A sample using this method can be found in [Working With Binary Data](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/BinaryData/Tasks/WorkingBinaryData.html#//apple_ref/doc/uid/20000717).

## See Also

### Finding Data

- [- rangeOfData:options:range:](<range(of_options_in_).md>) — Finds and returns the range of the first occurrence of the given data, within the given range, subject to given options.
- [SearchOptions](searchoptions.md) — Options for method used to search data objects.
