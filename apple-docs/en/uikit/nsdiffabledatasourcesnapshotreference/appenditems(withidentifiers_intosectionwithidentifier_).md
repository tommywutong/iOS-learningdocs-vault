---
title: 'appendItems(withIdentifiers:intoSectionWithIdentifier:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/nsdiffabledatasourcesnapshotreference/appenditems(withidentifiers:intosectionwithidentifier:)'
source_url: 'https://developer.apple.com/documentation/uikit/nsdiffabledatasourcesnapshotreference/appenditems(withidentifiers:intosectionwithidentifier:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nsdiffabledatasourcesnapshotreference/appenditems%28withidentifiers%3Aintosectionwithidentifier%3A%29.json'
content_hash: 'sha256:496ca4f30ea6ce38'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSDiffableDataSourceSnapshotReference](../nsdiffabledatasourcesnapshotreference.md)

# appendItems(withIdentifiers:intoSectionWithIdentifier:)

<sub>Instance Method</sub>

Adds the items with the specified identifiers to the specified section of the snapshot.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func appendItems(withIdentifiers identifiers: [Any], intoSectionWithIdentifier sectionIdentifier: Any)
```

## Parameters

- `identifiers` — An array of identifiers specifying the items to add to the snapshot.

- `sectionIdentifier` — The section to which to add the items.

## See Also

### Creating a snapshot

- [- appendSectionsWithIdentifiers:](<appendsections(withidentifiers_).md>) — Adds the sections with the specified identifiers to the snapshot.
- [- appendItemsWithIdentifiers:](<appenditems(withidentifiers_).md>) — Adds the items with the specified identifiers to the last section of the snapshot.
