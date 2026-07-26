---
title: downloadContentVersion
framework: StoreKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 6.0+（16.0 起废弃）, iPadOS 6.0+（16.0 起废弃）, Mac Catalyst 13.1+（16.0 起废弃）, macOS 10.14+（13.0 起废弃）, tvOS（16.0 起废弃）, visionOS 1.0+（2.0 起废弃）, watchOS 6.2+（9.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/storekit/skproduct/downloadcontentversion
source_url: 'https://developer.apple.com/documentation/storekit/skproduct/downloadcontentversion'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/skproduct/downloadcontentversion.json'
content_hash: 'sha256:3738da39fd7869b1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [SKProduct](../skproduct.md)

# downloadContentVersion

<sub>Instance Property</sub>

A string that identifies which version of the content is available for download.

> [!warning] Deprecated
> Hosted content is no longer supported.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var downloadContentVersion: String { get }
```

## Discussion

The version string is formatted as a series of integers separated by periods.

## See Also

### Getting Downloadable Content Information

- [isDownloadable](isdownloadable.md) — A Boolean value that indicates whether the App Store has downloadable content for this product. _(deprecated)_
- [downloadContentLengths](downloadcontentlengths.md) — The lengths of the downloadable files available for this product. _(deprecated)_
- [downloadable](downloadable.md) — A Boolean value that indicates whether the App Store has downloadable content for this product. _(deprecated)_
