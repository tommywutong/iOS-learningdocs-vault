---
title: invalid
framework: Photos
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 13.0+（15.0 起废弃）, iPadOS 13.0+（15.0 起废弃）, Mac Catalyst 13.0+（15.0 起废弃）, macOS 10.15+（12.0 起废弃）, tvOS 13.0+（15.0 起废弃）, visionOS 1.0+（1.0 起废弃）]
languages: [swift, swift]
beta: false
deprecated: true
doc_path: /documentation/photos/phphotoserror-swift.struct/invalid
source_url: 'https://developer.apple.com/documentation/photos/phphotoserror-swift.struct/invalid'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phphotoserror-swift.struct/invalid.json'
content_hash: 'sha256:2b9a57808140fa53'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHPhotosError](../phphotoserror-swift.struct.md)

# invalid

<sub>Type Property</sub>

The requested operation is invalid.

> [!warning] Deprecated
> Use [internalError](internalerror.md) instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
static var invalid: PHPhotosError.Code { get }
```

## See Also

### Error Codes

- [PHPhotosErrorInvalid](../phphotoserrorinvalid.md) — The requested operation is invalid. _(deprecated)_
- [PHPhotosErrorLibraryVolumeOffline](../phphotoserrorlibraryvolumeoffline.md) — The photo library is unavailable because the file system volume that stores it isn’t mounted. _(deprecated)_
- [PHPhotosErrorRelinquishingLibraryBundleToWriter](../phphotoserrorrelinquishinglibrarybundletowriter.md) — The photo library is unavailable because the user moved, renamed, or deleted the system photo library. _(deprecated)_
- [PHPhotosErrorSwitchingSystemPhotoLibrary](../phphotoserrorswitchingsystemphotolibrary.md) — The photo library is unavailable because the user switched the system photo library. _(deprecated)_
- [PHPhotosErrorUserCancelled](../phphotoserrorusercancelled.md) — The user canceled the asset retrieval or editing request. _(deprecated)_
