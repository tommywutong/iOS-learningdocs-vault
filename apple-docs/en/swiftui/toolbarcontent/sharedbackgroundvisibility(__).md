---
title: 'sharedBackgroundVisibility(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/toolbarcontent/sharedbackgroundvisibility(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/toolbarcontent/sharedbackgroundvisibility(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/toolbarcontent/sharedbackgroundvisibility%28_%3A%29.json'
content_hash: 'sha256:430409347becfcc5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ToolbarContent](../toolbarcontent.md)

# sharedBackgroundVisibility(_:)

<sub>Instance Method</sub>

Controls the visibility of the glass background effect on items in the toolbar. In certain contexts, such as the navigation bar on iOS and the window toolbar on macOS, toolbar items will be given a glass background effect that is shared with other items in the same logical grouping.

<sub>iOS, iPadOS, Mac Catalyst, macOS</sub>

```swift
nonisolated func sharedBackgroundVisibility(_ visibility: Visibility) -> some ToolbarContent

```

## Parameters

- `visibility` — The visibility of the background effect.

## Discussion

This modifier adjusts the visibility of that effect. Hiding the effect will cause the item to be placed in its own grouping.

```swift
ContentView()
    .toolbar {
        ToolbarItem(placement: principal) {
            BuildStatus()
        }
        .sharedBackgroundVisibility(.hidden)
    }
```
