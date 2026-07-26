---
title: isNetworkAccessAllowed
framework: Photos
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 10.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photos/phimagerequestoptions/isnetworkaccessallowed
source_url: 'https://developer.apple.com/documentation/photos/phimagerequestoptions/isnetworkaccessallowed'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phimagerequestoptions/isnetworkaccessallowed.json'
content_hash: 'sha256:10e19f7794a64e8a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHImageRequestOptions](../phimagerequestoptions.md)

# isNetworkAccessAllowed

<sub>Instance Property</sub>

A Boolean value that specifies whether Photos can download the requested image from iCloud.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var isNetworkAccessAllowed: Bool { get set }
```

## Discussion

If `true`, and the requested image is not stored on the local device, Photos downloads the image from iCloud. To be notified of the download’s progress, use the [progressHandler](progresshandler.md) property to provide a block that Photos calls periodically while downloading the image. If `false` (the default), and the image is not on the local device, the [PHImageResultIsInCloudKey](../phimageresultisincloudkey.md) value in the result handler’s `info` dictionary indicates that the image is not available unless you enable network access.

## See Also

### Fetching Image Data from iCloud

- [progressHandler](progresshandler.md) — A block that Photos calls periodically while downloading the image.
- [PHAssetImageProgressHandler](../phassetimageprogresshandler.md) — The signature for a block that Photos calls while downloading asset data from iCloud. Used by the [progressHandler](progresshandler.md) property.
