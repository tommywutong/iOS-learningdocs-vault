---
title: 'insertSections(_:beforeSection:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, tvOS 13.0+, visionOS]
languages: [swift, swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/uikit/nsdiffabledatasourcesnapshot-swift.struct/insertsections(_:beforesection:)'
source_url: 'https://developer.apple.com/documentation/uikit/nsdiffabledatasourcesnapshot-swift.struct/insertsections(_:beforesection:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nsdiffabledatasourcesnapshot-swift.struct/insertsections%28_%3Abeforesection%3A%29.json'
content_hash: 'sha256:108ff50570f610c3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSDiffableDataSourceSnapshot](../nsdiffabledatasourcesnapshot-swift.struct.md)

# insertSections(_:beforeSection:)

<sub>Instance Method</sub>

Inserts the provided sections immediately before the section with the specified identifier in the snapshot.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
mutating func insertSections(_ identifiers: [SectionIdentifierType], beforeSection toIdentifier: SectionIdentifierType)
```

## Parameters

- `identifiers` — The array of identifiers corresponding to the sections to add to the snapshot.

- `toIdentifier` — The identifier of the section before which to insert the new sections.

## See Also

### Inserting items and sections

- [insertItems(_:afterItem:)](<insertitems(__afteritem_).md>) — Inserts the provided items immediately after the item with the specified identifier in the snapshot.
- [insertItems(_:beforeItem:)](<insertitems(__beforeitem_).md>) — Inserts the provided items immediately before the item with the specified identifier in the snapshot.
- [insertSections(_:afterSection:)](<insertsections(__aftersection_).md>) — Inserts the provided sections immediately after the section with the specified identifier in the snapshot.
