---
title: 'resourceValues(forKeys:fromBookmarkData:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/url/resourcevalues(forkeys:frombookmarkdata:)'
source_url: 'https://developer.apple.com/documentation/foundation/url/resourcevalues(forkeys:frombookmarkdata:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/url/resourcevalues%28forkeys%3Afrombookmarkdata%3A%29.json'
content_hash: 'sha256:b8ec29ca78e5e7ac'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URL](../url.md)

# resourceValues(forKeys:fromBookmarkData:)

<sub>Type Method</sub>

Returns the resource values for properties identified by a specified array of keys contained in specified bookmark data.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func resourceValues(forKeys keys: Set<URLResourceKey>, fromBookmarkData data: Data) -> URLResourceValues?
```

## Discussion

If the result dictionary does not contain a resource value for one or more of the requested resource keys, it means those resource properties are not available in the bookmark data.

## See Also

### Creating bookmarks

- [bookmarkData(options:includingResourceValuesForKeys:relativeTo:)](<bookmarkdata(options_includingresourcevaluesforkeys_relativeto_).md>) — Returns bookmark data for the URL, created with specified options and resource values.
- [bookmarkData(withContentsOf:)](<bookmarkdata(withcontentsof_).md>) — Initializes and returns bookmark data derived from an alias file pointed to by a specified URL.
- [writeBookmarkData(_:to:)](<writebookmarkdata(__to_).md>) — Creates an alias file on disk at a specified location with specified bookmark data.
- [BookmarkCreationOptions](bookmarkcreationoptions.md) — An alias for bookmark creation options.
- [BookmarkCreationOptions](../nsurl/bookmarkcreationoptions.md) — Options used when creating bookmark data.
