---
title: primaryBackgroundStyle
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uisplitviewcontroller/primarybackgroundstyle
source_url: 'https://developer.apple.com/documentation/uikit/uisplitviewcontroller/primarybackgroundstyle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uisplitviewcontroller/primarybackgroundstyle.json'
content_hash: 'sha256:15ef5e8914bc0bc7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISplitViewController](../uisplitviewcontroller.md)

# primaryBackgroundStyle

<sub>Instance Property</sub>

The background style of the primary view controller.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var primaryBackgroundStyle: UISplitViewController.BackgroundStyle { get set }
```

## Discussion

In macOS, the sidebar of a split view has Liquid Glass behind its view. To achieve this effect in your iPad app when it runs in macOS, set [primaryBackgroundStyle](primarybackgroundstyle.md) to [UISplitViewControllerBackgroundStyleSidebar](backgroundstyle/sidebar.md). Set the style to [UISplitViewControllerBackgroundStyleNone](backgroundstyle/none.md) when you want to control the background appearance of the primary view controller.

> [!note] Note
> Setting the background style to [UISplitViewControllerBackgroundStyleSidebar](backgroundstyle/sidebar.md) has no effect when your app is running in iOS or tvOS.

## See Also

### Managing the background style

- [BackgroundStyle](backgroundstyle.md) — Styles that apply a visual effect to the background of a primary view controller.
