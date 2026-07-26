---
title: contentVersion
framework: StoreKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 6.0+（16.0 起废弃）, iPadOS 6.0+（16.0 起废弃）, Mac Catalyst 13.1+（16.0 起废弃）, macOS 10.8+（13.0 起废弃）, tvOS 9.0+（16.0 起废弃）, watchOS 6.2+（9.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/storekit/skdownload/contentversion
source_url: 'https://developer.apple.com/documentation/storekit/skdownload/contentversion'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/skdownload/contentversion.json'
content_hash: 'sha256:8aa204d8c83f4e23'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [SKDownload](../skdownload.md)

# contentVersion

<sub>Instance Property</sub>

A string that identifies which version of the content is available for download.

> [!warning] Deprecated
> Hosted content is no longer supported.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, watchOS</sub>

```swift
var contentVersion: String { get }
```

## Discussion

The version string must be formatted as a series of integers separated by periods.

## See Also

### Getting Content Information

- [expectedContentLength](expectedcontentlength.md) — The length of the downloadable content, in bytes. _(deprecated)_
- [contentIdentifier](contentidentifier.md) — A string that uniquely identifies the downloadable content. _(deprecated)_
- [transaction](transaction.md) — The transaction associated with the downloadable file. _(deprecated)_
- [contentLength](contentlength.md) — The length of the downloadable content, in bytes. _(deprecated)_
