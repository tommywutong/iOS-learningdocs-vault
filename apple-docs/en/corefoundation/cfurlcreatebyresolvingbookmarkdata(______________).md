---
title: 'CFURLCreateByResolvingBookmarkData(_:_:_:_:_:_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfurlcreatebyresolvingbookmarkdata(_:_:_:_:_:_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfurlcreatebyresolvingbookmarkdata(_:_:_:_:_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfurlcreatebyresolvingbookmarkdata%28_%3A_%3A_%3A_%3A_%3A_%3A_%3A%29.json'
content_hash: 'sha256:10c5f49399aa9bb7'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFURLCreateByResolvingBookmarkData(_:_:_:_:_:_:_:)

<sub>Function</sub>

Returns a new URL made by resolving bookmark data.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFURLCreateByResolvingBookmarkData(_ allocator: CFAllocator!, _ bookmark: CFData!, _ options: CFURLBookmarkResolutionOptions, _ relativeToURL: CFURL!, _ resourcePropertiesToInclude: CFArray!, _ isStale: UnsafeMutablePointer<DarwinBoolean>!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Unmanaged<CFURL>!
```

## Parameters

- `allocator` — The allocator to use to allocate memory for the new `CFURL` object. Pass `NULL` or [kCFAllocatorDefault](kcfallocatordefault.md) to use the current default allocator.

- `bookmark` — The bookmark data the URL is derived from.

- `options` — Options taken into account when resolving the bookmark data. To resolve a security-scoped bookmark to support App Sandbox, you must include (by way of bitwise `OR` operators with any other options in this parameter) the [kCFURLBookmarkResolutionWithSecurityScope](cfurlbookmarkresolutionoptions/cfurlbookmarkresolutionwithsecurityscope.md) option.

- `relativeToURL` — The base URL that the bookmark data is relative to. Can be `NULL`. If you are resolving a security-scoped bookmark to obtain a security-scoped URL, use this parameter as follows: - To resolve an app-scoped bookmark, use a value of `nil`. - To resolve a document-scoped bookmark, use the _absolute_ path (despite this parameter’s name) to the document from which you retrieved the bookmark.

- `resourcePropertiesToInclude` — An array of resource properties to include when creating the URL. Can be `NULL`.

- `isStale` — If [true](../swift/true.md), the bookmark data is stale.

- `error` — The error that occurred in the case that the URL cannot be created.

## Return Value

A new URL made by resolving `bookmark`, or `NULL` if an error occurs.

## Discussion

To obtain a security-scoped URL from a security-scoped bookmark, call this method using the [kCFURLBookmarkResolutionWithSecurityScope](cfurlbookmarkresolutionoptions/cfurlbookmarkresolutionwithsecurityscope.md) option. In addition, to use security scope, you must first have enabled the appropriate entitlements for your app, as described in [Enabling Security-Scoped Bookmark and URL Access](https://developer.apple.com/library/archive/documentation/Miscellaneous/Reference/EntitlementKeyReference/Chapters/EnablingAppSandbox.html#//apple_ref/doc/uid/TP40011195-CH4-SW18).

To then obtain access to the file-system resource pointed to by a security-scoped URL (in other words, to bring the resource into your app’s sandbox), call the [CFURLStartAccessingSecurityScopedResource](<cfurlstartaccessingsecurityscopedresource(__).md>) function (or its Cocoa equivalent) on the URL.

For an app-scoped bookmark, no sandboxed app other than the one that created the bookmark can obtain access to the file-system resource that the URL (obtained from the bookmark) points to.

For a document-scoped bookmark, any sandboxed app that has access to the bookmark data itself, and has access to the document that owns the bookmark, can obtain access to the resource.

> [!note] Version note
> Security-scoped bookmarks are not available in versions of macOS prior to OS X v10.7.3.

## See Also

### Related Documentation

- [CFURLCreateBookmarkData](<cfurlcreatebookmarkdata(____________).md>) — Returns bookmark data for a URL, created with specified options and resource values.

### Creating a CFURL

- [CFURLCopyAbsoluteURL](<cfurlcopyabsoluteurl(__).md>) — Creates a new `CFURL` object by resolving the relative portion of a URL against its base.
- [CFURLCreateAbsoluteURLWithBytes](<cfurlcreateabsoluteurlwithbytes(____________).md>) — Creates a new `CFURL` object by resolving the relative portion of a URL, specified as bytes, against its given base URL.
- [CFURLCreateCopyAppendingPathComponent](<cfurlcreatecopyappendingpathcomponent(________).md>) — Creates a copy of a given URL and appends a path component.
- [CFURLCreateCopyAppendingPathExtension](<cfurlcreatecopyappendingpathextension(______).md>) — Creates a copy of a given URL and appends a path extension.
- [CFURLCreateCopyDeletingLastPathComponent](<cfurlcreatecopydeletinglastpathcomponent(____).md>) — Creates a copy of a given URL with the last path component deleted.
- [CFURLCreateCopyDeletingPathExtension](<cfurlcreatecopydeletingpathextension(____).md>) — Creates a copy of a given URL with its last path extension removed.
- [CFURLCreateFilePathURL](<cfurlcreatefilepathurl(______).md>) — Returns a new file path URL that refers to the same resource as a specified URL.
- [CFURLCreateFileReferenceURL](<cfurlcreatefilereferenceurl(______).md>) — Returns a new file reference URL that points to the same resource as a specified URL.
- [CFURLCreateFromFileSystemRepresentation](<cfurlcreatefromfilesystemrepresentation(________).md>) — Creates a new `CFURL` object for a file system entity using the native representation.
- [CFURLCreateFromFileSystemRepresentationRelativeToBase](<cfurlcreatefromfilesystemrepresentationrelativetobase(__________).md>) — Creates a `CFURL` object from a native character string path relative to a base URL.
- [CFURLCreateFromFSRef](<cfurlcreatefromfsref(____).md>) — Creates a URL from a given directory or file. _(deprecated)_
- [CFURLCreateWithBytes](<cfurlcreatewithbytes(__________).md>) — Creates a `CFURL` object using a given character bytes.
- [CFURLCreateWithFileSystemPath](<cfurlcreatewithfilesystempath(________).md>) — Creates a `CFURL` object using a local file system path string.
- [CFURLCreateWithFileSystemPathRelativeToBase](<cfurlcreatewithfilesystempathrelativetobase(__________).md>) — Creates a `CFURL` object using a local file system path string relative to a base URL.
- [CFURLCreateWithString](<cfurlcreatewithstring(______).md>) — Creates a `CFURL` object using a given `CFString` object.
