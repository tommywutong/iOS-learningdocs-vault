---
title: UIImagePickerController.SourceType
framework: UIKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS, iPadOS, Mac Catalyst, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiimagepickercontroller/sourcetype-swift.enum
source_url: 'https://developer.apple.com/documentation/uikit/uiimagepickercontroller/sourcetype-swift.enum'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiimagepickercontroller/sourcetype-swift.enum.json'
content_hash: 'sha256:8f02948fe4cae3ae'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIImagePickerController](../uiimagepickercontroller.md)

# UIImagePickerController.SourceType

<sub>Enumeration</sub>

Constants that describe the source to use when picking an image or when determining available media types.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
enum SourceType
```

## Overview

A given source may not be available on a given device because the source is not physically present or because it cannot currently be accessed.

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Constants

- [UIImagePickerControllerSourceTypeCamera](sourcetype-swift.enum/camera.md) — Specifies the device’s built-in camera as the source for the image picker controller.
- [UIImagePickerControllerSourceTypePhotoLibrary](sourcetype-swift.enum/photolibrary.md) — Specifies the device’s photo library as the source for the image picker controller. _(deprecated)_
- [UIImagePickerControllerSourceTypeSavedPhotosAlbum](sourcetype-swift.enum/savedphotosalbum.md) — Specifies the device’s Camera Roll album as the source for the image picker controller. _(deprecated)_

### Initializers

- [init(rawValue:)](<sourcetype-swift.enum/init(rawvalue_).md>)

## See Also

### Setting the picker source

- [+ availableMediaTypesForSourceType:](<availablemediatypes(for_).md>) — Retrieves the available media types for the specified source type.
- [+ isSourceTypeAvailable:](<issourcetypeavailable(__).md>) — Queries whether the device supports picking media using the specified source type.
- [sourceType](sourcetype-swift.property.md) — The type of picker interface to be displayed by the controller.
