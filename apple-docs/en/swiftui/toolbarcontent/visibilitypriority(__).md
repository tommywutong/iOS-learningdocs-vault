---
title: 'visibilityPriority(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 26.1+, tvOS 27.0+ beta, visionOS 27.0+ beta, watchOS 27.0+ beta]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/toolbarcontent/visibilitypriority(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/toolbarcontent/visibilitypriority(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/toolbarcontent/visibilitypriority%28_%3A%29.json'
content_hash: 'sha256:a141203c3664ffa0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ToolbarContent](../toolbarcontent.md)

# visibilityPriority(_:)

<sub>Instance Method</sub>

Defines the visibility priority for a toolbar item.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@MainActor @preconcurrency func visibilityPriority(_ priority: ToolbarItemVisibilityPriority) -> some ToolbarContent

```

## Parameters

- `priority` — The visibility priority for this toolbar item.

## Discussion

When toolbar space is limited, items with a lower priority move into the overflow menu before items with a higher priority. The default is [automatic](../toolbaritemvisibilitypriority/automatic.md).

For example, an important control can appear at the trailing edge of the toolbar, but still be shown as the window is made smaller:

```swift
struct RootView: View {
    var body: some View {
        ContentView()
            .toolbar {
                ToolbarItem {
                    SecondaryControl()
                }
                ToolbarItem {
                    PrimaryControl()
                }
                .visibilityPriority(.high)
            }
    }
}
```

## See Also

### Controlling item visibility

- [ToolbarItemVisibilityPriority](../toolbaritemvisibilitypriority.md) — A value that defines the visibility priority of a toolbar item.
