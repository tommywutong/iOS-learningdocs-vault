---
title: 'insertItems(_:beforeItem:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, tvOS 13.0+, visionOS]
languages: [swift, swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/uikit/nsdiffabledatasourcesnapshot-swift.struct/insertitems(_:beforeitem:)'
source_url: 'https://developer.apple.com/documentation/uikit/nsdiffabledatasourcesnapshot-swift.struct/insertitems(_:beforeitem:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nsdiffabledatasourcesnapshot-swift.struct/insertitems%28_%3Abeforeitem%3A%29.json'
content_hash: 'sha256:c2e296deef39e214'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSDiffableDataSourceSnapshot](../nsdiffabledatasourcesnapshot-swift.struct.md)

# insertItems(_:beforeItem:)

<sub>Instance Method</sub>

Inserts the provided items immediately before the item with the specified identifier in the snapshot.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
mutating func insertItems(_ identifiers: [ItemIdentifierType], beforeItem beforeIdentifier: ItemIdentifierType)
```

## Parameters

- `identifiers` — The array of identifiers corresponding to the items to add to the snapshot.

- `beforeIdentifier` — The identifier of the item before which to insert the new items.

## See Also

### Inserting items and sections

- [insertItems(_:afterItem:)](<insertitems(__afteritem_).md>) — Inserts the provided items immediately after the item with the specified identifier in the snapshot.
- [insertSections(_:afterSection:)](<insertsections(__aftersection_).md>) — Inserts the provided sections immediately after the section with the specified identifier in the snapshot.
- [insertSections(_:beforeSection:)](<insertsections(__beforesection_).md>) — Inserts the provided sections immediately before the section with the specified identifier in the snapshot.
