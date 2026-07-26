---
title: ToolbarMinimizationSafeAreaAdjustment
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta, watchOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: /documentation/swiftui/toolbarminimizationsafeareaadjustment
source_url: 'https://developer.apple.com/documentation/swiftui/toolbarminimizationsafeareaadjustment'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/toolbarminimizationsafeareaadjustment.json'
content_hash: 'sha256:c85dd4baa6f1678f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# ToolbarMinimizationSafeAreaAdjustment

<sub>Structure</sub>

The safe area adjustment during toolbar minimization.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct ToolbarMinimizationSafeAreaAdjustment
```

## Overview

Use this type with the [toolbarMinimizationSafeAreaAdjustment(_:for:)](<view/toolbarminimizationsafeareaadjustment(__for_).md>) modifier to control whether the safe area updates as bars minimize. By default the safe area adjusts interactively, but you can disable this to keep content in place – for example, when displaying full-bleed media beneath a minimizing bar.

```swift
.toolbarMinimizationBehavior(
    .onScrollDown, for: .navigationBar)
.toolbarMinimizationSafeAreaAdjustment(
    .disabled, for: .navigationBar)
```

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Minimization adjustment options

- [automatic](toolbarminimizationsafeareaadjustment/automatic.md) — The system determines the safe area adjustment. _(beta)_
- [disabled](toolbarminimizationsafeareaadjustment/disabled.md) — The safe area remains unchanged as bars minimize. _(beta)_
- [enabled](toolbarminimizationsafeareaadjustment/enabled.md) — The safe area adjusts interactively as bars minimize. _(beta)_

## See Also

### Minimizing a toolbar

- [toolbarMinimizationBehavior(_:for:)](<view/toolbarminimizationbehavior(__for_).md>) — Sets the minimize behavior for the specified bars. _(beta)_
- [ToolbarMinimizationBehavior](toolbarminimizationbehavior.md) — The minimization behavior of a toolbar. _(beta)_
- [toolbarMinimizationRestoration(_:for:)](<view/toolbarminimizationrestoration(__for_).md>) — Sets the restoration behavior for the specified bars during minimization. _(beta)_
- [ToolbarMinimizationRestoration](toolbarminimizationrestoration.md) — The restoration behavior during toolbar minimization. _(beta)_
- [toolbarMinimizationSafeAreaAdjustment(_:for:)](<view/toolbarminimizationsafeareaadjustment(__for_).md>) — Sets the safe area adjustment for the specified bars during minimization. _(beta)_
