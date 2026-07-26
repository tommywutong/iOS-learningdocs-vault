---
title: NewDocumentAction
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [macOS 13.0+（27.0 起废弃）]
languages: [swift]
beta: false
deprecated: true
doc_path: /documentation/swiftui/newdocumentaction
source_url: 'https://developer.apple.com/documentation/swiftui/newdocumentaction'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/newdocumentaction.json'
content_hash: 'sha256:98afe98ea804e1d0'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# NewDocumentAction

<sub>Structure</sub>

An action that presents a new document.

> [!warning] Deprecated
> Conform your document type to Document instead.

<sub>macOS</sub>

```swift
@MainActor @preconcurrency struct NewDocumentAction
```

## Overview

Use the [newDocument](environmentvalues/newdocument.md) environment value to get the instance of this structure for a given [Environment](environment.md). Then call the instance to present a new document. You call the instance directly because it defines a [callAsFunction(_:)](<newdocumentaction/callasfunction(__).md>) method that Swift calls when you call the instance.

For example, you can define a button that creates a new document from the selected text:

```swift
struct NewDocumentFromSelection: View {
    @FocusedBinding(\.selectedText) private var selectedText: String?
    @Environment(\.newDocument) private var newDocument

    var body: some View {
        Button("New Document With Selection") {
            newDocument(TextDocument(text: selectedText))
        }
        .disabled(selectedText?.isEmpty != false)
    }
}
```

The above example assumes that you define a `TextDocument` that conforms to the [FileDocument](filedocument.md) or [ReferenceFileDocument](referencefiledocument.md) protocol, and a [DocumentGroup](documentgroup.md) that handles the associated file type.

## Relationships

- **Conforms To**: [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Calling the action

- [callAsFunction(_:)](<newdocumentaction/callasfunction(__).md>) — Presents a new document window for the in-memory document returned by the provided closure. _(beta)_
- [callAsFunction(contentType:)](<newdocumentaction/callasfunction(contenttype_).md>) — Presents a new document window.
- [callAsFunction(contentType:prepareDocument:)](<newdocumentaction/callasfunction(contenttype_preparedocument_).md>) — Presents a new document window with preset contents.

## See Also

### Deprecated

- [FileDocument](filedocument.md) — A type that you use to serialize documents to and from file. _(deprecated)_
- [FileDocumentConfiguration](filedocumentconfiguration.md) — The properties of an open file document. _(deprecated)_
- [FileDocumentReadConfiguration](filedocumentreadconfiguration.md) — The configuration for reading file contents. _(deprecated)_
- [FileDocumentWriteConfiguration](filedocumentwriteconfiguration.md) — The configuration for serializing file contents. _(deprecated)_
- [ReferenceFileDocument](referencefiledocument.md) — A type that you use to serialize reference type documents to and from file. _(deprecated)_
- [ReferenceFileDocumentConfiguration](referencefiledocumentconfiguration.md) — The properties of an open reference file document. _(deprecated)_
