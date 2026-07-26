---
title: newDocument
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [macOS 13.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/environmentvalues/newdocument
source_url: 'https://developer.apple.com/documentation/swiftui/environmentvalues/newdocument'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/environmentvalues/newdocument.json'
content_hash: 'sha256:8fcaed88301d986c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [EnvironmentValues](../environmentvalues.md)

# newDocument

<sub>Instance Property</sub>

An action in the environment that presents a new document.

<sub>macOS</sub>

```swift
var newDocument: NewDocumentAction { get }
```

## Discussion

Use the `newDocument` environment value to get the instance of the [NewDocumentAction](../newdocumentaction.md) structure for a given [Environment](../environment.md). Then call the instance to present a new document. You call the instance directly because it defines a [callAsFunction(_:)](<../newdocumentaction/callasfunction(__).md>) method that Swift calls when you call the instance.

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

The above example assumes that you define a `TextDocument` that conforms to the [FileDocument](../filedocument.md) or [ReferenceFileDocument](../referencefiledocument.md) protocol, and a [DocumentGroup](../documentgroup.md) that handles the associated file type.

## See Also

### Opening a document programmatically

- [openDocument](opendocument.md) — An action in the environment that presents an existing document.
- [OpenDocumentAction](../opendocumentaction.md) — An action that presents an existing document.
