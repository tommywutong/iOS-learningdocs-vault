---
title: 'indexRange(in:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/indexset/indexrange(in:)-539lz'
source_url: 'https://developer.apple.com/documentation/foundation/indexset/indexrange(in:)-539lz'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/indexset/indexrange%28in%3A%29-539lz.json'
content_hash: 'sha256:93bbe39b95be164e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [IndexSet](../indexset.md)

# indexRange(in:)

<sub>Instance Method</sub>

Return a `Range<IndexSet.Index>` which can be used to subscript the index set.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func indexRange(in range: Range<IndexSet.Element>) -> Range<IndexSet.Index>
```

## Parameters

- `range` — The range of integers to include.

## Discussion

The resulting range is the range of the intersection of the integers in `range` with the index set. The resulting range will be `isEmpty` if the intersection is empty.

## See Also

### Manipulating Indexes

- [startIndex](startindex.md) — The beginning index in the set.
- [endIndex](endindex.md) — The ending index in the set.
- [index(after:)](<index(after_).md>) — Returns the index that follows the given index in the set.
- [index(before:)](<index(before_).md>) — Returns the index that precedes the given index in the set.
- [formIndex(after:)](<formindex(after_).md>) — Modifies the given index to refer to the item after the one it currently refers to.
- [formIndex(before:)](<formindex(before_).md>) — Modifies the given index to refer to the item before the one it currently refers to.
