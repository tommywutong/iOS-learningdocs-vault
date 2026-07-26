---
title: 'animated(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/scrolltransitionconfiguration/animated(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/scrolltransitionconfiguration/animated(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/scrolltransitionconfiguration/animated%28_%3A%29.json'
content_hash: 'sha256:821ae61539402f06'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ScrollTransitionConfiguration](../scrolltransitionconfiguration.md)

# animated(_:)

<sub>Type Method</sub>

Creates a new configuration that discretely animates the transition when the view becomes visible.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func animated(_ animation: Animation = .default) -> ScrollTransitionConfiguration
```

## Parameters

- `animation` — The animation to use when transitioning between states.

## Return Value

A configuration that discretely animates between transition phases.

## Discussion

Unlike the interactive configuration, the transition isn’t interpolated as the scroll view is scrolled. Instead, the transition phase only changes once the threshold has been reached, at which time the given animation is used to animate to the new phase.

## See Also

### Getting the configuration

- [identity](identity.md) — Creates a new configuration that does not change the appearance of the view.
- [animated](animated.md) — Creates a new configuration that discretely animates the transition when the view becomes visible.
- [interactive](interactive.md) — Creates a new configuration that interactively interpolates the transition’s effect as the view is scrolled into the visible region of the container.
- [interactive(timingCurve:)](<interactive(timingcurve_).md>) — Creates a new configuration that interactively interpolates the transition’s effect as the view is scrolled into the visible region of the container.
