---
title: overrideUserInterfaceStyle
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiviewcontroller/overrideuserinterfacestyle
source_url: 'https://developer.apple.com/documentation/uikit/uiviewcontroller/overrideuserinterfacestyle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiviewcontroller/overrideuserinterfacestyle.json'
content_hash: 'sha256:b950e58f21cf6d6a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIViewController](../uiviewcontroller.md)

# overrideUserInterfaceStyle

<sub>Instance Property</sub>

The user interface style adopted by the view controller and all of its children.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var overrideUserInterfaceStyle: UIUserInterfaceStyle { get set }
```

## Discussion

Use this property to force the view controller to always adopt a light or dark interface style. The default value of this property is [UIUserInterfaceStyleUnspecified](../uiuserinterfacestyle/unspecified.md), which causes the view controller to inherit the interface style from the system or a parent view controller. If you assign a different value, the new style applies to the view controller, its entire view hierarchy, and any embedded child view controllers.

## See Also

### Adjusting the interface style

- [preferredUserInterfaceStyle](preferreduserinterfacestyle.md) — The preferred interface style for this view controller.
- [childViewControllerForUserInterfaceStyle](childviewcontrollerforuserinterfacestyle.md) — The child view controller that supports the preferred user interface style.
- [- setNeedsUserInterfaceAppearanceUpdate](<setneedsuserinterfaceappearanceupdate().md>) — Notifies the view controller that a change occurred that might affect the preferred interface style.
- [UIUserInterfaceStyle](../uiuserinterfacestyle.md) — Constants that indicate the interface style for the app.
