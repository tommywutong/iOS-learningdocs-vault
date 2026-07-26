---
title: PHPhotosErrorUserCancelled
framework: Photos
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 13.0+（14.0 起废弃）, iPadOS 13.0+（14.0 起废弃）, Mac Catalyst 13.0+（14.0 起废弃）, macOS 10.15+（11.0 起废弃）, tvOS 13.0+（14.0 起废弃）, visionOS 1.0+（1.0 起废弃）]
languages: [swift, swift]
beta: false
deprecated: true
doc_path: /documentation/photos/phphotoserrorusercancelled
source_url: 'https://developer.apple.com/documentation/photos/phphotoserrorusercancelled'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phphotoserrorusercancelled.json'
content_hash: 'sha256:d4dc1eb4b628836c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Photos](../photos.md)

# PHPhotosErrorUserCancelled

<sub>Global Variable</sub>

The user canceled the asset retrieval or editing request.

> [!warning] Deprecated
> Use [PHPhotosErrorUserCancelled](phphotoserror-swift.struct/code/usercancelled.md) instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var PHPhotosErrorUserCancelled: Int { get }
```

## See Also

### Error Codes

- [invalid](phphotoserror-swift.struct/invalid.md) — The requested operation is invalid. _(deprecated)_
- [PHPhotosErrorInvalid](phphotoserrorinvalid.md) — The requested operation is invalid. _(deprecated)_
- [PHPhotosErrorLibraryVolumeOffline](phphotoserrorlibraryvolumeoffline.md) — The photo library is unavailable because the file system volume that stores it isn’t mounted. _(deprecated)_
- [PHPhotosErrorRelinquishingLibraryBundleToWriter](phphotoserrorrelinquishinglibrarybundletowriter.md) — The photo library is unavailable because the user moved, renamed, or deleted the system photo library. _(deprecated)_
- [PHPhotosErrorSwitchingSystemPhotoLibrary](phphotoserrorswitchingsystemphotolibrary.md) — The photo library is unavailable because the user switched the system photo library. _(deprecated)_
