---
title: showsCameraControls
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.1+, iPadOS 3.1+, Mac Catalyst 13.1+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiimagepickercontroller/showscameracontrols
source_url: 'https://developer.apple.com/documentation/uikit/uiimagepickercontroller/showscameracontrols'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiimagepickercontroller/showscameracontrols.json'
content_hash: 'sha256:71b7636dc053652e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIImagePickerController](../uiimagepickercontroller.md)

# showsCameraControls

<sub>Instance Property</sub>

A Boolean value that indicates whether the image picker displays the default camera controls.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
var showsCameraControls: Bool { get set }
```

## Discussion

The default value of this property is [true](../../swift/true.md), which specifies that the default camera controls are visible in the picker. Set it to [false](../../swift/false.md) to hide the default controls if you want to instead provide a custom overlay view using the [cameraOverlayView](cameraoverlayview.md) property.

> [!note] Note
> In iOS 3.1.3 and earlier, hiding the default camera controls limits you to taking still pictures only, regardless of whether movie capture is available on the device.

If you set this property to [false](../../swift/false.md) and provide your own custom controls, you can take multiple pictures before dismissing the image picker interface. However, if you set this property to [true](../../swift/true.md), your delegate must dismiss the image picker interface after the user takes one picture or cancels the operation.

You can access this property only when the source type of the image picker is set to [UIImagePickerControllerSourceTypeCamera](sourcetype-swift.enum/camera.md). Attempting to access this property for other source types results in the throwing of an [invalidArgumentException](../../foundation/nsexceptionname/invalidargumentexception.md) exception. Depending on the value you assign to the [mediaTypes](mediatypes.md) property, the default controls display the still camera or movie camera interface, or a selection control that lets the user choose the picker interface.

## See Also

### Related Documentation

- [- takePicture](<takepicture().md>) — Captures a still image using the camera.

### Customizing the camera controls

- [Customizing an image picker controller](../customizing-an-image-picker-controller.md) — Manage user interactions and present custom information when taking pictures by adding an overlay view to your image picker.
- [cameraOverlayView](cameraoverlayview.md) — The view to display on top of the default image picker interface.
- [cameraViewTransform](cameraviewtransform.md) — The transform to apply to the camera’s preview image.
