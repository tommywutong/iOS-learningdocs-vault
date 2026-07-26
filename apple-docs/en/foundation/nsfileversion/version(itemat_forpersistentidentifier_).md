---
title: 'version(itemAt:forPersistentIdentifier:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsfileversion/version(itemat:forpersistentidentifier:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsfileversion/version(itemat:forpersistentidentifier:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsfileversion/version%28itemat%3Aforpersistentidentifier%3A%29.json'
content_hash: 'sha256:98175b1691c23fc8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSFileVersion](../nsfileversion.md)

# version(itemAt:forPersistentIdentifier:)

<sub>Type Method</sub>

Returns the version of the file that has the specified persistent ID.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class func version(itemAt url: URL, forPersistentIdentifier persistentIdentifier: Any) -> NSFileVersion?
```

## Parameters

- `url` — The URL of the file whose version you want.

- `persistentIdentifier` — The persistent ID of the `NSFileVersion` object you want.

## Return Value

The file version object with the specified ID or `nil` if no such version object exists.

## See Also

### Related Documentation

- [persistentIdentifier](persistentidentifier.md) — The identifier for this version of the file.

### Getting the Version of a File

- [+ currentVersionOfItemAtURL:](<currentversionofitem(at_).md>) — Returns the most recent version object for the file at the specified URL.
- [+ otherVersionsOfItemAtURL:](<otherversionsofitem(at_).md>) — Returns all versions of the specified file except the current version.
- [+ temporaryDirectoryURLForNewVersionOfItemAtURL:](<temporarydirectoryurlfornewversionofitem(at_).md>) — Creates and returns a temporary directory to use for saving the contents of the file.
