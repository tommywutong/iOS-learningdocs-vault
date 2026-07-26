---
title: reloadedItemIdentifiers
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS]
languages: [swift, swift, swift]
beta: false
deprecated: false
doc_path: /documentation/uikit/nsdiffabledatasourcesnapshot-swift.struct/reloadeditemidentifiers
source_url: 'https://developer.apple.com/documentation/uikit/nsdiffabledatasourcesnapshot-swift.struct/reloadeditemidentifiers'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nsdiffabledatasourcesnapshot-swift.struct/reloadeditemidentifiers.json'
content_hash: 'sha256:a500d4622e6b40ce'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSDiffableDataSourceSnapshot](../nsdiffabledatasourcesnapshot-swift.struct.md)

# reloadedItemIdentifiers

<sub>Instance Property</sub>

Identifies the items reloaded by the changes to the snapshot.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var reloadedItemIdentifiers: [ItemIdentifierType] { get }
```

## Discussion

After you make updates to the snapshot, this method returns an array of identifiers corresponding to the items that the view reloads when you apply the snapshot to your data source.

## See Also

### Reloading data

- [reconfigureItems(_:)](<reconfigureitems(__).md>) — Updates the data for the items you specify in the snapshot, preserving the existing cells for the items.
- [reconfiguredItemIdentifiers](reconfigureditemidentifiers.md) — Identifies the items reconfigured by the changes to the snapshot.
- [reloadItems(_:)](<reloaditems(__).md>) — Reloads the data within the specified items in the snapshot.
- [reloadSections(_:)](<reloadsections(__).md>) — Reloads the data within the specified sections of the snapshot.
- [reloadedSectionIdentifiers](reloadedsectionidentifiers.md) — Identifies the sections reloaded by the changes to the snapshot.
