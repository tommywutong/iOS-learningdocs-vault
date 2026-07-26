---
title: 'imagePickerController:didFinishPickingImage:editingInfo:'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+（3.0 起废弃）, iPadOS 2.0+（3.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: '/documentation/uikit/uiimagepickercontrollerdelegate/imagepickercontroller:didfinishpickingimage:editinginfo:'
source_url: 'https://developer.apple.com/documentation/uikit/uiimagepickercontrollerdelegate/imagepickercontroller:didfinishpickingimage:editinginfo:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiimagepickercontrollerdelegate/imagepickercontroller%3Adidfinishpickingimage%3Aeditinginfo%3A.json'
content_hash: 'sha256:8f8beb670e4a661d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIImagePickerControllerDelegate](../uiimagepickercontrollerdelegate.md)

# imagePickerController:didFinishPickingImage:editingInfo:

<sub>Instance Method</sub>

Tells the delegate that the user picked an image.

> [!warning] Deprecated
> Use [- imagePickerController:didFinishPickingMediaWithInfo:](<imagepickercontroller(__didfinishpickingmediawithinfo_).md>) instead.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
- (void) imagePickerController:(UIImagePickerController *) picker didFinishPickingImage:(UIImage *) image editingInfo:(NSDictionary<NSString *,id> *) editingInfo;
```

## Parameters

- `picker` — The controller object managing the image picker interface.

- `image` — The image that the user picked. If user editing is enabled, this may be a cropped and adjusted version of the original image. In this case, the original image, and the editing information, are available in the `editingInfo` parameter.

- `editingInfo` — A dictionary containing any relevant editing information. If editing is disabled, this parameter is `nil`. The keys for this dictionary are listed in `Editing Information Keys`.

## Discussion

Your delegate’s implementation of this method should pass the specified image on to any custom code that needs it and then dismiss the picker view.

When user editing is enabled, the picker view presents the user with a preview of the currently selected image along with controls for modifying it. (This behavior is managed by the picker view prior to calling this method.) If the user modifies the image, the editing information is available in the `editingInfo` parameter. If you don’t need the editing information, simply use the image in the `image` parameter as is.

### Special Considerations

This deprecated method supports picking only still pictures. The replacement method, [- imagePickerController:didFinishPickingMediaWithInfo:](<imagepickercontroller(__didfinishpickingmediawithinfo_).md>), supports picking movies as well as still pictures.

## See Also

### Closing the picker

- [- imagePickerController:didFinishPickingMediaWithInfo:](<imagepickercontroller(__didfinishpickingmediawithinfo_).md>) — Tells the delegate that the user picked a still image or movie.
- [- imagePickerControllerDidCancel:](<imagepickercontrollerdidcancel(__).md>) — Tells the delegate that the user canceled the pick operation.
