---
title: parentDirectoryURLKey
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/urlresourcekey/parentdirectoryurlkey
source_url: 'https://developer.apple.com/documentation/foundation/urlresourcekey/parentdirectoryurlkey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlresourcekey/parentdirectoryurlkey.json'
content_hash: 'sha256:da4e7f6b0987e581'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLResourceKey](../urlresourcekey.md)

# parentDirectoryURLKey

<sub>Type Property</sub>

The container directory of the resource.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let parentDirectoryURLKey: URLResourceKey
```

## Discussion

The corresponding value is a read-only `NSURL` object, or `nil` if the resource is the root directory of its volume.

## See Also

### Directory keys

- [NSURLIsDirectoryKey](isdirectorykey.md) — A key for determining whether the resource is a directory.
- [NSURLDirectoryEntryCountKey](directoryentrycountkey.md) — The key for a count of items in the directory.
