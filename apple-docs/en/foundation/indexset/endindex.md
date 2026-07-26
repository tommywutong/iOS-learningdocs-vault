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
doc_path: /documentation/foundation/indexset/endindex
source_url: 'https://developer.apple.com/documentation/foundation/indexset/endindex'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/indexset/endindex.json'
content_hash: 'sha256:23776f6caa08a128'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [IndexSet](../indexset.md)

# endIndex

<sub>Instance Property</sub>

The ending index in the set.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var endIndex: IndexSet.Index { get }
```

## See Also

### Manipulating Indexes

- [startIndex](startindex.md) — The beginning index in the set.
- [index(after:)](<index(after_).md>) — Returns the index that follows the given index in the set.
- [index(before:)](<index(before_).md>) — Returns the index that precedes the given index in the set.
- [formIndex(after:)](<formindex(after_).md>) — Modifies the given index to refer to the item after the one it currently refers to.
- [formIndex(before:)](<formindex(before_).md>) — Modifies the given index to refer to the item before the one it currently refers to.
- [indexRange(in:)](<indexrange(in_)-539lz.md>) — Return a `Range<IndexSet.Index>` which can be used to subscript the index set.
