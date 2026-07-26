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
doc_path: /documentation/photos/phimagerequestoptions/preferhdr
source_url: 'https://developer.apple.com/documentation/photos/phimagerequestoptions/preferhdr'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phimagerequestoptions/preferhdr.json'
content_hash: 'sha256:5395dcc5932ca23c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHImageRequestOptions](../phimagerequestoptions.md)

# preferHDR

<sub>Instance Property</sub>

Request HDR image data if available (such as PQ/HLG formats).

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var preferHDR: Bool { get set }
```

## Discussion

When set to `YES`, the image manager will attempt to provide HDR image data if the asset contains HDR content. Defaults to `NO`.
