---
title: 'init(_:contentType:source:prepareDocumentURL:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, visionOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: '/documentation/swiftui/newdocumentbutton/init(_:contenttype:source:preparedocumenturl:)'
source_url: 'https://developer.apple.com/documentation/swiftui/newdocumentbutton/init(_:contenttype:source:preparedocumenturl:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/newdocumentbutton/init%28_%3Acontenttype%3Asource%3Apreparedocumenturl%3A%29.json'
content_hash: 'sha256:c9b454cd073dde15'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [NewDocumentButton](../newdocumentbutton.md)

# init(_:contentType:source:prepareDocumentURL:)

<sub>Initializer</sub>

Creates and opens new URL-based documents from a template picker.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
nonisolated init(_ title: LocalizedStringKey, contentType: UTType, source: DocumentCreationSource, prepareDocumentURL: @escaping () async throws -> URL? = { nil })
```

## Parameters

- `title` — A title key for the button.

- `contentType` — The content type of the document to create.

- `source` — A source for the document creation flow. When a document is created, you can retrieve its source from [FileDocumentConfiguration](../filedocumentconfiguration.md) or [URLDocumentConfiguration](../urldocumentconfiguration.md).

- `prepareDocumentURL` — Called when the user taps the button.

## See Also

### Creating and opening a document with a creation source

- [init(_:contentType:source:)](<init(__contenttype_source_).md>) — Creates and opens new documents, tagging them with a creation source. _(beta)_
- [init(_:contentType:source:_:)](<init(__contenttype_source___).md>) — Creates and opens new URL-based documents from a template picker. _(beta)_
