---
title: 'moveSection(withIdentifier:beforeSectionWithIdentifier:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/nsdiffabledatasourcesnapshotreference/movesection(withidentifier:beforesectionwithidentifier:)'
source_url: 'https://developer.apple.com/documentation/uikit/nsdiffabledatasourcesnapshotreference/movesection(withidentifier:beforesectionwithidentifier:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nsdiffabledatasourcesnapshotreference/movesection%28withidentifier%3Abeforesectionwithidentifier%3A%29.json'
content_hash: 'sha256:43dcae72cbab1f2f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSDiffableDataSourceSnapshotReference](../nsdiffabledatasourcesnapshotreference.md)

# moveSection(withIdentifier:beforeSectionWithIdentifier:)

<sub>Instance Method</sub>

Moves the section from its current position in the snapshot to the position immediately before the specified section.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func moveSection(withIdentifier fromSectionIdentifier: Any, beforeSectionWithIdentifier toSectionIdentifier: Any)
```

## Parameters

- `fromSectionIdentifier` — The identifier of the section to move in the snapshot.

- `toSectionIdentifier` — The identifier of the section before which to move the specified section.

## See Also

### Reordering items and sections

- [- moveItemWithIdentifier:afterItemWithIdentifier:](<moveitem(withidentifier_afteritemwithidentifier_).md>) — Moves the item from its current position in the snapshot to the position immediately after the specified item.
- [- moveItemWithIdentifier:beforeItemWithIdentifier:](<moveitem(withidentifier_beforeitemwithidentifier_).md>) — Moves the item from its current position in the snapshot to the position immediately before the specified item.
- [- moveSectionWithIdentifier:afterSectionWithIdentifier:](<movesection(withidentifier_aftersectionwithidentifier_).md>) — Moves the section from its current position in the snapshot to the position immediately after the specified section.
