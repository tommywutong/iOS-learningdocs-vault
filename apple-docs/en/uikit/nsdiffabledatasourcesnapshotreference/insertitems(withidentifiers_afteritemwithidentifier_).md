---
title: 'insertItems(withIdentifiers:afterItemWithIdentifier:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/nsdiffabledatasourcesnapshotreference/insertitems(withidentifiers:afteritemwithidentifier:)'
source_url: 'https://developer.apple.com/documentation/uikit/nsdiffabledatasourcesnapshotreference/insertitems(withidentifiers:afteritemwithidentifier:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nsdiffabledatasourcesnapshotreference/insertitems%28withidentifiers%3Aafteritemwithidentifier%3A%29.json'
content_hash: 'sha256:3e88f71911d017cb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSDiffableDataSourceSnapshotReference](../nsdiffabledatasourcesnapshotreference.md)

# insertItems(withIdentifiers:afterItemWithIdentifier:)

<sub>Instance Method</sub>

Inserts the provided items immediately after the item with the specified identifier in the snapshot.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func insertItems(withIdentifiers identifiers: [Any], afterItemWithIdentifier itemIdentifier: Any)
```

## Parameters

- `identifiers` — The array of identifiers corresponding to the items to add to the snapshot.

- `itemIdentifier` — The identifier of the item after which to insert the new items.

## See Also

### Inserting items and sections

- [- insertItemsWithIdentifiers:beforeItemWithIdentifier:](<insertitems(withidentifiers_beforeitemwithidentifier_).md>) — Inserts the provided items immediately before the item with the specified identifier in the snapshot.
- [- insertSectionsWithIdentifiers:afterSectionWithIdentifier:](<insertsections(withidentifiers_aftersectionwithidentifier_).md>) — Inserts the provided sections immediately after the section with the specified identifier in the snapshot.
- [- insertSectionsWithIdentifiers:beforeSectionWithIdentifier:](<insertsections(withidentifiers_beforesectionwithidentifier_).md>) — Inserts the provided sections immediately before the section with the specified identifier in the snapshot.
