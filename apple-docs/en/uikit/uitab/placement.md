---
title: UITab.Placement
framework: UIKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, tvOS 18.0+, visionOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitab/placement
source_url: 'https://developer.apple.com/documentation/uikit/uitab/placement'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitab/placement.json'
content_hash: 'sha256:37d4bc54d2f858e3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITab](../uitab.md)

# UITab.Placement

<sub>Enumeration</sub>

A tab’s placement when displayed in contexts that allow different placement.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
enum Placement
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Placement values

- [UITabPlacementAutomatic](placement/automatic.md) — The system adds only top-level items to the tab bar, but people can add, remove, or move this item.
- [UITabPlacementDefault](placement/default.md) — The item appears in the tab bar, but people can move or remove it.
- [UITabPlacementFixed](placement/fixed.md) — The item appears in the tab bar’s leading edge, and people can’t move or remove it.
- [UITabPlacementMovable](placement/movable.md) — The item appears in the tab bar, people can move it but can’t remove it.
- [UITabPlacementOptional](placement/optional.md) — The item doesn’t appear in the tab bar, but people can add it and move it.
- [UITabPlacementPinned](placement/pinned.md) — The item appears as a pinned tab, on the trailing edge of the tab bar.
- [UITabPlacementSidebarOnly](placement/sidebaronly.md) — The item only appears in the sidebar.

### Initializers

- [init(rawValue:)](<placement/init(rawvalue_).md>)

## See Also

### Managing customization

- [hidden](ishidden.md) — A Boolean value that indicates whether an item is hidden in a sidebar.
- [hiddenByDefault](ishiddenbydefault.md) — A Boolean value that indicates whether an item is hidden by default.
- [allowsHiding](allowshiding.md) — A Boolean value that indicates whether people can hide a tab in a sidebar.
- [preferredPlacement](preferredplacement.md) — The preferred placement for a tab when displayed in contexts that allow different placement.
