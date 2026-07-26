---
title: progressHandler
framework: Photos
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 10.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photos/phassetresourcerequestoptions/progresshandler
source_url: 'https://developer.apple.com/documentation/photos/phassetresourcerequestoptions/progresshandler'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phassetresourcerequestoptions/progresshandler.json'
content_hash: 'sha256:fdb0f0641dee472f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHAssetResourceRequestOptions](../phassetresourcerequestoptions.md)

# progressHandler

<sub>Instance Property</sub>

A block that Photos calls periodically while downloading the asset resource data.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var progressHandler: PHAssetResourceProgressHandler? { get set }
```

## Discussion

If you request an asset resource whose data is not on the local device, and you have enabled downloading with the [networkAccessAllowed](isnetworkaccessallowed.md) property, Photos calls your block periodically to report progress.

## See Also

### Fetching Resource Data from iCloud

- [networkAccessAllowed](isnetworkaccessallowed.md) — A Boolean value that specifies whether Photos can download the requested asset resource data from iCloud.
- [PHAssetResourceProgressHandler](../phassetresourceprogresshandler.md) — The signature for a block that Photos calls while downloading asset resource data from iCloud. Used by the [progressHandler](progresshandler.md) property.
