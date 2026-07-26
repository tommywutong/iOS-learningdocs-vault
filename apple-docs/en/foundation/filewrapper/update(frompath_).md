---
title: 'update(fromPath:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.0+（10.10 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/foundation/filewrapper/update(frompath:)'
source_url: 'https://developer.apple.com/documentation/foundation/filewrapper/update(frompath:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/filewrapper/update%28frompath%3A%29.json'
content_hash: 'sha256:9c2b67c5f91cb25f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [FileWrapper](../filewrapper.md)

# update(fromPath:)

<sub>Instance Method</sub>

Updates the file wrapper to match a given file-system node.

> [!warning] Deprecated
> Use [- readFromURL:options:error:](<read(from_options_).md>) instead.

<sub>macOS</sub>

```swift
func update(fromPath path: String) -> Bool
```

## Return Value

[true](../../swift/true.md) if the update is carried out, [false](../../swift/false.md) if it isn’t needed.

## Discussion

For a directory file wrapper, the contained file wrappers are also sent [- updateFromPath:](<update(frompath_).md>) messages. If nodes in the corresponding directory on the file system have been added or removed, corresponding file wrappers are released or created as needed.

### Special Considerations

Beginning with OS X v10.6, the preferred method of referring to files is with a `file://` URL. Therefore, this method has been deprecated in favor of [- readFromURL:options:error:](<read(from_options_).md>).

## See Also

### Related Documentation

- [- updateAttachmentsFromPath:](<../nsmutableattributedstring/updateattachments(frompath_).md>) — Updates all attachments based on files contained in the RTFD file package at the specified file path.

### Updating File Wrappers

- [- needsToBeUpdatedFromPath:](<needstobeupdated(frompath_).md>) — Indicates whether the file wrapper needs to be updated to match a given file-system node. _(deprecated)_
- [- matchesContentsOfURL:](<matchescontents(of_).md>) — Indicates whether the contents of a file wrapper matches a directory, regular file, or symbolic link on disk.
- [- readFromURL:options:error:](<read(from_options_).md>) — Recursively rereads the entire contents of a file wrapper from the specified location on disk.
