---
title: 'index(after:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/indexset/index(after:)'
source_url: 'https://developer.apple.com/documentation/foundation/indexset/index(after:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/indexset/index%28after%3A%29.json'
content_hash: 'sha256:d1ec19a1a11feb1c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [IndexSet](../indexset.md)

# index(after:)

<sub>Instance Method</sub>

Returns the index that follows the given index in the set.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func index(after i: IndexSet.Index) -> IndexSet.Index
```

## See Also

### Manipulating Indexes

- [startIndex](startindex.md) — The beginning index in the set.
- [endIndex](endindex.md) — The ending index in the set.
- [index(before:)](<index(before_).md>) — Returns the index that precedes the given index in the set.
- [formIndex(after:)](<formindex(after_).md>) — Modifies the given index to refer to the item after the one it currently refers to.
- [formIndex(before:)](<formindex(before_).md>) — Modifies the given index to refer to the item before the one it currently refers to.
- [indexRange(in:)](<indexrange(in_)-539lz.md>) — Return a `Range<IndexSet.Index>` which can be used to subscript the index set.
