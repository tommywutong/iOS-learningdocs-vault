---
title: hidesBottomBarWhenPushed
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS, iPadOS, Mac Catalyst, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiviewcontroller/hidesbottombarwhenpushed
source_url: 'https://developer.apple.com/documentation/uikit/uiviewcontroller/hidesbottombarwhenpushed'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiviewcontroller/hidesbottombarwhenpushed.json'
content_hash: 'sha256:039ea94b8108faf5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIViewController](../uiviewcontroller.md)

# hidesBottomBarWhenPushed

<sub>Instance Property</sub>

A Boolean value indicating whether the toolbar at the bottom of the screen is hidden when the view controller is pushed on to a navigation controller.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var hidesBottomBarWhenPushed: Bool { get set }
```

## Discussion

A view controller added as a child of a navigation controller can display an optional toolbar at the bottom of the screen. The value of this property on the topmost view controller determines whether the toolbar is visible. If the value of this property is [true](../../swift/true.md), the toolbar is hidden. If the value of this property is [false](../../swift/false.md), the bar is visible.

## See Also

### Configuring a navigation interface

- [navigationItem](navigationitem.md) — The navigation item used to represent the view controller in a parent’s navigation bar.
- [- setToolbarItems:animated:](<settoolbaritems(__animated_).md>) — Sets the toolbar items to be displayed along with the view controller.
- [toolbarItems](toolbaritems.md) — The toolbar items associated with the view controller.
