---
title: isEditable
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, visionOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitextinput/iseditable
source_url: 'https://developer.apple.com/documentation/uikit/uitextinput/iseditable'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextinput/iseditable.json'
content_hash: 'sha256:26d0f8f5da044bab'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextInput](../uitextinput.md)

# isEditable

<sub>Instance Property</sub>

A Boolean value that indicates whether the text view contains editable text.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
optional var isEditable: Bool { get }
```

## Discussion

Text views are normally editable, and the default value of this property is [true](../../swift/true.md) if you don’t provide an implementation. When implementing a custom text view, you might implement this property and return [false](../../swift/false.md) to prevent outside agents from modifying the content of your view. For example, you might disable editing to prevent the system’s writing tools panel from pasting content into your view.
