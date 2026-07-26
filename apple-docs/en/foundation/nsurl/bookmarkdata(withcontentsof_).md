---
title: 'bookmarkData(withContentsOf:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsurl/bookmarkdata(withcontentsof:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsurl/bookmarkdata(withcontentsof:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsurl/bookmarkdata%28withcontentsof%3A%29.json'
content_hash: 'sha256:0706f4dc20ce68b5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSURL](../nsurl.md)

# bookmarkData(withContentsOf:)

<sub>Type Method</sub>

Initializes and returns bookmark data derived from an alias file pointed to by a specified URL.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class func bookmarkData(withContentsOf bookmarkFileURL: URL) throws -> Data
```

## Parameters

- `bookmarkFileURL` — The URL that points to a file containing bookmark data.

## Return Value

The bookmark data for the alias file.

## Discussion

This method doesn’t check to see if `bookmarkFileURL` points to an alias file. This allows this method to work with any file containing bookmark data. If `bookmarkFileURL` refers to a file which does not contain bookmark data or to a non-file object, such as a directory or symbolic link, this method returns `nil` produces an error.

This method returns `nil` if bookmark data cannot be created.

> [!note] Handling Errors in Swift
> In Swift, this method returns a nonoptional result and is marked with the `throws` keyword to indicate that it throws an error in cases of failure.
>
> You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [Error Handling](https://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [The Swift Programming Language](https://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## See Also

### Working with Bookmark Data

- [- bookmarkDataWithOptions:includingResourceValuesForKeys:relativeToURL:error:](<bookmarkdata(options_includingresourcevaluesforkeys_relativeto_).md>) — Returns a bookmark for the URL, created with specified options and resource values.
- [+ resourceValuesForKeys:fromBookmarkData:](<resourcevalues(forkeys_frombookmarkdata_).md>) — Returns the resource values for properties identified by a specified array of keys contained in specified bookmark data.
- [+ writeBookmarkData:toURL:options:error:](<writebookmarkdata(__to_options_).md>) — Creates an alias file on disk at a specified location with specified bookmark data.
- [- startAccessingSecurityScopedResource](<startaccessingsecurityscopedresource().md>) — In an app that has adopted App Sandbox, makes the resource pointed to by a security-scoped URL available to the app.
- [- stopAccessingSecurityScopedResource](<stopaccessingsecurityscopedresource().md>) — In an app that adopts App Sandbox, revokes access to the resource pointed to by a security-scoped URL.
- [BookmarkFileCreationOptions](bookmarkfilecreationoptions.md) — Options used when creating file bookmark data
- [BookmarkCreationOptions](bookmarkcreationoptions.md) — Options used when creating bookmark data.
- [BookmarkResolutionOptions](bookmarkresolutionoptions.md) — Options used when resolving bookmark data.
