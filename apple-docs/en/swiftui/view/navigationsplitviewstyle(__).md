---
title: 'navigationSplitViewStyle(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift, swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/navigationsplitviewstyle(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/navigationsplitviewstyle(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/navigationsplitviewstyle%28_%3A%29.json'
content_hash: 'sha256:4c7b60cf9ded007d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# navigationSplitViewStyle(_:)

<sub>Instance Method</sub>

Sets the style for navigation split views within this view.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func navigationSplitViewStyle<S>(_ style: S) -> some View where S : NavigationSplitViewStyle

```

## Parameters

- `style` — The style to set.

## Return Value

A view that uses the specified navigation split view style.

## See Also

### Presenting views in columns

- [Bringing robust navigation structure to your SwiftUI app](../bringing-robust-navigation-structure-to-your-swiftui-app.md) — Use navigation links, stacks, destinations, and paths to provide a streamlined experience for all platforms, as well as behaviors such as deep linking and state restoration.
- [Migrating to new navigation types](../migrating-to-new-navigation-types.md) — Improve navigation behavior in your app by replacing navigation views with navigation stacks and navigation split views.
- [NavigationSplitView](../navigationsplitview.md) — A view that presents views in two or three columns, where selections in leading columns control presentations in subsequent columns.
- [navigationSplitViewColumnWidth(_:)](<navigationsplitviewcolumnwidth(__).md>) — Sets a fixed, preferred width for the column containing this view.
- [navigationSplitViewColumnWidth(min:ideal:max:)](<navigationsplitviewcolumnwidth(min_ideal_max_).md>) — Sets a flexible, preferred width for the column containing this view.
- [NavigationSplitViewVisibility](../navigationsplitviewvisibility.md) — The visibility of the leading columns in a navigation split view.
- [NavigationLink](../navigationlink.md) — A view that controls a navigation presentation.
