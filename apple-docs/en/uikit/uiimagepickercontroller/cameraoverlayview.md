---
title: cameraOverlayView
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.1+, iPadOS 3.1+, Mac Catalyst 13.1+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiimagepickercontroller/cameraoverlayview
source_url: 'https://developer.apple.com/documentation/uikit/uiimagepickercontroller/cameraoverlayview'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiimagepickercontroller/cameraoverlayview.json'
content_hash: 'sha256:ec3436229451ad63'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIImagePickerController](../uiimagepickercontroller.md)

# cameraOverlayView

<sub>Instance Property</sub>

The view to display on top of the default image picker interface.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
var cameraOverlayView: UIView? { get set }
```

## Discussion

You can use an overlay view to present a custom view hierarchy on top of the default image picker interface. The image picker layers your custom overlay view on top of the other image picker views and positions it relative to the screen coordinates. If you have the default camera controls set to be visible, incorporate transparency into your view, or position it to avoid obscuring the underlying content.

You can access this property only when the source type of the image picker is set to [UIImagePickerControllerSourceTypeCamera](sourcetype-swift.enum/camera.md). Attempting to access this property for other source types results in throwing an [invalidArgumentException](../../foundation/nsexceptionname/invalidargumentexception.md) exception.

## See Also

### Customizing the camera controls

- [Customizing an image picker controller](../customizing-an-image-picker-controller.md) — Manage user interactions and present custom information when taking pictures by adding an overlay view to your image picker.
- [showsCameraControls](showscameracontrols.md) — A Boolean value that indicates whether the image picker displays the default camera controls.
- [cameraViewTransform](cameraviewtransform.md) — The transform to apply to the camera’s preview image.
