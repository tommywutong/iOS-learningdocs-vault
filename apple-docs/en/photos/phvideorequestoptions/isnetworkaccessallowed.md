---
title: isNetworkAccessAllowed
framework: Photos
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 10.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photos/phvideorequestoptions/isnetworkaccessallowed
source_url: 'https://developer.apple.com/documentation/photos/phvideorequestoptions/isnetworkaccessallowed'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phvideorequestoptions/isnetworkaccessallowed.json'
content_hash: 'sha256:ac168db59ce4438f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHVideoRequestOptions](../phvideorequestoptions.md)

# isNetworkAccessAllowed

<sub>Instance Property</sub>

A Boolean value that specifies whether Photos can download the requested video from iCloud.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var isNetworkAccessAllowed: Bool { get set }
```

## Discussion

If `true`, and the requested video is not stored on the local device, Photos downloads the video from iCloud. To be notified of the download’s progress, use the [progressHandler](progresshandler.md) property to provide a block that Photos calls periodically while downloading the video. If `false` (the default), and the video is not on the local device, the [PHImageResultIsInCloudKey](../phimageresultisincloudkey.md) value in the result handler’s `info` dictionary indicates that the video is not available unless you enable network access.

## See Also

### Fetching Video Data from iCloud

- [progressHandler](progresshandler.md) — A block Photos calls periodically while downloading the video.
- [PHAssetVideoProgressHandler](../phassetvideoprogresshandler.md) — The signature for a block that Photos calls while downloading asset data from iCloud. Used by the [progressHandler](progresshandler.md) property.
