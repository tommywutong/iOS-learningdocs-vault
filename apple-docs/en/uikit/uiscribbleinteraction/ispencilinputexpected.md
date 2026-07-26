---
title: isPencilInputExpected
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiscribbleinteraction/ispencilinputexpected
source_url: 'https://developer.apple.com/documentation/uikit/uiscribbleinteraction/ispencilinputexpected'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiscribbleinteraction/ispencilinputexpected.json'
content_hash: 'sha256:77f174a6b0624e07'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIScribbleInteraction](../uiscribbleinteraction.md)

# isPencilInputExpected

<sub>Type Property</sub>

A Boolean value that indicates the user is likely to use Apple Pencil and handwriting instead of the keyboard to enter text.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
class var isPencilInputExpected: Bool { get }
```

## Discussion

If set to [true](../../swift/true.md), adjust the layout of UI elements that aren’t optimal for direct handwriting input. This allows more room for interaction with Apple Pencil. For example, small or resizable text fields can temporarily change their height to receive input from Apple Pencil, while preserving padding along the bottom of the text field.
