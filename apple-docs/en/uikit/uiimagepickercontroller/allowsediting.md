---
title: allowsEditing
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.1+, iPadOS 3.1+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiimagepickercontroller/allowsediting
source_url: 'https://developer.apple.com/documentation/uikit/uiimagepickercontroller/allowsediting'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiimagepickercontroller/allowsediting.json'
content_hash: 'sha256:04f9db86f423d20a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIImagePickerController](../uiimagepickercontroller.md)

# allowsEditing

<sub>Instance Property</sub>

A Boolean value that indicates whether the user is allowed to edit a selected still image or movie.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var allowsEditing: Bool { get set }
```

## Discussion

If you allow the user to edit still images or movies, the delegate may receive a dictionary with information about the edits that were made. The protocol for the delegate is described in [UIImagePickerControllerDelegate](../uiimagepickercontrollerdelegate.md).

This property is set to [false](../../swift/false.md) by default.

## See Also

### Configuring the picker

- [mediaTypes](mediatypes.md) — An array that indicates the media types to access by the media picker controller.
