---
title: 'init(_:contentType:source:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, visionOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: '/documentation/swiftui/newdocumentbutton/init(_:contenttype:source:)'
source_url: 'https://developer.apple.com/documentation/swiftui/newdocumentbutton/init(_:contenttype:source:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/newdocumentbutton/init%28_%3Acontenttype%3Asource%3A%29.json'
content_hash: 'sha256:718c5eeaba3b9933'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [NewDocumentButton](../newdocumentbutton.md)

# init(_:contentType:source:)

<sub>Initializer</sub>

Creates and opens new documents, tagging them with a creation source.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
nonisolated init(_ label: Text? = nil, contentType: UTType? = nil, source: DocumentCreationSource)
```

## Parameters

- `label` — A label for the button.

- `contentType` — An optional content type of the document to create. If not provided, the first content type of the first document type listed in the app definition is used.

- `source` — A source for the document creation flow. When a document is created, you can retrieve its source from [FileDocumentConfiguration](../filedocumentconfiguration.md) or [URLDocumentConfiguration](../urldocumentconfiguration.md).

## Discussion

```swift
extension DocumentCreationSource {
    static let brainstorming: Self =
        DocumentCreationSource(id: "brainstorming")
}

DocumentGroupLaunchScene("Meeting Minutes") {
    NewDocumentButton(Text("New meeting minutes…"))
    NewDocumentButton(
        Text("New brainstorming meeting…"),
        source: .brainstorming
    )
}
```

## See Also

### Creating and opening a document with a creation source

- [init(_:contentType:source:_:)](<init(__contenttype_source___).md>) — Creates and opens new URL-based documents from a template picker. _(beta)_
- [init(_:contentType:source:prepareDocumentURL:)](<init(__contenttype_source_preparedocumenturl_).md>) — Creates and opens new URL-based documents from a template picker. _(beta)_
