---
title: 'scrollIndicatorsFlash(trigger:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/scrollindicatorsflash(trigger:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/scrollindicatorsflash(trigger:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/scrollindicatorsflash%28trigger%3A%29.json'
content_hash: 'sha256:3edb0ca7629751aa'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# scrollIndicatorsFlash(trigger:)

<sub>Instance Method</sub>

Flashes the scroll indicators of scrollable views when a value changes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func scrollIndicatorsFlash(trigger value: some Equatable) -> some View

```

## Parameters

- `value` — The value that causes scroll indicators to flash. The value must conform to the [Equatable](../../swift/equatable.md) protocol.

## Return Value

A view that flashes any visible scroll indicators when a value changes.

## Discussion

When the value that you provide to this modifier changes, the scroll indicators of any scrollable views within the modified view hierarchy briefly flash. The following example configures the scroll indicators to flash any time `flashCount` changes:

```swift
@State private var isPresented = false
@State private var flashCount = 0

ScrollView {
    // ...
}
.scrollIndicatorsFlash(trigger: flashCount)
.sheet(isPresented: $isPresented) {
    // ...
}
.onChange(of: isPresented) { newValue in
    if newValue {
        flashCount += 1
    }
}
```

Only scroll indicators that you configure to be visible flash. To flash scroll indicators when a scroll view initially appears, use [scrollIndicatorsFlash(onAppear:)](<scrollindicatorsflash(onappear_).md>) instead.

## See Also

### Showing scroll indicators

- [scrollIndicatorsFlash(onAppear:)](<scrollindicatorsflash(onappear_).md>) — Flashes the scroll indicators of a scrollable view when it appears.
- [scrollIndicators(_:axes:)](<scrollindicators(__axes_).md>) — Sets the visibility of scroll indicators within this view.
- [horizontalScrollIndicatorVisibility](../environmentvalues/horizontalscrollindicatorvisibility.md) — The visibility to apply to scroll indicators of any horizontally scrollable content.
- [verticalScrollIndicatorVisibility](../environmentvalues/verticalscrollindicatorvisibility.md) — The visiblity to apply to scroll indicators of any vertically scrollable content.
- [ScrollIndicatorVisibility](../scrollindicatorvisibility.md) — The visibility of scroll indicators of a UI element.
