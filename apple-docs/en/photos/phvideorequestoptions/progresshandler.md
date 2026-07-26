---
title: progressHandler
framework: Photos
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 10.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photos/phvideorequestoptions/progresshandler
source_url: 'https://developer.apple.com/documentation/photos/phvideorequestoptions/progresshandler'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phvideorequestoptions/progresshandler.json'
content_hash: 'sha256:b72eb13228701a9e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHVideoRequestOptions](../phvideorequestoptions.md)

# progressHandler

<sub>Instance Property</sub>

A block Photos calls periodically while downloading the video.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var progressHandler: PHAssetVideoProgressHandler? { get set }
```

## Discussion

If you request a video whose data is not on the local device, and you have enabled downloading with the [networkAccessAllowed](isnetworkaccessallowed.md) property, Photos calls your block periodically to report progress and to allow you to cancel the download.

## See Also

### Fetching Video Data from iCloud

- [networkAccessAllowed](isnetworkaccessallowed.md) — A Boolean value that specifies whether Photos can download the requested video from iCloud.
- [PHAssetVideoProgressHandler](../phassetvideoprogresshandler.md) — The signature for a block that Photos calls while downloading asset data from iCloud. Used by the [progressHandler](progresshandler.md) property.
