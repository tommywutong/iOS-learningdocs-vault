---
title: 'bookmarkData(options:includingResourceValuesForKeys:relativeTo:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/url/bookmarkdata(options:includingresourcevaluesforkeys:relativeto:)'
source_url: 'https://developer.apple.com/documentation/foundation/url/bookmarkdata(options:includingresourcevaluesforkeys:relativeto:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/url/bookmarkdata%28options%3Aincludingresourcevaluesforkeys%3Arelativeto%3A%29.json'
content_hash: 'sha256:b51fe175e545312f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URL](../url.md)

# bookmarkData(options:includingResourceValuesForKeys:relativeTo:)

<sub>Instance Method</sub>

Returns bookmark data for the URL, created with specified options and resource values.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func bookmarkData(options: URL.BookmarkCreationOptions = [], includingResourceValuesForKeys keys: Set<URLResourceKey>? = nil, relativeTo url: URL? = nil) throws -> Data
```

## See Also

### Creating bookmarks

- [bookmarkData(withContentsOf:)](<bookmarkdata(withcontentsof_).md>) — Initializes and returns bookmark data derived from an alias file pointed to by a specified URL.
- [writeBookmarkData(_:to:)](<writebookmarkdata(__to_).md>) — Creates an alias file on disk at a specified location with specified bookmark data.
- [resourceValues(forKeys:fromBookmarkData:)](<resourcevalues(forkeys_frombookmarkdata_).md>) — Returns the resource values for properties identified by a specified array of keys contained in specified bookmark data.
- [BookmarkCreationOptions](bookmarkcreationoptions.md) — An alias for bookmark creation options.
- [BookmarkCreationOptions](../nsurl/bookmarkcreationoptions.md) — Options used when creating bookmark data.
