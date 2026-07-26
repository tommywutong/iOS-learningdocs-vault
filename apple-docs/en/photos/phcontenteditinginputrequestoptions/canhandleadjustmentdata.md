---
title: canHandleAdjustmentData
framework: Photos
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 10.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photos/phcontenteditinginputrequestoptions/canhandleadjustmentdata
source_url: 'https://developer.apple.com/documentation/photos/phcontenteditinginputrequestoptions/canhandleadjustmentdata'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phcontenteditinginputrequestoptions/canhandleadjustmentdata.json'
content_hash: 'sha256:e24364d894818c78'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHContentEditingInputRequestOptions](../phcontenteditinginputrequestoptions.md)

# canHandleAdjustmentData

<sub>Instance Property</sub>

A block to be called when Photos needs to determine whether your app can continue previous edits made to an asset.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var canHandleAdjustmentData: (PHAdjustmentData) -> Bool { get set }
```

## Discussion

When an asset is edited, Photos stores a [PHAdjustmentData](../phadjustmentdata.md) object provided by the app or extension that edited the asset. This object provides all information necessary to reconstruct the edited asset using the original asset data. When your app requests to edit an asset, Photos calls this block to inquire whether your app can handle the asset’s past adjustments.

The block takes the following parameter:

- **adjustmentData** — A [PHAdjustmentData](../phadjustmentdata.md) object you can use to determine whether your app can work with past edits made to the asset. Typically, you make this decision based on the adjustment data’s [formatIdentifier](../phadjustmentdata/formatidentifier.md) and [formatVersion](../phadjustmentdata/formatversion.md) properties.

If your block returns `true`, Photos provides the original asset data for editing. Your app uses the adjustment data to alter, add to, or reapply previous edits. (For example, an adjustment data may describe filters applied to a photo. Your app reapplies those filters and allows the user to change filter parameters, add new filters, or remove filters.)

If your block returns `false`, Photos provides the most recent asset data—the rendered output of all previous edits—for editing.

## See Also

### Specifying Edting Request Options

- [originalResourceChoice](originalresourcechoice.md) — The original resource to use as the unadjusted base when fulfilling the request. _(beta)_
- [skipsDisplaySizeImage](skipsdisplaysizeimage.md) — Set this value to `true` if you don’t want a `displaySizeImage` on the `PHContentEditingInput`. This can give performance wins when the image will not be used. _(beta)_
