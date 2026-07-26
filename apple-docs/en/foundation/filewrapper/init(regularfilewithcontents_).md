---
title: 'init(regularFileWithContents:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/filewrapper/init(regularfilewithcontents:)'
source_url: 'https://developer.apple.com/documentation/foundation/filewrapper/init(regularfilewithcontents:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/filewrapper/init%28regularfilewithcontents%3A%29.json'
content_hash: 'sha256:53e66fcf83c5f756'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [FileWrapper](../filewrapper.md)

# init(regularFileWithContents:)

<sub>Initializer</sub>

Initializes the receiver as a regular-file file wrapper.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(regularFileWithContents contents: Data)
```

## Parameters

- `contents` — Contents of the file.

## Return Value

Initialized regular-file file wrapper containing `contents`.

## Discussion

After initialization, the file wrapper is not associated with a file-system node until you save it using [- writeToURL:options:originalContentsURL:error:](<write(to_options_originalcontentsurl_).md>).

The file wrapper is initialized with open permissions: anyone can write to or read the file wrapper.

## See Also

### Related Documentation

- [preferredFilename](preferredfilename.md) — The preferred filename for the file wrapper object.
- [filename](filename.md) — The filename of the file wrapper object
- [fileAttributes](fileattributes.md) — A dictionary of file attributes.
- [regularFileContents](regularfilecontents.md) — The contents of the file-system node associated with a regular-file file wrapper.

### Creating File Wrappers

- [- initWithURL:options:error:](<init(url_options_)-70161.md>) — Initializes a file wrapper instance whose kind is determined by the type of file-system node located by the URL.
- [- initWithPath:](<init(path_).md>) — Initializes a file wrapper instance whose kind is determined by the type of file-system node located by the path. _(deprecated)_
- [- initDirectoryWithFileWrappers:](<init(directorywithfilewrappers_).md>) — Initializes the receiver as a directory file wrapper, with a given file-wrapper list.
- [- initSymbolicLinkWithDestination:](<init(symboliclinkwithdestination_).md>) — Initializes the receiver as a symbolic-link file wrapper. _(deprecated)_
- [- initSymbolicLinkWithDestinationURL:](<init(symboliclinkwithdestinationurl_).md>) — Initializes the receiver as a symbolic-link file wrapper that links to a specified file.
- [- initWithSerializedRepresentation:](<init(serializedrepresentation_).md>) — Initializes the receiver as a regular-file file wrapper from given serialized data.
