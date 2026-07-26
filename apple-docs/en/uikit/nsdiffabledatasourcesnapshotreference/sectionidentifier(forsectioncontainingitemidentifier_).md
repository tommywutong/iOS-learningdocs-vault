---
title: 'sectionIdentifier(forSectionContainingItemIdentifier:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/nsdiffabledatasourcesnapshotreference/sectionidentifier(forsectioncontainingitemidentifier:)'
source_url: 'https://developer.apple.com/documentation/uikit/nsdiffabledatasourcesnapshotreference/sectionidentifier(forsectioncontainingitemidentifier:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nsdiffabledatasourcesnapshotreference/sectionidentifier%28forsectioncontainingitemidentifier%3A%29.json'
content_hash: 'sha256:3538575d43d1973e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSDiffableDataSourceSnapshotReference](../nsdiffabledatasourcesnapshotreference.md)

# sectionIdentifier(forSectionContainingItemIdentifier:)

<sub>Instance Method</sub>

Returns the identifier of the section containing the specified item in the snapshot.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func sectionIdentifier(forSectionContainingItemIdentifier itemIdentifier: Any) -> Any?
```

## Parameters

- `itemIdentifier` — The identifier of the item contained in the section of the snapshot.

## Return Value

The identifier of the section containing the specified item, or `nil` if the specified item doesn’t exist in any section of the snapshot.

## See Also

### Identifying items and sections

- [itemIdentifiers](itemidentifiers.md) — The identifiers of all of the items in the snapshot.
- [sectionIdentifiers](sectionidentifiers.md) — The identifiers of all of the sections in the snapshot.
- [- indexOfItemIdentifier:](<index(ofitemidentifier_).md>) — Returns the index of the item in the snapshot with the specified identifier.
- [- indexOfSectionIdentifier:](<index(ofsectionidentifier_).md>) — Returns the index of the section of the snapshot with the specified identifier.
- [- itemIdentifiersInSectionWithIdentifier:](<itemidentifiersinsection(withidentifier_).md>) — Returns the identifiers of all of the items in the specified section of the snapshot.
