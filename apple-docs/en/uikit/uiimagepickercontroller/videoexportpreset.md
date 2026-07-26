---
title: videoExportPreset
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+（27.0 起废弃）, iPadOS 11.0+（27.0 起废弃）, Mac Catalyst 13.1+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/uiimagepickercontroller/videoexportpreset
source_url: 'https://developer.apple.com/documentation/uikit/uiimagepickercontroller/videoexportpreset'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiimagepickercontroller/videoexportpreset.json'
content_hash: 'sha256:db7417c89d045536'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIImagePickerController](../uiimagepickercontroller.md)

# videoExportPreset

<sub>Instance Property</sub>

The preset to use when preparing video for export to your app.

> [!warning] Deprecated
> Use [PHPickerViewController](../../photosui/phpickerviewcontroller.md) with [AVAssetExportSession](../../avfoundation/avassetexportsession.md) instead.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var videoExportPreset: String { get set }
```

## Discussion

The value of this key is one of the export presets supported by the [AVAssetExportSession](../../avfoundation/avassetexportsession.md) class. For a list of possible values, see the export preset constants in [AVAssetExportSession](../../avfoundation/avassetexportsession.md).

## See Also

### Configuring the export presets

- [imageExportPreset](imageexportpreset.md) — The preset to use when preparing images for export to your app. _(deprecated)_
- [ImageURLExportPreset](imageurlexportpreset.md) — Constants that indicate how to export images to the client app. _(deprecated)_
