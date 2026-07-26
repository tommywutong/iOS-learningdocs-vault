---
title: canContainCollections
framework: Photos
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 10.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photos/phcollection/cancontaincollections
source_url: 'https://developer.apple.com/documentation/photos/phcollection/cancontaincollections'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phcollection/cancontaincollections.json'
content_hash: 'sha256:f9a1de429310a2e2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHCollection](../phcollection.md)

# canContainCollections

<sub>Instance Property</sub>

A Boolean value indicating whether the collection can contain other collections.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var canContainCollections: Bool { get }
```

## Discussion

If this value is `true`, the collection is a [PHCollectionList](../phcollectionlist.md) object; otherwise, `false`. For details on collection lists, see [PHCollectionList](../phcollectionlist.md).

## See Also

### Determining Collection Capabilities

- [canContainAssets](cancontainassets.md) — A Boolean value indicating whether the collection can contain assets.
- [- canPerformEditOperation:](<canperform(__).md>) — Returns whether the collection supports the specified editing operation.
- [PHCollectionEditOperation](../phcollectioneditoperation.md) — Values identifying possible actions that a collection can support, used by the [- canPerformEditOperation:](<canperform(__).md>) method.
