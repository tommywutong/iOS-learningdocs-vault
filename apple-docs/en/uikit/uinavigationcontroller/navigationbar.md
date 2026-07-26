---
title: navigationBar
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uinavigationcontroller/navigationbar
source_url: 'https://developer.apple.com/documentation/uikit/uinavigationcontroller/navigationbar'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uinavigationcontroller/navigationbar.json'
content_hash: 'sha256:cda5a55faa829030'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UINavigationController](../uinavigationcontroller.md)

# navigationBar

<sub>Instance Property</sub>

The navigation bar managed by the navigation controller.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var navigationBar: UINavigationBar { get }
```

## Discussion

It is permissible to customize the appearance of the navigation bar using the methods and properties of the [UINavigationBar](../uinavigationbar.md) class but you must never change its [frame](../uiview/frame.md), [bounds](../uiview/bounds.md), or [alpha](../uiview/alpha.md) values or modify its view hierarchy directly. To show or hide the navigation bar, you should always do so through the navigation controller by changing its [navigationBarHidden](isnavigationbarhidden.md) property or calling the [- setNavigationBarHidden:animated:](<setnavigationbarhidden(__animated_).md>) method.

## See Also

### Configuring navigation bars

- [- setNavigationBarHidden:animated:](<setnavigationbarhidden(__animated_).md>) — Sets whether the navigation bar is hidden.
- [Customizing your app’s navigation bar](../customizing-your-app-s-navigation-bar.md) — Create custom titles, prompts, and buttons in your app’s navigation bar.
