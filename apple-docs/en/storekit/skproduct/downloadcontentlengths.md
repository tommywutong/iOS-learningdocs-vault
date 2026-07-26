---
title: downloadContentLengths
framework: StoreKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 6.0+（16.0 起废弃）, iPadOS 6.0+（16.0 起废弃）, Mac Catalyst 13.1+（16.0 起废弃）, macOS 10.14+（13.0 起废弃）, tvOS（16.0 起废弃）, visionOS 1.0+（2.0 起废弃）, watchOS 6.2+（9.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/storekit/skproduct/downloadcontentlengths
source_url: 'https://developer.apple.com/documentation/storekit/skproduct/downloadcontentlengths'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/skproduct/downloadcontentlengths.json'
content_hash: 'sha256:61918f8d2aae299a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [SKProduct](../skproduct.md)

# downloadContentLengths

<sub>Instance Property</sub>

The lengths of the downloadable files available for this product.

> [!warning] Deprecated
> Hosted content is no longer supported.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var downloadContentLengths: [NSNumber] { get }
```

## Discussion

The array holds [NSNumber](../../foundation/nsnumber.md) objects, each of which holds a `long long` value that is the size of one of the downloadable files (in bytes).

## See Also

### Getting Downloadable Content Information

- [isDownloadable](isdownloadable.md) — A Boolean value that indicates whether the App Store has downloadable content for this product. _(deprecated)_
- [downloadContentVersion](downloadcontentversion.md) — A string that identifies which version of the content is available for download. _(deprecated)_
- [downloadable](downloadable.md) — A Boolean value that indicates whether the App Store has downloadable content for this product. _(deprecated)_
