---
title: 'init(path:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [macOS 10.0+（10.10 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/foundation/filewrapper/init(path:)'
source_url: 'https://developer.apple.com/documentation/foundation/filewrapper/init(path:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/filewrapper/init%28path%3A%29.json'
content_hash: 'sha256:c0bde58aed3226ba'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [FileWrapper](../filewrapper.md)

# init(path:)

<sub>Initializer</sub>

Initializes a file wrapper instance whose kind is determined by the type of file-system node located by the path.

> [!warning] Deprecated
> Use [- initWithURL:options:error:](<init(url_options_)-70161.md>) instead.

<sub>macOS</sub>

```swift
convenience init?(path: String)
```

## Parameters

- `path` — Pathname of the file-system node the file wrapper is to represent.

## Return Value

File wrapper for `node`.

## Discussion

If `node` is a directory, this method recursively creates file wrappers for each node within that directory.

### Special Considerations

Beginning with OS X v10.6, the preferred method of referring to files is with a `file://` URL. Therefore, this method has been deprecated in favor of [- initWithURL:options:error:](<init(url_options_)-70161.md>).

## See Also

### Related Documentation

- [preferredFilename](preferredfilename.md) — The preferred filename for the file wrapper object.
- [filename](filename.md) — The filename of the file wrapper object
- [fileAttributes](fileattributes.md) — A dictionary of file attributes.

### Creating File Wrappers

- [- initWithURL:options:error:](<init(url_options_)-70161.md>) — Initializes a file wrapper instance whose kind is determined by the type of file-system node located by the URL.
- [- initDirectoryWithFileWrappers:](<init(directorywithfilewrappers_).md>) — Initializes the receiver as a directory file wrapper, with a given file-wrapper list.
- [- initRegularFileWithContents:](<init(regularfilewithcontents_).md>) — Initializes the receiver as a regular-file file wrapper.
- [- initSymbolicLinkWithDestination:](<init(symboliclinkwithdestination_).md>) — Initializes the receiver as a symbolic-link file wrapper. _(deprecated)_
- [- initSymbolicLinkWithDestinationURL:](<init(symboliclinkwithdestinationurl_).md>) — Initializes the receiver as a symbolic-link file wrapper that links to a specified file.
- [- initWithSerializedRepresentation:](<init(serializedrepresentation_).md>) — Initializes the receiver as a regular-file file wrapper from given serialized data.
