---
title: directoryEntryCount
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/urlresourcevalues/directoryentrycount
source_url: 'https://developer.apple.com/documentation/foundation/urlresourcevalues/directoryentrycount'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlresourcevalues/directoryentrycount.json'
content_hash: 'sha256:cc0859e253ba438f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLResourceValues](../urlresourcevalues.md)

# directoryEntryCount

<sub>Instance Property</sub>

The count of file system objects in the directory.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var directoryEntryCount: Int? { get }
```

## Discussion

This value is a count of objects that are actually in the file system, so it excludes virtual items like “`.`” and “`..`”. This property is useful for quickly identifying an empty directory for backup and syncing. If the URL isn’t a directory, or the file system can’t cheaply compute the value, the value is `nil`.

Not all file systems can provide this information.

## See Also

### Directory values

- [isDirectory](isdirectory.md) — A Boolean value that indicates whether the resource is a directory.
