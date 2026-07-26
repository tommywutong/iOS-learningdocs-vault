---
title: isEditable
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+（27.0 起废弃）, iPadOS 14.0+（27.0 起废弃）, Mac Catalyst 14.0+（27.0 起废弃）, macOS 11.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）]
languages: [swift]
beta: false
deprecated: true
doc_path: /documentation/swiftui/filedocumentconfiguration/iseditable
source_url: 'https://developer.apple.com/documentation/swiftui/filedocumentconfiguration/iseditable'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/filedocumentconfiguration/iseditable.json'
content_hash: 'sha256:a9aa378ad850fa12'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [FileDocumentConfiguration](../filedocumentconfiguration.md)

# isEditable

<sub>Instance Property</sub>

A Boolean that indicates whether you can edit the document.

> [!warning] Deprecated
> Conform your type to Document and use URLDocumentConfiguration instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
var isEditable: Bool
```

## Discussion

This value is `false` if the document is in viewing mode, or if the file is not writable.

## See Also

### Getting document properties

- [fileURL](fileurl.md) — The URL of the open file document. _(deprecated)_
