---
title: 'selectAll(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiresponderstandardeditactions/selectall(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiresponderstandardeditactions/selectall(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiresponderstandardeditactions/selectall%28_%3A%29.json'
content_hash: 'sha256:793e53ff85b2686a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIResponderStandardEditActions](../uiresponderstandardeditactions.md)

# selectAll(_:)

<sub>Instance Method</sub>

Selects all of the content in the current responder.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func selectAll(_ sender: Any?)
```

## Parameters

- `sender` — The object calling this method.

## Discussion

UIKit calls this method when the user selects the Select All command from an editing menu. The command selects all content in the responder. For example, a text view selects all of its text and displays an appropriate selection interface.

## See Also

### Handling selection commands

- [- select:](<select(__).md>) — Selects the content in your responder.
