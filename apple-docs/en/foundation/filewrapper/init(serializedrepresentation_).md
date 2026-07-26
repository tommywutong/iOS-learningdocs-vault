---
title: 'init(serializedRepresentation:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/filewrapper/init(serializedrepresentation:)'
source_url: 'https://developer.apple.com/documentation/foundation/filewrapper/init(serializedrepresentation:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/filewrapper/init%28serializedrepresentation%3A%29.json'
content_hash: 'sha256:8b98c80a2241f80e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [FileWrapper](../filewrapper.md)

# init(serializedRepresentation:)

<sub>Initializer</sub>

Initializes the receiver as a regular-file file wrapper from given serialized data.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init?(serializedRepresentation serializeRepresentation: Data)
```

## Parameters

- `serializeRepresentation` — Serialized representation of a file wrapper in the format used for the `NSFileContentsPboardType` pasteboard type. Data of this format is returned by such methods as [serializedRepresentation](serializedrepresentation.md) and [- RTFDFromRange:documentAttributes:](<../nsattributedstring/rtfd(from_documentattributes_).md>) ([NSAttributedString](../nsattributedstring.md)).

## Return Value

Regular-file file wrapper initialized from `serializedRepresentation`.

## Discussion

The file wrapper is not associated with a file-system node until you save it using [- writeToURL:options:originalContentsURL:error:](<write(to_options_originalcontentsurl_).md>).

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
- [- initSymbolicLinkWithDestinationURL:](<init(symboliclinkwithdestinationurl_).md>) — Initializes the receiver as a symbolic-link file wrapper that links to a specified file.
