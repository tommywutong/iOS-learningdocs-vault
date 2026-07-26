---
title: 'positionOfToken(at:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uisearchtextfield/positionoftoken(at:)'
source_url: 'https://developer.apple.com/documentation/uikit/uisearchtextfield/positionoftoken(at:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uisearchtextfield/positionoftoken%28at%3A%29.json'
content_hash: 'sha256:ad8b52b0cf5c1249'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISearchTextField](../uisearchtextfield.md)

# positionOfToken(at:)

<sub>Instance Method</sub>

Converts a token index into a text position.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
func positionOfToken(at tokenIndex: Int) -> UITextPosition
```

## Parameters

- `tokenIndex` — The array index of the token.

## Return Value

The text position of the token.

## Discussion

Use this method to convert a token’s index in the [tokens](tokens.md) array into the token’s [UITextPosition](../uitextposition.md) in the overall contents of the text field. Many [UITextInput](../uitextinput.md) methods for interacting with text take a [UITextPosition](../uitextposition.md) or [UITextRange](../uitextrange.md) (constructed from two text positions) as a parameter.

To select a search token, assign a [UITextRange](../uitextrange.md) that contains the token’s position to the [selectedTextRange](../uitextinput/selectedtextrange.md) property.

## See Also

### Customizing token behavior

- [tokenBackgroundColor](tokenbackgroundcolor.md) — The background color for all tokens in the search text field.
- [- tokensInRange:](<tokens(in_).md>) — Returns the search field’s tokens that are within a given range.
