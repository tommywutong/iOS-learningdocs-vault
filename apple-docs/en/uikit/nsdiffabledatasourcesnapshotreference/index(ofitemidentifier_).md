---
title: 'index(ofItemIdentifier:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/nsdiffabledatasourcesnapshotreference/index(ofitemidentifier:)'
source_url: 'https://developer.apple.com/documentation/uikit/nsdiffabledatasourcesnapshotreference/index(ofitemidentifier:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nsdiffabledatasourcesnapshotreference/index%28ofitemidentifier%3A%29.json'
content_hash: 'sha256:736870a6f66b6242'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSDiffableDataSourceSnapshotReference](../nsdiffabledatasourcesnapshotreference.md)

# index(ofItemIdentifier:)

<sub>Instance Method</sub>

Returns the index of the item in the snapshot with the specified identifier.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func index(ofItemIdentifier itemIdentifier: Any) -> Int
```

## Parameters

- `itemIdentifier` — The identifier of the item in the snapshot.

## Return Value

The index of the item in the snapshot, or `NSNotFound` if the item with the specified identifier doesn’t exist in the snapshot. This index value is 0-based.

## See Also

### Identifying items and sections

- [itemIdentifiers](itemidentifiers.md) — The identifiers of all of the items in the snapshot.
- [sectionIdentifiers](sectionidentifiers.md) — The identifiers of all of the sections in the snapshot.
- [- indexOfSectionIdentifier:](<index(ofsectionidentifier_).md>) — Returns the index of the section of the snapshot with the specified identifier.
- [- itemIdentifiersInSectionWithIdentifier:](<itemidentifiersinsection(withidentifier_).md>) — Returns the identifiers of all of the items in the specified section of the snapshot.
- [- sectionIdentifierForSectionContainingItemIdentifier:](<sectionidentifier(forsectioncontainingitemidentifier_).md>) — Returns the identifier of the section containing the specified item in the snapshot.
