---
title: fileURL
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/documentconfiguration/fileurl
source_url: 'https://developer.apple.com/documentation/swiftui/documentconfiguration/fileurl'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/documentconfiguration/fileurl.json'
content_hash: 'sha256:3979d891f7d105fb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [DocumentConfiguration](../documentconfiguration.md)

# fileURL

<sub>Instance Property</sub>

A URL of an open document.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
var fileURL: URL? { get }
```

## Discussion

If the document has never been saved, returns `nil`.

## See Also

### Getting configuration values

- [isEditable](iseditable.md) — A Boolean value that indicates whether you can edit the document.
