---
title: 'sectionIdentifier(containingItem:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, tvOS 13.0+, visionOS]
languages: [swift, swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/uikit/nsdiffabledatasourcesnapshot-swift.struct/sectionidentifier(containingitem:)'
source_url: 'https://developer.apple.com/documentation/uikit/nsdiffabledatasourcesnapshot-swift.struct/sectionidentifier(containingitem:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nsdiffabledatasourcesnapshot-swift.struct/sectionidentifier%28containingitem%3A%29.json'
content_hash: 'sha256:2849a4a680875080'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSDiffableDataSourceSnapshot](../nsdiffabledatasourcesnapshot-swift.struct.md)

# sectionIdentifier(containingItem:)

<sub>Instance Method</sub>

Returns the identifier of the section containing the specified item in the snapshot.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func sectionIdentifier(containingItem identifier: ItemIdentifierType) -> SectionIdentifierType?
```

## Parameters

- `identifier` — The identifier of the item contained in the section of the snapshot.

## Return Value

The identifier of the section containing the specified item, or `nil` if the specified item doesn’t exist in any section of the snapshot.

## See Also

### Identifying items and sections

- [itemIdentifiers](itemidentifiers.md) — The identifiers of all of the items in the snapshot.
- [sectionIdentifiers](sectionidentifiers.md) — The identifiers of all of the sections in the snapshot.
- [indexOfItem(_:)](<indexofitem(__).md>) — Returns the index of the item in the snapshot with the specified identifier.
- [indexOfSection(_:)](<indexofsection(__).md>) — Returns the index of the section of the snapshot with the specified identifier.
- [itemIdentifiers(inSection:)](<itemidentifiers(insection_).md>) — Returns the identifiers of all of the items in the specified section of the snapshot.
