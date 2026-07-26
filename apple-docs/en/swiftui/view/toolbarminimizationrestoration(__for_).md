---
title: 'toolbarMinimizationRestoration(_:for:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta, watchOS 27.0+ beta]
languages: [swift, swift]
beta: true
deprecated: false
doc_path: '/documentation/swiftui/view/toolbarminimizationrestoration(_:for:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/toolbarminimizationrestoration(_:for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/toolbarminimizationrestoration%28_%3Afor%3A%29.json'
content_hash: 'sha256:2712350e6a27764d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# toolbarMinimizationRestoration(_:for:)

<sub>Instance Method</sub>

Sets the restoration behavior for the specified bars during minimization.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func toolbarMinimizationRestoration(_ restoration: ToolbarMinimizationRestoration, for bars: ToolbarPlacement...) -> some View

```

## Parameters

- `restoration` — The restoration behavior.

- `bars` — The bars to apply the restoration behavior to.

## Discussion

Use this modifier alongside [toolbarMinimizationBehavior(_:for:)](<toolbarminimizationbehavior(__for_).md>) to customize when a minimized bar restores. By default, the bar restores when the user reverses scroll direction. Use [atScrollEdge](../toolbarminimizationrestoration/atscrolledge.md) to restrict restoration to when the scroll view’s content reaches the scroll edge – appropriate for screens where the bar is mostly chrome that doesn’t need to follow the user.

```swift
NavigationStack {
    ScrollView {
        // ...
    }
    .toolbarMinimizationBehavior(
        .onScrollDown, for: .navigationBar)
    .toolbarMinimizationRestoration(
        .atScrollEdge, for: .navigationBar)
}
```

Currently, only [navigationBar](../toolbarplacement/navigationbar.md) supports customizing the restoration behavior, and only when used in combination with [onScrollDown](../toolbarminimizationbehavior/onscrolldown.md).

## See Also

### Minimizing a toolbar

- [toolbarMinimizationBehavior(_:for:)](<toolbarminimizationbehavior(__for_).md>) — Sets the minimize behavior for the specified bars. _(beta)_
- [ToolbarMinimizationBehavior](../toolbarminimizationbehavior.md) — The minimization behavior of a toolbar. _(beta)_
- [ToolbarMinimizationRestoration](../toolbarminimizationrestoration.md) — The restoration behavior during toolbar minimization. _(beta)_
- [toolbarMinimizationSafeAreaAdjustment(_:for:)](<toolbarminimizationsafeareaadjustment(__for_).md>) — Sets the safe area adjustment for the specified bars during minimization. _(beta)_
- [ToolbarMinimizationSafeAreaAdjustment](../toolbarminimizationsafeareaadjustment.md) — The safe area adjustment during toolbar minimization. _(beta)_
