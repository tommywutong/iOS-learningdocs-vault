---
title: isEditable
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+（27.0 起废弃）, iPadOS 14.0+（27.0 起废弃）, Mac Catalyst 14.0+（27.0 起废弃）, macOS 11.0+（27.0 起废弃）, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: true
doc_path: /documentation/swiftui/referencefiledocumentconfiguration/iseditable
source_url: 'https://developer.apple.com/documentation/swiftui/referencefiledocumentconfiguration/iseditable'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/referencefiledocumentconfiguration/iseditable.json'
content_hash: 'sha256:81e2019562a106f2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ReferenceFileDocumentConfiguration](../referencefiledocumentconfiguration.md)

# isEditable

<sub>Instance Property</sub>

A Boolean that indicates whether you can edit the document.

> [!warning] Deprecated
> Use Document protocol and URLDocumentConfiguration instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
@MainActor @preconcurrency var isEditable: Bool
```

## Discussion

The value is `false` if the document is in viewing mode, or if the file is not writable.

## See Also

### Getting document properties

- [fileURL](fileurl.md) — The URL of the open file document. _(deprecated)_
