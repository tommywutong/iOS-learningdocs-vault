---
title: objectWasDeleted
framework: Photos
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 10.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photos/phobjectchangedetails/objectwasdeleted
source_url: 'https://developer.apple.com/documentation/photos/phobjectchangedetails/objectwasdeleted'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phobjectchangedetails/objectwasdeleted.json'
content_hash: 'sha256:aae92ab1d0d65080'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHObjectChangeDetails](../phobjectchangedetails.md)

# objectWasDeleted

<sub>Instance Property</sub>

A Boolean value that indicates whether the object has been deleted from the Photos library.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var objectWasDeleted: Bool { get }
```

## Discussion

If this value is `true`, the asset or collection has been permanently deleted from the Photos library.

To instead track the removal of assets from collections (or collections from collection lists), fetch the collection’s contents and use the [changeDetails(for:)](<../phchange/changedetails(for_)-33a6n.md>) method to track changes to the fetch result.

## See Also

### Getting Change Information

- [assetContentChanged](assetcontentchanged.md) — A Boolean value that indicates whether the asset’s photo or video content has changed.
