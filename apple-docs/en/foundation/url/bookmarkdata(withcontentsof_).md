---
title: 'bookmarkData(withContentsOf:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/url/bookmarkdata(withcontentsof:)'
source_url: 'https://developer.apple.com/documentation/foundation/url/bookmarkdata(withcontentsof:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/url/bookmarkdata%28withcontentsof%3A%29.json'
content_hash: 'sha256:ccbfd68025074011'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URL](../url.md)

# bookmarkData(withContentsOf:)

<sub>Type Method</sub>

Initializes and returns bookmark data derived from an alias file pointed to by a specified URL.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func bookmarkData(withContentsOf url: URL) throws -> Data
```

## Discussion

If bookmarkFileURL refers to an alias file created prior to OS X 10.6 that contains Alias Manager information but no bookmark data, this method synthesizes bookmark data for the file.

## See Also

### Creating bookmarks

- [bookmarkData(options:includingResourceValuesForKeys:relativeTo:)](<bookmarkdata(options_includingresourcevaluesforkeys_relativeto_).md>) — Returns bookmark data for the URL, created with specified options and resource values.
- [writeBookmarkData(_:to:)](<writebookmarkdata(__to_).md>) — Creates an alias file on disk at a specified location with specified bookmark data.
- [resourceValues(forKeys:fromBookmarkData:)](<resourcevalues(forkeys_frombookmarkdata_).md>) — Returns the resource values for properties identified by a specified array of keys contained in specified bookmark data.
- [BookmarkCreationOptions](bookmarkcreationoptions.md) — An alias for bookmark creation options.
- [BookmarkCreationOptions](../nsurl/bookmarkcreationoptions.md) — Options used when creating bookmark data.
