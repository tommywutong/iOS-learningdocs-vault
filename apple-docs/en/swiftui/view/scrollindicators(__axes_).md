---
title: 'scrollIndicators(_:axes:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/scrollindicators(_:axes:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/scrollindicators(_:axes:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/scrollindicators%28_%3Aaxes%3A%29.json'
content_hash: 'sha256:b85ceef00367daa4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# scrollIndicators(_:axes:)

<sub>Instance Method</sub>

Sets the visibility of scroll indicators within this view.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func scrollIndicators(_ visibility: ScrollIndicatorVisibility, axes: Axis.Set = [.vertical, .horizontal]) -> some View

```

## Parameters

- `visibility` — The visibility to apply to scrollable views.

- `axes` — The axes of scrollable views that the visibility applies to.

## Return Value

A view with the specified scroll indicator visibility.

## Discussion

Use this modifier to hide or show scroll indicators on scrollable content in views like a [ScrollView](../scrollview.md), [List](../list.md), or [TextEditor](../texteditor.md). This modifier applies the preferred visibility to any scrollable content within a view hierarchy.

```swift
ScrollView {
    VStack(alignment: .leading) {
        ForEach(0..<100) {
            Text("Row \($0)")
        }
    }
}
.scrollIndicators(.hidden)
```

Use the [hidden](../scrollindicatorvisibility/hidden.md) value to indicate that you prefer that views never show scroll indicators along a given axis. Use [visible](../scrollindicatorvisibility/visible.md) when you prefer that views show scroll indicators. Depending on platform conventions, visible scroll indicators might only appear while scrolling. Pass [automatic](../scrollindicatorvisibility/automatic.md) to allow views to decide whether or not to show their indicators.

## See Also

### Showing scroll indicators

- [scrollIndicatorsFlash(onAppear:)](<scrollindicatorsflash(onappear_).md>) — Flashes the scroll indicators of a scrollable view when it appears.
- [scrollIndicatorsFlash(trigger:)](<scrollindicatorsflash(trigger_).md>) — Flashes the scroll indicators of scrollable views when a value changes.
- [horizontalScrollIndicatorVisibility](../environmentvalues/horizontalscrollindicatorvisibility.md) — The visibility to apply to scroll indicators of any horizontally scrollable content.
- [verticalScrollIndicatorVisibility](../environmentvalues/verticalscrollindicatorvisibility.md) — The visiblity to apply to scroll indicators of any vertically scrollable content.
- [ScrollIndicatorVisibility](../scrollindicatorvisibility.md) — The visibility of scroll indicators of a UI element.
