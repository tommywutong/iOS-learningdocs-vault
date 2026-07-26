---
title: 'reloadSections(withIdentifiers:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/nsdiffabledatasourcesnapshotreference/reloadsections(withidentifiers:)'
source_url: 'https://developer.apple.com/documentation/uikit/nsdiffabledatasourcesnapshotreference/reloadsections(withidentifiers:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nsdiffabledatasourcesnapshotreference/reloadsections%28withidentifiers%3A%29.json'
content_hash: 'sha256:550eef180c2f0037'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSDiffableDataSourceSnapshotReference](../nsdiffabledatasourcesnapshotreference.md)

# reloadSections(withIdentifiers:)

<sub>Instance Method</sub>

Reloads the data within the specified sections of the snapshot.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func reloadSections(withIdentifiers sectionIdentifiers: [Any])
```

## Parameters

- `sectionIdentifiers` — The array of identifiers corresponding to the sections to reload in the snapshot.

## See Also

### Reloading data

- [- reconfigureItemsWithIdentifiers:](<reconfigureitems(withidentifiers_).md>) — Updates the data for the items you specify in the snapshot, preserving the existing cells for the items.
- [reconfiguredItemIdentifiers](reconfigureditemidentifiers.md) — Identifies the items reconfigured by the changes to the snapshot.
- [- reloadItemsWithIdentifiers:](<reloaditems(withidentifiers_).md>) — Reloads the data within the specified items in the snapshot.
- [reloadedItemIdentifiers](reloadeditemidentifiers.md) — Identifies the items reloaded by the changes to the snapshot.
- [reloadedSectionIdentifiers](reloadedsectionidentifiers.md) — Identifies the sections reloaded by the changes to the snapshot.
