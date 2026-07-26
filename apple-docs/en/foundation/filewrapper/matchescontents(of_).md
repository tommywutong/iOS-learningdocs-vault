---
title: 'matchesContents(of:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/filewrapper/matchescontents(of:)'
source_url: 'https://developer.apple.com/documentation/foundation/filewrapper/matchescontents(of:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/filewrapper/matchescontents%28of%3A%29.json'
content_hash: 'sha256:96b56ccf42a80209'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [FileWrapper](../filewrapper.md)

# matchesContents(of:)

<sub>Instance Method</sub>

Indicates whether the contents of a file wrapper matches a directory, regular file, or symbolic link on disk.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func matchesContents(of url: URL) -> Bool
```

## Parameters

- `url` — URL of the file-system node with which to compare the file wrapper.

## Return Value

[true](../../swift/true.md) when the contents of the file wrapper match the contents of `url`, [false](../../swift/false.md) otherwise.

## Discussion

The contents of files are not compared; matching of regular files is based on file modification dates. For a directory, children are compared against the files in the directory, recursively.

Because children of directory file wrappers are not read immediately by the [- initWithURL:options:error:](<init(url_options_)-70161.md>) method unless the `NSFileWrapperReadingImmediate` reading option is used, even a newly-created directory file wrapper might not have the same contents as the directory on disk. You can use this method to determine whether the file wrapper’s contents in memory need to be updated.

If the file wrapper needs updating, use the [- readFromURL:options:error:](<read(from_options_).md>) method with the `NSFileWrapperReadingImmediate` reading option.

This table describes which attributes of the file wrapper and file-system node are compared to determine whether the file wrapper matches the node on disk:

| File-wrapper type | Comparison determinants |
|---|---|
| Regular file | Modification date and access permissions. |
| Directory | Children (recursive). |
| Symbolic link | Destination pathname. |

## See Also

### Related Documentation

- [fileAttributes](fileattributes.md) — A dictionary of file attributes.

### Updating File Wrappers

- [- needsToBeUpdatedFromPath:](<needstobeupdated(frompath_).md>) — Indicates whether the file wrapper needs to be updated to match a given file-system node. _(deprecated)_
- [- updateFromPath:](<update(frompath_).md>) — Updates the file wrapper to match a given file-system node. _(deprecated)_
- [- readFromURL:options:error:](<read(from_options_).md>) — Recursively rereads the entire contents of a file wrapper from the specified location on disk.
