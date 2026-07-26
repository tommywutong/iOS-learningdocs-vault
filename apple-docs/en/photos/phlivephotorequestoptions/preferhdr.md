---
title: preferHDR
framework: Photos
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photos/phlivephotorequestoptions/preferhdr
source_url: 'https://developer.apple.com/documentation/photos/phlivephotorequestoptions/preferhdr'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phlivephotorequestoptions/preferhdr.json'
content_hash: 'sha256:2ccd30f68ffc4a46'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHLivePhotoRequestOptions](../phlivephotorequestoptions.md)

# preferHDR

<sub>Instance Property</sub>

Request HDR image data if available (such as PQ/HLG formats).

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var preferHDR: Bool { get set }
```

## Discussion

Off by default. For best results, only enable this when you intend to display an HDR experience in `PHLivePhotoView` — for example, when the view’s `preferredImageDynamicRange` is greater than standard (SDR). Defaults to `NO`.
