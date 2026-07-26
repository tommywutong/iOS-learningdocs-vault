---
title: endIndex
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/data/endindex
source_url: 'https://developer.apple.com/documentation/foundation/data/endindex'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/data/endindex.json'
content_hash: 'sha256:16d3487dcf3f9654'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Data](../data.md)

# endIndex

<sub>Instance Property</sub>

The end index into the data.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var endIndex: Data.Index { get }
```

## Discussion

This is the “one-past-the-end” position, and will always be equal to the `count`.

## See Also

### Manipulating Indexes

- [Index](index.md) — A type used to indicate a position in a data’s buffer.
- [startIndex](startindex.md) — The beginning index into the data.
- [index(after:)](<index(after_).md>) — Returns the index that immediately follows the specified index.
- [index(before:)](<index(before_).md>) — Returns the index that immediately precedes the specified index.
