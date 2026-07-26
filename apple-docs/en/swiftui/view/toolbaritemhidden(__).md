---
title: 'toolbarItemHidden(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 15.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/toolbaritemhidden(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/toolbaritemhidden(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/toolbaritemhidden%28_%3A%29.json'
content_hash: 'sha256:96467eb953208bec'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# toolbarItemHidden(_:)

<sub>Instance Method</sub>

Hides an individual view within a control group toolbar item.

<sub>macOS</sub>

```swift
nonisolated func toolbarItemHidden(_ hidden: Bool = true) -> some View

```

## Parameters

- `hidden` — Whether the view in a control group toolbar item is hidden.

## Discussion

Use this modifier to hide individual views of a `ControlGroup` without hiding the entire group. On macOS and iOS, hidden items will be displayed during user customization.

The following example displays a collaboration button in a group when there is an active collaboration session.

```swift
struct ContentView {
    @State private var inCollaboration = false

    var body: some View {
        BrowserView()
            .toolbar(id: "browserToolbar") {
                ToolbarItem(id: "share") {
                    ControlGroup {
                        ShareButton()
                        CollaborationButton()
                            .toolbarItemHidden(!inCollaboration)
                    }
                }
            }
    }
}
```

## See Also

### Populating a customizable toolbar

- [toolbar(id:content:)](<toolbar(id_content_).md>) — Populates the toolbar or navigation bar with the specified items, allowing for user customization.
- [CustomizableToolbarContent](../customizabletoolbarcontent.md) — Conforming types represent items that can be placed in various locations in a customizable toolbar.
- [ToolbarCustomizationBehavior](../toolbarcustomizationbehavior.md) — The customization behavior of customizable toolbar content.
- [ToolbarCustomizationOptions](../toolbarcustomizationoptions.md) — Options that influence the default customization behavior of customizable toolbar content.
- [SearchToolbarBehavior](../searchtoolbarbehavior.md) — The behavior of a search field in a toolbar.
