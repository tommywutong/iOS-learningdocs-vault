---
title: 'addFile(withPath:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.0+（10.10 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/foundation/filewrapper/addfile(withpath:)'
source_url: 'https://developer.apple.com/documentation/foundation/filewrapper/addfile(withpath:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/filewrapper/addfile%28withpath%3A%29.json'
content_hash: 'sha256:481e619dd6746718'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [FileWrapper](../filewrapper.md)

# addFile(withPath:)

<sub>Instance Method</sub>

Creates a file wrapper from a given file-system node and adds it to the receiver, which must be a directory file wrapper.

> [!warning] Deprecated
> Use [- addFileWrapper:](<addfilewrapper(__).md>) instead.

<sub>macOS</sub>

```swift
func addFile(withPath path: String) -> String
```

## Parameters

- `path` — File-System node from which to create the file wrapper to add to the directory.

## Return Value

Dictionary key used to store the new file wrapper in the directory’s list of file wrappers. See [Accessing File Wrapper Identities](https://developer.apple.com/library/archive/documentation/FileManagement/Conceptual/FileSystemProgrammingGuide/FileWrappers/FileWrappers.html#//apple_ref/doc/uid/TP40010672-CH13-SW1) in [File System Programming Guide](https://developer.apple.com/library/archive/documentation/FileManagement/Conceptual/FileSystemProgrammingGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40010672) for more information.

## Discussion

Beginning with OS X v10.6, the preferred method of referring to files is with a `file://` URL. Instead of using this method, you can instantiate `NSFileWrapper` with one of the initializers, set its [preferredFilename](preferredfilename.md) property if necessary, and pass the result to [- addFileWrapper:](<addfilewrapper(__).md>).

This method raises `NSInternalInconsistencyException` if the receiver is not a directory file wrapper.

## See Also

### Accessing File-Wrapper Information

- [fileWrappers](filewrappers.md) — The file wrappers contained by a directory file wrapper.
- [- addFileWrapper:](<addfilewrapper(__).md>) — Adds a child file wrapper to the receiver, which must be a directory file wrapper.
- [- removeFileWrapper:](<removefilewrapper(__).md>) — Removes a child file wrapper from the receiver, which must be a directory file wrapper.
- [- addRegularFileWithContents:preferredFilename:](<addregularfile(withcontents_preferredfilename_).md>) — Creates a regular-file file wrapper with the given contents and adds it to the receiver, which must be a directory file wrapper.
- [- addSymbolicLinkWithDestination:preferredFilename:](<addsymboliclink(withdestination_preferredfilename_).md>) — Creates a symbolic-link file wrapper pointing to a given file-system node and adds it to the receiver, which must be a directory file wrapper. _(deprecated)_
- [- keyForFileWrapper:](<keyforchildfilewrapper(__).md>) — Returns the dictionary key used by a directory to identify a given file wrapper.
- [- symbolicLinkDestination](<symboliclinkdestination().md>) — Provides the pathname referenced by the file wrapper object, which must be a symbolic-link file wrapper. _(deprecated)_
- [symbolicLinkDestinationURL](symboliclinkdestinationurl.md) — The URL referenced by the file wrapper object, which must be a symbolic-link file wrapper.
