---
title: 'toolbarMinimizationBehavior(_:for:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta, watchOS 27.0+ beta]
languages: [swift, swift]
beta: true
deprecated: false
doc_path: '/documentation/swiftui/view/toolbarminimizationbehavior(_:for:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/toolbarminimizationbehavior(_:for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/toolbarminimizationbehavior%28_%3Afor%3A%29.json'
content_hash: 'sha256:fe959e844e73a4fd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# toolbarMinimizationBehavior(_:for:)

<sub>Instance Method</sub>

Sets the minimize behavior for the specified bars.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func toolbarMinimizationBehavior(_ behavior: ToolbarMinimizationBehavior, for bars: ToolbarPlacement...) -> some View

```

## Parameters

- `behavior` — The minimize behavior.

- `bars` — The bars to apply the behavior to.

## Discussion

Use this modifier to enable toolbar minimization in response to scrolling. The supported placement is [navigationBar](../toolbarplacement/navigationbar.md). When the navigation bar minimizes, an integrated top tab bar will also minimize.

By default, the safe area adjusts as the navigation bar minimizes. Use [toolbarMinimizationSafeAreaAdjustment(_:for:)](<toolbarminimizationsafeareaadjustment(__for_).md>) to customize this.

```swift
NavigationStack {
    ScrollView {
        ForEach(0 ..< 50) { index in
            Text("\(index)").padding()
        }
    }
    .navigationTitle("Minimizing Title")
    .toolbarMinimizationBehavior(.onScrollDown, for: .navigationBar)
}
```

## See Also

### Minimizing a toolbar

- [ToolbarMinimizationBehavior](../toolbarminimizationbehavior.md) — The minimization behavior of a toolbar. _(beta)_
- [toolbarMinimizationRestoration(_:for:)](<toolbarminimizationrestoration(__for_).md>) — Sets the restoration behavior for the specified bars during minimization. _(beta)_
- [ToolbarMinimizationRestoration](../toolbarminimizationrestoration.md) — The restoration behavior during toolbar minimization. _(beta)_
- [toolbarMinimizationSafeAreaAdjustment(_:for:)](<toolbarminimizationsafeareaadjustment(__for_).md>) — Sets the safe area adjustment for the specified bars during minimization. _(beta)_
- [ToolbarMinimizationSafeAreaAdjustment](../toolbarminimizationsafeareaadjustment.md) — The safe area adjustment during toolbar minimization. _(beta)_
