---
title: 'select(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiresponderstandardeditactions/select(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiresponderstandardeditactions/select(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiresponderstandardeditactions/select%28_%3A%29.json'
content_hash: 'sha256:4d6778f09042f84f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIResponderStandardEditActions](../uiresponderstandardeditactions.md)

# select(_:)

<sub>Instance Method</sub>

Selects the content in your responder.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func select(_ sender: Any?)
```

## Parameters

- `sender` — The object calling this method.

## Discussion

UIKit calls this method when the user selects the Select command from an editing menu. The command is used for the targeted selection of content in a view. For example, a text view uses this to select one or more words in the view and to display the selection interface.

## See Also

### Handling selection commands

- [- selectAll:](<selectall(__).md>) — Selects all of the content in the current responder.
