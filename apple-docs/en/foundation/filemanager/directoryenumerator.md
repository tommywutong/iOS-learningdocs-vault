---
title: FileManager.DirectoryEnumerator
framework: Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/filemanager/directoryenumerator
source_url: 'https://developer.apple.com/documentation/foundation/filemanager/directoryenumerator'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/filemanager/directoryenumerator.json'
content_hash: 'sha256:43ad733f4b748d5e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [FileManager](../filemanager.md)

# FileManager.DirectoryEnumerator

<sub>Class</sub>

An object that enumerates the contents of a directory.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class DirectoryEnumerator
```

## Overview

You obtain a directory enumerator using [FileManager](../filemanager.md)’s [- enumeratorAtPath:](<enumerator(atpath_).md>) method. The enumeration provides the pathnames of all files and directories contained within that directory. These pathnames are relative to the directory.

An enumeration is recursive, including the files of all subdirectories, and crosses device boundaries. An enumeration does not resolve symbolic links, or attempt to traverse symbolic links that point to directories.

## Relationships

- **Inherits From**: [NSEnumerator](../nsenumerator.md)

- **Conforms To**: [CVarArg](../../swift/cvararg.md), [CustomDebugStringConvertible](../../swift/customdebugstringconvertible.md), [CustomStringConvertible](../../swift/customstringconvertible.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [NSFastEnumeration](../nsfastenumeration.md), [NSObjectProtocol](../../objectivec/nsobjectprotocol.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md), [Sequence](../../swift/sequence.md)

## Topics

### Getting File and Directory Attributes

- [directoryAttributes](directoryenumerator/directoryattributes.md) — A dictionary with the attributes of the directory at which enumeration started.
- [fileAttributes](directoryenumerator/fileattributes.md) — A dictionary with the attributes of the most recently returned file or subdirectory (as referenced by the pathname).
- [level](directoryenumerator/level.md) — The number of levels deep the current object is in the directory hierarchy being enumerated.

### Skipping Subdirectories

- [- skipDescendents](<directoryenumerator/skipdescendents().md>) — Causes the receiver to skip recursion into the most recently obtained subdirectory.
- [- skipDescendants](<directoryenumerator/skipdescendants().md>) — Causes the receiver to skip recursion into the most recently obtained subdirectory.

### Instance Properties

- [isEnumeratingDirectoryPostOrder](directoryenumerator/isenumeratingdirectorypostorder.md)

## See Also

### Discovering directory contents

- [- contentsOfDirectoryAtURL:includingPropertiesForKeys:options:error:](<contentsofdirectory(at_includingpropertiesforkeys_options_).md>) — Performs a shallow search of the specified directory and returns URLs for the contained items.
- [- contentsOfDirectoryAtPath:error:](<contentsofdirectory(atpath_).md>) — Performs a shallow search of the specified directory and returns the paths of any contained items.
- [enumerator(at:includingPropertiesForKeys:options:errorHandler:)](<enumerator(at_includingpropertiesforkeys_options_errorhandler_).md>) — Returns a directory enumerator object that can be used to perform a deep enumeration of the directory at the specified URL.
- [- enumeratorAtPath:](<enumerator(atpath_).md>) — Returns a directory enumerator object that can be used to perform a deep enumeration of the directory at the specified path.
- [- mountedVolumeURLsIncludingResourceValuesForKeys:options:](<mountedvolumeurls(includingresourcevaluesforkeys_options_).md>) — Returns an array of URLs that identify the mounted volumes available on the device.
- [VolumeEnumerationOptions](volumeenumerationoptions.md) — Options for enumerating mounted volumes with the [- mountedVolumeURLsIncludingResourceValuesForKeys:options:](<mountedvolumeurls(includingresourcevaluesforkeys_options_).md>) method.
- [- subpathsOfDirectoryAtPath:error:](<subpathsofdirectory(atpath_).md>) — Performs a deep enumeration of the specified directory and returns the paths of all of the contained subdirectories.
- [- subpathsAtPath:](<subpaths(atpath_).md>) — Returns an array of strings identifying the paths for all items in the specified directory.
