---
title: UINavigationBar.NSToolbarSection
framework: UIKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uinavigationbar/nstoolbarsection
source_url: 'https://developer.apple.com/documentation/uikit/uinavigationbar/nstoolbarsection'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uinavigationbar/nstoolbarsection.json'
content_hash: 'sha256:16433ad1f80d866d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UINavigationBar](../uinavigationbar.md)

# UINavigationBar.NSToolbarSection

<sub>Enumeration</sub>

Constants that determine how the system hosts the navigation bar in an AppKit toolbar.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
enum NSToolbarSection
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Constants

- [UINavigationBarNSToolbarSectionNone](nstoolbarsection/none.md) — A constant that disables hosting the navigation bar in the toolbar.
- [UINavigationBarNSToolbarSectionSidebar](nstoolbarsection/sidebar.md) — A constant that hosts the navigation bar in the toolbar’s sidebar column.
- [UINavigationBarNSToolbarSectionSupplementary](nstoolbarsection/supplementary.md) — A constant that hosts the navigation bar in the toolbar’s supplementary column.
- [UINavigationBarNSToolbarSectionContent](nstoolbarsection/content.md) — A constant that hosts the navigation bar in the toolbar’s content column.

### Initializers

- [init(rawValue:)](<nstoolbarsection/init(rawvalue_).md>)

## See Also

### Building with Mac Catalyst

- [behavioralStyle](behavioralstyle.md) — The behavioral style of the navigation bar.
- [preferredBehavioralStyle](preferredbehavioralstyle.md) — The preferred behavioral style of the navigation bar.
- [currentNSToolbarSection](currentnstoolbarsection.md) — The toolbar section that the navigation bar is currently using.
