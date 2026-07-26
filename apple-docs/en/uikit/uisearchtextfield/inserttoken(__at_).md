---
title: 'insertToken(_:at:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uisearchtextfield/inserttoken(_:at:)'
source_url: 'https://developer.apple.com/documentation/uikit/uisearchtextfield/inserttoken(_:at:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uisearchtextfield/inserttoken%28_%3Aat%3A%29.json'
content_hash: 'sha256:e1f8f60a8e009f03'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISearchTextField](../uisearchtextfield.md)

# insertToken(_:at:)

<sub>Instance Method</sub>

Adds a search token at a specific index.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
func insertToken(_ token: UISearchToken, at tokenIndex: Int)
```

## Parameters

- `token` — The search token to be inserted.

- `tokenIndex` — Within the [tokens](tokens.md) array, the index at which to insert the token.

## Discussion

If you’re converting part of the search field’s text into a token, use [- replaceTextualPortionOfRange:withToken:atIndex:](<replacetextualportion(of_with_at_).md>).

## See Also

### Adding and removing tokens

- [tokens](tokens.md) — The collection of tokens in the search text field.
- [- removeTokenAtIndex:](<removetoken(at_).md>) — Removes a particular search token from the search text field.
