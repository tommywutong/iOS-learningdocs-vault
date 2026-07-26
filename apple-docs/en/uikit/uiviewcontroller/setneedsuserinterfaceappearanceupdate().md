---
title: setNeedsUserInterfaceAppearanceUpdate()
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [tvOS 11.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiviewcontroller/setneedsuserinterfaceappearanceupdate()
source_url: 'https://developer.apple.com/documentation/uikit/uiviewcontroller/setneedsuserinterfaceappearanceupdate()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiviewcontroller/setneedsuserinterfaceappearanceupdate%28%29.json'
content_hash: 'sha256:08aa77bb66600e01'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIViewController](../uiviewcontroller.md)

# setNeedsUserInterfaceAppearanceUpdate()

<sub>Instance Method</sub>

Notifies the view controller that a change occurred that might affect the preferred interface style.

<sub>tvOS</sub>

```swift
func setNeedsUserInterfaceAppearanceUpdate()
```

## Discussion

UIKit calls this method to let the view controller know when system-level interface style changes occur. You can also call it to let UIKit know when you change your view controller in a way that affects the preferred user interface style.

## See Also

### Adjusting the interface style

- [overrideUserInterfaceStyle](overrideuserinterfacestyle.md) — The user interface style adopted by the view controller and all of its children.
- [preferredUserInterfaceStyle](preferreduserinterfacestyle.md) — The preferred interface style for this view controller.
- [childViewControllerForUserInterfaceStyle](childviewcontrollerforuserinterfacestyle.md) — The child view controller that supports the preferred user interface style.
- [UIUserInterfaceStyle](../uiuserinterfacestyle.md) — Constants that indicate the interface style for the app.
