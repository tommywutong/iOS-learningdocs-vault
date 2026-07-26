---
title: delegate
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiimagepickercontroller/delegate
source_url: 'https://developer.apple.com/documentation/uikit/uiimagepickercontroller/delegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiimagepickercontroller/delegate.json'
content_hash: 'sha256:3064dac52d6666e2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIImagePickerController](../uiimagepickercontroller.md)

# delegate

<sub>Instance Property</sub>

The image picker’s delegate object.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
weak var delegate: (any UIImagePickerControllerDelegate & UINavigationControllerDelegate)? { get set }
```

## Discussion

The delegate receives notifications when the user picks an image or movie, or exits the picker interface. The delegate also decides when to dismiss the picker interface, so you must provide a delegate to use a picker. If this property is `nil`, the picker is dismissed immediately if you try to show it.

For information about the methods you can implement for your delegate object, see [UIImagePickerControllerDelegate](../uiimagepickercontrollerdelegate.md).

## See Also

### Responding to interactions with the picker

- [UIImagePickerControllerDelegate](../uiimagepickercontrollerdelegate.md) — A set of methods that your delegate object must implement to interact with the image picker interface.
