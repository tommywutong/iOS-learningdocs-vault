---
title: 'toolbar(removing:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/toolbar(removing:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/toolbar(removing:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/toolbar%28removing%3A%29.json'
content_hash: 'sha256:155d4d561ff97682'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# toolbar(removing:)

<sub>Instance Method</sub>

Remove a toolbar item present by default

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func toolbar(removing defaultItemKind: ToolbarDefaultItemKind?) -> some View

```

## Parameters

- `defaultItemKind` — The kind of default item to remove

## Discussion

Use this modifier to remove toolbar items other `View`s add by default. For example, to remove the sidebar toggle toolbar item provided by `NavigationSplitView`:

```swift
NavigationSplitView {
    SidebarView()
        .toolbar(removing: .sidebarToggle)
} detail: {
    DetailView()
}
```

## See Also

### Removing default items

- [ToolbarDefaultItemKind](../toolbardefaultitemkind.md) — A kind of toolbar item a `View` adds by default.
