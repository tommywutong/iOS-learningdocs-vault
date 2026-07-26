---
title: 'moveSection(_:beforeSection:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, tvOS 13.0+, visionOS]
languages: [swift, swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/uikit/nsdiffabledatasourcesnapshot-swift.struct/movesection(_:beforesection:)'
source_url: 'https://developer.apple.com/documentation/uikit/nsdiffabledatasourcesnapshot-swift.struct/movesection(_:beforesection:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nsdiffabledatasourcesnapshot-swift.struct/movesection%28_%3Abeforesection%3A%29.json'
content_hash: 'sha256:6daa95e6d0c52ca7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSDiffableDataSourceSnapshot](../nsdiffabledatasourcesnapshot-swift.struct.md)

# moveSection(_:beforeSection:)

<sub>Instance Method</sub>

Moves the section from its current position in the snapshot to the position immediately before the specified section.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
mutating func moveSection(_ identifier: SectionIdentifierType, beforeSection toIdentifier: SectionIdentifierType)
```

## Parameters

- `identifier` — The identifier of the section to move in the snapshot.

- `toIdentifier` — The identifier of the section before which to move the specified section.

## See Also

### Reordering items and sections

- [moveItem(_:afterItem:)](<moveitem(__afteritem_).md>) — Moves the item from its current position in the snapshot to the position immediately after the specified item.
- [moveItem(_:beforeItem:)](<moveitem(__beforeitem_).md>) — Moves the item from its current position in the snapshot to the position immediately before the specified item.
- [moveSection(_:afterSection:)](<movesection(__aftersection_).md>) — Moves the section from its current position in the snapshot to the position immediately after the specified section.
