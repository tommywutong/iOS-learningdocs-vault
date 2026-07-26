---
title: 'parent(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [visionOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/ornamentattachmentanchor/parent(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/ornamentattachmentanchor/parent(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/ornamentattachmentanchor/parent%28_%3A%29.json'
content_hash: 'sha256:2e409c61cf1c8f2b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [OrnamentAttachmentAnchor](../ornamentattachmentanchor.md)

# parent(_:)

<sub>Type Method</sub>

The anchor point for the ornament expressed as a 3D unit point relative to its parent.

<sub>visionOS</sub>

```swift
static func parent(_ anchor: UnitPoint3D) -> OrnamentAttachmentAnchor
```

## Discussion

The parent depends on where the ornament modifier is placed. When used inside another ornament context, that ornament is the parent. Otherwise, it’s the Scene itself.
