---
title: isNetworkAccessAllowed
framework: Photos
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 10.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photos/phassetresourcerequestoptions/isnetworkaccessallowed
source_url: 'https://developer.apple.com/documentation/photos/phassetresourcerequestoptions/isnetworkaccessallowed'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phassetresourcerequestoptions/isnetworkaccessallowed.json'
content_hash: 'sha256:e26e578a44038614'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHAssetResourceRequestOptions](../phassetresourcerequestoptions.md)

# isNetworkAccessAllowed

<sub>Instance Property</sub>

A Boolean value that specifies whether Photos can download the requested asset resource data from iCloud.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var isNetworkAccessAllowed: Bool { get set }
```

## Discussion

If `true`, and the requested resource data is not stored on the local device, Photos downloads that data from iCloud. To be notified of the download’s progress, use the [progressHandler](progresshandler.md) property to provide a block that Photos calls periodically while downloading the resource data. If `false` (the default), and the resource data is not on the local device, Photos calls the `completionHandler` block you provided in your request, with an `NSError` object indicating that the resource requires network access.

## See Also

### Fetching Resource Data from iCloud

- [progressHandler](progresshandler.md) — A block that Photos calls periodically while downloading the asset resource data.
- [PHAssetResourceProgressHandler](../phassetresourceprogresshandler.md) — The signature for a block that Photos calls while downloading asset resource data from iCloud. Used by the [progressHandler](progresshandler.md) property.
