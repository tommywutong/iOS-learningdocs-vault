---
title: 'init(_:contentType:source:_:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, visionOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: '/documentation/swiftui/newdocumentbutton/init(_:contenttype:source:_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/newdocumentbutton/init(_:contenttype:source:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/newdocumentbutton/init%28_%3Acontenttype%3Asource%3A_%3A%29.json'
content_hash: 'sha256:04f823cbc3520641'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [NewDocumentButton](../newdocumentbutton.md)

# init(_:contentType:source:_:)

<sub>Initializer</sub>

Creates and opens new URL-based documents from a template picker.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
nonisolated init(_ label: Text? = nil, contentType: UTType, source: DocumentCreationSource, _ prepareDocumentURL: @escaping () async throws -> URL? = { nil })
```

## Parameters

- `label` — A label for the button.

- `contentType` — The content type of the document to create.

- `source` — A source for the document creation flow. When a document is created, you can retrieve its source from [FileDocumentConfiguration](../filedocumentconfiguration.md) or [URLDocumentConfiguration](../urldocumentconfiguration.md).

- `prepareDocumentURL` — Called when the user taps the button. Present a template picker or other UI, then return the URL of the prepared document, `nil` to request an empty document, or throw on cancellation.

## Discussion

```swift
NewDocumentButton(
    contentType: .text,
    source: .template
) {
    try await withCheckedThrowingContinuation { continuation in
        documentCreationContinuation = continuation
        showTemplatePicker = true
    }
}
```

## See Also

### Creating and opening a document with a creation source

- [init(_:contentType:source:)](<init(__contenttype_source_).md>) — Creates and opens new documents, tagging them with a creation source. _(beta)_
- [init(_:contentType:source:prepareDocumentURL:)](<init(__contenttype_source_preparedocumenturl_).md>) — Creates and opens new URL-based documents from a template picker. _(beta)_
