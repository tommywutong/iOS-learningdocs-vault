---
title: ToolbarMinimizationRestoration
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta, watchOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: /documentation/swiftui/toolbarminimizationrestoration
source_url: 'https://developer.apple.com/documentation/swiftui/toolbarminimizationrestoration'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/toolbarminimizationrestoration.json'
content_hash: 'sha256:10b1b0d01d650d91'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# ToolbarMinimizationRestoration

<sub>Structure</sub>

The restoration behavior during toolbar minimization.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct ToolbarMinimizationRestoration
```

## Overview

Use this type with the [toolbarMinimizationRestoration(_:for:)](<view/toolbarminimizationrestoration(__for_).md>) modifier to control when a minimized toolbar restores. By default the toolbar restores when the user reverses scroll direction; with [atScrollEdge](toolbarminimizationrestoration/atscrolledge.md), the toolbar instead restores only when the scroll view’s content reaches the scroll edge – appropriate for screens where the bar is mostly chrome that doesn’t need to follow the user.

```swift
.toolbarMinimizationBehavior(
    .onScrollDown, for: .navigationBar)
.toolbarMinimizationRestoration(
    .atScrollEdge, for: .navigationBar)
```

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Getting restoration options

- [atScrollEdge](toolbarminimizationrestoration/atscrolledge.md) — The toolbar restores only when the scroll view’s content reaches the scroll edge. _(beta)_
- [automatic](toolbarminimizationrestoration/automatic.md) — The system determines the restoration behavior. _(beta)_

## See Also

### Minimizing a toolbar

- [toolbarMinimizationBehavior(_:for:)](<view/toolbarminimizationbehavior(__for_).md>) — Sets the minimize behavior for the specified bars. _(beta)_
- [ToolbarMinimizationBehavior](toolbarminimizationbehavior.md) — The minimization behavior of a toolbar. _(beta)_
- [toolbarMinimizationRestoration(_:for:)](<view/toolbarminimizationrestoration(__for_).md>) — Sets the restoration behavior for the specified bars during minimization. _(beta)_
- [toolbarMinimizationSafeAreaAdjustment(_:for:)](<view/toolbarminimizationsafeareaadjustment(__for_).md>) — Sets the safe area adjustment for the specified bars during minimization. _(beta)_
- [ToolbarMinimizationSafeAreaAdjustment](toolbarminimizationsafeareaadjustment.md) — The safe area adjustment during toolbar minimization. _(beta)_
