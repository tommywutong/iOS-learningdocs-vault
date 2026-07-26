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
doc_path: '/documentation/swiftui/toolbarcontent/hidden(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/toolbarcontent/hidden(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/toolbarcontent/hidden%28_%3A%29.json'
content_hash: 'sha256:09dbf1c8bb24fec5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ToolbarContent](../toolbarcontent.md)

# hidden(_:)

<sub>Instance Method</sub>

Hides a toolbar item within its toolbar.

<sub>macOS</sub>

```swift
nonisolated func hidden(_ hidden: Bool = true) -> some ToolbarContent

```

## Parameters

- `hidden` — Whether the toolbar item is hidden.

## Discussion

Use this modifier to conditionally display a toolbar item in the toolbar.

```swift
struct ContentView {
    @State private var showDownloads = false

    var body: some View {
        BrowserView()
            .toolbar {
                ToolbarItem {
                    DownloadsButton()
                }
                .hidden(!showDownloads)
            }
    }
}
```
