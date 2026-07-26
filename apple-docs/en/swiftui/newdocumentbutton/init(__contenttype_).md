---
title: 'init(_:contentType:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, visionOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/newdocumentbutton/init(_:contenttype:)'
source_url: 'https://developer.apple.com/documentation/swiftui/newdocumentbutton/init(_:contenttype:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/newdocumentbutton/init%28_%3Acontenttype%3A%29.json'
content_hash: 'sha256:5c87cff84504ff3e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [NewDocumentButton](../newdocumentbutton.md)

# init(_:contentType:)

<sub>Initializer</sub>

Creates and opens new documents.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
@export(implementation) nonisolated init(_ title: LocalizedStringResource, contentType: UTType? = nil)
```

## Parameters

- `title` — A title resource to use as the button title.

- `contentType` — An optional content type of the document to create.

## See Also

### Creating and opening a document

- [init(_:contentType:prepareDocumentURL:)](<init(__contenttype_preparedocumenturl_).md>) — Creates and opens new documents.
