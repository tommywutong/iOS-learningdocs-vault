---
title: 'animation(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+（15.0 起废弃）, iPadOS 13.0+（15.0 起废弃）, Mac Catalyst 13.0+（15.0 起废弃）, macOS 10.15+（12.0 起废弃）, tvOS 13.0+（15.0 起废弃）, visionOS 1.0+（1.0 起废弃）, watchOS 6.0+（8.0 起废弃）]
languages: [swift]
beta: false
deprecated: true
doc_path: '/documentation/swiftui/view/animation(_:)-1hc0p'
source_url: 'https://developer.apple.com/documentation/swiftui/view/animation(_:)-1hc0p'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/animation%28_%3A%29-1hc0p.json'
content_hash: 'sha256:74cc81769b803b04'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# animation(_:)

<sub>Instance Method</sub>

Applies the given animation to all animatable values within this view.

> [!warning] Deprecated
> Use [withAnimation(_:_:)](<../withanimation(____).md>) or [animation(_:value:)](<animation(__value_).md>) instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func animation(_ animation: Animation?) -> some View

```

## Parameters

- `animation` — The animation to apply to animatable values within this view.

## Return Value

A view that wraps this view and applies `animation` to all animatable values used within the view.

## Discussion

Use this modifier on leaf views rather than container views. The animation applies to all child views within this view; calling `animation(_:)` on a container view can lead to unbounded scope.
