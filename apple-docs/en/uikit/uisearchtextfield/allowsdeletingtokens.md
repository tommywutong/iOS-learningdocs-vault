---
title: allowsDeletingTokens
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uisearchtextfield/allowsdeletingtokens
source_url: 'https://developer.apple.com/documentation/uikit/uisearchtextfield/allowsdeletingtokens'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uisearchtextfield/allowsdeletingtokens.json'
content_hash: 'sha256:38b26963d7bb523f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISearchTextField](../uisearchtextfield.md)

# allowsDeletingTokens

<sub>Instance Property</sub>

A Boolean that indicates whether the user can remove tokens from the search field.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var allowsDeletingTokens: Bool { get set }
```

## Discussion

The default value for this property is [true](../../swift/true.md).

You can always remove tokens programmatically. When this value is [true](../../swift/true.md), the user can also delete tokens and your app needs to handle tokens being re-added to the field with Undo.

## See Also

### Supporting token interactions

- [allowsCopyingTokens](allowscopyingtokens.md) — A Boolean that indicates whether the user can copy or drag tokens from the search field.
- [delegate](../uitextfield/delegate.md) — The text field’s delegate.
- [UISearchTextFieldDelegate](../uisearchtextfielddelegate.md) — The interface for the delegate of a search field.
- [UISearchTextFieldPasteItem](../uisearchtextfieldpasteitem.md) — A protocol that supports pasting tokens.
