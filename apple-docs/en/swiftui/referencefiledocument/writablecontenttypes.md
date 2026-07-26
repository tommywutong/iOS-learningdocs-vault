---
title: writableContentTypes
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 14.0+（27.0 起废弃）, iPadOS 14.0+（27.0 起废弃）, Mac Catalyst 14.0+（27.0 起废弃）, macOS 11.0+（27.0 起废弃）, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: true
doc_path: /documentation/swiftui/referencefiledocument/writablecontenttypes
source_url: 'https://developer.apple.com/documentation/swiftui/referencefiledocument/writablecontenttypes'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/referencefiledocument/writablecontenttypes.json'
content_hash: 'sha256:ae06ade47af34e03'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ReferenceFileDocument](../referencefiledocument.md)

# writableContentTypes

<sub>Type Property</sub>

The file types that the document supports saving or exporting to.

> [!warning] Deprecated
> Use Document protocol instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
static var writableContentTypes: [UTType] { get }
```

## Discussion

By default, SwiftUI assumes that your document reads and writes the same set of content types. Only define this property if you need to indicate a different set of types for writing files. Otherwise, the default implementation of this property returns the list that you specify in your implementation of [readableContentTypes](readablecontenttypes.md).

## Default Implementations

### ReferenceFileDocument Implementations

- [writableContentTypes](writablecontenttypes-41rwk.md) — The file types that the document supports saving or exporting to.

## See Also

### Writing a document

- [fileWrapper(snapshot:configuration:)](<filewrapper(snapshot_configuration_).md>) — Serializes a document snapshot to a file wrapper. _(deprecated)_
- [WriteConfiguration](writeconfiguration.md) — The configuration for writing document contents. _(deprecated)_
