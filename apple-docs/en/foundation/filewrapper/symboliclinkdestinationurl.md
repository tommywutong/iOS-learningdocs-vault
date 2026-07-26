---
title: symbolicLinkDestinationURL
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/filewrapper/symboliclinkdestinationurl
source_url: 'https://developer.apple.com/documentation/foundation/filewrapper/symboliclinkdestinationurl'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/filewrapper/symboliclinkdestinationurl.json'
content_hash: 'sha256:b6353f0a8e94d460'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [FileWrapper](../filewrapper.md)

# symbolicLinkDestinationURL

<sub>Instance Property</sub>

The URL referenced by the file wrapper object, which must be a symbolic-link file wrapper.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var symbolicLinkDestinationURL: URL? { get }
```

## Discussion

This property may contain `nil` if the user modifies the symbolic link after you call [- readFromURL:options:error:](<read(from_options_).md>) or [- initWithURL:options:error:](<init(url_options_)-70161.md>) but before [FileWrapper](../filewrapper.md) has read the contents of the link.  Use the [NSFileWrapperReadingImmediate](readingoptions/immediate.md) reading option to reduce the likelihood of that problem.

### Special Considerations

This property raises `NSInternalInconsistencyException` if the file wrapper object is not a symbolic-link file wrapper.

## See Also

### Accessing File-Wrapper Information

- [fileWrappers](filewrappers.md) — The file wrappers contained by a directory file wrapper.
- [- addFileWrapper:](<addfilewrapper(__).md>) — Adds a child file wrapper to the receiver, which must be a directory file wrapper.
- [- removeFileWrapper:](<removefilewrapper(__).md>) — Removes a child file wrapper from the receiver, which must be a directory file wrapper.
- [- addFileWithPath:](<addfile(withpath_).md>) — Creates a file wrapper from a given file-system node and adds it to the receiver, which must be a directory file wrapper. _(deprecated)_
- [- addRegularFileWithContents:preferredFilename:](<addregularfile(withcontents_preferredfilename_).md>) — Creates a regular-file file wrapper with the given contents and adds it to the receiver, which must be a directory file wrapper.
- [- addSymbolicLinkWithDestination:preferredFilename:](<addsymboliclink(withdestination_preferredfilename_).md>) — Creates a symbolic-link file wrapper pointing to a given file-system node and adds it to the receiver, which must be a directory file wrapper. _(deprecated)_
- [- keyForFileWrapper:](<keyforchildfilewrapper(__).md>) — Returns the dictionary key used by a directory to identify a given file wrapper.
- [- symbolicLinkDestination](<symboliclinkdestination().md>) — Provides the pathname referenced by the file wrapper object, which must be a symbolic-link file wrapper. _(deprecated)_
