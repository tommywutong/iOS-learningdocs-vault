---
title: isNetworkAccessAllowed
framework: Photos
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 9.1+, iPadOS 9.1+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 10.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photos/phlivephotorequestoptions/isnetworkaccessallowed
source_url: 'https://developer.apple.com/documentation/photos/phlivephotorequestoptions/isnetworkaccessallowed'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phlivephotorequestoptions/isnetworkaccessallowed.json'
content_hash: 'sha256:a42d11d28fe9d66b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHLivePhotoRequestOptions](../phlivephotorequestoptions.md)

# isNetworkAccessAllowed

<sub>Instance Property</sub>

A Boolean value that specifies whether Photos can download the requested Live Photo data from iCloud.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var isNetworkAccessAllowed: Bool { get set }
```

## Discussion

If `true`, and the requested Live Photo data is not stored on the local device, Photos downloads that data from iCloud. To be notified of the download’s progress, use the [progressHandler](progresshandler.md) property to provide a block that Photos calls periodically while downloading. If `false` (the default), and the Live Photo data is not on the local device, the [PHImageResultIsInCloudKey](../phimageresultisincloudkey.md) value in the result handler’s `info` dictionary indicates that the data is not available unless you enable network access.

## See Also

### Fetching Image Data from iCloud

- [progressHandler](progresshandler.md) — A block that Photos calls periodically while downloading the Live Photo.
