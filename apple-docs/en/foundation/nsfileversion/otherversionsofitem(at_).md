---
title: 'otherVersionsOfItem(at:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsfileversion/otherversionsofitem(at:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsfileversion/otherversionsofitem(at:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsfileversion/otherversionsofitem%28at%3A%29.json'
content_hash: 'sha256:7117f8250c8108fb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSFileVersion](../nsfileversion.md)

# otherVersionsOfItem(at:)

<sub>Type Method</sub>

Returns all versions of the specified file except the current version.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class func otherVersionsOfItem(at url: URL) -> [NSFileVersion]?
```

## Parameters

- `url` — The URL of the file whose versions you want.

## Return Value

An array of file version objects or `nil` if there is no such file. The array does not contain the version object returned by the [+ currentVersionOfItemAtURL:](<currentversionofitem(at_).md>) method.

## Discussion

For locally based files, this property typically contains versions of the file that you saved explicitly or that were saved at appropriate times while the file was being edited. For documents residing in the cloud, this property typically returns zero or more file versions representing conflicting versions of a file that need to be resolved with the current version.

## See Also

### Getting the Version of a File

- [+ currentVersionOfItemAtURL:](<currentversionofitem(at_).md>) — Returns the most recent version object for the file at the specified URL.
- [+ versionOfItemAtURL:forPersistentIdentifier:](<version(itemat_forpersistentidentifier_).md>) — Returns the version of the file that has the specified persistent ID.
- [+ temporaryDirectoryURLForNewVersionOfItemAtURL:](<temporarydirectoryurlfornewversionofitem(at_).md>) — Creates and returns a temporary directory to use for saving the contents of the file.
