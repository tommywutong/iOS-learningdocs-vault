---
title: adjustmentData
framework: Photos
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS 10.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photos/phcontenteditingoutput/adjustmentdata
source_url: 'https://developer.apple.com/documentation/photos/phcontenteditingoutput/adjustmentdata'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phcontenteditingoutput/adjustmentdata.json'
content_hash: 'sha256:0941d8967513a226'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHContentEditingOutput](../phcontenteditingoutput.md)

# adjustmentData

<sub>Instance Property</sub>

An object describing the changes made to the asset.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var adjustmentData: PHAdjustmentData? { get set }
```

## Discussion

You use adjustment data to describe the “recipe” for an edit that later edits can make use of. For example, a photo editing app can use this property to save information about the filters applied to a photo. Later, the same app (or another app that understands its adjustment data format) can load the filter information, change the filter parameters, and reapply the filters to the original photo.

If you write new asset content to the URL specified by the [renderedContentURL](renderedcontenturl.md) property, you must also provide a new, distinct [PHAdjustmentData](../phadjustmentdata.md) object describing your edit. Passing a preexisting adjustment data object (that describes an earlier edit) results in undefined behavior.

## See Also

### Providing Edit and Adjustment Data

- [renderedContentURL](renderedcontenturl.md) — The URL at which to write a file containing edited asset content.
