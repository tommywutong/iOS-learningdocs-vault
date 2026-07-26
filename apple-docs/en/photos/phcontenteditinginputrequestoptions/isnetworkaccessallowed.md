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
doc_path: /documentation/photos/phcontenteditinginputrequestoptions/isnetworkaccessallowed
source_url: 'https://developer.apple.com/documentation/photos/phcontenteditinginputrequestoptions/isnetworkaccessallowed'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phcontenteditinginputrequestoptions/isnetworkaccessallowed.json'
content_hash: 'sha256:2945d6b68d2b16af'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHContentEditingInputRequestOptions](../phcontenteditinginputrequestoptions.md)

# isNetworkAccessAllowed

<sub>Instance Property</sub>

A Boolean value that specifies whether Photos can download the asset from iCloud.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var isNetworkAccessAllowed: Bool { get set }
```

## Discussion

By default, the value is `false`. If `true`, Photos downloads the asset for editing if it’s not available on the local device. Use the [progressHandler](progresshandler.md) property to track the progress of the download.

## See Also

### Fetching Asset Data from iCloud

- [progressHandler](progresshandler.md) — A block Photos calls periodically while downloading the asset.
