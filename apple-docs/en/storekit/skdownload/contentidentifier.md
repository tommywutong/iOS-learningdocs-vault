---
title: contentIdentifier
framework: StoreKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 6.0+（16.0 起废弃）, iPadOS 6.0+（16.0 起废弃）, Mac Catalyst 13.1+（16.0 起废弃）, macOS 10.8+（13.0 起废弃）, tvOS 9.0+（16.0 起废弃）, watchOS 6.2+（9.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/storekit/skdownload/contentidentifier
source_url: 'https://developer.apple.com/documentation/storekit/skdownload/contentidentifier'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/skdownload/contentidentifier.json'
content_hash: 'sha256:d8489397f1b96f4b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [SKDownload](../skdownload.md)

# contentIdentifier

<sub>Instance Property</sub>

A string that uniquely identifies the downloadable content.

> [!warning] Deprecated
> Hosted content is no longer supported.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, watchOS</sub>

```swift
var contentIdentifier: String { get }
```

## Discussion

Each piece of downloadable content associated with a product has its own unique identifier. The content identifier is specified in App Store Connect when you add the content.

## See Also

### Related Documentation

- [In-App Purchase Programming Guide](https://developer.apple.com/library/archive/documentation/NetworkingInternet/Conceptual/StoreKitGuide/Introduction.html#//apple_ref/doc/uid/TP40008267)

### Getting Content Information

- [expectedContentLength](expectedcontentlength.md) — The length of the downloadable content, in bytes. _(deprecated)_
- [contentVersion](contentversion.md) — A string that identifies which version of the content is available for download. _(deprecated)_
- [transaction](transaction.md) — The transaction associated with the downloadable file. _(deprecated)_
- [contentLength](contentlength.md) — The length of the downloadable content, in bytes. _(deprecated)_
