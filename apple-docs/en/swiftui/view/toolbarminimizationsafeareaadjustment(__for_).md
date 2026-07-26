---
title: 'toolbarMinimizationSafeAreaAdjustment(_:for:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta, watchOS 27.0+ beta]
languages: [swift, swift]
beta: true
deprecated: false
doc_path: '/documentation/swiftui/view/toolbarminimizationsafeareaadjustment(_:for:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/toolbarminimizationsafeareaadjustment(_:for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/toolbarminimizationsafeareaadjustment%28_%3Afor%3A%29.json'
content_hash: 'sha256:9775b0b6abb20af3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# toolbarMinimizationSafeAreaAdjustment(_:for:)

<sub>Instance Method</sub>

Sets the safe area adjustment for the specified bars during minimization.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func toolbarMinimizationSafeAreaAdjustment(_ adjustment: ToolbarMinimizationSafeAreaAdjustment, for bars: ToolbarPlacement...) -> some View

```

## Parameters

- `adjustment` — The safe area adjustment.

- `bars` — The bars to apply the adjustment to.

## Discussion

By default, the safe area adjusts as bars minimize, allowing content to reflow into the space vacated by the bar. Use this modifier to disable that adjustment when content should remain in place – for example, when displaying full-bleed media beneath a minimizing bar.

Currently, only [navigationBar](../toolbarplacement/navigationbar.md) supports customizing the safe area adjustment.

Use this modifier alongside [toolbarMinimizationBehavior(_:for:)](<toolbarminimizationbehavior(__for_).md>):

```swift
NavigationStack {
    ScrollView {
        // ...
    }
    .toolbarMinimizationBehavior(
        .onScrollDown, for: .navigationBar)
    .toolbarMinimizationSafeAreaAdjustment(
        .disabled, for: .navigationBar)
}
```

## See Also

### Minimizing a toolbar

- [toolbarMinimizationBehavior(_:for:)](<toolbarminimizationbehavior(__for_).md>) — Sets the minimize behavior for the specified bars. _(beta)_
- [ToolbarMinimizationBehavior](../toolbarminimizationbehavior.md) — The minimization behavior of a toolbar. _(beta)_
- [toolbarMinimizationRestoration(_:for:)](<toolbarminimizationrestoration(__for_).md>) — Sets the restoration behavior for the specified bars during minimization. _(beta)_
- [ToolbarMinimizationRestoration](../toolbarminimizationrestoration.md) — The restoration behavior during toolbar minimization. _(beta)_
- [ToolbarMinimizationSafeAreaAdjustment](../toolbarminimizationsafeareaadjustment.md) — The safe area adjustment during toolbar minimization. _(beta)_
