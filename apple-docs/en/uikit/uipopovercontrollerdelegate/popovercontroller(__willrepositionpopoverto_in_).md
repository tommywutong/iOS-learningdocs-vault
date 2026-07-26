---
title: 'popoverController(_:willRepositionPopoverTo:in:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+（9.0 起废弃）, iPadOS 7.0+（9.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, tvOS（9.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/uikit/uipopovercontrollerdelegate/popovercontroller(_:willrepositionpopoverto:in:)'
source_url: 'https://developer.apple.com/documentation/uikit/uipopovercontrollerdelegate/popovercontroller(_:willrepositionpopoverto:in:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipopovercontrollerdelegate/popovercontroller%28_%3Awillrepositionpopoverto%3Ain%3A%29.json'
content_hash: 'sha256:a7d4266267431403'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPopoverControllerDelegate](../uipopovercontrollerdelegate.md)

# popoverController(_:willRepositionPopoverTo:in:)

<sub>Instance Method</sub>

Tells the delegate that the popover controller needs to change the popover’s location in its view.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
optional func popoverController(_ popoverController: UIPopoverController, willRepositionPopoverTo rect: UnsafeMutablePointer<CGRect>, in view: AutoreleasingUnsafeMutablePointer<UIView>)
```

## Parameters

- `popoverController` — The popover controller changing the position of its content.

- `rect` — On input, the proposed rectangle for the popover. This popover is in the coordinate space of the view in the `view` parameter. If you want to propose a different rectangle for the popover, put the new value in this parameter.

- `view` — On input, the proposed view for containing the popover. If you want to propose a different view for the popover, put the new view in this parameter.

## Discussion

For popovers that were presented using the [- presentPopoverFromRect:inView:permittedArrowDirections:animated:](<../uipopovercontroller/present(from_in_permittedarrowdirections_animated_).md>) method, the popover controller calls this method when the interface orientation changes. Your delegate can use this method to adjust the proposed position of the popover. The popover controller does not call this method if you presented the popover from a bar button item.
