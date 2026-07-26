---
title: 'focusEffectDisabled(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/focuseffectdisabled(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/focuseffectdisabled(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/focuseffectdisabled%28_%3A%29.json'
content_hash: 'sha256:db4b1c99b8cfee4f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# focusEffectDisabled(_:)

<sub>Instance Method</sub>

Adds a condition that controls whether this view can display focus effects, such as a default focus ring or hover effect.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func focusEffectDisabled(_ disabled: Bool = true) -> some View

```

## Parameters

- `disabled` — A Boolean value that determines whether this view can display focus effects.

## Return Value

A view that controls whether focus effects can be displayed in this view.

## Discussion

The higher views in a view hierarchy can override the value you set on this view. In the following example, the button does not display a focus effect because the outer `focusEffectDisabled(_:)` modifier overrides the inner one:

```swift
HStack {
    Button("Press") {}
        .focusEffectDisabled(false)
}
.focusEffectDisabled(true)
```

## See Also

### Configuring effects

- [isFocusEffectEnabled](../environmentvalues/isfocuseffectenabled.md) — A Boolean value that indicates whether the view associated with this environment allows focus effects to be displayed.
