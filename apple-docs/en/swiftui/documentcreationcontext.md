---
title: DocumentCreationContext
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, visionOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: /documentation/swiftui/documentcreationcontext
source_url: 'https://developer.apple.com/documentation/swiftui/documentcreationcontext'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/documentcreationcontext.json'
content_hash: 'sha256:6a09114d639b5c85'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# DocumentCreationContext

<sub>Structure</sub>

Context about how a document was created.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
struct DocumentCreationContext
```

## Overview

SwiftUI passes this to the `makeDocument` closure of [DocumentGroup](documentgroup.md). Use [creationSource](documentcreationcontext/creationsource.md) to determine which [NewDocumentButton](newdocumentbutton.md) the person tapped and configure the document accordingly:

```swift
DocumentGroup { document in
    EditorView(document: document)
} makeDocument: { configuration, context in
    let document = NotesDocument()
    if context.creationSource == .checklist {
        document.template = .checklist
    }
    return document
}
```

## Relationships

- **Conforms To**: [Copyable](../swift/copyable.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Escapable](../swift/escapable.md), [Hashable](../swift/hashable.md)

## Topics

### Accessing creation properties

- [creationSource](documentcreationcontext/creationsource.md) — The source associated with the button that created this document. _(beta)_

## See Also

### Storing document data in a reference type instance

- [Document](document.md) — A document that supports both reading and writing. _(beta)_
- [ReadableDocument](readabledocument.md) — A document type that supports reading from file. _(beta)_
- [WritableDocument](writabledocument.md) — A document type that supports writing to file. _(beta)_
- [URLDocumentConfiguration](urldocumentconfiguration.md) — The configuration of an open document that stores its file URL, last modification date, and related metadata. _(beta)_
- [DocumentBaseBox](documentbasebox.md) — A Box that allows setting its Document base not requiring the caller to know the exact types of the box and its base.
