---
title: NSToolbarItemGroup.SelectionMode
framework: AppKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/appkit/nstoolbaritemgroup/selectionmode-swift.enum
source_url: 'https://developer.apple.com/documentation/appkit/nstoolbaritemgroup/selectionmode-swift.enum'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/appkit/nstoolbaritemgroup/selectionmode-swift.enum.json'
content_hash: 'sha256:abbb5508b7341d7e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AppKit](../../appkit.md) · [NSToolbarItemGroup](../nstoolbaritemgroup.md)

# NSToolbarItemGroup.SelectionMode

<sub>Enumeration</sub>

A value that indicates how a grouped toolbar item selects its subitems.

<sub>Mac Catalyst, macOS</sub>

```swift
enum SelectionMode
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Selection modes

- [NSToolbarItemGroupSelectionModeMomentary](selectionmode-swift.enum/momentary.md) — The system temporarily highlights the select group item when the user selects the item.
- [NSToolbarItemGroupSelectionModeSelectAny](selectionmode-swift.enum/selectany.md) — The system toggles a highlight on any item selected.
- [NSToolbarItemGroupSelectionModeSelectOne](selectionmode-swift.enum/selectone.md) — The system displays a highlighted mode on the most recent item selected.

### Initializers

- [init(rawValue:)](<selectionmode-swift.enum/init(rawvalue_).md>)

## See Also

### Items

- [NSToolbarItem](../nstoolbaritem.md) — A single item that appears in a window’s toolbar.
- [NSToolbarItemGroup](../nstoolbaritemgroup.md) — A group of subitems in a toolbar item.
- [ControlRepresentation](controlrepresentation-swift.enum.md)
- [NSMenuToolbarItem](../nsmenutoolbaritem.md) — A control that presents a menu in a window’s toolbar.
- [NSSearchToolbarItem](../nssearchtoolbaritem.md) — A toolbar item that contains a search field optimized for performing text-based searches.
- [NSTrackingSeparatorToolbarItem](../nstrackingseparatortoolbaritem.md) — A toolbar separator that aligns with the vertical split view in the same window.
