---
title: 'bookmarkData(options:includingResourceValuesForKeys:relativeTo:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsurl/bookmarkdata(options:includingresourcevaluesforkeys:relativeto:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsurl/bookmarkdata(options:includingresourcevaluesforkeys:relativeto:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsurl/bookmarkdata%28options%3Aincludingresourcevaluesforkeys%3Arelativeto%3A%29.json'
content_hash: 'sha256:71998ad461997452'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSURL](../nsurl.md)

# bookmarkData(options:includingResourceValuesForKeys:relativeTo:)

<sub>Instance Method</sub>

Returns a bookmark for the URL, created with specified options and resource values.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func bookmarkData(options: NSURL.BookmarkCreationOptions = [], includingResourceValuesForKeys keys: [URLResourceKey]?, relativeTo relativeURL: URL?) throws -> Data
```

## Parameters

- `options` — Options taken into account when creating the bookmark for the URL. The possible flags (which can be combined with bitwise `OR` operations) are described in [BookmarkCreationOptions](bookmarkcreationoptions.md). To create a security-scoped bookmark to support App Sandbox, include the [NSURLBookmarkCreationWithSecurityScope](bookmarkcreationoptions/withsecurityscope.md) flag. When you later resolve the bookmark, you can use the resulting security-scoped URL to obtain read/write access to the file-system resource pointed to by the URL. If you instead want to create a security-scoped bookmark that, when resolved, enables you to obtain read-only access to a file-system resource, bitwise `OR` this parameter’s value with both the [NSURLBookmarkCreationWithSecurityScope](bookmarkcreationoptions/withsecurityscope.md) option and the [NSURLBookmarkCreationSecurityScopeAllowOnlyReadAccess](bookmarkcreationoptions/securityscopeallowonlyreadaccess.md) option.

- `keys` — An array of names of URL resource properties to store as part of the bookmark. You can later access these values (without resolving the bookmark) by calling the [+ resourceValuesForKeys:fromBookmarkData:](<resourcevalues(forkeys_frombookmarkdata_).md>) method. The values of these properties must be of a type that the bookmark generation code can serialize. Specifically, the values can contain any of the following primitive types: - `NSString` or `CFString` - `NSData` or `CFData` - `NSDate` or `CFDate` - `NSNumber` or `CFNumber` - `CFBoolean` - `NSURL` or `CFURL` - `kCFNull` or [NSNull](../nsnull.md) - `CFUUID` In addition, the properties can contain the following collection classes: - `NSArray` or `CFArray` containing only the above primitive types - `NSDictionary` or `CFDictionary` with `NSString` or `CFString` keys, in which all values contain only the above primitive types

- `relativeURL` — The URL that the bookmark data will be relative to. If you are creating a security-scoped bookmark to support App Sandbox, use this parameter as follows: - To create an app-scoped bookmark, use a value of `nil`. - To create a document-scoped bookmark, use the _absolute_ path (despite this parameter’s name) to the document file that is to own the new security-scoped bookmark. App Sandbox does not restrict which URL values may be passed to this parameter.

## Return Value

A bookmark for the URL.

## Discussion

This method returns bookmark data that can later be resolved into a URL object for a file even if the user moves or renames it (if the volume format on which the file resides supports doing so).

> [!note] Note
> If the specified URL is not a file URL, this method returns a bookmark containing only the URL, and the `options` and `keys` parameters are ignored.

You can also use this method to create a security-scoped bookmark to support App Sandbox. Before you do so, you must first enable the appropriate entitlements for your app, as described in [Enabling Security-Scoped Bookmark and URL Access](https://developer.apple.com/library/archive/documentation/Miscellaneous/Reference/EntitlementKeyReference/Chapters/EnablingAppSandbox.html#//apple_ref/doc/uid/TP40011195-CH4-SW18). In addition, be sure to understand the behavior of the `options` and `relativeURL` parameters.

For an app-scoped bookmark, no sandboxed app other than the one that created the bookmark can obtain access to the file-system resource that the URL (obtained from the bookmark) points to. Specifically, a bookmark created with security scope fails to resolve if the caller does not have the same code signing identity as the caller that created the bookmark.

For a document-scoped bookmark, any sandboxed app that has access to the bookmark data itself, and has access to the document that owns the bookmark, can obtain access to the resource.

> [!note] Version note
> Security-scoped bookmarks are not available in versions of macOS prior to OS X v10.7.3.

> [!note] Handling Errors in Swift
> In Swift, this method returns a nonoptional result and is marked with the `throws` keyword to indicate that it throws an error in cases of failure.
>
> You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [Error Handling](https://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [The Swift Programming Language](https://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## See Also

### Working with Bookmark Data

- [+ bookmarkDataWithContentsOfURL:error:](<bookmarkdata(withcontentsof_).md>) — Initializes and returns bookmark data derived from an alias file pointed to by a specified URL.
- [+ resourceValuesForKeys:fromBookmarkData:](<resourcevalues(forkeys_frombookmarkdata_).md>) — Returns the resource values for properties identified by a specified array of keys contained in specified bookmark data.
- [+ writeBookmarkData:toURL:options:error:](<writebookmarkdata(__to_options_).md>) — Creates an alias file on disk at a specified location with specified bookmark data.
- [- startAccessingSecurityScopedResource](<startaccessingsecurityscopedresource().md>) — In an app that has adopted App Sandbox, makes the resource pointed to by a security-scoped URL available to the app.
- [- stopAccessingSecurityScopedResource](<stopaccessingsecurityscopedresource().md>) — In an app that adopts App Sandbox, revokes access to the resource pointed to by a security-scoped URL.
- [BookmarkFileCreationOptions](bookmarkfilecreationoptions.md) — Options used when creating file bookmark data
- [BookmarkCreationOptions](bookmarkcreationoptions.md) — Options used when creating bookmark data.
- [BookmarkResolutionOptions](bookmarkresolutionoptions.md) — Options used when resolving bookmark data.
