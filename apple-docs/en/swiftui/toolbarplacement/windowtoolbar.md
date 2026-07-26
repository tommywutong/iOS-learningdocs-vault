---
title: windowToolbar
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [macOS 13.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/toolbarplacement/windowtoolbar
source_url: 'https://developer.apple.com/documentation/swiftui/toolbarplacement/windowtoolbar'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/toolbarplacement/windowtoolbar.json'
content_hash: 'sha256:54655896df0140fb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ToolbarPlacement](../toolbarplacement.md)

# windowToolbar

<sub>Type Property</sub>

The placement for the containing window’s toolbar, sometimes referred to as the titlebar.

<sub>macOS</sub>

```swift
static var windowToolbar: ToolbarPlacement { get }
```

## Discussion

When hidden using [toolbarVisibility(_:for:)](<../view/toolbarvisibility(__for_).md>), this hides the entire window toolbar, including the title and “traffic light” window controls. To remove the custom toolbar item content only, use [automatic](automatic.md).

Use [toolbarBackground(_:for:)](<../view/toolbarbackground(__for_).md>) to hide the background of the window toolbar.

## See Also

### Getting placements

- [automatic](automatic.md) — The primary toolbar.
- [accessoryBar(id:)](<accessorybar(id_).md>) — Creates a unique accessory bar placement.
- [bottomBar](bottombar.md) — The bottom toolbar of an app.
- [bottomOrnament](bottomornament.md) — The bottom ornament of an app.
- [navigationBar](navigationbar.md) — The navigation bar of an app.
- [tabBar](tabbar.md) — The tab bar of an app.
