---
title: 'CFURLCreateBookmarkDataFromFile(_:_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfurlcreatebookmarkdatafromfile(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfurlcreatebookmarkdatafromfile(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfurlcreatebookmarkdatafromfile%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:1ee48650d3737044'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFURLCreateBookmarkDataFromFile(_:_:_:)

<sub>Function</sub>

Initializes and returns bookmark data derived from a file pointed to by a specified URL.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFURLCreateBookmarkDataFromFile(_ allocator: CFAllocator!, _ fileURL: CFURL!, _ errorRef: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Unmanaged<CFData>!
```

## Parameters

- `allocator` — The allocator to use to allocate memory for the new `CFURL` object. Pass `NULL` or [kCFAllocatorDefault](kcfallocatordefault.md) to use the current default allocator.

- `fileURL` — The file URL.

- `errorRef` — The error that occurred in the case that the bookmark data cannot be created.

## Return Value

The bookmark data for the file, or `NULL` if an error occurs.

## See Also

### Working with Bookmark Data

- [CFURLCreateBookmarkData](<cfurlcreatebookmarkdata(____________).md>) — Returns bookmark data for a URL, created with specified options and resource values.
- [CFURLCreateBookmarkDataFromAliasRecord](<cfurlcreatebookmarkdatafromaliasrecord(____).md>) — Initializes and returns bookmark data derived from an alias record. _(deprecated)_
- [CFURLWriteBookmarkDataToFile](<cfurlwritebookmarkdatatofile(________).md>) — Creates an alias file on disk at a specified location with specified bookmark data.
- [CFURLStartAccessingSecurityScopedResource](<cfurlstartaccessingsecurityscopedresource(__).md>) — In an app that has adopted App Sandbox, makes the resource pointed to by a security-scoped URL available to the app.
- [CFURLStopAccessingSecurityScopedResource](<cfurlstopaccessingsecurityscopedresource(__).md>) — In an app that adopts App Sandbox, revokes access to the resource pointed to by a security-scoped URL.
