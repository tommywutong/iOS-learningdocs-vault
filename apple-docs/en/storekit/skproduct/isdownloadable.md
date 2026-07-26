---
title: isDownloadable
framework: StoreKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 6.0+（16.0 起废弃）, iPadOS 6.0+（16.0 起废弃）, Mac Catalyst 13.1+（16.0 起废弃）, macOS 10.15+（13.0 起废弃）, tvOS（16.0 起废弃）, visionOS 1.0+（2.0 起废弃）, watchOS 6.2+（9.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/storekit/skproduct/isdownloadable
source_url: 'https://developer.apple.com/documentation/storekit/skproduct/isdownloadable'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/skproduct/isdownloadable.json'
content_hash: 'sha256:0b1dba3db81e1d5b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [SKProduct](../skproduct.md)

# isDownloadable

<sub>Instance Property</sub>

A Boolean value that indicates whether the App Store has downloadable content for this product.

> [!warning] Deprecated
> Hosted content is no longer supported.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var isDownloadable: Bool { get }
```

## Discussion

You can associate a set of data files with the App Store Connect record you created for a product. The value of this property is [true](../../swift/true.md) if at least one file has been associated with the product.

## See Also

### Getting Downloadable Content Information

- [downloadContentLengths](downloadcontentlengths.md) — The lengths of the downloadable files available for this product. _(deprecated)_
- [downloadContentVersion](downloadcontentversion.md) — A string that identifies which version of the content is available for download. _(deprecated)_
- [downloadable](downloadable.md) — A Boolean value that indicates whether the App Store has downloadable content for this product. _(deprecated)_
