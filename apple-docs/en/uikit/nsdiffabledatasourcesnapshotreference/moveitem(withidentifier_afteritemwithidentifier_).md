---
title: 'moveItem(withIdentifier:afterItemWithIdentifier:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/nsdiffabledatasourcesnapshotreference/moveitem(withidentifier:afteritemwithidentifier:)'
source_url: 'https://developer.apple.com/documentation/uikit/nsdiffabledatasourcesnapshotreference/moveitem(withidentifier:afteritemwithidentifier:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nsdiffabledatasourcesnapshotreference/moveitem%28withidentifier%3Aafteritemwithidentifier%3A%29.json'
content_hash: 'sha256:ce9ce599a14cb968'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSDiffableDataSourceSnapshotReference](../nsdiffabledatasourcesnapshotreference.md)

# moveItem(withIdentifier:afterItemWithIdentifier:)

<sub>Instance Method</sub>

Moves the item from its current position in the snapshot to the position immediately after the specified item.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func moveItem(withIdentifier fromIdentifier: Any, afterItemWithIdentifier toIdentifier: Any)
```

## Parameters

- `fromIdentifier` — The identifier of the item to move in the snapshot.

- `toIdentifier` — The identifier of the item after which to move the specified item.

## See Also

### Reordering items and sections

- [- moveItemWithIdentifier:beforeItemWithIdentifier:](<moveitem(withidentifier_beforeitemwithidentifier_).md>) — Moves the item from its current position in the snapshot to the position immediately before the specified item.
- [- moveSectionWithIdentifier:afterSectionWithIdentifier:](<movesection(withidentifier_aftersectionwithidentifier_).md>) — Moves the section from its current position in the snapshot to the position immediately after the specified section.
- [- moveSectionWithIdentifier:beforeSectionWithIdentifier:](<movesection(withidentifier_beforesectionwithidentifier_).md>) — Moves the section from its current position in the snapshot to the position immediately before the specified section.
