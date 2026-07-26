---
title: 'animation(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/scrolltransitionconfiguration/animation(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/scrolltransitionconfiguration/animation(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/scrolltransitionconfiguration/animation%28_%3A%29.json'
content_hash: 'sha256:b9abff960b427748'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ScrollTransitionConfiguration](../scrolltransitionconfiguration.md)

# animation(_:)

<sub>Instance Method</sub>

Sets the animation with which the transition will be applied.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func animation(_ animation: Animation) -> ScrollTransitionConfiguration
```

## Parameters

- `animation` — An animation that will be used to apply the transition to the view.

## Return Value

A copy of this configuration with the animation set to the given value.

## Discussion

If the transition is interactive, the given animation will be used to animate the effect toward the current interpolated value, causing the effect to lag behind the current scroll position.

## See Also

### Accessing the configuration

- [threshold(_:)](<threshold(__).md>) — Sets the threshold at which the view will be considered fully visible.
- [Threshold](threshold.md) — Describes a specific point in the progression of a target view within a container from hidden (fully outside the container) to visible.
