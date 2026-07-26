---
title: NSURL.BookmarkFileCreationOptions
framework: Foundation
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsurl/bookmarkfilecreationoptions
source_url: 'https://developer.apple.com/documentation/foundation/nsurl/bookmarkfilecreationoptions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsurl/bookmarkfilecreationoptions.json'
content_hash: 'sha256:ac067643b3b5863e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSURL](../nsurl.md)

# NSURL.BookmarkFileCreationOptions

<sub>Type Alias</sub>

Options used when creating file bookmark data

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
typealias BookmarkFileCreationOptions = Int
```

## Discussion

See [BookmarkCreationOptions](bookmarkcreationoptions.md) for more information.

## See Also

### Working with Bookmark Data

- [+ bookmarkDataWithContentsOfURL:error:](<bookmarkdata(withcontentsof_).md>) — Initializes and returns bookmark data derived from an alias file pointed to by a specified URL.
- [- bookmarkDataWithOptions:includingResourceValuesForKeys:relativeToURL:error:](<bookmarkdata(options_includingresourcevaluesforkeys_relativeto_).md>) — Returns a bookmark for the URL, created with specified options and resource values.
- [+ resourceValuesForKeys:fromBookmarkData:](<resourcevalues(forkeys_frombookmarkdata_).md>) — Returns the resource values for properties identified by a specified array of keys contained in specified bookmark data.
- [+ writeBookmarkData:toURL:options:error:](<writebookmarkdata(__to_options_).md>) — Creates an alias file on disk at a specified location with specified bookmark data.
- [- startAccessingSecurityScopedResource](<startaccessingsecurityscopedresource().md>) — In an app that has adopted App Sandbox, makes the resource pointed to by a security-scoped URL available to the app.
- [- stopAccessingSecurityScopedResource](<stopaccessingsecurityscopedresource().md>) — In an app that adopts App Sandbox, revokes access to the resource pointed to by a security-scoped URL.
- [BookmarkCreationOptions](bookmarkcreationoptions.md) — Options used when creating bookmark data.
- [BookmarkResolutionOptions](bookmarkresolutionoptions.md) — Options used when resolving bookmark data.
