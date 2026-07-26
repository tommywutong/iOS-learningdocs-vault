---
title: contentType
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+（27.0 起废弃）, iPadOS 14.0+（27.0 起废弃）, Mac Catalyst 14.0+（27.0 起废弃）, macOS 11.0+（27.0 起废弃）, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: true
doc_path: /documentation/swiftui/filedocumentwriteconfiguration/contenttype
source_url: 'https://developer.apple.com/documentation/swiftui/filedocumentwriteconfiguration/contenttype'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/filedocumentwriteconfiguration/contenttype.json'
content_hash: 'sha256:f90b339df641fbda'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [FileDocumentWriteConfiguration](../filedocumentwriteconfiguration.md)

# contentType

<sub>Instance Property</sub>

The expected uniform type of the file contents.

> [!warning] Deprecated
> Use the Document protocol and URLDocumentConfiguration.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
let contentType: UTType
```

## See Also

### Writing the content

- [existingFile](existingfile.md) — The file wrapper containing the current document content. `nil` if the document is unsaved. _(deprecated)_
