---
title: sourceType
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiimagepickercontroller/sourcetype-swift.property
source_url: 'https://developer.apple.com/documentation/uikit/uiimagepickercontroller/sourcetype-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiimagepickercontroller/sourcetype-swift.property.json'
content_hash: 'sha256:63eb3b69101ae3f1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIImagePickerController](../uiimagepickercontroller.md)

# sourceType

<sub>Instance Property</sub>

The type of picker interface to be displayed by the controller.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var sourceType: UIImagePickerController.SourceType { get set }
```

## Discussion

Prior to running the picker interface, set this value to the desired source type. The source type you set must be available and an exception is thrown if it is not. If you change this property while the picker is visible, the picker interface changes to match the new value in this property.

The various source types are listed in the [SourceType](sourcetype-swift.enum.md) enumeration. The default value is [UIImagePickerControllerSourceTypePhotoLibrary](sourcetype-swift.enum/photolibrary.md).

## See Also

### Setting the picker source

- [+ availableMediaTypesForSourceType:](<availablemediatypes(for_).md>) — Retrieves the available media types for the specified source type.
- [+ isSourceTypeAvailable:](<issourcetypeavailable(__).md>) — Queries whether the device supports picking media using the specified source type.
- [SourceType](sourcetype-swift.enum.md) — Constants that describe the source to use when picking an image or when determining available media types.
