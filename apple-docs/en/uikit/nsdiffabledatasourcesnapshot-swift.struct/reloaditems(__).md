---
title: 'reloadItems(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, tvOS 13.0+, visionOS]
languages: [swift, swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/uikit/nsdiffabledatasourcesnapshot-swift.struct/reloaditems(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/nsdiffabledatasourcesnapshot-swift.struct/reloaditems(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nsdiffabledatasourcesnapshot-swift.struct/reloaditems%28_%3A%29.json'
content_hash: 'sha256:44ebbd96bed0c6cb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSDiffableDataSourceSnapshot](../nsdiffabledatasourcesnapshot-swift.struct.md)

# reloadItems(_:)

<sub>Instance Method</sub>

Reloads the data within the specified items in the snapshot.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
mutating func reloadItems(_ identifiers: [ItemIdentifierType])
```

## Parameters

- `identifiers` — The array of identifiers corresponding to the items to reload in the snapshot.

## See Also

### Reloading data

- [reconfigureItems(_:)](<reconfigureitems(__).md>) — Updates the data for the items you specify in the snapshot, preserving the existing cells for the items.
- [reconfiguredItemIdentifiers](reconfigureditemidentifiers.md) — Identifies the items reconfigured by the changes to the snapshot.
- [reloadedItemIdentifiers](reloadeditemidentifiers.md) — Identifies the items reloaded by the changes to the snapshot.
- [reloadSections(_:)](<reloadsections(__).md>) — Reloads the data within the specified sections of the snapshot.
- [reloadedSectionIdentifiers](reloadedsectionidentifiers.md) — Identifies the sections reloaded by the changes to the snapshot.
