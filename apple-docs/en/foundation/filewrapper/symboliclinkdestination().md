---
title: symbolicLinkDestination()
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.0+（10.10 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/foundation/filewrapper/symboliclinkdestination()
source_url: 'https://developer.apple.com/documentation/foundation/filewrapper/symboliclinkdestination()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/filewrapper/symboliclinkdestination%28%29.json'
content_hash: 'sha256:c092829c8043d46e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [FileWrapper](../filewrapper.md)

# symbolicLinkDestination()

<sub>Instance Method</sub>

Provides the pathname referenced by the file wrapper object, which must be a symbolic-link file wrapper.

> [!warning] Deprecated
> Use [symbolicLinkDestinationURL](symboliclinkdestinationurl.md) instead.

<sub>macOS</sub>

```swift
func symbolicLinkDestination() -> String
```

## Return Value

Pathname the file wrapper references (the destination of the symbolic link the file wrapper represents).

## Discussion

Beginning with OS X v10.6, the preferred method of referring to files is with a `file://` URL. Therefore, this method has been deprecated in favor of [symbolicLinkDestinationURL](symboliclinkdestinationurl.md).

This method raises `NSInternalInconsistencyException` if the receiver is not a symbolic-link file wrapper.

## See Also

### Accessing File-Wrapper Information

- [fileWrappers](filewrappers.md) — The file wrappers contained by a directory file wrapper.
- [- addFileWrapper:](<addfilewrapper(__).md>) — Adds a child file wrapper to the receiver, which must be a directory file wrapper.
- [- removeFileWrapper:](<removefilewrapper(__).md>) — Removes a child file wrapper from the receiver, which must be a directory file wrapper.
- [- addFileWithPath:](<addfile(withpath_).md>) — Creates a file wrapper from a given file-system node and adds it to the receiver, which must be a directory file wrapper. _(deprecated)_
- [- addRegularFileWithContents:preferredFilename:](<addregularfile(withcontents_preferredfilename_).md>) — Creates a regular-file file wrapper with the given contents and adds it to the receiver, which must be a directory file wrapper.
- [- addSymbolicLinkWithDestination:preferredFilename:](<addsymboliclink(withdestination_preferredfilename_).md>) — Creates a symbolic-link file wrapper pointing to a given file-system node and adds it to the receiver, which must be a directory file wrapper. _(deprecated)_
- [- keyForFileWrapper:](<keyforchildfilewrapper(__).md>) — Returns the dictionary key used by a directory to identify a given file wrapper.
- [symbolicLinkDestinationURL](symboliclinkdestinationurl.md) — The URL referenced by the file wrapper object, which must be a symbolic-link file wrapper.
