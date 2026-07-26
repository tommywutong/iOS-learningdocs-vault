---
title: Visibility
framework: SwiftUI
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/visibility
source_url: 'https://developer.apple.com/documentation/swiftui/visibility'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/visibility.json'
content_hash: 'sha256:84aad6168523f296'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# Visibility

<sub>Enumeration</sub>

The visibility of a UI element, chosen automatically based on the platform, current context, and other factors.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@frozen enum Visibility
```

## Overview

For example, the preferred visibility of list row separators can be configured using the [listRowSeparator(_:edges:)](<view/listrowseparator(__edges_).md>).

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [CaseIterable](../swift/caseiterable.md), [Copyable](../swift/copyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Getting visibility options

- [Visibility.automatic](visibility/automatic.md) — The element may be visible or hidden depending on the policies of the component accepting the visibility configuration.
- [Visibility.visible](visibility/visible.md) — The element may be visible.
- [Visibility.hidden](visibility/hidden.md) — The element may be hidden.

## See Also

### Hiding system elements

- [labelsHidden()](<view/labelshidden().md>) — Hides the labels of any controls contained within this view.
- [labelsVisibility(_:)](<view/labelsvisibility(__).md>) — Controls the visibility of labels of any controls contained within this view.
- [labelsVisibility](environmentvalues/labelsvisibility.md) — The labels visibility set by [labelsVisibility(_:)](<view/labelsvisibility(__).md>).
- [menuIndicator(_:)](<view/menuindicator(__).md>) — Sets the menu indicator visibility for controls within this view.
- [statusBarHidden(_:)](<view/statusbarhidden(__).md>) — Sets the visibility of the status bar. _(deprecated)_
- [persistentSystemOverlays(_:)](<view/persistentsystemoverlays(__).md>) — Sets the preferred visibility of the non-transient system views overlaying the app.
