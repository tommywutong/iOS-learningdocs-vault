---
title: serializedRepresentation
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/filewrapper/serializedrepresentation
source_url: 'https://developer.apple.com/documentation/foundation/filewrapper/serializedrepresentation'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/filewrapper/serializedrepresentation.json'
content_hash: 'sha256:75d28642d24df022'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [FileWrapper](../filewrapper.md)

# serializedRepresentation

<sub>Instance Property</sub>

The contents of the file wrapper as an opaque data object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var serializedRepresentation: Data? { get }
```

## Discussion

This property contains a data object in the format used by the [fileContents](../../appkit/nspasteboard/pasteboardtype/filecontents.md) pasteboard type. This data object is also suitable for passing to [- initWithSerializedRepresentation:](<init(serializedrepresentation_).md>).

This property may be `nil` if the user modifies the contents of the file system node after you call [- readFromURL:options:error:](<read(from_options_).md>) or [- initWithURL:options:error:](<init(url_options_)-70161.md>), but before [FileWrapper](../filewrapper.md) has read the contents of the file.  You can use the [NSFileWrapperReadingImmediate](readingoptions/immediate.md) reading option to reduce the likelihood of this problem.

## See Also

### Related Documentation

- [- initWithSerializedRepresentation:](<init(serializedrepresentation_).md>) — Initializes the receiver as a regular-file file wrapper from given serialized data.
