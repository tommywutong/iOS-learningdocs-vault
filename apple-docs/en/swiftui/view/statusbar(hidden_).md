---
title: 'statusBar(hidden:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+（27.0 起废弃）, iPadOS 13.0+（27.0 起废弃）, Mac Catalyst 13.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）]
languages: [swift]
beta: false
deprecated: true
doc_path: '/documentation/swiftui/view/statusbar(hidden:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/statusbar(hidden:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/statusbar%28hidden%3A%29.json'
content_hash: 'sha256:9be428b50ec77c8a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# statusBar(hidden:)

<sub>Instance Method</sub>

Sets the visibility of the status bar.

> [!warning] Deprecated
> Use [statusBarHidden(_:)](<statusbarhidden(__).md>) instead.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
nonisolated func statusBar(hidden: Bool) -> some View

```

## Discussion

Use this method to show or hide the status bar.

## See Also

### Auxiliary view modifiers

- [navigationBarTitle(_:)](<navigationbartitle(__).md>) — Sets the title in the navigation bar for this view. _(deprecated)_
- [navigationBarTitle(_:displayMode:)](<navigationbartitle(__displaymode_).md>) — Sets the title and display mode in the navigation bar for this view. _(deprecated)_
- [navigationBarItems(leading:)](<navigationbaritems(leading_).md>) — Sets the navigation bar items for this view. _(deprecated)_
- [navigationBarItems(leading:trailing:)](<navigationbaritems(leading_trailing_).md>) — Sets the navigation bar items for this view. _(deprecated)_
- [navigationBarItems(trailing:)](<navigationbaritems(trailing_).md>) — Configures the navigation bar items for this view. _(deprecated)_
- [navigationBarHidden(_:)](<navigationbarhidden(__).md>) — Hides the navigation bar for this view. _(deprecated)_
- [contextMenu(_:)](<contextmenu(__).md>) — Adds a context menu to the view. _(deprecated)_
