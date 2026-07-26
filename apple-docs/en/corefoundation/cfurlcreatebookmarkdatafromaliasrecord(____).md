---
title: 'CFURLCreateBookmarkDataFromAliasRecord(_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.6+（11.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/corefoundation/cfurlcreatebookmarkdatafromaliasrecord(_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfurlcreatebookmarkdatafromaliasrecord(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfurlcreatebookmarkdatafromaliasrecord%28_%3A_%3A%29.json'
content_hash: 'sha256:bee28179b5b58c22'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFURLCreateBookmarkDataFromAliasRecord(_:_:)

<sub>Function</sub>

Initializes and returns bookmark data derived from an alias record.

> [!warning] Deprecated
> The Carbon Alias Manager is deprecated. This function should only be used to convert Carbon AliasRecords to bookmark data.

<sub>macOS</sub>

```swift
func CFURLCreateBookmarkDataFromAliasRecord(_ allocatorRef: CFAllocator!, _ aliasRecordDataRef: CFData!) -> Unmanaged<CFData>!
```

## Parameters

- `allocatorRef` — The allocator to use to allocate memory for the new `CFURL` object. Pass `NULL` or [kCFAllocatorDefault](kcfallocatordefault.md) to use the current default allocator.

- `aliasRecordDataRef` — The alias record.

## Return Value

The bookmark data for the alias record.

## See Also

### Working with Bookmark Data

- [CFURLCreateBookmarkData](<cfurlcreatebookmarkdata(____________).md>) — Returns bookmark data for a URL, created with specified options and resource values.
- [CFURLCreateBookmarkDataFromFile](<cfurlcreatebookmarkdatafromfile(______).md>) — Initializes and returns bookmark data derived from a file pointed to by a specified URL.
- [CFURLWriteBookmarkDataToFile](<cfurlwritebookmarkdatatofile(________).md>) — Creates an alias file on disk at a specified location with specified bookmark data.
- [CFURLStartAccessingSecurityScopedResource](<cfurlstartaccessingsecurityscopedresource(__).md>) — In an app that has adopted App Sandbox, makes the resource pointed to by a security-scoped URL available to the app.
- [CFURLStopAccessingSecurityScopedResource](<cfurlstopaccessingsecurityscopedresource(__).md>) — In an app that adopts App Sandbox, revokes access to the resource pointed to by a security-scoped URL.
