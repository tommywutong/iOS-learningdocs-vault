---
title: Snapshot
framework: SwiftUI
symbol_kind: associatedtype
role: symbol
role_heading: Associated Type
platforms: [iOS 14.0+（27.0 起废弃）, iPadOS 14.0+（27.0 起废弃）, Mac Catalyst 14.0+（27.0 起废弃）, macOS 11.0+（27.0 起废弃）, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: true
doc_path: /documentation/swiftui/referencefiledocument/snapshot
source_url: 'https://developer.apple.com/documentation/swiftui/referencefiledocument/snapshot'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/referencefiledocument/snapshot.json'
content_hash: 'sha256:4b02822d82a5ca43'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ReferenceFileDocument](../referencefiledocument.md)

# Snapshot

<sub>Associated Type</sub>

A type that represents the document’s stored content.

> [!warning] Deprecated
> Use Document protocol instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
associatedtype Snapshot
```

## Discussion

Define this type to represent all the data that your document stores. When someone issues a Save command, SwiftUI asks your document for a value of this type by calling the document’s [snapshot(contentType:)](<snapshot(contenttype_).md>) method. SwiftUI sends the snapshot that you provide to the document’s [fileWrapper(snapshot:configuration:)](<filewrapper(snapshot_configuration_).md>) method, where you serialize the contents of the snapshot into a file wrapper.

## See Also

### Getting a snapshot

- [snapshot(contentType:)](<snapshot(contenttype_).md>) — Creates a snapshot that represents the current state of the document. _(deprecated)_
