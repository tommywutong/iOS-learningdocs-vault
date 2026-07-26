---
title: 'navigationViewStyle(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+（27.0 起废弃）, iPadOS 13.0+（27.0 起废弃）, Mac Catalyst 13.0+（27.0 起废弃）, macOS 10.15+（27.0 起废弃）, tvOS 13.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）, watchOS 7.0+（27.0 起废弃）]
languages: [swift, swift]
beta: false
deprecated: true
doc_path: '/documentation/swiftui/view/navigationviewstyle(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/navigationviewstyle(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/navigationviewstyle%28_%3A%29.json'
content_hash: 'sha256:7fa13935892046c3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# navigationViewStyle(_:)

<sub>Instance Method</sub>

Sets the style for navigation views within this view.

> [!warning] Deprecated
> Replace a styled [NavigationView](../navigationview.md) with a [NavigationStack](../navigationstack.md) or [NavigationSplitView](../navigationsplitview.md). For more information, see [Migrating to new navigation types](../migrating-to-new-navigation-types.md).

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func navigationViewStyle<S>(_ style: S) -> some View where S : NavigationViewStyle

```

## Discussion

Use this modifier to change the appearance and behavior of navigation views. For example, by default, navigation views appear with multiple columns in wider environments, like iPad in landscape orientation:

![A screenshot of an iPad in landscape orientation mode showing a](../../../../attachments/6ea0c512dea9061acb17a64140b660e6/View-navigationViewStyle-1@2x.png)

You can apply the [stack](../navigationviewstyle/stack.md) style to force single-column stack navigation in these environments:

```swift
NavigationView {
    List {
        NavigationLink("Purple", destination: ColorDetail(color: .purple))
        NavigationLink("Pink", destination: ColorDetail(color: .pink))
        NavigationLink("Orange", destination: ColorDetail(color: .orange))
    }
    .navigationTitle("Colors")

    Text("Select a Color") // A placeholder to show before selection.
}
.navigationViewStyle(.stack)
```

![](../../../../attachments/5df851308e1be644de4f133b0780d285/View-navigationViewStyle-2@2x.png)

<sub>A screenshot of an iPad in landscape orientation mode showing a single column containing the list Purple, Pink, and Orange.</sub>

## See Also

### Styling navigation views

- [NavigationViewStyle](../navigationviewstyle.md) — A specification for the appearance and interaction of a navigation view. _(deprecated)_
