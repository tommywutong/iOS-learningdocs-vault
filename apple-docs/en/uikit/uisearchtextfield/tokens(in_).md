---
title: 'tokens(in:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uisearchtextfield/tokens(in:)'
source_url: 'https://developer.apple.com/documentation/uikit/uisearchtextfield/tokens(in:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uisearchtextfield/tokens%28in%3A%29.json'
content_hash: 'sha256:d44a2ad4757af572'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISearchTextField](../uisearchtextfield.md)

# tokens(in:)

<sub>Instance Method</sub>

Returns the search field’s tokens that are within a given range.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
func tokens(in textRange: UITextRange) -> [UISearchToken]
```

## Parameters

- `textRange` — The range specifying a subset of the tokens.

## Return Value

The tokens contained within the provided range.

## Discussion

Use this method to find out which tokens are included in the user’s current selection. You can provide a range that spans a mixture of tokens and text.

## See Also

### Customizing token behavior

- [tokenBackgroundColor](tokenbackgroundcolor.md) — The background color for all tokens in the search text field.
- [- positionOfTokenAtIndex:](<positionoftoken(at_).md>) — Converts a token index into a text position.
