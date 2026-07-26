---
title: skipsDisplaySizeImage
framework: Photos
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: /documentation/photos/phcontenteditinginputrequestoptions/skipsdisplaysizeimage
source_url: 'https://developer.apple.com/documentation/photos/phcontenteditinginputrequestoptions/skipsdisplaysizeimage'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phcontenteditinginputrequestoptions/skipsdisplaysizeimage.json'
content_hash: 'sha256:585d4c701c24b184'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHContentEditingInputRequestOptions](../phcontenteditinginputrequestoptions.md)

# skipsDisplaySizeImage

<sub>Instance Property</sub>

Set this value to `true` if you don’t want a `displaySizeImage` on the `PHContentEditingInput`. This can give performance wins when the image will not be used.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var skipsDisplaySizeImage: Bool { get set }
```

## See Also

### Specifying Edting Request Options

- [canHandleAdjustmentData](canhandleadjustmentdata.md) — A block to be called when Photos needs to determine whether your app can continue previous edits made to an asset.
- [originalResourceChoice](originalresourcechoice.md) — The original resource to use as the unadjusted base when fulfilling the request. _(beta)_
