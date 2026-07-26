---
title: 'CFURLWriteBookmarkDataToFile(_:_:_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfurlwritebookmarkdatatofile(_:_:_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfurlwritebookmarkdatatofile(_:_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfurlwritebookmarkdatatofile%28_%3A_%3A_%3A_%3A%29.json'
content_hash: 'sha256:4b0ee1721cca72ca'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFURLWriteBookmarkDataToFile(_:_:_:_:)

<sub>Function</sub>

Creates an alias file on disk at a specified location with specified bookmark data.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFURLWriteBookmarkDataToFile(_ bookmarkRef: CFData!, _ fileURL: CFURL!, _ options: CFURLBookmarkFileCreationOptions, _ errorRef: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool
```

## Parameters

- `bookmarkRef` — The bookmark data containing information for the alias file.

- `fileURL` — The desired location of the alias file.

- `options` — Options taken into account when creating the alias file.

- `errorRef` — The error that occurred in the case that the alias file cannot be created.

## Return Value

`true` if the alias file is successfully created; otherwise, `false`.

## See Also

### Working with Bookmark Data

- [CFURLCreateBookmarkData](<cfurlcreatebookmarkdata(____________).md>) — Returns bookmark data for a URL, created with specified options and resource values.
- [CFURLCreateBookmarkDataFromAliasRecord](<cfurlcreatebookmarkdatafromaliasrecord(____).md>) — Initializes and returns bookmark data derived from an alias record. _(deprecated)_
- [CFURLCreateBookmarkDataFromFile](<cfurlcreatebookmarkdatafromfile(______).md>) — Initializes and returns bookmark data derived from a file pointed to by a specified URL.
- [CFURLStartAccessingSecurityScopedResource](<cfurlstartaccessingsecurityscopedresource(__).md>) — In an app that has adopted App Sandbox, makes the resource pointed to by a security-scoped URL available to the app.
- [CFURLStopAccessingSecurityScopedResource](<cfurlstopaccessingsecurityscopedresource(__).md>) — In an app that adopts App Sandbox, revokes access to the resource pointed to by a security-scoped URL.
