---
title: isEditable
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/documentconfiguration/iseditable
source_url: 'https://developer.apple.com/documentation/swiftui/documentconfiguration/iseditable'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/documentconfiguration/iseditable.json'
content_hash: 'sha256:d4da3e71af59cf50'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [DocumentConfiguration](../documentconfiguration.md)

# isEditable

<sub>Instance Property</sub>

A Boolean value that indicates whether you can edit the document.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
var isEditable: Bool { get }
```

## Discussion

On macOS, the document could be non-editable if the user lacks write permissions, the parent directory or volume is read-only, or the document couldn’t be autosaved.

On iOS, the document is not editable if there was an error reading or saving it, there’s an unresolved conflict, the document is being uploaded or downloaded, or otherwise, it is currently busy and unsafe for user edits.

## See Also

### Getting configuration values

- [fileURL](fileurl.md) — A URL of an open document.
