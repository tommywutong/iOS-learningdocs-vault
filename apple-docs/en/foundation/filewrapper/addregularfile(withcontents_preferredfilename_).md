---
title: 'addRegularFile(withContents:preferredFilename:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/filewrapper/addregularfile(withcontents:preferredfilename:)'
source_url: 'https://developer.apple.com/documentation/foundation/filewrapper/addregularfile(withcontents:preferredfilename:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/filewrapper/addregularfile%28withcontents%3Apreferredfilename%3A%29.json'
content_hash: 'sha256:9321576de5cc83ac'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [FileWrapper](../filewrapper.md)

# addRegularFile(withContents:preferredFilename:)

<sub>Instance Method</sub>

Creates a regular-file file wrapper with the given contents and adds it to the receiver, which must be a directory file wrapper.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func addRegularFile(withContents data: Data, preferredFilename fileName: String) -> String
```

## Parameters

- `data` — Contents for the new regular-file file wrapper.

- `fileName` — Preferred filename for the new regular-file file wrapper.

## Return Value

Dictionary key used to store the new file wrapper in the directory’s list of file wrappers. The dictionary key is a unique filename, which is the same as the passed-in file wrapper’s preferred filename unless that name is already in use as a key in the directory’s dictionary of children. See [Accessing File Wrapper Identities](https://developer.apple.com/library/archive/documentation/FileManagement/Conceptual/FileSystemProgrammingGuide/FileWrappers/FileWrappers.html#//apple_ref/doc/uid/TP40010672-CH13-SW1) in [File System Programming Guide](https://developer.apple.com/library/archive/documentation/FileManagement/Conceptual/FileSystemProgrammingGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40010672) for more information about the file-wrapper list structure.

## Discussion

This is a convenience method. The default implementation allocates a new file wrapper, initializes it with [- initRegularFileWithContents:](<init(regularfilewithcontents_).md>), set its [preferredFilename](preferredfilename.md) property, adds it to the directory with [- addFileWrapper:](<addfilewrapper(__).md>), and returns what [- addFileWrapper:](<addfilewrapper(__).md>) returned.

### Special Considerations

This method raises `NSInternalInconsistencyException` if the receiver is not a directory file wrapper.

This method raises `NSInvalidArgumentException` if you pass `nil` or an empty value for `filename`.

## See Also

### Accessing File-Wrapper Information

- [fileWrappers](filewrappers.md) — The file wrappers contained by a directory file wrapper.
- [- addFileWrapper:](<addfilewrapper(__).md>) — Adds a child file wrapper to the receiver, which must be a directory file wrapper.
- [- removeFileWrapper:](<removefilewrapper(__).md>) — Removes a child file wrapper from the receiver, which must be a directory file wrapper.
- [- addFileWithPath:](<addfile(withpath_).md>) — Creates a file wrapper from a given file-system node and adds it to the receiver, which must be a directory file wrapper. _(deprecated)_
- [- addSymbolicLinkWithDestination:preferredFilename:](<addsymboliclink(withdestination_preferredfilename_).md>) — Creates a symbolic-link file wrapper pointing to a given file-system node and adds it to the receiver, which must be a directory file wrapper. _(deprecated)_
- [- keyForFileWrapper:](<keyforchildfilewrapper(__).md>) — Returns the dictionary key used by a directory to identify a given file wrapper.
- [- symbolicLinkDestination](<symboliclinkdestination().md>) — Provides the pathname referenced by the file wrapper object, which must be a symbolic-link file wrapper. _(deprecated)_
- [symbolicLinkDestinationURL](symboliclinkdestinationurl.md) — The URL referenced by the file wrapper object, which must be a symbolic-link file wrapper.
