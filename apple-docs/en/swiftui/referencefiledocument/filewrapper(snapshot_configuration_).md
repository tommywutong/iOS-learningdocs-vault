---
title: 'fileWrapper(snapshot:configuration:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+（27.0 起废弃）, iPadOS 14.0+（27.0 起废弃）, Mac Catalyst 14.0+（27.0 起废弃）, macOS 11.0+（27.0 起废弃）, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: true
doc_path: '/documentation/swiftui/referencefiledocument/filewrapper(snapshot:configuration:)'
source_url: 'https://developer.apple.com/documentation/swiftui/referencefiledocument/filewrapper(snapshot:configuration:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/referencefiledocument/filewrapper%28snapshot%3Aconfiguration%3A%29.json'
content_hash: 'sha256:42d7fb673cca078a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ReferenceFileDocument](../referencefiledocument.md)

# fileWrapper(snapshot:configuration:)

<sub>Instance Method</sub>

Serializes a document snapshot to a file wrapper.

> [!warning] Deprecated
> Use Document protocol instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
func fileWrapper(snapshot: Self.Snapshot, configuration: Self.WriteConfiguration) throws -> FileWrapper
```

## Parameters

- `snapshot` — The document snapshot to save.

- `configuration` — Information about a file that already exists for the document, if any.

## Return Value

The destination to serialize the document contents to. The value can be a newly created [FileWrapper](../../foundation/filewrapper.md) or an update of the one provided in the `configuration` input.

## Discussion

To store a document — for example, in response to a Save command — SwiftUI begins by calling the [snapshot(contentType:)](<snapshot(contenttype_).md>) method to get a copy of the document data in its current state. Then SwiftUI passes that snapshot to this method, where you serialize it and create or modify a file wrapper with the serialized data:

```swift
func fileWrapper(snapshot: Snapshot, configuration: WriteConfiguration) throws -> FileWrapper {
    let data = try JSONEncoder().encode(snapshot)
    return FileWrapper(regularFileWithContents: data)
}
```

SwiftUI disables document edits during the snapshot to ensure that the document’s data remains coherent, but reenables edits during the serialization operation.

> [!note] Note
> SwiftUI calls this method on a background thread. Don’t make user interface changes from that thread.

## See Also

### Writing a document

- [writableContentTypes](writablecontenttypes.md) — The file types that the document supports saving or exporting to. _(deprecated)_
- [WriteConfiguration](writeconfiguration.md) — The configuration for writing document contents. _(deprecated)_
