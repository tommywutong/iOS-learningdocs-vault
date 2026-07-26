---
title: 'init(forRow:inSection:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsindexpath/init(forrow:insection:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsindexpath/init(forrow:insection:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsindexpath/init%28forrow%3Ainsection%3A%29.json'
content_hash: 'sha256:09deef50af081bce'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSIndexPath](../nsindexpath.md)

# init(forRow:inSection:)

<sub>Initializer</sub>

Initializes an index path with the indexes of a specific row and section in a table view.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
convenience init(forRow row: Int, inSection section: Int)
```

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
convenience init(row: Int, section: Int)
```

## Parameters

- `row` — An index number identifying a row in a [UITableView](../../uikit/uitableview.md) object in a section identified by `section`.

- `section` — An index number identifying a section in a [UITableView](../../uikit/uitableview.md) object.

## Return Value

An [NSIndexPath](../nsindexpath.md) object.

## See Also

### Using Special Node Names

- [+ indexPathForItem:inSection:](<init(foritem_insection_).md>) — Initializes an index path with the indexes of a specific item and section in a collection view.
- [section](section.md) — An index number identifying a section in a table view or collection view.
- [row](row.md) — An index number identifying a row in a section of a table view.
- [item](item.md) — An index number identifying an item in a section of a collection view.
