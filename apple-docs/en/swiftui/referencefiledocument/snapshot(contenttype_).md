---
title: 'snapshot(contentType:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+（27.0 起废弃）, iPadOS 14.0+（27.0 起废弃）, Mac Catalyst 14.0+（27.0 起废弃）, macOS 11.0+（27.0 起废弃）, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: true
doc_path: '/documentation/swiftui/referencefiledocument/snapshot(contenttype:)'
source_url: 'https://developer.apple.com/documentation/swiftui/referencefiledocument/snapshot(contenttype:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/referencefiledocument/snapshot%28contenttype%3A%29.json'
content_hash: 'sha256:f471952043962e6c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ReferenceFileDocument](../referencefiledocument.md)

# snapshot(contentType:)

<sub>Instance Method</sub>

Creates a snapshot that represents the current state of the document.

> [!warning] Deprecated
> Use Document protocol instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
func snapshot(contentType: UTType) throws -> Self.Snapshot
```

## Parameters

- `contentType` — The content type that you create the document snapshot for.

## Return Value

A snapshot of the document content that the system provides to the [fileWrapper(snapshot:configuration:)](<filewrapper(snapshot_configuration_).md>) method for serialization.

## Discussion

To store a document — for example, in response to a Save command — SwiftUI begins by calling this method. Return a copy of the document’s content from your implementation of the method. For example, you might define an initializer for your document’s model object that copies the contents of the document’s instance, and return that:

```swift
func snapshot(contentType: UTType) throws -> Snapshot {
    Model(from: model) // Creates a copy.
}
```

SwiftUI prevents document edits during the snapshot operation to ensure that the model state remains coherent. After the call completes, SwiftUI reenables edits, and then calls the [fileWrapper(snapshot:configuration:)](<filewrapper(snapshot_configuration_).md>) method, where you serialize the snapshot and store it to a file.

> [!note] Note
> SwiftUI calls this method on a background thread. Don’t make user interface changes from that thread.

## See Also

### Getting a snapshot

- [Snapshot](snapshot.md) — A type that represents the document’s stored content. _(deprecated)_
