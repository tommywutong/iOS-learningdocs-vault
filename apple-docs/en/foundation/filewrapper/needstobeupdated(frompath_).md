---
title: 'needsToBeUpdated(fromPath:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.0+（10.10 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/foundation/filewrapper/needstobeupdated(frompath:)'
source_url: 'https://developer.apple.com/documentation/foundation/filewrapper/needstobeupdated(frompath:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/filewrapper/needstobeupdated%28frompath%3A%29.json'
content_hash: 'sha256:935275bc2d9bd215'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [FileWrapper](../filewrapper.md)

# needsToBeUpdated(fromPath:)

<sub>Instance Method</sub>

Indicates whether the file wrapper needs to be updated to match a given file-system node.

> [!warning] Deprecated
> Use [- matchesContentsOfURL:](<matchescontents(of_).md>) instead.

<sub>macOS</sub>

```swift
func needsToBeUpdated(fromPath path: String) -> Bool
```

## Parameters

- `path` — File-System node with which to compare the file wrapper.

## Return Value

[false](../../swift/false.md) when the file wrapper needs to be updated to match `node`, [false](../../swift/false.md) otherwise.

## Discussion

This table describes which attributes of the file wrapper and `node` are compared to determine whether the file wrapper needs to be updated:

| File-wrapper type | Comparison determinants |
|---|---|
| Regular file | Modification date and access permissions. |
| Directory | Member hierarchy (recursive). |
| Symbolic link | Destination pathname. |

### Special Considerations

Beginning with OS X v10.6, the preferred method of referring to files is with a `file://` URL. Therefore, this method has been deprecated in favor of [- matchesContentsOfURL:](<matchescontents(of_).md>).

## See Also

### Related Documentation

- [fileAttributes](fileattributes.md) — A dictionary of file attributes.

### Updating File Wrappers

- [- matchesContentsOfURL:](<matchescontents(of_).md>) — Indicates whether the contents of a file wrapper matches a directory, regular file, or symbolic link on disk.
- [- updateFromPath:](<update(frompath_).md>) — Updates the file wrapper to match a given file-system node. _(deprecated)_
- [- readFromURL:options:error:](<read(from_options_).md>) — Recursively rereads the entire contents of a file wrapper from the specified location on disk.
