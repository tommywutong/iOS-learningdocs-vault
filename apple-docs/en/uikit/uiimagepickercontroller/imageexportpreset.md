---
title: imageExportPreset
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+（27.0 起废弃）, iPadOS 11.0+（27.0 起废弃）, Mac Catalyst 13.1+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/uiimagepickercontroller/imageexportpreset
source_url: 'https://developer.apple.com/documentation/uikit/uiimagepickercontroller/imageexportpreset'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiimagepickercontroller/imageexportpreset.json'
content_hash: 'sha256:433937918d9c9a2b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIImagePickerController](../uiimagepickercontroller.md)

# imageExportPreset

<sub>Instance Property</sub>

The preset to use when preparing images for export to your app.

> [!warning] Deprecated
> Use [PHPickerViewController](../../photosui/phpickerviewcontroller.md) instead.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var imageExportPreset: UIImagePickerController.ImageURLExportPreset { get set }
```

## Discussion

The default value of this property is [UIImagePickerControllerImageURLExportPresetCompatible](imageurlexportpreset/compatible.md).

## See Also

### Configuring the export presets

- [ImageURLExportPreset](imageurlexportpreset.md) — Constants that indicate how to export images to the client app. _(deprecated)_
- [videoExportPreset](videoexportpreset.md) — The preset to use when preparing video for export to your app. _(deprecated)_
