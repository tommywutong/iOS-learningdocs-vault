---
title: PHAssetResourceProgressHandler
framework: Photos
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 10.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photos/phassetresourceprogresshandler
source_url: 'https://developer.apple.com/documentation/photos/phassetresourceprogresshandler'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phassetresourceprogresshandler.json'
content_hash: 'sha256:8f97cb367c5df499'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Photos](../photos.md)

# PHAssetResourceProgressHandler

<sub>Type Alias</sub>

The signature for a block that Photos calls while downloading asset resource data from iCloud. Used by the [progressHandler](phassetresourcerequestoptions/progresshandler.md) property.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
typealias PHAssetResourceProgressHandler = (Double) -> Void
```

## Discussion

If you request an asset resource whose data is not on the local device, and you have enabled downloading with the [networkAccessAllowed](phassetresourcerequestoptions/isnetworkaccessallowed.md) property, Photos calls your block periodically to report progress.

The block takes a single parameter:

- **progress** — A floating-point value indicating the progress of the download. A value of `0.0` indicates that the download has just started, and a value of `1.0` indicates the download is complete.

## See Also

### Fetching Resource Data from iCloud

- [networkAccessAllowed](phassetresourcerequestoptions/isnetworkaccessallowed.md) — A Boolean value that specifies whether Photos can download the requested asset resource data from iCloud.
- [progressHandler](phassetresourcerequestoptions/progresshandler.md) — A block that Photos calls periodically while downloading the asset resource data.
