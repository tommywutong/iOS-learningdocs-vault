---
title: 'insertSections(withIdentifiers:afterSectionWithIdentifier:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/nsdiffabledatasourcesnapshotreference/insertsections(withidentifiers:aftersectionwithidentifier:)'
source_url: 'https://developer.apple.com/documentation/uikit/nsdiffabledatasourcesnapshotreference/insertsections(withidentifiers:aftersectionwithidentifier:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nsdiffabledatasourcesnapshotreference/insertsections%28withidentifiers%3Aaftersectionwithidentifier%3A%29.json'
content_hash: 'sha256:aa7e47d562047ddd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSDiffableDataSourceSnapshotReference](../nsdiffabledatasourcesnapshotreference.md)

# insertSections(withIdentifiers:afterSectionWithIdentifier:)

<sub>Instance Method</sub>

Inserts the provided sections immediately after the section with the specified identifier in the snapshot.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func insertSections(withIdentifiers sectionIdentifiers: [Any], afterSectionWithIdentifier toSectionIdentifier: Any)
```

## Parameters

- `sectionIdentifiers` — The array of identifiers corresponding to the sections to add to the snapshot.

- `toSectionIdentifier` — The identifier of the section after which to insert the new sections.

## See Also

### Inserting items and sections

- [- insertItemsWithIdentifiers:afterItemWithIdentifier:](<insertitems(withidentifiers_afteritemwithidentifier_).md>) — Inserts the provided items immediately after the item with the specified identifier in the snapshot.
- [- insertItemsWithIdentifiers:beforeItemWithIdentifier:](<insertitems(withidentifiers_beforeitemwithidentifier_).md>) — Inserts the provided items immediately before the item with the specified identifier in the snapshot.
- [- insertSectionsWithIdentifiers:beforeSectionWithIdentifier:](<insertsections(withidentifiers_beforesectionwithidentifier_).md>) — Inserts the provided sections immediately before the section with the specified identifier in the snapshot.
