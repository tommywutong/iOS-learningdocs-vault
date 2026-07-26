---
title: stopAccessingSecurityScopedResource()
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsurl/stopaccessingsecurityscopedresource()
source_url: 'https://developer.apple.com/documentation/foundation/nsurl/stopaccessingsecurityscopedresource()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsurl/stopaccessingsecurityscopedresource%28%29.json'
content_hash: 'sha256:aee80ef18dd5f19f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSURL](../nsurl.md)

# stopAccessingSecurityScopedResource()

<sub>Instance Method</sub>

In an app that adopts App Sandbox, revokes access to the resource pointed to by a security-scoped URL.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func stopAccessingSecurityScopedResource()
```

## Discussion

When you no longer need access to a file or directory pointed to by a security-scoped URL, such as one returned by resolving a security-scoped bookmark, call this method on the URL to relinquish access. You can also use its Core Foundation equivalent, the [CFURLStopAccessingSecurityScopedResource(_:)](<../../corefoundation/cfurlstopaccessingsecurityscopedresource(__).md>) function.

You must balance each call to [- startAccessingSecurityScopedResource](<startaccessingsecurityscopedresource().md>) for a given security-scoped URL with a call to [- stopAccessingSecurityScopedResource](<stopaccessingsecurityscopedresource().md>). When you make the last balanced call to [- stopAccessingSecurityScopedResource](<stopaccessingsecurityscopedresource().md>), you immediately lose access to the resource in question.

> [!warning] Warning
> If you fail to relinquish your access to file-system resources when you no longer need them, your app leaks kernel resources. If sufficient kernel resources leak, your app loses its ability to add file-system locations to its sandbox, such as with Powerbox or security-scoped bookmarks, until relaunched.

If you call this method on a URL whose referenced resource you don’t have access to, nothing happens.

> [!note] Version note
> Security-scoped bookmarks aren’t available in versions of macOS prior to OS X 10.7.3.

## See Also

### Working with Bookmark Data

- [+ bookmarkDataWithContentsOfURL:error:](<bookmarkdata(withcontentsof_).md>) — Initializes and returns bookmark data derived from an alias file pointed to by a specified URL.
- [- bookmarkDataWithOptions:includingResourceValuesForKeys:relativeToURL:error:](<bookmarkdata(options_includingresourcevaluesforkeys_relativeto_).md>) — Returns a bookmark for the URL, created with specified options and resource values.
- [+ resourceValuesForKeys:fromBookmarkData:](<resourcevalues(forkeys_frombookmarkdata_).md>) — Returns the resource values for properties identified by a specified array of keys contained in specified bookmark data.
- [+ writeBookmarkData:toURL:options:error:](<writebookmarkdata(__to_options_).md>) — Creates an alias file on disk at a specified location with specified bookmark data.
- [- startAccessingSecurityScopedResource](<startaccessingsecurityscopedresource().md>) — In an app that has adopted App Sandbox, makes the resource pointed to by a security-scoped URL available to the app.
- [BookmarkFileCreationOptions](bookmarkfilecreationoptions.md) — Options used when creating file bookmark data
- [BookmarkCreationOptions](bookmarkcreationoptions.md) — Options used when creating bookmark data.
- [BookmarkResolutionOptions](bookmarkresolutionoptions.md) — Options used when resolving bookmark data.
