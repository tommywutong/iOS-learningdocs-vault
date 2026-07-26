---
title: 'hidden(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 15.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/customizabletoolbarcontent/hidden(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/customizabletoolbarcontent/hidden(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/customizabletoolbarcontent/hidden%28_%3A%29.json'
content_hash: 'sha256:5f53cfdde93e77c7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [CustomizableToolbarContent](../customizabletoolbarcontent.md)

# hidden(_:)

<sub>Instance Method</sub>

Hides a toolbar item within its toolbar.

<sub>macOS</sub>

```swift
nonisolated func hidden(_ hidden: Bool = true) -> some CustomizableToolbarContent

```

## Parameters

- `hidden` — Whether the toolbar item is hidden.

## Discussion

Use this modifier to conditionally display a toolbar item in the toolbar. On macOS, hidden items will be displayed during user customization.

The following example hides a downloads button when there are no downloads, but it is displayed during customization.

```swift
struct ContentView {
    @State private var showDownloads = false

    var body: some View {
        BrowserView()
            .toolbar(id: "browserToolbar") {
                ToolbarItem(id: "downloads") {
                    DownloadsButton()
                }
                .hidden(!showDownloads)
            }
    }
}
```
