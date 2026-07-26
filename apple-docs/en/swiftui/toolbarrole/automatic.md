---
title: automatic
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/toolbarrole/automatic
source_url: 'https://developer.apple.com/documentation/swiftui/toolbarrole/automatic'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/toolbarrole/automatic.json'
content_hash: 'sha256:f75b8a273660b41e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ToolbarRole](../toolbarrole.md)

# automatic

<sub>Type Property</sub>

The automatic role.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var automatic: ToolbarRole { get }
```

## Discussion

In iOS, tvOS, and watchOS this resolves to the [navigationStack](navigationstack.md) role. In macOS, this resolves to the [editor](editor.md) role.
