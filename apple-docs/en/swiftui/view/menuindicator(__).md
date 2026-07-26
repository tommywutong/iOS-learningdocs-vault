---
title: 'menuIndicator(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 17.0+, visionOS 1.0+]
languages: [swift, swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/menuindicator(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/menuindicator(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/menuindicator%28_%3A%29.json'
content_hash: 'sha256:e5d2e9cc4c6865cf'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# menuIndicator(_:)

<sub>Instance Method</sub>

Sets the menu indicator visibility for controls within this view.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
nonisolated func menuIndicator(_ visibility: Visibility) -> some View

```

## Parameters

- `visibility` — The menu indicator visibility to apply.

## Discussion

Use this modifier to override the default menu indicator visibility for controls in this view. For example, the code below creates a menu without an indicator:

```swift
Menu {
    ForEach(history , id: \.self) { historyItem in
        Button(historyItem.title) {
            self.openURL(historyItem.url)
        }
    }
} label: {
    Label("Back", systemImage: "chevron.backward")
        .labelStyle(.iconOnly)
} primaryAction: {
    if let last = history.last {
        self.openURL(last.url)
    }
}
.menuIndicator(.hidden)
```

> [!note] Note
> On tvOS, the standard button styles do not include a menu indicator, so this modifier will have no effect when using a built-in button style. You can implement an indicator in your own [ButtonStyle](../buttonstyle.md) implementation by checking the value of the `menuIndicatorVisibility` environment value.

## See Also

### Showing a menu indicator

- [menuIndicatorVisibility](../environmentvalues/menuindicatorvisibility.md) — The menu indicator visibility to apply to controls within a view.
