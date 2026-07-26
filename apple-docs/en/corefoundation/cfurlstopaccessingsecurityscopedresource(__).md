---
title: 'CFURLStopAccessingSecurityScopedResource(_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfurlstopaccessingsecurityscopedresource(_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfurlstopaccessingsecurityscopedresource(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfurlstopaccessingsecurityscopedresource%28_%3A%29.json'
content_hash: 'sha256:07aa541a9c66a1a9'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFURLStopAccessingSecurityScopedResource(_:)

<sub>Function</sub>

In an app that adopts App Sandbox, revokes access to the resource pointed to by a security-scoped URL.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFURLStopAccessingSecurityScopedResource(_ url: CFURL!)
```

## Parameters

- `url` — The security-scoped URL that points to the file-system resource you want to stop accessing.

## Discussion

When you no longer need access to a file or directory pointed to by a security-scoped URL, such as one returned by resolving a security-scoped bookmark, call this function (or its Cocoa equivalent, [stopAccessingSecurityScopedResource()](<../foundation/nsurl/stopaccessingsecurityscopedresource().md>)) on the URL.

> [!warning] Warning
> You must balance every call to the [CFURLStartAccessingSecurityScopedResource](<cfurlstartaccessingsecurityscopedresource(__).md>) method with a corresponding call to the [CFURLStopAccessingSecurityScopedResource](<cfurlstopaccessingsecurityscopedresource(__).md>) method. If you fail to relinquish your access when you no longer need a file-system resource, your app leaks kernel resources. If sufficient kernel resources are leaked, your app loses its ability to add file-system locations to its sandbox, such as via Powerbox or security-scoped bookmarks, until relaunched.

> [!note] Version note
> Security-scoped bookmarks are not available in versions of macOS prior to OS X v10.7.3.

## See Also

### Working with Bookmark Data

- [CFURLCreateBookmarkData](<cfurlcreatebookmarkdata(____________).md>) — Returns bookmark data for a URL, created with specified options and resource values.
- [CFURLCreateBookmarkDataFromAliasRecord](<cfurlcreatebookmarkdatafromaliasrecord(____).md>) — Initializes and returns bookmark data derived from an alias record. _(deprecated)_
- [CFURLCreateBookmarkDataFromFile](<cfurlcreatebookmarkdatafromfile(______).md>) — Initializes and returns bookmark data derived from a file pointed to by a specified URL.
- [CFURLWriteBookmarkDataToFile](<cfurlwritebookmarkdatatofile(________).md>) — Creates an alias file on disk at a specified location with specified bookmark data.
- [CFURLStartAccessingSecurityScopedResource](<cfurlstartaccessingsecurityscopedresource(__).md>) — In an app that has adopted App Sandbox, makes the resource pointed to by a security-scoped URL available to the app.
