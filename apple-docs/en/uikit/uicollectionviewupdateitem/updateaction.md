---
title: updateAction
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicollectionviewupdateitem/updateaction
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionviewupdateitem/updateaction'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionviewupdateitem/updateaction.json'
content_hash: 'sha256:80db497793ab1447'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionViewUpdateItem](../uicollectionviewupdateitem.md)

# updateAction

<sub>Instance Property</sub>

The action being performed on the item.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var updateAction: UICollectionViewUpdateItem.Action { get }
```

## Discussion

For a list of relevant action types, see [Action](action.md).

## See Also

### Accessing the item changes

- [indexPathBeforeUpdate](indexpathbeforeupdate.md) — The index path of the item before the update.
- [indexPathAfterUpdate](indexpathafterupdate.md) — The index path of the item after the update.
- [Action](action.md) — Constants indicating the type of action being performed on an item.
