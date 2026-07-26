---
title: isToolbarHidden
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uinavigationcontroller/istoolbarhidden
source_url: 'https://developer.apple.com/documentation/uikit/uinavigationcontroller/istoolbarhidden'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uinavigationcontroller/istoolbarhidden.json'
content_hash: 'sha256:e19bc3fd24200873'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UINavigationController](../uinavigationcontroller.md)

# isToolbarHidden

<sub>Instance Property</sub>

A Boolean indicating whether the navigation controller’s built-in toolbar is visible.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var isToolbarHidden: Bool { get set }
```

## Discussion

If this property is set to [true](../../swift/true.md), the toolbar is not visible. The default value of this property is [true](../../swift/true.md).

## See Also

### Configuring custom toolbars

- [toolbar](toolbar.md) — The custom toolbar associated with the navigation controller.
- [- setToolbarHidden:animated:](<settoolbarhidden(__animated_).md>) — Changes the visibility of the navigation controller’s built-in toolbar.
- [UINavigationControllerHideShowBarDuration](hideshowbarduration.md) — A variable that specifies the duration when animating the navigation bar.
