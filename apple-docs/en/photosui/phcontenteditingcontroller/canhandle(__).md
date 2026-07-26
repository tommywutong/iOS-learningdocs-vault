---
title: 'canHandle(_:)'
framework: PhotosUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 14.0+, macOS 10.11+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/photosui/phcontenteditingcontroller/canhandle(_:)'
source_url: 'https://developer.apple.com/documentation/photosui/phcontenteditingcontroller/canhandle(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photosui/phcontenteditingcontroller/canhandle%28_%3A%29.json'
content_hash: 'sha256:7d55b01556ff7a0c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [PhotosUI](../../photosui.md) · [PHContentEditingController](../phcontenteditingcontroller.md)

# canHandle(_:)

<sub>Instance Method</sub>

Asks your extension whether it can continue working with the most recent edit that was made to an asset.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
func canHandle(_ adjustmentData: PHAdjustmentData) -> Bool
```

## Parameters

- `adjustmentData` — Use this object to determine whether your extension can work with past edits made to the asset. Typically, you make this decision based on the adjustment data’s [formatIdentifier](../../photos/phadjustmentdata/formatidentifier.md) and [formatVersion](../../photos/phadjustmentdata/formatversion.md) properties.

## Return Value

`true` if your extension supports the adjustment data; otherwise, `false`.

## Discussion

When an asset is edited, Photos stores a [PHAdjustmentData](../../photos/phadjustmentdata.md) object that is provided by the app (or by the extension) that edited the asset. This object provides whatever information is necessary to reconstruct the edited asset using the previous version of the asset’s content. When a user attempts to edit an asset with your extension, Photos calls this block to learn whether your extension can handle the asset’s past adjustments.

If you return `true` from this method, Photos provides the previous asset version for editing. Your extension uses the adjustment data to alter, add to, or reapply the last edit. (For example, an adjustment data may describe filters applied to a photo. Your extension reapplies those filters and allows the user to change filter parameters, add new filters, or remove filters.)

If you return `false` from this method, Photos provides the most recent asset data—the rendered output of the previous edit—for editing.

For more information, see `Working with Asset Versions and Adjustments`.
