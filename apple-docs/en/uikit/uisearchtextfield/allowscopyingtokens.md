---
title: allowsCopyingTokens
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uisearchtextfield/allowscopyingtokens
source_url: 'https://developer.apple.com/documentation/uikit/uisearchtextfield/allowscopyingtokens'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uisearchtextfield/allowscopyingtokens.json'
content_hash: 'sha256:20bb1933724deed7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISearchTextField](../uisearchtextfield.md)

# allowsCopyingTokens

<sub>Instance Property</sub>

A Boolean that indicates whether the user can copy or drag tokens from the search field.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var allowsCopyingTokens: Bool { get set }
```

## Discussion

The default value for this property is [true](../../swift/true.md).

To support copying tokens, [allowsCopyingTokens](allowscopyingtokens.md) must be [true](../../swift/true.md) and the search field’s [delegate](../uitextfield/delegate.md) must also implement [- searchTextField:itemProviderForCopyingToken:](<../uisearchtextfielddelegate/searchtextfield(__itemproviderforcopying_).md>).

[UISearchTextField](../uisearchtextfield.md) enables the Copy command when a user selects text, even if the selection also includes tokens and [allowsCopyingTokens](allowscopyingtokens.md) is [false](../../swift/false.md).

## See Also

### Supporting token interactions

- [allowsDeletingTokens](allowsdeletingtokens.md) — A Boolean that indicates whether the user can remove tokens from the search field.
- [delegate](../uitextfield/delegate.md) — The text field’s delegate.
- [UISearchTextFieldDelegate](../uisearchtextfielddelegate.md) — The interface for the delegate of a search field.
- [UISearchTextFieldPasteItem](../uisearchtextfieldpasteitem.md) — A protocol that supports pasting tokens.
