---
title: downloadable
framework: StoreKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [macOS 10.8+（10.15 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/storekit/skproduct/downloadable
source_url: 'https://developer.apple.com/documentation/storekit/skproduct/downloadable'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/skproduct/downloadable.json'
content_hash: 'sha256:733711d770fac250'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [SKProduct](../skproduct.md)

# downloadable

<sub>Instance Property</sub>

A Boolean value that indicates whether the App Store has downloadable content for this product.

> [!warning] Deprecated
> Use [isDownloadable](isdownloadable.md) instead.

<sub>macOS</sub>

```swift
var downloadable: Bool { get }
```

## Discussion

You can associate a set of data files with the App Store Connect record you created for a product. The value of this property is [true](../../swift/true.md) if at least one file has been associated with the product.

## See Also

### Getting Downloadable Content Information

- [isDownloadable](isdownloadable.md) — A Boolean value that indicates whether the App Store has downloadable content for this product. _(deprecated)_
- [downloadContentLengths](downloadcontentlengths.md) — The lengths of the downloadable files available for this product. _(deprecated)_
- [downloadContentVersion](downloadcontentversion.md) — A string that identifies which version of the content is available for download. _(deprecated)_
