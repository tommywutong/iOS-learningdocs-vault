---
title: 'navigationBarHidden(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+（27.0 起废弃）, iPadOS 13.0+（27.0 起废弃）, Mac Catalyst 13.0+（27.0 起废弃）, tvOS 13.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）, watchOS 6.0+（27.0 起废弃）]
languages: [swift]
beta: false
deprecated: true
doc_path: '/documentation/swiftui/view/navigationbarhidden(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/navigationbarhidden(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/navigationbarhidden%28_%3A%29.json'
content_hash: 'sha256:7ba1cb77ec7109b2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# navigationBarHidden(_:)

<sub>Instance Method</sub>

Hides the navigation bar for this view.

> [!warning] Deprecated
> Use [toolbar(_:for:)](<toolbar(__for_).md>) with the [Visibility.hidden](../visibility/hidden.md) visibility and the [navigationBar](../toolbarplacement/navigationbar.md) placement instead.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func navigationBarHidden(_ hidden: Bool) -> some View

```

## Parameters

- `hidden` — A Boolean value that indicates whether to hide the navigation bar.

## Discussion

Use this method to hide the navigation bar. This modifier only takes effect when the modified view is inside of and visible within a [NavigationView](../navigationview.md).

## See Also

### Auxiliary view modifiers

- [navigationBarTitle(_:)](<navigationbartitle(__).md>) — Sets the title in the navigation bar for this view. _(deprecated)_
- [navigationBarTitle(_:displayMode:)](<navigationbartitle(__displaymode_).md>) — Sets the title and display mode in the navigation bar for this view. _(deprecated)_
- [navigationBarItems(leading:)](<navigationbaritems(leading_).md>) — Sets the navigation bar items for this view. _(deprecated)_
- [navigationBarItems(leading:trailing:)](<navigationbaritems(leading_trailing_).md>) — Sets the navigation bar items for this view. _(deprecated)_
- [navigationBarItems(trailing:)](<navigationbaritems(trailing_).md>) — Configures the navigation bar items for this view. _(deprecated)_
- [statusBar(hidden:)](<statusbar(hidden_).md>) — Sets the visibility of the status bar. _(deprecated)_
- [contextMenu(_:)](<contextmenu(__).md>) — Adds a context menu to the view. _(deprecated)_
