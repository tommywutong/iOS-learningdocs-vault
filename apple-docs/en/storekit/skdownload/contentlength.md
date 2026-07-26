---
title: contentLength
framework: StoreKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 6.0+（13.0 起废弃）, iPadOS 6.0+（13.0 起废弃）, Mac Catalyst 13.0+（13.0 起废弃）, macOS 10.8+（10.15 起废弃）, tvOS 9.0+（13.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/storekit/skdownload/contentlength
source_url: 'https://developer.apple.com/documentation/storekit/skdownload/contentlength'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/skdownload/contentlength.json'
content_hash: 'sha256:1c97cc6a7ac55b8d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [SKDownload](../skdownload.md)

# contentLength

<sub>Instance Property</sub>

The length of the downloadable content, in bytes.

> [!warning] Deprecated
> Use [expectedContentLength](expectedcontentlength.md) instead.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
var contentLength: Int64 { get }
```

<sub>macOS</sub>

```swift
@NSCopying var contentLength: NSNumber { get }
```

## See Also

### Getting Content Information

- [expectedContentLength](expectedcontentlength.md) — The length of the downloadable content, in bytes. _(deprecated)_
- [contentIdentifier](contentidentifier.md) — A string that uniquely identifies the downloadable content. _(deprecated)_
- [contentVersion](contentversion.md) — A string that identifies which version of the content is available for download. _(deprecated)_
- [transaction](transaction.md) — The transaction associated with the downloadable file. _(deprecated)_
