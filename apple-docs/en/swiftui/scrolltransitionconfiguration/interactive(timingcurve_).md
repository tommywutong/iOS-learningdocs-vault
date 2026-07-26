---
title: 'interactive(timingCurve:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/scrolltransitionconfiguration/interactive(timingcurve:)'
source_url: 'https://developer.apple.com/documentation/swiftui/scrolltransitionconfiguration/interactive(timingcurve:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/scrolltransitionconfiguration/interactive%28timingcurve%3A%29.json'
content_hash: 'sha256:cd0b7e7023dcc397'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ScrollTransitionConfiguration](../scrolltransitionconfiguration.md)

# interactive(timingCurve:)

<sub>Type Method</sub>

Creates a new configuration that interactively interpolates the transition’s effect as the view is scrolled into the visible region of the container.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func interactive(timingCurve: UnitCurve = .easeInOut) -> ScrollTransitionConfiguration
```

## Parameters

- `timingCurve` — The curve that adjusts the pace at which the effect is interpolated between phases of the transition. For example, an `.easeIn` curve causes interpolation to begin slowly as the view reaches the edge of the scroll view, then speed up as it reaches the visible threshold. The curve is applied ‘forward’ while the view is appearing, meaning that time zero corresponds to the view being just hidden, and time 1.0 corresponds to the pont at which the view reaches the configuration threshold. This also means that the timing curve is applied in reversed while the view is moving away from the center of the scroll view.

## Return Value

A configuration that interactively interpolates between transition phases based on the current scroll position.

## See Also

### Getting the configuration

- [identity](identity.md) — Creates a new configuration that does not change the appearance of the view.
- [animated](animated.md) — Creates a new configuration that discretely animates the transition when the view becomes visible.
- [animated(_:)](<animated(__).md>) — Creates a new configuration that discretely animates the transition when the view becomes visible.
- [interactive](interactive.md) — Creates a new configuration that interactively interpolates the transition’s effect as the view is scrolled into the visible region of the container.
