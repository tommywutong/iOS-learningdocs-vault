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
doc_path: /documentation/photos/phcontenteditinginputrequestoptions/progresshandler
source_url: 'https://developer.apple.com/documentation/photos/phcontenteditinginputrequestoptions/progresshandler'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phcontenteditinginputrequestoptions/progresshandler.json'
content_hash: 'sha256:7e979b0c203654fb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHContentEditingInputRequestOptions](../phcontenteditinginputrequestoptions.md)

# progressHandler

<sub>Instance Property</sub>

A block Photos calls periodically while downloading the asset.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var progressHandler: ((Double, UnsafeMutablePointer<ObjCBool>) -> Void)? { get set }
```

## Discussion

If you request an asset whose data is not on the local device, and have enabled downloading with the [networkAccessAllowed](isnetworkaccessallowed.md) property, Photos calls your block periodically to report progress and allow canceling the download.

The block takes the following parameters:

- **progress** — A floating-point value indicating the progress of the download. A value of `0.0` indicates the download has just started, and a value of `1.0` indicates the download is complete.
- **stop** — A pointer to a Boolean value. Set `*stop` to `true` inside the block to cancel the download.

## See Also

### Fetching Asset Data from iCloud

- [networkAccessAllowed](isnetworkaccessallowed.md) — A Boolean value that specifies whether Photos can download the asset from iCloud.
