---
title: FileWrapper
framework: Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/filewrapper
source_url: 'https://developer.apple.com/documentation/foundation/filewrapper'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/filewrapper.json'
content_hash: 'sha256:7857a8b04b15b5fc'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# FileWrapper

<sub>Class</sub>

A representation of a node (a file, directory, or symbolic link) in the file system.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class FileWrapper
```

## Overview

The [FileWrapper](filewrapper.md) class provides access to the attributes and contents of file system nodes. A file system node is a file, directory, or symbolic link. Instances of this class are known as file wrappers.

> [!note] Note
> Starting in macOS 10.7, [FileWrapper](filewrapper.md) moved from Application Kit to Foundation. As a result of this the `icon`, and `setIcon:` methods have moved to a new category of [FileWrapper](filewrapper.md) that remains in Application Kit.

File wrappers represent a file system node as an object that can be displayed as an image (and possibly edited in place), saved to the file system, or transmitted to another application.

There are three types of file wrappers:

- Regular-file file wrapper: Represents a regular file.
- Directory file wrapper: Represents a directory.
- Symbolic-link file wrapper: Represents a symbolic link.

A file wrapper has these attributes:

- Filename. Name of the file system node the file wrapper represents.
- file-system attributes. See [FileManager](filemanager.md) for information on the contents of the `attributes` dictionary.
- Regular-file contents. Applicable only to regular-file file wrappers.
- File wrappers. Applicable only to directory file wrappers.
- Destination node. Applicable only to symbolic-link file wrappers.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](nscoding.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSSecureCoding](nssecurecoding.md)

## Topics

### Creating File Wrappers

- [- initWithURL:options:error:](<filewrapper/init(url_options_)-70161.md>) — Initializes a file wrapper instance whose kind is determined by the type of file-system node located by the URL.
- [- initWithPath:](<filewrapper/init(path_).md>) — Initializes a file wrapper instance whose kind is determined by the type of file-system node located by the path. _(deprecated)_
- [- initDirectoryWithFileWrappers:](<filewrapper/init(directorywithfilewrappers_).md>) — Initializes the receiver as a directory file wrapper, with a given file-wrapper list.
- [- initRegularFileWithContents:](<filewrapper/init(regularfilewithcontents_).md>) — Initializes the receiver as a regular-file file wrapper.
- [- initSymbolicLinkWithDestination:](<filewrapper/init(symboliclinkwithdestination_).md>) — Initializes the receiver as a symbolic-link file wrapper. _(deprecated)_
- [- initSymbolicLinkWithDestinationURL:](<filewrapper/init(symboliclinkwithdestinationurl_).md>) — Initializes the receiver as a symbolic-link file wrapper that links to a specified file.
- [- initWithSerializedRepresentation:](<filewrapper/init(serializedrepresentation_).md>) — Initializes the receiver as a regular-file file wrapper from given serialized data.

### Querying File Wrappers

- [regularFile](filewrapper/isregularfile.md) — This property contains a boolean value that indicates whether the file wrapper object is a regular-file.
- [directory](filewrapper/isdirectory.md) — This property contains a boolean value indicating whether the file wrapper is a directory file wrapper.
- [symbolicLink](filewrapper/issymboliclink.md) — A boolean that indicates whether the file wrapper object is a symbolic-link file wrapper.

### Accessing File-Wrapper Information

- [fileWrappers](filewrapper/filewrappers.md) — The file wrappers contained by a directory file wrapper.
- [- addFileWrapper:](<filewrapper/addfilewrapper(__).md>) — Adds a child file wrapper to the receiver, which must be a directory file wrapper.
- [- removeFileWrapper:](<filewrapper/removefilewrapper(__).md>) — Removes a child file wrapper from the receiver, which must be a directory file wrapper.
- [- addFileWithPath:](<filewrapper/addfile(withpath_).md>) — Creates a file wrapper from a given file-system node and adds it to the receiver, which must be a directory file wrapper. _(deprecated)_
- [- addRegularFileWithContents:preferredFilename:](<filewrapper/addregularfile(withcontents_preferredfilename_).md>) — Creates a regular-file file wrapper with the given contents and adds it to the receiver, which must be a directory file wrapper.
- [- addSymbolicLinkWithDestination:preferredFilename:](<filewrapper/addsymboliclink(withdestination_preferredfilename_).md>) — Creates a symbolic-link file wrapper pointing to a given file-system node and adds it to the receiver, which must be a directory file wrapper. _(deprecated)_
- [- keyForFileWrapper:](<filewrapper/keyforchildfilewrapper(__).md>) — Returns the dictionary key used by a directory to identify a given file wrapper.
- [- symbolicLinkDestination](<filewrapper/symboliclinkdestination().md>) — Provides the pathname referenced by the file wrapper object, which must be a symbolic-link file wrapper. _(deprecated)_
- [symbolicLinkDestinationURL](filewrapper/symboliclinkdestinationurl.md) — The URL referenced by the file wrapper object, which must be a symbolic-link file wrapper.

### Updating File Wrappers

- [- needsToBeUpdatedFromPath:](<filewrapper/needstobeupdated(frompath_).md>) — Indicates whether the file wrapper needs to be updated to match a given file-system node. _(deprecated)_
- [- matchesContentsOfURL:](<filewrapper/matchescontents(of_).md>) — Indicates whether the contents of a file wrapper matches a directory, regular file, or symbolic link on disk.
- [- updateFromPath:](<filewrapper/update(frompath_).md>) — Updates the file wrapper to match a given file-system node. _(deprecated)_
- [- readFromURL:options:error:](<filewrapper/read(from_options_).md>) — Recursively rereads the entire contents of a file wrapper from the specified location on disk.

### Serializing

- [serializedRepresentation](filewrapper/serializedrepresentation.md) — The contents of the file wrapper as an opaque data object.

### Accessing Files

- [filename](filewrapper/filename.md) — The filename of the file wrapper object
- [preferredFilename](filewrapper/preferredfilename.md) — The preferred filename for the file wrapper object.
- [fileAttributes](filewrapper/fileattributes.md) — A dictionary of file attributes.
- [regularFileContents](filewrapper/regularfilecontents.md) — The contents of the file-system node associated with a regular-file file wrapper.

### Writing Files

- [- writeToFile:atomically:updateFilenames:](<filewrapper/write(tofile_atomically_updatefilenames_).md>) — Writes a file wrapper’s contents to a given file-system node. _(deprecated)_
- [- writeToURL:options:originalContentsURL:error:](<filewrapper/write(to_options_originalcontentsurl_).md>) — Recursively writes the entire contents of a file wrapper to a given file-system URL.

### Working with Icons

- [icon](filewrapper/icon.md) — The icon that represents the file wrapper.

### Constants

- [ReadingOptions](filewrapper/readingoptions.md) — Reading options that can be set by the [- initWithURL:options:error:](<filewrapper/init(url_options_)-70161.md>) and [- readFromURL:options:error:](<filewrapper/read(from_options_).md>) methods.
- [WritingOptions](filewrapper/writingoptions.md) — Writing options that can be set by the [- writeToURL:options:originalContentsURL:error:](<filewrapper/write(to_options_originalcontentsurl_).md>) method.

### Initializers

- [init(URL:options:)](<filewrapper/init(url_options_)-6g2yr.md>)
- [- initWithCoder:](<filewrapper/init(coder_).md>)

## See Also

### Managed file access

- [FileHandle](filehandle.md) — An object-oriented wrapper for a file descriptor.
- [NSFileSecurity](nsfilesecurity.md) — A stub class that encapsulates security information about a file.
- [NSFileVersion](nsfileversion.md) — A snapshot of a file at a specific point in time.
