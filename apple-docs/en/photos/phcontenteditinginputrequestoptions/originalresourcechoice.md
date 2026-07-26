---
title: originalResourceChoice
framework: Photos
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: /documentation/photos/phcontenteditinginputrequestoptions/originalresourcechoice
source_url: 'https://developer.apple.com/documentation/photos/phcontenteditinginputrequestoptions/originalresourcechoice'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phcontenteditinginputrequestoptions/originalresourcechoice.json'
content_hash: 'sha256:cc3cb4f7659bafc7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHContentEditingInputRequestOptions](../phcontenteditinginputrequestoptions.md)

# originalResourceChoice

<sub>Instance Property</sub>

The original resource to use as the unadjusted base when fulfilling the request.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var originalResourceChoice: PHAsset.OriginalResourceChoice { get set }
```

## Discussion

When set, the content editing input request is fulfilled as though the asset’s original resource choice were the value specified here. This property applies to RAW+JPEG assets only, and is intended for switching between the RAW and compressed resource of such an asset. Setting it for an asset that has only a RAW resource is an error.

## See Also

### Specifying Edting Request Options

- [canHandleAdjustmentData](canhandleadjustmentdata.md) — A block to be called when Photos needs to determine whether your app can continue previous edits made to an asset.
- [skipsDisplaySizeImage](skipsdisplaysizeimage.md) — Set this value to `true` if you don’t want a `displaySizeImage` on the `PHContentEditingInput`. This can give performance wins when the image will not be used. _(beta)_
