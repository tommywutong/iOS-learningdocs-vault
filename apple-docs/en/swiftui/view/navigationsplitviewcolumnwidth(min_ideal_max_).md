---
title: 'navigationSplitViewColumnWidth(min:ideal:max:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/navigationsplitviewcolumnwidth(min:ideal:max:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/navigationsplitviewcolumnwidth(min:ideal:max:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/navigationsplitviewcolumnwidth%28min%3Aideal%3Amax%3A%29.json'
content_hash: 'sha256:3bda9f2e904e5080'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# navigationSplitViewColumnWidth(min:ideal:max:)

<sub>Instance Method</sub>

Sets a flexible, preferred width for the column containing this view.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func navigationSplitViewColumnWidth(min: CGFloat? = nil, ideal: CGFloat, max: CGFloat? = nil) -> some View

```

## Discussion

Apply this modifier to the content of a column in a [NavigationSplitView](../navigationsplitview.md) to specify a preferred flexible width for the column. Use [navigationSplitViewColumnWidth(_:)](<navigationsplitviewcolumnwidth(__).md>) if you need to specify a fixed width.

The following example shows a three-column navigation split view where the first column has a preferred width of 150 points, and the second column has a flexible, preferred width between 150 and 400 points:

```swift
NavigationSplitView {
    MySidebar()
        .navigationSplitViewColumnWidth(150)
} contents: {
    MyContents()
        .navigationSplitViewColumnWidth(
            min: 150, ideal: 200, max: 400)
} detail: {
    MyDetail()
}
```

Only some platforms enable resizing columns. If you specify a width that the current presentation environment doesn’t support, SwiftUI may use a different width for your column.

## See Also

### Presenting views in columns

- [Bringing robust navigation structure to your SwiftUI app](../bringing-robust-navigation-structure-to-your-swiftui-app.md) — Use navigation links, stacks, destinations, and paths to provide a streamlined experience for all platforms, as well as behaviors such as deep linking and state restoration.
- [Migrating to new navigation types](../migrating-to-new-navigation-types.md) — Improve navigation behavior in your app by replacing navigation views with navigation stacks and navigation split views.
- [NavigationSplitView](../navigationsplitview.md) — A view that presents views in two or three columns, where selections in leading columns control presentations in subsequent columns.
- [navigationSplitViewStyle(_:)](<navigationsplitviewstyle(__).md>) — Sets the style for navigation split views within this view.
- [navigationSplitViewColumnWidth(_:)](<navigationsplitviewcolumnwidth(__).md>) — Sets a fixed, preferred width for the column containing this view.
- [NavigationSplitViewVisibility](../navigationsplitviewvisibility.md) — The visibility of the leading columns in a navigation split view.
- [NavigationLink](../navigationlink.md) — A view that controls a navigation presentation.
