---
title: childViewControllerForUserInterfaceStyle
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [tvOS 11.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiviewcontroller/childviewcontrollerforuserinterfacestyle
source_url: 'https://developer.apple.com/documentation/uikit/uiviewcontroller/childviewcontrollerforuserinterfacestyle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiviewcontroller/childviewcontrollerforuserinterfacestyle.json'
content_hash: 'sha256:8ea40095c06dd716'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIViewController](../uiviewcontroller.md)

# childViewControllerForUserInterfaceStyle

<sub>Instance Property</sub>

The child view controller that supports the preferred user interface style.

<sub>tvOS</sub>

```swift
var childViewControllerForUserInterfaceStyle: UIViewController? { get }
```

## Discussion

The default value of this property is `nil`. A container view controller can override this property and return the child view controller that supports the currently preferred user interface style, as determined by the [preferredUserInterfaceStyle](preferreduserinterfacestyle.md) property.

## See Also

### Adjusting the interface style

- [overrideUserInterfaceStyle](overrideuserinterfacestyle.md) — The user interface style adopted by the view controller and all of its children.
- [preferredUserInterfaceStyle](preferreduserinterfacestyle.md) — The preferred interface style for this view controller.
- [- setNeedsUserInterfaceAppearanceUpdate](<setneedsuserinterfaceappearanceupdate().md>) — Notifies the view controller that a change occurred that might affect the preferred interface style.
- [UIUserInterfaceStyle](../uiuserinterfacestyle.md) — Constants that indicate the interface style for the app.
