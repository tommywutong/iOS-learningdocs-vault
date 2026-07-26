---
title: allowsImageEditing
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+（3.1 起废弃）, iPadOS 2.0+（3.1 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/uiimagepickercontroller/allowsimageediting
source_url: 'https://developer.apple.com/documentation/uikit/uiimagepickercontroller/allowsimageediting'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiimagepickercontroller/allowsimageediting.json'
content_hash: 'sha256:46b612c85a10f411'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIImagePickerController](../uiimagepickercontroller.md)

# allowsImageEditing

<sub>Instance Property</sub>

A Boolean value that indicates whether the user is allowed to edit a selected image.

> [!warning] Deprecated
> Use [allowsEditing](allowsediting.md) instead.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
@property (nonatomic) BOOL allowsImageEditing;
```

## Discussion

If you allow the user to edit images, the delegate may receive a dictionary with information about the edits that were made.

This property is set to [false](../../swift/false.md) by default.

## See Also

### Configuring the picker

- [mediaTypes](mediatypes.md) — An array that indicates the media types to access by the media picker controller.
- [allowsEditing](allowsediting.md) — A Boolean value that indicates whether the user is allowed to edit a selected still image or movie.
