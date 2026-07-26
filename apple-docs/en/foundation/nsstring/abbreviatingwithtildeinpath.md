---
title: abbreviatingWithTildeInPath
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsstring/abbreviatingwithtildeinpath
source_url: 'https://developer.apple.com/documentation/foundation/nsstring/abbreviatingwithtildeinpath'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsstring/abbreviatingwithtildeinpath.json'
content_hash: 'sha256:7a28d6edb66d2b86'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSString](../nsstring.md)

# abbreviatingWithTildeInPath

<sub>Instance Property</sub>

A new string that replaces the current home directory portion of the current path with a tilde (`~`) character.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var abbreviatingWithTildeInPath: String { get }
```

## Discussion

A new string based on the current string object. If the new string specifies a file in the current home directory, the home directory portion of the path is replaced with a tilde (`~`) character. If the string does not specify a file in the current home directory, this method returns a new string object whose path is unchanged from the path in the current string.

Note that this method only works with file paths. It does not work for string representations of URLs.

For sandboxed apps in macOS, the current home directory is not the same as the user’s home directory. For a sandboxed app, the home directory is the app’s home directory. So if you specified a path of `/Users/`_\<current_user\>_`/file.txt` for a sandboxed app, the returned path would be unchanged from the original. However, if you specified the same path for an app not in a sandbox, this method would replace the `/Users/`_\<current_user\>_ portion of the path with a tilde.

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
- [- stringByAppendingPathComponent:](<appendingpathcomponent(__).md>) — Returns a new string made by appending to the receiver a given string.
- [- stringByAppendingPathExtension:](<appendingpathextension(__).md>) — Returns a new string made by appending to the receiver an extension separator followed by a given extension.
- [stringByDeletingLastPathComponent](deletinglastpathcomponent.md) — A new string made by deleting the last path component from the receiver, along with any final path separator.
- [stringByDeletingPathExtension](deletingpathextension.md) — A new string made by deleting the extension (if any, and only the last) from the receiver.
- [stringByExpandingTildeInPath](expandingtildeinpath.md) — A new string made by expanding the initial component of the receiver to its full path value.
- [stringByResolvingSymlinksInPath](resolvingsymlinksinpath.md) — A new string made from the receiver by resolving all symbolic links and standardizing path.
- [stringByStandardizingPath](standardizingpath.md) — A new string made by removing extraneous path components from the receiver.
