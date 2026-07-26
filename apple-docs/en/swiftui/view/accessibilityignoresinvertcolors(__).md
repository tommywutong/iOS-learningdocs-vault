---
title: 'accessibilityIgnoresInvertColors(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/accessibilityignoresinvertcolors(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/accessibilityignoresinvertcolors(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/accessibilityignoresinvertcolors%28_%3A%29.json'
content_hash: 'sha256:cdab5fae005508e6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# accessibilityIgnoresInvertColors(_:)

<sub>Instance Method</sub>

Sets whether this view should ignore the system Smart Invert setting.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func accessibilityIgnoresInvertColors(_ active: Bool = true) -> some View

```

## Parameters

- `active` — A true value ignores the system Smart Invert setting. A false value follows the system setting.

## Discussion

Use this modifier to suppress Smart Invert in a view that shouldn’t be inverted. Or pass an `active` argument of `false` to begin following the Smart Invert setting again when it was previously disabled.

## See Also

### Managing color

- [accessibilityInvertColors](../environmentvalues/accessibilityinvertcolors.md) — Whether the system preference for Invert Colors is enabled.
- [accessibilityDifferentiateWithoutColor](../environmentvalues/accessibilitydifferentiatewithoutcolor.md) — Whether the system preference for Differentiate without Color is enabled.
