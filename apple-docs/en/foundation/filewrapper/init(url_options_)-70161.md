---
title: 'init(url:options:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/filewrapper/init(url:options:)-70161'
source_url: 'https://developer.apple.com/documentation/foundation/filewrapper/init(url:options:)-70161'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/filewrapper/init%28url%3Aoptions%3A%29-70161.json'
content_hash: 'sha256:717ffbf9f4da4f3c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [FileWrapper](../filewrapper.md)

# init(url:options:)

<sub>Initializer</sub>

Initializes a file wrapper instance whose kind is determined by the type of file-system node located by the URL.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(url: URL, options: FileWrapper.ReadingOptions = []) throws
```

## Parameters

- `url` — URL of the file-system node the file wrapper is to represent.

- `options` — Option flags for reading the node located at `url`. See [ReadingOptions](readingoptions.md) for possible values.

## Return Value

File wrapper for the file-system node at `url`. May be a directory, file, or symbolic link, depending on what is located at the URL. Returns [false](../../swift/false.md) (0) if reading is not successful.

## Discussion

If `url` is a directory, this method recursively creates file wrappers for each node within that directory. Use the [fileWrappers](filewrappers.md) property to get the file wrappers of the nodes contained by the directory.

> [!note] Handling Errors in Swift
> In Swift, this API is imported as an initializer and is marked with the `throws` keyword to indicate that it throws an error in cases of failure.
>
> You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [Error Handling](https://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [The Swift Programming Language](https://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## See Also

### Related Documentation

- [fileWrappers](filewrappers.md) — The file wrappers contained by a directory file wrapper.
- [preferredFilename](preferredfilename.md) — The preferred filename for the file wrapper object.
- [- readFromURL:options:error:](<read(from_options_).md>) — Recursively rereads the entire contents of a file wrapper from the specified location on disk.
- [filename](filename.md) — The filename of the file wrapper object
- [File System Programming Guide](https://developer.apple.com/library/archive/documentation/FileManagement/Conceptual/FileSystemProgrammingGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40010672)
- [fileAttributes](fileattributes.md) — A dictionary of file attributes.

### Creating File Wrappers

- [- initWithPath:](<init(path_).md>) — Initializes a file wrapper instance whose kind is determined by the type of file-system node located by the path. _(deprecated)_
- [- initDirectoryWithFileWrappers:](<init(directorywithfilewrappers_).md>) — Initializes the receiver as a directory file wrapper, with a given file-wrapper list.
- [- initRegularFileWithContents:](<init(regularfilewithcontents_).md>) — Initializes the receiver as a regular-file file wrapper.
- [- initSymbolicLinkWithDestination:](<init(symboliclinkwithdestination_).md>) — Initializes the receiver as a symbolic-link file wrapper. _(deprecated)_
- [- initSymbolicLinkWithDestinationURL:](<init(symboliclinkwithdestinationurl_).md>) — Initializes the receiver as a symbolic-link file wrapper that links to a specified file.
- [- initWithSerializedRepresentation:](<init(serializedrepresentation_).md>) — Initializes the receiver as a regular-file file wrapper from given serialized data.
