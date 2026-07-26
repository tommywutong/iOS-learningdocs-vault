---
title: 'itemIdentifiers(inSection:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, tvOS 13.0+, visionOS]
languages: [swift, swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/uikit/nsdiffabledatasourcesnapshot-swift.struct/itemidentifiers(insection:)'
source_url: 'https://developer.apple.com/documentation/uikit/nsdiffabledatasourcesnapshot-swift.struct/itemidentifiers(insection:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nsdiffabledatasourcesnapshot-swift.struct/itemidentifiers%28insection%3A%29.json'
content_hash: 'sha256:fd44b9fb7e2ea2d9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSDiffableDataSourceSnapshot](../nsdiffabledatasourcesnapshot-swift.struct.md)

# itemIdentifiers(inSection:)

<sub>Instance Method</sub>

Returns the identifiers of all of the items in the specified section of the snapshot.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func itemIdentifiers(inSection identifier: SectionIdentifierType) -> [ItemIdentifierType]
```

## Parameters

- `identifier` — The identifier of the section of the snapshot.

## Return Value

An array of identifiers of the items contained in the section.

## See Also

### Identifying items and sections

- [itemIdentifiers](itemidentifiers.md) — The identifiers of all of the items in the snapshot.
- [sectionIdentifiers](sectionidentifiers.md) — The identifiers of all of the sections in the snapshot.
- [indexOfItem(_:)](<indexofitem(__).md>) — Returns the index of the item in the snapshot with the specified identifier.
- [indexOfSection(_:)](<indexofsection(__).md>) — Returns the index of the section of the snapshot with the specified identifier.
- [sectionIdentifier(containingItem:)](<sectionidentifier(containingitem_).md>) — Returns the identifier of the section containing the specified item in the snapshot.
