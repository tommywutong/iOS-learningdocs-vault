---
title: regularFileContents
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/filewrapper/regularfilecontents
source_url: 'https://developer.apple.com/documentation/foundation/filewrapper/regularfilecontents'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/filewrapper/regularfilecontents.json'
content_hash: 'sha256:ed31c6eb9b11328f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [FileWrapper](../filewrapper.md)

# regularFileContents

<sub>Instance Property</sub>

The contents of the file-system node associated with a regular-file file wrapper.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var regularFileContents: Data? { get }
```

## Discussion

This property may contain `nil` if the user modifies the file after you call [- readFromURL:options:error:](<read(from_options_).md>) or [- initWithURL:options:error:](<init(url_options_)-70161.md>) but before [FileWrapper](../filewrapper.md) has read the contents of the file. Use the [NSFileWrapperReadingImmediate](readingoptions/immediate.md) reading option to reduce the likelihood of that problem.

### Special Considerations

This property raises `NSInternalInconsistencyException` if the file wrapper object is not a regular-file file wrapper.

## See Also

### Related Documentation

- [- readFromURL:options:error:](<read(from_options_).md>) — Recursively rereads the entire contents of a file wrapper from the specified location on disk.
- [- initRegularFileWithContents:](<init(regularfilewithcontents_).md>) — Initializes the receiver as a regular-file file wrapper.

### Accessing Files

- [filename](filename.md) — The filename of the file wrapper object
- [preferredFilename](preferredfilename.md) — The preferred filename for the file wrapper object.
- [fileAttributes](fileattributes.md) — A dictionary of file attributes.
