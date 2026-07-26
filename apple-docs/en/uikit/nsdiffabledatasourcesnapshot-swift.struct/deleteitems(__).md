---
title: 'deleteItems(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, tvOS 13.0+, visionOS]
languages: [swift, swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/uikit/nsdiffabledatasourcesnapshot-swift.struct/deleteitems(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/nsdiffabledatasourcesnapshot-swift.struct/deleteitems(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nsdiffabledatasourcesnapshot-swift.struct/deleteitems%28_%3A%29.json'
content_hash: 'sha256:96bf056c05eba756'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSDiffableDataSourceSnapshot](../nsdiffabledatasourcesnapshot-swift.struct.md)

# deleteItems(_:)

<sub>Instance Method</sub>

Deletes the items with the specified identifiers from the snapshot.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
mutating func deleteItems(_ identifiers: [ItemIdentifierType])
```

## Parameters

- `identifiers` — The array of identifiers corresponding to the items to delete from the snapshot.

## See Also

### Removing items and sections

- [deleteAllItems()](<deleteallitems().md>) — Deletes all of the items from the snapshot.
- [deleteSections(_:)](<deletesections(__).md>) — Deletes the sections with the specified identifiers from the snapshot.
