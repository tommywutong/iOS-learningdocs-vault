---
title: reconfiguredItemIdentifiers
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/nsdiffabledatasourcesnapshotreference/reconfigureditemidentifiers
source_url: 'https://developer.apple.com/documentation/uikit/nsdiffabledatasourcesnapshotreference/reconfigureditemidentifiers'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nsdiffabledatasourcesnapshotreference/reconfigureditemidentifiers.json'
content_hash: 'sha256:94b6e9422fc1b12d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSDiffableDataSourceSnapshotReference](../nsdiffabledatasourcesnapshotreference.md)

# reconfiguredItemIdentifiers

<sub>Instance Property</sub>

Identifies the items reconfigured by the changes to the snapshot.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var reconfiguredItemIdentifiers: [Any] { get }
```

## Discussion

After you make updates to the snapshot, this method returns an array of identifiers corresponding to the items that the view reconfigures when you apply the snapshot to your data source.

## See Also

### Reloading data

- [- reconfigureItemsWithIdentifiers:](<reconfigureitems(withidentifiers_).md>) — Updates the data for the items you specify in the snapshot, preserving the existing cells for the items.
- [- reloadItemsWithIdentifiers:](<reloaditems(withidentifiers_).md>) — Reloads the data within the specified items in the snapshot.
- [reloadedItemIdentifiers](reloadeditemidentifiers.md) — Identifies the items reloaded by the changes to the snapshot.
- [- reloadSectionsWithIdentifiers:](<reloadsections(withidentifiers_).md>) — Reloads the data within the specified sections of the snapshot.
- [reloadedSectionIdentifiers](reloadedsectionidentifiers.md) — Identifies the sections reloaded by the changes to the snapshot.
