---
title: 'writeBookmarkData(_:to:options:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsurl/writebookmarkdata(_:to:options:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsurl/writebookmarkdata(_:to:options:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsurl/writebookmarkdata%28_%3Ato%3Aoptions%3A%29.json'
content_hash: 'sha256:8915d6727b539c6f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSURL](../nsurl.md)

# writeBookmarkData(_:to:options:)

<sub>Type Method</sub>

Creates an alias file on disk at a specified location with specified bookmark data.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class func writeBookmarkData(_ bookmarkData: Data, to bookmarkFileURL: URL, options: NSURL.BookmarkFileCreationOptions) throws
```

## Parameters

- `bookmarkData` — The bookmark data containing information for the alias file.

- `bookmarkFileURL` — The desired location of the alias file.

- `options` — Options taken into account when creating the alias file.

## Discussion

This method will produce an error if `bookmarkData` was not created with the `NSURLBookmarkCreationSuitableForBookmarkFile` option.

If `bookmarkFileURL` points to a directory, the alias file will be created in that directory with its name derived from the information in `bookmarkData`. If `bookmarkFileURL` points to a file, the alias file will be created with the location and name indicated by `bookmarkFileURL`, and its extension will be changed to `.alias` if it is not already.

> [!note] Handling Errors in Swift
> In Swift, this method returns a nonoptional result and is marked with the `throws` keyword to indicate that it throws an error in cases of failure.
>
> You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [Error Handling](https://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [The Swift Programming Language](https://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## See Also

### Working with Bookmark Data

- [+ bookmarkDataWithContentsOfURL:error:](<bookmarkdata(withcontentsof_).md>) — Initializes and returns bookmark data derived from an alias file pointed to by a specified URL.
- [- bookmarkDataWithOptions:includingResourceValuesForKeys:relativeToURL:error:](<bookmarkdata(options_includingresourcevaluesforkeys_relativeto_).md>) — Returns a bookmark for the URL, created with specified options and resource values.
- [+ resourceValuesForKeys:fromBookmarkData:](<resourcevalues(forkeys_frombookmarkdata_).md>) — Returns the resource values for properties identified by a specified array of keys contained in specified bookmark data.
- [- startAccessingSecurityScopedResource](<startaccessingsecurityscopedresource().md>) — In an app that has adopted App Sandbox, makes the resource pointed to by a security-scoped URL available to the app.
- [- stopAccessingSecurityScopedResource](<stopaccessingsecurityscopedresource().md>) — In an app that adopts App Sandbox, revokes access to the resource pointed to by a security-scoped URL.
- [BookmarkFileCreationOptions](bookmarkfilecreationoptions.md) — Options used when creating file bookmark data
- [BookmarkCreationOptions](bookmarkcreationoptions.md) — Options used when creating bookmark data.
- [BookmarkResolutionOptions](bookmarkresolutionoptions.md) — Options used when resolving bookmark data.
