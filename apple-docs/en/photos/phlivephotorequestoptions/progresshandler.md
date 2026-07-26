---
title: progressHandler
framework: Photos
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 9.1+, iPadOS 9.1+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 10.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photos/phlivephotorequestoptions/progresshandler
source_url: 'https://developer.apple.com/documentation/photos/phlivephotorequestoptions/progresshandler'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phlivephotorequestoptions/progresshandler.json'
content_hash: 'sha256:9af3ff04b06ccdd5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHLivePhotoRequestOptions](../phlivephotorequestoptions.md)

# progressHandler

<sub>Instance Property</sub>

A block that Photos calls periodically while downloading the Live Photo.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var progressHandler: PHAssetImageProgressHandler? { get set }
```

## Discussion

If you request a Live Photo whose data is not on the local device, and you have enabled downloading with the [PHLivePhotoRequestOptions](../phlivephotorequestoptions.md) property, Photos calls your block periodically to report progress and to allow you to cancel the download.

## See Also

### Fetching Image Data from iCloud

- [networkAccessAllowed](isnetworkaccessallowed.md) — A Boolean value that specifies whether Photos can download the requested Live Photo data from iCloud.
