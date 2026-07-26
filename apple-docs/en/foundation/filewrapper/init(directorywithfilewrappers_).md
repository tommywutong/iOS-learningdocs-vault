---
title: 'init(directoryWithFileWrappers:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/filewrapper/init(directorywithfilewrappers:)'
source_url: 'https://developer.apple.com/documentation/foundation/filewrapper/init(directorywithfilewrappers:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/filewrapper/init%28directorywithfilewrappers%3A%29.json'
content_hash: 'sha256:ae22c719488b01ce'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [FileWrapper](../filewrapper.md)

# init(directoryWithFileWrappers:)

<sub>Initializer</sub>

Initializes the receiver as a directory file wrapper, with a given file-wrapper list.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(directoryWithFileWrappers childrenByPreferredName: [String : FileWrapper])
```

## Parameters

- `childrenByPreferredName` — Key-value dictionary of file wrappers with which to initialize the receiver. The dictionary must contain entries whose values are the file wrappers that are to become children and whose keys are filenames. See [Accessing File Wrapper Identities](https://developer.apple.com/library/archive/documentation/FileManagement/Conceptual/FileSystemProgrammingGuide/FileWrappers/FileWrappers.html#//apple_ref/doc/uid/TP40010672-CH13-SW1) in [File System Programming Guide](https://developer.apple.com/library/archive/documentation/FileManagement/Conceptual/FileSystemProgrammingGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40010672) for more information about the file-wrapper list structure.

## Return Value

Initialized file wrapper for `fileWrappers`.

## Discussion

After initialization, the file wrapper is not associated with a file-system node until you save it using [- writeToURL:options:originalContentsURL:error:](<write(to_options_originalcontentsurl_).md>).

The receiver is initialized with open permissions: anyone can read, write, or modify the directory on disk.

If any file wrapper in the directory doesn’t have a preferred filename, its preferred name is automatically set to its corresponding key in the `childrenByPreferredName` dictionary.

## See Also

### Related Documentation

- [preferredFilename](preferredfilename.md) — The preferred filename for the file wrapper object.
- [filename](filename.md) — The filename of the file wrapper object
- [fileAttributes](fileattributes.md) — A dictionary of file attributes.

### Creating File Wrappers

- [- initWithURL:options:error:](<init(url_options_)-70161.md>) — Initializes a file wrapper instance whose kind is determined by the type of file-system node located by the URL.
- [- initWithPath:](<init(path_).md>) — Initializes a file wrapper instance whose kind is determined by the type of file-system node located by the path. _(deprecated)_
- [- initRegularFileWithContents:](<init(regularfilewithcontents_).md>) — Initializes the receiver as a regular-file file wrapper.
- [- initSymbolicLinkWithDestination:](<init(symboliclinkwithdestination_).md>) — Initializes the receiver as a symbolic-link file wrapper. _(deprecated)_
- [- initSymbolicLinkWithDestinationURL:](<init(symboliclinkwithdestinationurl_).md>) — Initializes the receiver as a symbolic-link file wrapper that links to a specified file.
- [- initWithSerializedRepresentation:](<init(serializedrepresentation_).md>) — Initializes the receiver as a regular-file file wrapper from given serialized data.
