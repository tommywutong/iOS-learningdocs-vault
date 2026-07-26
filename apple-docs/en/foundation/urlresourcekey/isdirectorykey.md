---
title: isDirectoryKey
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/urlresourcekey/isdirectorykey
source_url: 'https://developer.apple.com/documentation/foundation/urlresourcekey/isdirectorykey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlresourcekey/isdirectorykey.json'
content_hash: 'sha256:3322a600a2774d75'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLResourceKey](../urlresourcekey.md)

# isDirectoryKey

<sub>Type Property</sub>

A key for determining whether the resource is a directory.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let isDirectoryKey: URLResourceKey
```

## Discussion

The corresponding value is a read-only Boolean `NSNumber` object.

## See Also

### Directory keys

- [NSURLParentDirectoryURLKey](parentdirectoryurlkey.md) — The container directory of the resource.
- [NSURLDirectoryEntryCountKey](directoryentrycountkey.md) — The key for a count of items in the directory.
