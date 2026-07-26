---
title: 'init(forItem:inSection:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsindexpath/init(foritem:insection:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsindexpath/init(foritem:insection:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsindexpath/init%28foritem%3Ainsection%3A%29.json'
content_hash: 'sha256:ca3b4d904015115b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSIndexPath](../nsindexpath.md)

# init(forItem:inSection:)

<sub>Initializer</sub>

Initializes an index path with the indexes of a specific item and section in a collection view.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
convenience init(forItem item: Int, inSection section: Int)
```

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
convenience init(item: Int, section: Int)
```

<sub>macOS</sub>

```swift
init(forItem item: Int, inSection section: Int)
```

## Parameters

- `item` — An index number identifying an item in a [UICollectionView](../../uikit/uicollectionview.md) object in a section identified by the `section` parameter.

- `section` — An index number identifying a section in a [UICollectionView](../../uikit/uicollectionview.md) object.

## Return Value

An [NSIndexPath](../nsindexpath.md) object.

## See Also

### Using Special Node Names

- [+ indexPathForRow:inSection:](<init(forrow_insection_).md>) — Initializes an index path with the indexes of a specific row and section in a table view.
- [section](section.md) — An index number identifying a section in a table view or collection view.
- [row](row.md) — An index number identifying a row in a section of a table view.
- [item](item.md) — An index number identifying an item in a section of a collection view.
