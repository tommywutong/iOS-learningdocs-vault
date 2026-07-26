---
title: row
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsindexpath/row
source_url: 'https://developer.apple.com/documentation/foundation/nsindexpath/row'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsindexpath/row.json'
content_hash: 'sha256:7d97600343114b09'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSIndexPath](../nsindexpath.md)

# row

<sub>Instance Property</sub>

An index number identifying a row in a section of a table view.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var row: Int { get }
```

## Discussion

The section the row is in is identified by the value of [section](section.md).

## See Also

### Using Special Node Names

- [+ indexPathForRow:inSection:](<init(forrow_insection_).md>) — Initializes an index path with the indexes of a specific row and section in a table view.
- [+ indexPathForItem:inSection:](<init(foritem_insection_).md>) — Initializes an index path with the indexes of a specific item and section in a collection view.
- [section](section.md) — An index number identifying a section in a table view or collection view.
- [item](item.md) — An index number identifying an item in a section of a collection view.
