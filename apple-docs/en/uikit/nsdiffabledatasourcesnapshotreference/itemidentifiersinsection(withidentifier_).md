---
title: 'itemIdentifiersInSection(withIdentifier:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/nsdiffabledatasourcesnapshotreference/itemidentifiersinsection(withidentifier:)'
source_url: 'https://developer.apple.com/documentation/uikit/nsdiffabledatasourcesnapshotreference/itemidentifiersinsection(withidentifier:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nsdiffabledatasourcesnapshotreference/itemidentifiersinsection%28withidentifier%3A%29.json'
content_hash: 'sha256:9b1272582735180e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSDiffableDataSourceSnapshotReference](../nsdiffabledatasourcesnapshotreference.md)

# itemIdentifiersInSection(withIdentifier:)

<sub>Instance Method</sub>

Returns the identifiers of all of the items in the specified section of the snapshot.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func itemIdentifiersInSection(withIdentifier sectionIdentifier: Any) -> [Any]
```

## Parameters

- `sectionIdentifier` — The identifier of the section of the snapshot.

## Return Value

An array of identifiers of the items contained in the section.

## See Also

### Identifying items and sections

- [itemIdentifiers](itemidentifiers.md) — The identifiers of all of the items in the snapshot.
- [sectionIdentifiers](sectionidentifiers.md) — The identifiers of all of the sections in the snapshot.
- [- indexOfItemIdentifier:](<index(ofitemidentifier_).md>) — Returns the index of the item in the snapshot with the specified identifier.
- [- indexOfSectionIdentifier:](<index(ofsectionidentifier_).md>) — Returns the index of the section of the snapshot with the specified identifier.
- [- sectionIdentifierForSectionContainingItemIdentifier:](<sectionidentifier(forsectioncontainingitemidentifier_).md>) — Returns the identifier of the section containing the specified item in the snapshot.
