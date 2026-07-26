---
title: 'isSourceTypeAvailable(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiimagepickercontroller/issourcetypeavailable(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiimagepickercontroller/issourcetypeavailable(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiimagepickercontroller/issourcetypeavailable%28_%3A%29.json'
content_hash: 'sha256:26924bd9c942f3c0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIImagePickerController](../uiimagepickercontroller.md)

# isSourceTypeAvailable(_:)

<sub>Type Method</sub>

Queries whether the device supports picking media using the specified source type.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
class func isSourceTypeAvailable(_ sourceType: UIImagePickerController.SourceType) -> Bool
```

## Parameters

- `sourceType` — The source to use to pick an image or movie.

## Return Value

[true](../../swift/true.md) if the device supports the specified source type; [false](../../swift/false.md) if the specified source type is not available.

## Discussion

Because a media source may not be present or may be unavailable, devices may not always support all source types. For example, if you attempt to pick an image from the user’s library and the library is empty, this method returns [false](../../swift/false.md). Similarly, if the camera is already in use, this method returns [false](../../swift/false.md).

Before attempting to use an `UIImagePickerController` object to pick an image, you must call this method to ensure that the desired source type is available.

## See Also

### Setting the picker source

- [+ availableMediaTypesForSourceType:](<availablemediatypes(for_).md>) — Retrieves the available media types for the specified source type.
- [sourceType](sourcetype-swift.property.md) — The type of picker interface to be displayed by the controller.
- [SourceType](sourcetype-swift.enum.md) — Constants that describe the source to use when picking an image or when determining available media types.
