---
title: 'index(ofSectionIdentifier:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/nsdiffabledatasourcesnapshotreference/index(ofsectionidentifier:)'
source_url: 'https://developer.apple.com/documentation/uikit/nsdiffabledatasourcesnapshotreference/index(ofsectionidentifier:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nsdiffabledatasourcesnapshotreference/index%28ofsectionidentifier%3A%29.json'
content_hash: 'sha256:db8b9a6c3deb1138'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSDiffableDataSourceSnapshotReference](../nsdiffabledatasourcesnapshotreference.md)

# index(ofSectionIdentifier:)

<sub>Instance Method</sub>

Returns the index of the section of the snapshot with the specified identifier.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func index(ofSectionIdentifier sectionIdentifier: Any) -> Int
```

## Parameters

- `sectionIdentifier` — The identifier of the section of the snapshot.

## Return Value

The index of the section of the snapshot, or `NSNotFound` if the section with the specified identifier doesn’t exist in the snapshot. This index value is 0-based.

## See Also

### Identifying items and sections

- [itemIdentifiers](itemidentifiers.md) — The identifiers of all of the items in the snapshot.
- [sectionIdentifiers](sectionidentifiers.md) — The identifiers of all of the sections in the snapshot.
- [- indexOfItemIdentifier:](<index(ofitemidentifier_).md>) — Returns the index of the item in the snapshot with the specified identifier.
- [- itemIdentifiersInSectionWithIdentifier:](<itemidentifiersinsection(withidentifier_).md>) — Returns the identifiers of all of the items in the specified section of the snapshot.
- [- sectionIdentifierForSectionContainingItemIdentifier:](<sectionidentifier(forsectioncontainingitemidentifier_).md>) — Returns the identifier of the section containing the specified item in the snapshot.
