---
title: childViewControllerForTouchBar
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [Mac Catalyst 13.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiviewcontroller/childviewcontrollerfortouchbar
source_url: 'https://developer.apple.com/documentation/uikit/uiviewcontroller/childviewcontrollerfortouchbar'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiviewcontroller/childviewcontrollerfortouchbar.json'
content_hash: 'sha256:42969ece789f5f9f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIViewController](../uiviewcontroller.md)

# childViewControllerForTouchBar

<sub>Instance Property</sub>

The child view controller that the system uses to display content in the Touch Bar.

<sub>Mac Catalyst</sub>

```swift
var childViewControllerForTouchBar: UIViewController? { get }
```

## Discussion

Override this property to have the system use the [touchBar](../uiresponder/touchbar.md) object from a child view controller instead of the current view controller. If [childViewControllerForTouchBar](childviewcontrollerfortouchbar.md) is `nil`, the system uses the current view controller’s [touchBar](../uiresponder/touchbar.md) object.

The default value is `nil`.

## See Also

### Managing the Touch Bar

- [- setNeedsTouchBarUpdate](<setneedstouchbarupdate().md>) — Tells the system to update the Touch Bar.
