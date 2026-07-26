---
title: 'appendSections(withIdentifiers:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/nsdiffabledatasourcesnapshotreference/appendsections(withidentifiers:)'
source_url: 'https://developer.apple.com/documentation/uikit/nsdiffabledatasourcesnapshotreference/appendsections(withidentifiers:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nsdiffabledatasourcesnapshotreference/appendsections%28withidentifiers%3A%29.json'
content_hash: 'sha256:d6a3f09074e48828'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSDiffableDataSourceSnapshotReference](../nsdiffabledatasourcesnapshotreference.md)

# appendSections(withIdentifiers:)

<sub>Instance Method</sub>

Adds the sections with the specified identifiers to the snapshot.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func appendSections(withIdentifiers sectionIdentifiers: [Any])
```

## Parameters

- `sectionIdentifiers` — An array of identifiers specifying the sections to add to the snapshot.

## See Also

### Creating a snapshot

- [- appendItemsWithIdentifiers:intoSectionWithIdentifier:](<appenditems(withidentifiers_intosectionwithidentifier_).md>) — Adds the items with the specified identifiers to the specified section of the snapshot.
- [- appendItemsWithIdentifiers:](<appenditems(withidentifiers_).md>) — Adds the items with the specified identifiers to the last section of the snapshot.
