---
title: tokens
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uisearchtextfield/tokens
source_url: 'https://developer.apple.com/documentation/uikit/uisearchtextfield/tokens'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uisearchtextfield/tokens.json'
content_hash: 'sha256:8be6494fa8c492f7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISearchTextField](../uisearchtextfield.md)

# tokens

<sub>Instance Property</sub>

The collection of tokens in the search text field.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var tokens: [UISearchToken] { get set }
```

## Discussion

Use this property to access existing tokens, or to replace all tokens at once. To convert text in the search field into a token, use [- replaceTextualPortionOfRange:withToken:atIndex:](<replacetextualportion(of_with_at_).md>).

## See Also

### Adding and removing tokens

- [- insertToken:atIndex:](<inserttoken(__at_).md>) — Adds a search token at a specific index.
- [- removeTokenAtIndex:](<removetoken(at_).md>) — Removes a particular search token from the search text field.
