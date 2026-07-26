---
title: 'tabViewStyle(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift, swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/tabviewstyle(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/tabviewstyle(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/tabviewstyle%28_%3A%29.json'
content_hash: 'sha256:6b620d6d4aedd16f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# tabViewStyle(_:)

<sub>Instance Method</sub>

Sets the style for the tab view within the current environment.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func tabViewStyle<S>(_ style: S) -> some View where S : TabViewStyle

```

## Parameters

- `style` — The style to apply to this tab view.

## See Also

### Presenting views in tabs

- [Enhancing your app’s content with tab navigation](../enhancing-your-app-content-with-tab-navigation.md) — Keep your app content front and center while providing quick access to navigation using the tab bar.
- [TabView](../tabview.md) — A view that switches between multiple child views using interactive user interface elements.
- [Tab](../tab.md) — The content for a tab and the tab’s associated tab item in a tab view.
- [TabRole](../tabrole.md) — A value that defines the purpose of the tab.
- [TabSection](../tabsection.md) — A container that you can use to add hierarchy within a tab view.
