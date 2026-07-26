---
title: 'customizationBehavior(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/customizabletoolbarcontent/customizationbehavior(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/customizabletoolbarcontent/customizationbehavior(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/customizabletoolbarcontent/customizationbehavior%28_%3A%29.json'
content_hash: 'sha256:cb39e47fc92fd533'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [CustomizableToolbarContent](../customizabletoolbarcontent.md)

# customizationBehavior(_:)

<sub>Instance Method</sub>

Configures the customization behavior of customizable toolbar content.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func customizationBehavior(_ behavior: ToolbarCustomizationBehavior) -> some CustomizableToolbarContent

```

## Parameters

- `behavior` — The customization behavior of the customizable toolbar content.

## Discussion

Customizable toolbar items support different kinds of customization:

- A user can add an item that is not in the toolbar.
- A user can remove an item that is in the toolbar.
- A user can move an item within the toolbar.

Based on the customization behavior of the toolbar items, different edits will be supported.

Use this modifier to the customization behavior a user can perform on your toolbar items. In the following example, the customizable toolbar item supports all of the different kinds of toolbar customizations and starts in the toolbar.

```swift
ContentView()
    .toolbar(id: "main") {
        ToolbarItem(id: "new") {
            // new button here
        }
    }
```

You can create an item that can not be removed from the toolbar or moved within the toolbar  by passing a value of [disabled](../toolbarcustomizationbehavior/disabled.md) to this modifier.

```swift
ContentView()
    .toolbar(id: "main") {
        ToolbarItem(id: "new") {
            // new button here
        }
        .customizationBehavior(.disabled)
    }
```

You can create an item that can not be removed from the toolbar, but can be moved by passing a value of [reorderable](../toolbarcustomizationbehavior/reorderable.md).

```swift
ContentView()
    .toolbar(id: "main") {
        ToolbarItem(id: "new") {
            // new button here
        }
        .customizationBehavior(.reorderable)
    }
```
