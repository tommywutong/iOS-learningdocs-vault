---
title: preferredUserInterfaceStyle
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [tvOS 11.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiviewcontroller/preferreduserinterfacestyle
source_url: 'https://developer.apple.com/documentation/uikit/uiviewcontroller/preferreduserinterfacestyle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiviewcontroller/preferreduserinterfacestyle.json'
content_hash: 'sha256:6714c541b2f752ef'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIViewController](../uiviewcontroller.md)

# preferredUserInterfaceStyle

<sub>Instance Property</sub>

The preferred interface style for this view controller.

<sub>tvOS</sub>

```swift
var preferredUserInterfaceStyle: UIUserInterfaceStyle { get }
```

## Discussion

Use this property to apply a specific appearance in your tvOS app. The default value of this property is [UIUserInterfaceStyleUnspecified](../uiuserinterfacestyle/unspecified.md), which causes your view controller to follow the system’s current style. You can override this property to force the view controller to adopt a specific style.

## See Also

### Adjusting the interface style

- [overrideUserInterfaceStyle](overrideuserinterfacestyle.md) — The user interface style adopted by the view controller and all of its children.
- [childViewControllerForUserInterfaceStyle](childviewcontrollerforuserinterfacestyle.md) — The child view controller that supports the preferred user interface style.
- [- setNeedsUserInterfaceAppearanceUpdate](<setneedsuserinterfaceappearanceupdate().md>) — Notifies the view controller that a change occurred that might affect the preferred interface style.
- [UIUserInterfaceStyle](../uiuserinterfacestyle.md) — Constants that indicate the interface style for the app.
