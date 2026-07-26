---
title: 'scrollIndicatorsFlash(onAppear:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/scrollindicatorsflash(onappear:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/scrollindicatorsflash(onappear:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/scrollindicatorsflash%28onappear%3A%29.json'
content_hash: 'sha256:b63b01928ceea516'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# scrollIndicatorsFlash(onAppear:)

<sub>Instance Method</sub>

Flashes the scroll indicators of a scrollable view when it appears.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func scrollIndicatorsFlash(onAppear: Bool) -> some View

```

## Parameters

- `onAppear` — A Boolean value that indicates whether the scroll indicators flash when the scroll view appears.

## Return Value

A view that flashes any visible scroll indicators when it first appears.

## Discussion

Use this modifier to control whether the scroll indicators of a scroll view briefly flash when the view first appears. For example, you can make the indicators flash by setting the `onAppear` parameter to `true`:

```swift
ScrollView {
    // ...
}
.scrollIndicatorsFlash(onAppear: true)
```

Only scroll indicators that you configure to be visible flash. To flash scroll indicators when a value changes, use [scrollIndicatorsFlash(trigger:)](<scrollindicatorsflash(trigger_).md>) instead.

## See Also

### Showing scroll indicators

- [scrollIndicatorsFlash(trigger:)](<scrollindicatorsflash(trigger_).md>) — Flashes the scroll indicators of scrollable views when a value changes.
- [scrollIndicators(_:axes:)](<scrollindicators(__axes_).md>) — Sets the visibility of scroll indicators within this view.
- [horizontalScrollIndicatorVisibility](../environmentvalues/horizontalscrollindicatorvisibility.md) — The visibility to apply to scroll indicators of any horizontally scrollable content.
- [verticalScrollIndicatorVisibility](../environmentvalues/verticalscrollindicatorvisibility.md) — The visiblity to apply to scroll indicators of any vertically scrollable content.
- [ScrollIndicatorVisibility](../scrollindicatorvisibility.md) — The visibility of scroll indicators of a UI element.
