---
title: 'init(symbolicLinkWithDestination:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [macOS 10.0+（10.10 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/foundation/filewrapper/init(symboliclinkwithdestination:)'
source_url: 'https://developer.apple.com/documentation/foundation/filewrapper/init(symboliclinkwithdestination:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/filewrapper/init%28symboliclinkwithdestination%3A%29.json'
content_hash: 'sha256:1656ded887e7d6d4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [FileWrapper](../filewrapper.md)

# init(symbolicLinkWithDestination:)

<sub>Initializer</sub>

Initializes the receiver as a symbolic-link file wrapper.

> [!warning] Deprecated
> Use [- initSymbolicLinkWithDestinationURL:](<init(symboliclinkwithdestinationurl_).md>) instead.

<sub>macOS</sub>

```swift
convenience init(symbolicLinkWithDestination path: String)
```

## Parameters

- `path` — Pathname the receiver is to represent.

## Return Value

Initialized symbolic-link file wrapper referencing `node`.

## Discussion

The receiver is not associated to a file-system node until you save it using [- writeToFile:atomically:updateFilenames:](<write(tofile_atomically_updatefilenames_).md>). It’s also initialized with open permissions; anyone can read or write the disk representations it saves.

### Special Considerations

Beginning with OS X v10.6, the preferred method of referring to files is with a `file://` URL. Therefore, this method has been deprecated in favor of [- initSymbolicLinkWithDestinationURL:](<init(symboliclinkwithdestinationurl_).md>).

## See Also

### Related Documentation

- [preferredFilename](preferredfilename.md) — The preferred filename for the file wrapper object.
- [filename](filename.md) — The filename of the file wrapper object
- [fileAttributes](fileattributes.md) — A dictionary of file attributes.

### Creating File Wrappers

- [- initWithURL:options:error:](<init(url_options_)-70161.md>) — Initializes a file wrapper instance whose kind is determined by the type of file-system node located by the URL.
- [- initWithPath:](<init(path_).md>) — Initializes a file wrapper instance whose kind is determined by the type of file-system node located by the path. _(deprecated)_
- [- initDirectoryWithFileWrappers:](<init(directorywithfilewrappers_).md>) — Initializes the receiver as a directory file wrapper, with a given file-wrapper list.
- [- initRegularFileWithContents:](<init(regularfilewithcontents_).md>) — Initializes the receiver as a regular-file file wrapper.
- [- initSymbolicLinkWithDestinationURL:](<init(symboliclinkwithdestinationurl_).md>) — Initializes the receiver as a symbolic-link file wrapper that links to a specified file.
- [- initWithSerializedRepresentation:](<init(serializedrepresentation_).md>) — Initializes the receiver as a regular-file file wrapper from given serialized data.
