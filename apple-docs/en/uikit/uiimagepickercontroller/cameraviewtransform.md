---
title: cameraViewTransform
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.1+, iPadOS 3.1+, Mac Catalyst 13.1+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiimagepickercontroller/cameraviewtransform
source_url: 'https://developer.apple.com/documentation/uikit/uiimagepickercontroller/cameraviewtransform'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiimagepickercontroller/cameraviewtransform.json'
content_hash: 'sha256:fc25f4b92c101f56'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIImagePickerController](../uiimagepickercontroller.md)

# cameraViewTransform

<sub>Instance Property</sub>

The transform to apply to the camera’s preview image.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
var cameraViewTransform: CGAffineTransform { get set }
```

## Discussion

This transform affects the live preview image only and does not affect your custom overlay view or the default image picker controls. You can use this property in conjunction with custom controls to implement your own electronic zoom behaviors.

You can access this property only when the source type of the image picker is set to [UIImagePickerControllerSourceTypeCamera](sourcetype-swift.enum/camera.md). Attempting to access this property for other source types results in the throwing of an [invalidArgumentException](../../foundation/nsexceptionname/invalidargumentexception.md) exception.

## See Also

### Customizing the camera controls

- [Customizing an image picker controller](../customizing-an-image-picker-controller.md) — Manage user interactions and present custom information when taking pictures by adding an overlay view to your image picker.
- [showsCameraControls](showscameracontrols.md) — A Boolean value that indicates whether the image picker displays the default camera controls.
- [cameraOverlayView](cameraoverlayview.md) — The view to display on top of the default image picker interface.
