---
title: 'currentVersionOfItem(at:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsfileversion/currentversionofitem(at:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsfileversion/currentversionofitem(at:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsfileversion/currentversionofitem%28at%3A%29.json'
content_hash: 'sha256:9ae163159b5c6250'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSFileVersion](../nsfileversion.md)

# currentVersionOfItem(at:)

<sub>Type Method</sub>

Returns the most recent version object for the file at the specified URL.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class func currentVersionOfItem(at url: URL) -> NSFileVersion?
```

## Parameters

- `url` — The URL of the file whose version object you want.

## Return Value

The version object representing the current version of the file or `nil` if there is no such file.

## See Also

### Getting the Version of a File

- [+ otherVersionsOfItemAtURL:](<otherversionsofitem(at_).md>) — Returns all versions of the specified file except the current version.
- [+ versionOfItemAtURL:forPersistentIdentifier:](<version(itemat_forpersistentidentifier_).md>) — Returns the version of the file that has the specified persistent ID.
- [+ temporaryDirectoryURLForNewVersionOfItemAtURL:](<temporarydirectoryurlfornewversionofitem(at_).md>) — Creates and returns a temporary directory to use for saving the contents of the file.
