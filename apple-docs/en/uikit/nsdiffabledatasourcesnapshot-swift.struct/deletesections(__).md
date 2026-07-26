---
title: 'deleteSections(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, tvOS 13.0+, visionOS]
languages: [swift, swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/uikit/nsdiffabledatasourcesnapshot-swift.struct/deletesections(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/nsdiffabledatasourcesnapshot-swift.struct/deletesections(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nsdiffabledatasourcesnapshot-swift.struct/deletesections%28_%3A%29.json'
content_hash: 'sha256:ff8cb5f6bc5a10d1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSDiffableDataSourceSnapshot](../nsdiffabledatasourcesnapshot-swift.struct.md)

# deleteSections(_:)

<sub>Instance Method</sub>

Deletes the sections with the specified identifiers from the snapshot.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
mutating func deleteSections(_ identifiers: [SectionIdentifierType])
```

## Parameters

- `identifiers` — The array of identifiers corresponding to the sections to delete from the snapshot.

## See Also

### Removing items and sections

- [deleteAllItems()](<deleteallitems().md>) — Deletes all of the items from the snapshot.
- [deleteItems(_:)](<deleteitems(__).md>) — Deletes the items with the specified identifiers from the snapshot.
