---
title: 'init(id:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, visionOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: '/documentation/swiftui/documentcreationsource/init(id:)'
source_url: 'https://developer.apple.com/documentation/swiftui/documentcreationsource/init(id:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/documentcreationsource/init%28id%3A%29.json'
content_hash: 'sha256:2bcccb66cd330ffb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [DocumentCreationSource](../documentcreationsource.md)

# init(id:)

<sub>Initializer</sub>

Creates a document creation source with the given identifier.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
init(id: String)
```

## Parameters

- `id` — A string that uniquely identifies the creation flow within your app.

## Discussion

Use different sources to distinguish between document creation flows in your app.

```swift
extension DocumentCreationSource {
    static let scanner: Self =
        DocumentCreationSource(id: "document-from-scanner")

    static let template: Self =
        DocumentCreationSource(id: "document-from-template")
}

DocumentGroupLaunchScene("Documents") {
    NewDocumentButton("Scan Document", source: .scanner)
    NewDocumentButton("New from Template", source: .template)
}
```

When a document is created, you can retrieve its source from [URLDocumentConfiguration](../urldocumentconfiguration.md) or [FileDocumentConfiguration](../filedocumentconfiguration.md).
