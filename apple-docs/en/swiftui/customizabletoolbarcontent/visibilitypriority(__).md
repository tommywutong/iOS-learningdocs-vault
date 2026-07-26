---
title: 'visibilityPriority(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 26.1+, tvOS 27.0+ beta, visionOS 27.0+ beta, watchOS 27.0+ beta]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/customizabletoolbarcontent/visibilitypriority(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/customizabletoolbarcontent/visibilitypriority(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/customizabletoolbarcontent/visibilitypriority%28_%3A%29.json'
content_hash: 'sha256:3a7eb35bc46e1e04'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [CustomizableToolbarContent](../customizabletoolbarcontent.md)

# visibilityPriority(_:)

<sub>Instance Method</sub>

Defines the visibility priority for a toolbar item.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func visibilityPriority(_ priority: ToolbarItemVisibilityPriority) -> some CustomizableToolbarContent

```

## Parameters

- `priority` — The visibility priority for this toolbar item.

## Discussion

When toolbar space is limited, items with a lower priority move into the overflow menu before items with a higher priority. The default is [automatic](../toolbaritemvisibilitypriority/automatic.md).

In the following example, `PrimaryControl` stays visible in the toolbar longer than `SecondaryControl`:

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
