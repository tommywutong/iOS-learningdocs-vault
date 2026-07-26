---
title: immediate
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/filewrapper/readingoptions/immediate
source_url: 'https://developer.apple.com/documentation/foundation/filewrapper/readingoptions/immediate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/filewrapper/readingoptions/immediate.json'
content_hash: 'sha256:b6de30d709ae40e9'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [FileWrapper](../../filewrapper.md) · [ReadingOptions](../readingoptions.md)

# immediate

<sub>Type Property</sub>

The option to read files immediately after creating a file wrapper.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var immediate: FileWrapper.ReadingOptions { get }
```

## Discussion

When you create a file wrapper and pass the [NSFileWrapperReadingImmediate](immediate.md) reading option, the content of the file is read immediately. Otherwise, file content is read only when requested, such as by accessing the [regularFileContents](../regularfilecontents.md), [fileWrappers](../filewrappers.md), [serializedRepresentation](../serializedrepresentation.md), or [symbolicLinkDestinationURL](../symboliclinkdestinationurl.md) properties.

Reading a file immediately rather than lazily can help mitigate against reading errors caused by the user moving or deleting the file after a file wrapper is created. However, passing this option can result in unnecessary disk or network access—particularly when opening a document file package, which causes all of its directory contents to be enumerated and read preemptively.

Even when [NSFileWrapperReadingImmediate](immediate.md) is specified, [FileWrapper](../../filewrapper.md) may not read the contents of some file packages immediately. For example, because the contents of bundles are immutable to the user, [FileWrapper](../../filewrapper.md) may read the children of such a directory lazily as a performance optimization.

You can use this option to take a snapshot of a file or folder for writing later. For example, an application like TextEdit can use this option when creating new file wrappers to represent attachments that the user creates by copying and pasting or dragging and dropping from the Finder to a TextEdit document.

## See Also

### Constants

- [NSFileWrapperReadingWithoutMapping](withoutmapping.md) — Whether file mapping for regular file wrappers is disallowed.
