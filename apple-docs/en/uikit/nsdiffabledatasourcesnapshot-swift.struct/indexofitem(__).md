---
title: 'indexOfItem(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, tvOS 13.0+, visionOS]
languages: [swift, swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/uikit/nsdiffabledatasourcesnapshot-swift.struct/indexofitem(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/nsdiffabledatasourcesnapshot-swift.struct/indexofitem(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nsdiffabledatasourcesnapshot-swift.struct/indexofitem%28_%3A%29.json'
content_hash: 'sha256:89d4ef7dd228c125'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSDiffableDataSourceSnapshot](../nsdiffabledatasourcesnapshot-swift.struct.md)

# indexOfItem(_:)

<sub>Instance Method</sub>

Returns the index of the item in the snapshot with the specified identifier.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func indexOfItem(_ identifier: ItemIdentifierType) -> Int?
```

## Parameters

- `identifier` — The identifier of the item in the snapshot.

## Return Value

The index of the item in the snapshot, or `nil` if the item with the specified identifier doesn’t exist in the snapshot. This index value is 0-based.

## See Also

### Identifying items and sections

- [itemIdentifiers](itemidentifiers.md) — The identifiers of all of the items in the snapshot.
- [sectionIdentifiers](sectionidentifiers.md) — The identifiers of all of the sections in the snapshot.
- [indexOfSection(_:)](<indexofsection(__).md>) — Returns the index of the section of the snapshot with the specified identifier.
- [itemIdentifiers(inSection:)](<itemidentifiers(insection_).md>) — Returns the identifiers of all of the items in the specified section of the snapshot.
- [sectionIdentifier(containingItem:)](<sectionidentifier(containingitem_).md>) — Returns the identifier of the section containing the specified item in the snapshot.
