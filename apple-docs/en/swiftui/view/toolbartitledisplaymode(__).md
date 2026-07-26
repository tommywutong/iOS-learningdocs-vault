---
title: 'toolbarTitleDisplayMode(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/toolbartitledisplaymode(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/toolbartitledisplaymode(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/toolbartitledisplaymode%28_%3A%29.json'
content_hash: 'sha256:077cbee3f56f13c7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# toolbarTitleDisplayMode(_:)

<sub>Instance Method</sub>

Configures the toolbar title display mode for this view.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func toolbarTitleDisplayMode(_ mode: ToolbarTitleDisplayMode) -> some View

```

## Discussion

Use this modifier to override the default toolbar title display mode.

```swift
NavigationStack {
    ContentView()
        .toolbarTitleDisplayMode(.inlineLarge)
}
```

See [ToolbarTitleDisplayMode](../toolbartitledisplaymode.md) for more information on the different kinds of display modes. This modifier has no effect on macOS.

## See Also

### Configuring the toolbar title display mode

- [ToolbarTitleDisplayMode](../toolbartitledisplaymode.md) — A type that defines the behavior of title of a toolbar.
