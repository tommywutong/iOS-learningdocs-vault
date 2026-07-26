---
title: 'writeBookmarkData(_:to:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/url/writebookmarkdata(_:to:)'
source_url: 'https://developer.apple.com/documentation/foundation/url/writebookmarkdata(_:to:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/url/writebookmarkdata%28_%3Ato%3A%29.json'
content_hash: 'sha256:639caa41c12c6950'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URL](../url.md)

# writeBookmarkData(_:to:)

<sub>Type Method</sub>

Creates an alias file on disk at a specified location with specified bookmark data.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func writeBookmarkData(_ data: Data, to url: URL) throws
```

## Discussion

The `data` must have been created with the [NSURLBookmarkCreationSuitableForBookmarkFile](../nsurl/bookmarkcreationoptions/suitableforbookmarkfile.md) option. The `url` must either refer to an existing file (which will be overwritten), or to location in an existing directory.

## See Also

### Creating bookmarks

- [bookmarkData(options:includingResourceValuesForKeys:relativeTo:)](<bookmarkdata(options_includingresourcevaluesforkeys_relativeto_).md>) — Returns bookmark data for the URL, created with specified options and resource values.
- [bookmarkData(withContentsOf:)](<bookmarkdata(withcontentsof_).md>) — Initializes and returns bookmark data derived from an alias file pointed to by a specified URL.
- [resourceValues(forKeys:fromBookmarkData:)](<resourcevalues(forkeys_frombookmarkdata_).md>) — Returns the resource values for properties identified by a specified array of keys contained in specified bookmark data.
- [BookmarkCreationOptions](bookmarkcreationoptions.md) — An alias for bookmark creation options.
- [BookmarkCreationOptions](../nsurl/bookmarkcreationoptions.md) — Options used when creating bookmark data.
