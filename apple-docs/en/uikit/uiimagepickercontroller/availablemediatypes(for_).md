---
title: 'availableMediaTypes(for:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiimagepickercontroller/availablemediatypes(for:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiimagepickercontroller/availablemediatypes(for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiimagepickercontroller/availablemediatypes%28for%3A%29.json'
content_hash: 'sha256:06741103cbc83b47'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIImagePickerController](../uiimagepickercontroller.md)

# availableMediaTypes(for:)

<sub>Type Method</sub>

Retrieves the available media types for the specified source type.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
class func availableMediaTypes(for sourceType: UIImagePickerController.SourceType) -> [String]?
```

## Parameters

- `sourceType` — The source to use to pick an image.

## Return Value

An array whose elements identify the available media types for the specified source type.

## Discussion

Some iOS devices support video recording. Use this method, along with the [+ isSourceTypeAvailable:](<issourcetypeavailable(__).md>) method, to determine if video recording is available on a device. The availability of video recording is indicated by the presence of the `kUTTypeMovie` media type for the [UIImagePickerControllerSourceTypeCamera](sourcetype-swift.enum/camera.md) source type.

## See Also

### Setting the picker source

- [+ isSourceTypeAvailable:](<issourcetypeavailable(__).md>) — Queries whether the device supports picking media using the specified source type.
- [sourceType](sourcetype-swift.property.md) — The type of picker interface to be displayed by the controller.
- [SourceType](sourcetype-swift.enum.md) — Constants that describe the source to use when picking an image or when determining available media types.
