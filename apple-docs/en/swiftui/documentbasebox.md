---
title: DocumentBaseBox
framework: SwiftUI
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/documentbasebox
source_url: 'https://developer.apple.com/documentation/swiftui/documentbasebox'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/documentbasebox.json'
content_hash: 'sha256:e96e02867241a837'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# DocumentBaseBox

<sub>Protocol</sub>

A Box that allows setting its Document base not requiring the caller to know the exact types of the box and its base.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
protocol DocumentBaseBox<Document> : AnyObject
```

## Topics

### Specifying the document type

- [Document](documentbasebox/document.md) — The underlying document type.

### Accessing the document

- [base](documentbasebox/base.md) — Updates the underlying document to a new value.

## See Also

### Storing document data in a reference type instance

- [Document](document.md) — A document that supports both reading and writing. _(beta)_
- [ReadableDocument](readabledocument.md) — A document type that supports reading from file. _(beta)_
- [WritableDocument](writabledocument.md) — A document type that supports writing to file. _(beta)_
- [URLDocumentConfiguration](urldocumentconfiguration.md) — The configuration of an open document that stores its file URL, last modification date, and related metadata. _(beta)_
- [DocumentCreationContext](documentcreationcontext.md) — Context about how a document was created. _(beta)_
