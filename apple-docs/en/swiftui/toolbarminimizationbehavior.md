---
title: ToolbarMinimizationBehavior
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta, watchOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: /documentation/swiftui/toolbarminimizationbehavior
source_url: 'https://developer.apple.com/documentation/swiftui/toolbarminimizationbehavior'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/toolbarminimizationbehavior.json'
content_hash: 'sha256:13dbd6afdb43b036'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# ToolbarMinimizationBehavior

<sub>Structure</sub>

The minimization behavior of a toolbar.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct ToolbarMinimizationBehavior
```

## Overview

Use this type with the [toolbarMinimizationBehavior(_:for:)](<view/toolbarminimizationbehavior(__for_).md>) modifier to control how toolbars minimize in response to scrolling.

On iOS, you can minimize the navigation bar using [onScrollDown](toolbarminimizationbehavior/onscrolldown.md) or [onScrollUp](toolbarminimizationbehavior/onscrollup.md):

```swift
NavigationStack {
    ScrollView {
        // ...
    }
    .toolbarMinimizationBehavior(
        .onScrollDown, for: .navigationBar)
}
```

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Getting behaviors

- [automatic](toolbarminimizationbehavior/automatic.md) — The system determines the minimize behavior. By default, navigation bars on iOS will minimize when the view has a searchable using the [toolbarPrincipal](searchfieldplacement/toolbarprincipal.md) placement. _(beta)_
- [never](toolbarminimizationbehavior/never.md) — The toolbar cannot be minimized. _(beta)_
- [onScrollDown](toolbarminimizationbehavior/onscrolldown.md) — Minimize when scrolling down. _(beta)_
- [onScrollUp](toolbarminimizationbehavior/onscrollup.md) — Minimize when scrolling up. _(beta)_

## See Also

### Minimizing a toolbar

- [toolbarMinimizationBehavior(_:for:)](<view/toolbarminimizationbehavior(__for_).md>) — Sets the minimize behavior for the specified bars. _(beta)_
- [toolbarMinimizationRestoration(_:for:)](<view/toolbarminimizationrestoration(__for_).md>) — Sets the restoration behavior for the specified bars during minimization. _(beta)_
- [ToolbarMinimizationRestoration](toolbarminimizationrestoration.md) — The restoration behavior during toolbar minimization. _(beta)_
- [toolbarMinimizationSafeAreaAdjustment(_:for:)](<view/toolbarminimizationsafeareaadjustment(__for_).md>) — Sets the safe area adjustment for the specified bars during minimization. _(beta)_
- [ToolbarMinimizationSafeAreaAdjustment](toolbarminimizationsafeareaadjustment.md) — The safe area adjustment during toolbar minimization. _(beta)_
