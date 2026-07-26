---
title: 'init(symbolicLinkWithDestinationURL:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/filewrapper/init(symboliclinkwithdestinationurl:)'
source_url: 'https://developer.apple.com/documentation/foundation/filewrapper/init(symboliclinkwithdestinationurl:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/filewrapper/init%28symboliclinkwithdestinationurl%3A%29.json'
content_hash: 'sha256:38a4cd35191c1908'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [FileWrapper](../filewrapper.md)

# init(symbolicLinkWithDestinationURL:)

<sub>Initializer</sub>

Initializes the receiver as a symbolic-link file wrapper that links to a specified file.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(symbolicLinkWithDestinationURL url: URL)
```

## Parameters

- `url` — URL of the file the file wrapper is to reference.

## Return Value

Initialized symbolic-link file wrapper referencing `url`.

## Discussion

The file wrapper is not associated with a file-system node until you save it using [- writeToURL:options:originalContentsURL:error:](<write(to_options_originalcontentsurl_).md>).

The file wrapper is initialized with open permissions: anyone can modify or read the file reference. .

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
- [- initSymbolicLinkWithDestination:](<init(symboliclinkwithdestination_).md>) — Initializes the receiver as a symbolic-link file wrapper. _(deprecated)_
- [- initWithSerializedRepresentation:](<init(serializedrepresentation_).md>) — Initializes the receiver as a regular-file file wrapper from given serialized data.
