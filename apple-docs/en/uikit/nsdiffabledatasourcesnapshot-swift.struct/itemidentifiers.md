---
title: itemIdentifiers
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, tvOS 13.0+, visionOS]
languages: [swift, swift, swift]
beta: false
deprecated: false
doc_path: /documentation/uikit/nsdiffabledatasourcesnapshot-swift.struct/itemidentifiers
source_url: 'https://developer.apple.com/documentation/uikit/nsdiffabledatasourcesnapshot-swift.struct/itemidentifiers'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nsdiffabledatasourcesnapshot-swift.struct/itemidentifiers.json'
content_hash: 'sha256:e025e541af44badd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSDiffableDataSourceSnapshot](../nsdiffabledatasourcesnapshot-swift.struct.md)

# itemIdentifiers

<sub>Instance Property</sub>

The identifiers of all of the items in the snapshot.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var itemIdentifiers: [ItemIdentifierType] { get }
```

## See Also

### Identifying items and sections

- [sectionIdentifiers](sectionidentifiers.md) — The identifiers of all of the sections in the snapshot.
- [indexOfItem(_:)](<indexofitem(__).md>) — Returns the index of the item in the snapshot with the specified identifier.
- [indexOfSection(_:)](<indexofsection(__).md>) — Returns the index of the section of the snapshot with the specified identifier.
- [itemIdentifiers(inSection:)](<itemidentifiers(insection_).md>) — Returns the identifiers of all of the items in the specified section of the snapshot.
- [sectionIdentifier(containingItem:)](<sectionidentifier(containingitem_).md>) — Returns the identifier of the section containing the specified item in the snapshot.
