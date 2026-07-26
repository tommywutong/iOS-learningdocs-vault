---
title: preferredFilename
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/filewrapper/preferredfilename
source_url: 'https://developer.apple.com/documentation/foundation/filewrapper/preferredfilename'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/filewrapper/preferredfilename.json'
content_hash: 'sha256:48140c1b25eb616a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [FileWrapper](../filewrapper.md)

# preferredFilename

<sub>Instance Property</sub>

The preferred filename for the file wrapper object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var preferredFilename: String? { get set }
```

## Discussion

This name is normally used as the dictionary key when a child file wrapper is added to a directory file wrapper. However, if another file wrapper with the same preferred name already exists in the directory file wrapper when this object is added, the filename assigned as the dictionary key may differ from the preferred filename.

When you change the preferred filename, the default implementation of this property causes the existing parent directory file wrappers to remove and re-add the child to accommodate the change. Preferred filenames of children are not preserved when you write a file wrapper to disk and then later instantiate another file wrapper by reading the file from disk. If you need to preserve the user-visible names of attachments, you have to store the names yourself.

## See Also

### Related Documentation

- [- addFileWrapper:](<addfilewrapper(__).md>) — Adds a child file wrapper to the receiver, which must be a directory file wrapper.
- [- initWithURL:options:error:](<init(url_options_)-70161.md>) — Initializes a file wrapper instance whose kind is determined by the type of file-system node located by the URL.
- [- writeToURL:options:originalContentsURL:error:](<write(to_options_originalcontentsurl_).md>) — Recursively writes the entire contents of a file wrapper to a given file-system URL.
- [- initDirectoryWithFileWrappers:](<init(directorywithfilewrappers_).md>) — Initializes the receiver as a directory file wrapper, with a given file-wrapper list.

### Accessing Files

- [filename](filename.md) — The filename of the file wrapper object
- [fileAttributes](fileattributes.md) — A dictionary of file attributes.
- [regularFileContents](regularfilecontents.md) — The contents of the file-system node associated with a regular-file file wrapper.
