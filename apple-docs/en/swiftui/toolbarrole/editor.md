---
title: editor
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/toolbarrole/editor
source_url: 'https://developer.apple.com/documentation/swiftui/toolbarrole/editor'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/toolbarrole/editor.json'
content_hash: 'sha256:f0145e68bb5bf3f7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ToolbarRole](../toolbarrole.md)

# editor

<sub>Type Property</sub>

The editor role.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
static var editor: ToolbarRole { get }
```

## Discussion

Use this role for a toolbar that primarily displays controls geared towards editing document-like content. In iPadOS, this will leading align the navigation title, allow for toolbar items to occupy the center of the navigation bar, and provide a custom appearance for any back button present in the toolbar.

## See Also

### Behavior-specific roles

- [browser](browser.md) — The browser role.
- [navigationStack](navigationstack.md) — The navigationStack role.
