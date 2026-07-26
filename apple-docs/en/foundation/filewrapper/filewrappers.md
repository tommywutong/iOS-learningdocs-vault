---
title: fileWrappers
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/filewrapper/filewrappers
source_url: 'https://developer.apple.com/documentation/foundation/filewrapper/filewrappers'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/filewrapper/filewrappers.json'
content_hash: 'sha256:6fd99e24f7df5cb1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [FileWrapper](../filewrapper.md)

# fileWrappers

<sub>Instance Property</sub>

The file wrappers contained by a directory file wrapper.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var fileWrappers: [String : FileWrapper]? { get }
```

## Discussion

The dictionary contains entries whose values are the file wrappers and whose keys are the unique filenames that have been assigned to each one. See [Accessing File Wrapper Identities](https://developer.apple.com/library/archive/documentation/FileManagement/Conceptual/FileSystemProgrammingGuide/FileWrappers/FileWrappers.html#//apple_ref/doc/uid/TP40010672-CH13-SW1) in [File System Programming Guide](https://developer.apple.com/library/archive/documentation/FileManagement/Conceptual/FileSystemProgrammingGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40010672) for more information about the file-wrapper list structure.

This property may contain `nil` if the user modifies the directory after you call [- readFromURL:options:error:](<read(from_options_).md>) or [- initWithURL:options:error:](<init(url_options_)-70161.md>) but before [FileWrapper](../filewrapper.md) has read the contents of the directory.  Use the [NSFileWrapperReadingImmediate](readingoptions/immediate.md) reading option to reduce the likelihood of that problem.

### Special Considerations

This property raises `NSInternalInconsistencyException` if the file wrapper object is not a directory file wrapper.

## See Also

### Related Documentation

- [filename](filename.md) — The filename of the file wrapper object

### Accessing File-Wrapper Information

- [- addFileWrapper:](<addfilewrapper(__).md>) — Adds a child file wrapper to the receiver, which must be a directory file wrapper.
- [- removeFileWrapper:](<removefilewrapper(__).md>) — Removes a child file wrapper from the receiver, which must be a directory file wrapper.
- [- addFileWithPath:](<addfile(withpath_).md>) — Creates a file wrapper from a given file-system node and adds it to the receiver, which must be a directory file wrapper. _(deprecated)_
- [- addRegularFileWithContents:preferredFilename:](<addregularfile(withcontents_preferredfilename_).md>) — Creates a regular-file file wrapper with the given contents and adds it to the receiver, which must be a directory file wrapper.
- [- addSymbolicLinkWithDestination:preferredFilename:](<addsymboliclink(withdestination_preferredfilename_).md>) — Creates a symbolic-link file wrapper pointing to a given file-system node and adds it to the receiver, which must be a directory file wrapper. _(deprecated)_
- [- keyForFileWrapper:](<keyforchildfilewrapper(__).md>) — Returns the dictionary key used by a directory to identify a given file wrapper.
- [- symbolicLinkDestination](<symboliclinkdestination().md>) — Provides the pathname referenced by the file wrapper object, which must be a symbolic-link file wrapper. _(deprecated)_
- [symbolicLinkDestinationURL](symboliclinkdestinationurl.md) — The URL referenced by the file wrapper object, which must be a symbolic-link file wrapper.
