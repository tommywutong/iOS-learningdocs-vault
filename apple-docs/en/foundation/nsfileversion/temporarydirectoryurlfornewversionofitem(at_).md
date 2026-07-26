---
title: 'temporaryDirectoryURLForNewVersionOfItem(at:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [macOS 10.7+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsfileversion/temporarydirectoryurlfornewversionofitem(at:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsfileversion/temporarydirectoryurlfornewversionofitem(at:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsfileversion/temporarydirectoryurlfornewversionofitem%28at%3A%29.json'
content_hash: 'sha256:6c0b6f78af863bf6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSFileVersion](../nsfileversion.md)

# temporaryDirectoryURLForNewVersionOfItem(at:)

<sub>Type Method</sub>

Creates and returns a temporary directory to use for saving the contents of the file.

<sub>macOS</sub>

```swift
class func temporaryDirectoryURLForNewVersionOfItem(at url: URL) -> URL
```

## Parameters

- `url` — The URL of the file whose contents you want to save.

## Return Value

A URL identifying the temporary directory in which to create a the new file. You must delete the directory specified by this URL after you have created the file and moved it to its proper location.

## Discussion

You can use this method in situations where you want to create a file in a temporary location. For example, you might use this method when saving the contents of a file to disk for the first time. When you finish creating the temporary file, move it to a more appropriate location, such as the user’s `Documents` directory. You must delete the directory returned by this method when you are done with it.

## See Also

### Getting the Version of a File

- [+ currentVersionOfItemAtURL:](<currentversionofitem(at_).md>) — Returns the most recent version object for the file at the specified URL.
- [+ otherVersionsOfItemAtURL:](<otherversionsofitem(at_).md>) — Returns all versions of the specified file except the current version.
- [+ versionOfItemAtURL:forPersistentIdentifier:](<version(itemat_forpersistentidentifier_).md>) — Returns the version of the file that has the specified persistent ID.
