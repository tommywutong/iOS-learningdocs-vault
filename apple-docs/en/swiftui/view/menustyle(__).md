---
title: 'menuStyle(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 17.0+, visionOS 1.0+]
languages: [swift, swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/menustyle(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/menustyle(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/menustyle%28_%3A%29.json'
content_hash: 'sha256:01405f0853e8dd4e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# menuStyle(_:)

<sub>Instance Method</sub>

Sets the style for menus within this view.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
nonisolated func menuStyle<S>(_ style: S) -> some View where S : MenuStyle

```

## Discussion

To set a specific style for all menu instances within a view, use the `menuStyle(_:)` modifier:

```swift
Menu("PDF") {
    Button("Open in Preview", action: openInPreview)
    Button("Save as PDF", action: saveAsPDF)
}
.menuStyle(ButtonMenuStyle())
```

## See Also

### Creating a menu

- [Populating SwiftUI menus with adaptive controls](../populating-swiftui-menus-with-adaptive-controls.md) — Improve your app by populating menus with controls and organizing your content intuitively.
- [Menu](../menu.md) — A control for presenting a menu of actions.
