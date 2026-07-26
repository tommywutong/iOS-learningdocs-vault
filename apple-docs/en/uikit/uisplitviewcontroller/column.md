---
title: UISplitViewController.Column
framework: UIKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, tvOS 14.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uisplitviewcontroller/column
source_url: 'https://developer.apple.com/documentation/uikit/uisplitviewcontroller/column'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uisplitviewcontroller/column.json'
content_hash: 'sha256:ab102f857fc43b1c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISplitViewController](../uisplitviewcontroller.md)

# UISplitViewController.Column

<sub>Enumeration</sub>

Constants that describe the columns within the split view interface.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
enum Column
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Constants

- [UISplitViewControllerColumnPrimary](column/primary.md) — The column for the primary view controller.
- [UISplitViewControllerColumnSupplementary](column/supplementary.md) — The column for the supplementary view controller.
- [UISplitViewControllerColumnSecondary](column/secondary.md) — The column for the secondary, or detail, view controller.
- [UISplitViewControllerColumnCompact](column/compact.md) — The column for the view controller that’s shown when the split view controller is collapsed.
- [UISplitViewControllerColumnInspector](column/inspector.md) — The column for the inspector, or trailing, view controller.

### Initializers

- [init(rawValue:)](<column/init(rawvalue_).md>)

## See Also

### Managing the child view controllers

- [- setViewController:forColumn:](<setviewcontroller(__for_).md>) — Presents the provided view controller in the specified column of the split view interface.
- [- viewControllerForColumn:](<viewcontroller(for_).md>) — Returns the view controller associated with the specified column of the split view interface.
- [viewControllers](viewcontrollers.md) — The array of view controllers the split view controller manages.
