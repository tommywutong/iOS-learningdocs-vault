---
title: UIImagePickerController.ImageURLExportPreset
framework: UIKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 11.0+（27.0 起废弃）, iPadOS 11.0+（27.0 起废弃）, Mac Catalyst 13.1+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/uiimagepickercontroller/imageurlexportpreset
source_url: 'https://developer.apple.com/documentation/uikit/uiimagepickercontroller/imageurlexportpreset'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiimagepickercontroller/imageurlexportpreset.json'
content_hash: 'sha256:6e384168a3310847'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIImagePickerController](../uiimagepickercontroller.md)

# UIImagePickerController.ImageURLExportPreset

<sub>Enumeration</sub>

Constants that indicate how to export images to the client app.

> [!warning] Deprecated
> Use [PHPickerViewController](../../photosui/phpickerviewcontroller.md) instead.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
enum ImageURLExportPreset
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Constants

- [UIImagePickerControllerImageURLExportPresetCompatible](imageurlexportpreset/compatible.md) — A preset for converting HEIF formatted images to JPEG. _(deprecated)_
- [UIImagePickerControllerImageURLExportPresetCurrent](imageurlexportpreset/current.md) — A preset for passing image data as-is to the client. _(deprecated)_

### Initializers

- [init(rawValue:)](<imageurlexportpreset/init(rawvalue_).md>) _(deprecated)_

## See Also

### Configuring the export presets

- [imageExportPreset](imageexportpreset.md) — The preset to use when preparing images for export to your app. _(deprecated)_
- [videoExportPreset](videoexportpreset.md) — The preset to use when preparing video for export to your app. _(deprecated)_
