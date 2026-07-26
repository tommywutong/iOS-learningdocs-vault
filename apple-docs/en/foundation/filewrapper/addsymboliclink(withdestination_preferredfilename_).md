---
title: 'addSymbolicLink(withDestination:preferredFilename:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.0+（10.10 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/foundation/filewrapper/addsymboliclink(withdestination:preferredfilename:)'
source_url: 'https://developer.apple.com/documentation/foundation/filewrapper/addsymboliclink(withdestination:preferredfilename:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/filewrapper/addsymboliclink%28withdestination%3Apreferredfilename%3A%29.json'
content_hash: 'sha256:635b7a47081139db'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [FileWrapper](../filewrapper.md)

# addSymbolicLink(withDestination:preferredFilename:)

<sub>Instance Method</sub>

Creates a symbolic-link file wrapper pointing to a given file-system node and adds it to the receiver, which must be a directory file wrapper.

> [!warning] Deprecated
> Use [- addFileWrapper:](<addfilewrapper(__).md>) instead.

<sub>macOS</sub>

```swift
func addSymbolicLink(withDestination path: String, preferredFilename filename: String) -> String
```

## Parameters

- `path` — Pathname the new symbolic-link file wrapper is to reference.

- `filename` — Preferred filename for the new symbolic-link file wrapper.

## Return Value

Dictionary key used to store the new file wrapper in the directory’s list of file wrappers. See [Accessing File Wrapper Identities](https://developer.apple.com/library/archive/documentation/FileManagement/Conceptual/FileSystemProgrammingGuide/FileWrappers/FileWrappers.html#//apple_ref/doc/uid/TP40010672-CH13-SW1) in [File System Programming Guide](https://developer.apple.com/library/archive/documentation/FileManagement/Conceptual/FileSystemProgrammingGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40010672) for more information.

## Discussion

Beginning with OS X v10.6, the preferred method of referring to files is with a `file://` URL. Instead of using this method, you can instantiate `NSFileWrapper` with one of the initializers, set its [preferredFilename](preferredfilename.md) property if necessary, and pass the result to [- addFileWrapper:](<addfilewrapper(__).md>).

This method raises `NSInternalInconsistencyException` if the receiver is not a directory file wrapper.

This method raises `NSInvalidArgumentException` if you pass `nil` or an empty value for `preferredFilename`.

## See Also

### Accessing File-Wrapper Information

- [fileWrappers](filewrappers.md) — The file wrappers contained by a directory file wrapper.
- [- addFileWrapper:](<addfilewrapper(__).md>) — Adds a child file wrapper to the receiver, which must be a directory file wrapper.
- [- removeFileWrapper:](<removefilewrapper(__).md>) — Removes a child file wrapper from the receiver, which must be a directory file wrapper.
- [- addFileWithPath:](<addfile(withpath_).md>) — Creates a file wrapper from a given file-system node and adds it to the receiver, which must be a directory file wrapper. _(deprecated)_
- [- addRegularFileWithContents:preferredFilename:](<addregularfile(withcontents_preferredfilename_).md>) — Creates a regular-file file wrapper with the given contents and adds it to the receiver, which must be a directory file wrapper.
- [- keyForFileWrapper:](<keyforchildfilewrapper(__).md>) — Returns the dictionary key used by a directory to identify a given file wrapper.
- [- symbolicLinkDestination](<symboliclinkdestination().md>) — Provides the pathname referenced by the file wrapper object, which must be a symbolic-link file wrapper. _(deprecated)_
- [symbolicLinkDestinationURL](symboliclinkdestinationurl.md) — The URL referenced by the file wrapper object, which must be a symbolic-link file wrapper.
