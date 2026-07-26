---
title: canContainAssets
framework: Photos
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 10.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photos/phcollection/cancontainassets
source_url: 'https://developer.apple.com/documentation/photos/phcollection/cancontainassets'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phcollection/cancontainassets.json'
content_hash: 'sha256:94c997ad5fe0bf21'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHCollection](../phcollection.md)

# canContainAssets

<sub>Instance Property</sub>

A Boolean value indicating whether the collection can contain assets.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var canContainAssets: Bool { get }
```

## Discussion

If this value is `true`, the collection is a [PHAssetCollection](../phassetcollection.md) object; otherwise, `false`. For details on asset collections, see [PHAssetCollection](../phassetcollection.md).

## See Also

### Determining Collection Capabilities

- [canContainCollections](cancontaincollections.md) — A Boolean value indicating whether the collection can contain other collections.
- [- canPerformEditOperation:](<canperform(__).md>) — Returns whether the collection supports the specified editing operation.
- [PHCollectionEditOperation](../phcollectioneditoperation.md) — Values identifying possible actions that a collection can support, used by the [- canPerformEditOperation:](<canperform(__).md>) method.
