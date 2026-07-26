---
title: 'init(_:for:contentType:prepareDocument:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 18.0+（27.0 起废弃）, iPadOS 18.0+（27.0 起废弃）, Mac Catalyst 18.0+（27.0 起废弃）, macOS 15.0+（27.0 起废弃）, visionOS 2.0+（27.0 起废弃）]
languages: [swift]
beta: false
deprecated: true
doc_path: '/documentation/swiftui/newdocumentbutton/init(_:for:contenttype:preparedocument:)'
source_url: 'https://developer.apple.com/documentation/swiftui/newdocumentbutton/init(_:for:contenttype:preparedocument:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/newdocumentbutton/init%28_%3Afor%3Acontenttype%3Apreparedocument%3A%29.json'
content_hash: 'sha256:e0953c733c2d84d3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [NewDocumentButton](../newdocumentbutton.md)

# init(_:for:contentType:prepareDocument:)

<sub>Initializer</sub>

> [!warning] Deprecated
> Conform your document type to ReadableDocument instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
@export(implementation) nonisolated init<D>(_ title: LocalizedStringResource, for documentType: D.Type = D.self, contentType: UTType? = nil, prepareDocument: @escaping () async throws -> D? = { nil }) where D : FileDocument
```

## Parameters

- `title` — A title resource for the button.

- `documentType` — A type of the document to create.

- `contentType` — An optional content type of the document to create.

- `prepareDocument` — A closure is called when a user presses the button. At this point, you can present a document template picker or another UI that allows users to choose a theme, configuration, or a template to create a document from. Return a prepared document, or throw an error if document creation failed. Return `nil` to request creation of an empty document.
