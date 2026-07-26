---
title: deletingPathExtension
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsstring/deletingpathextension
source_url: 'https://developer.apple.com/documentation/foundation/nsstring/deletingpathextension'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsstring/deletingpathextension.json'
content_hash: 'sha256:d1d95b19f4312d61'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSString](../nsstring.md)

# deletingPathExtension

<sub>Instance Property</sub>

A new string made by deleting the extension (if any, and only the last) from the receiver.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var deletingPathExtension: String { get }
```

## Discussion

A new string made by deleting the extension (if any, and only the last) from the receiver. Strips any trailing path separator before checking for an extension. If the receiver represents the root path, it is returned unaltered.

The following table illustrates the effect of this method on a variety of different paths:

| Receiver’s String Value | Resulting String |
|---|---|
| “`/tmp/scratch.tiff`” | “`/tmp/scratch`” |
| “`/tmp/`” | “`/tmp`” |
| “`scratch.bundle/`” | “`scratch`” |
| “`scratch..tiff`” | “`scratch.`” |
| “`.tiff`” | “`.tiff`” |
| “`/`” | “`/`” |

Note that attempting to delete an extension from `@".tiff"` causes the result to be `@".tiff"` instead of an empty string. This difference is because a file named `@".tiff"` is not considered to have an extension, so nothing is deleted. Note also that this method only works with file paths (not, for example, string representations of URLs).

## See Also

### Working with Paths

- [+ pathWithComponents:](<path(withcomponents_).md>) — Returns a string built from the strings in a given array by concatenating them with a path separator between each pair.
- [pathComponents](pathcomponents.md) — The file-system path components of the receiver.
- [- completePathIntoString:caseSensitive:matchesIntoArray:filterTypes:](<completepath(into_casesensitive_matchesinto_filtertypes_).md>) — Interprets the receiver as a path in the file system and attempts to perform filename completion, returning a numeric value that indicates whether a match was possible, and by reference the longest path that matches the receiver.
- [fileSystemRepresentation](filesystemrepresentation.md) — A file system-specific representation of the receiver.
- [- getFileSystemRepresentation:maxLength:](<getfilesystemrepresentation(__maxlength_).md>) — Interprets the receiver as a system-independent path and fills a buffer with a C-string in a format and encoding suitable for use with file-system calls.
- [absolutePath](isabsolutepath.md) — A Boolean value that indicates whether the receiver represents an absolute path.
- [lastPathComponent](lastpathcomponent.md) — The last path component of the receiver.
- [pathExtension](pathextension.md) — The path extension, if any, of the string as interpreted as a path.
- [stringByAbbreviatingWithTildeInPath](abbreviatingwithtildeinpath.md) — A new string that replaces the current home directory portion of the current path with a tilde (`~`) character.
- [- stringByAppendingPathComponent:](<appendingpathcomponent(__).md>) — Returns a new string made by appending to the receiver a given string.
- [- stringByAppendingPathExtension:](<appendingpathextension(__).md>) — Returns a new string made by appending to the receiver an extension separator followed by a given extension.
- [stringByDeletingLastPathComponent](deletinglastpathcomponent.md) — A new string made by deleting the last path component from the receiver, along with any final path separator.
- [stringByExpandingTildeInPath](expandingtildeinpath.md) — A new string made by expanding the initial component of the receiver to its full path value.
- [stringByResolvingSymlinksInPath](resolvingsymlinksinpath.md) — A new string made from the receiver by resolving all symbolic links and standardizing path.
- [stringByStandardizingPath](standardizingpath.md) — A new string made by removing extraneous path components from the receiver.
