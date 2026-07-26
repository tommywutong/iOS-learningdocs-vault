---
title: 'toolbarTitleMenu(content:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/toolbartitlemenu(content:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/toolbartitlemenu(content:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/toolbartitlemenu%28content%3A%29.json'
content_hash: 'sha256:4521aa5e2be2a25b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# toolbarTitleMenu(content:)

<sub>Instance Method</sub>

Configure the title menu of a toolbar.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func toolbarTitleMenu<C>(@ContentBuilder content: () -> C) -> some View where C : View

```

## Parameters

- `content` — The content associated to the toolbar title menu.

## Discussion

A title menu represent common functionality that can be done on the content represented by your app’s toolbar or navigation title. This menu may be populated from your app’s commands like [saveItem](../commandgroupplacement/saveitem.md) or [printItem](../commandgroupplacement/printitem.md).

```swift
ContentView()
    .toolbar {
        ToolbarTitleMenu()
    }
```

You can provide your own set of actions to override this behavior.

```swift
ContentView()
    .toolbarTitleMenu {
        DuplicateButton()
        PrintButton()
    }
```

In iOS and iPadOS, this will construct a menu that can be presented by tapping the navigation title in the app’s navigation bar.

## See Also

### Setting the toolbar title menu

- [ToolbarTitleMenu](../toolbartitlemenu.md) — The title menu of a toolbar.
