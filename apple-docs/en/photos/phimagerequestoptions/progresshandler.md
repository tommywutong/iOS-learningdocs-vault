---
title: progressHandler
framework: Photos
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 10.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photos/phimagerequestoptions/progresshandler
source_url: 'https://developer.apple.com/documentation/photos/phimagerequestoptions/progresshandler'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phimagerequestoptions/progresshandler.json'
content_hash: 'sha256:b2490e470c69af73'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHImageRequestOptions](../phimagerequestoptions.md)

# progressHandler

<sub>Instance Property</sub>

A block that Photos calls periodically while downloading the image.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var progressHandler: PHAssetImageProgressHandler? { get set }
```

## Discussion

If you request an image whose data is not on the local device, and you have enabled downloading with the [networkAccessAllowed](isnetworkaccessallowed.md) property, Photos calls your block periodically to report progress and to allow you to cancel the download.

## See Also

### Fetching Image Data from iCloud

- [networkAccessAllowed](isnetworkaccessallowed.md) — A Boolean value that specifies whether Photos can download the requested image from iCloud.
- [PHAssetImageProgressHandler](../phassetimageprogresshandler.md) — The signature for a block that Photos calls while downloading asset data from iCloud. Used by the [progressHandler](progresshandler.md) property.
