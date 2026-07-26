---
title: creationSource
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, visionOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: /documentation/swiftui/urldocumentconfiguration/creationsource
source_url: 'https://developer.apple.com/documentation/swiftui/urldocumentconfiguration/creationsource'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/urldocumentconfiguration/creationsource.json'
content_hash: 'sha256:77961ae1cad5aa61'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [URLDocumentConfiguration](../urldocumentconfiguration.md)

# creationSource

<sub>Instance Property</sub>

The source associated with the button that created this document.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
@MainActor final var creationSource: DocumentCreationSource? { get }
```

## Discussion

On iOS, you can specify the source using a [NewDocumentButton](../newdocumentbutton.md) in [DocumentGroupLaunchScene](../documentgrouplaunchscene.md):

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

Use this property to determine which [NewDocumentButton](../newdocumentbutton.md) triggered the creation of the current document, allowing you to customize the UI accordingly.

## See Also

### Accessing document properties

- [fileURL](fileurl.md) — A URL of the open document if it is saved to disk. _(beta)_
- [lastContentModificationDate](lastcontentmodificationdate.md) — The date on which the contents of the document were last modified, if available. _(beta)_
