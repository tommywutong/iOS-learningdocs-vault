---
title: 'removeToken(at:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uisearchtextfield/removetoken(at:)'
source_url: 'https://developer.apple.com/documentation/uikit/uisearchtextfield/removetoken(at:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uisearchtextfield/removetoken%28at%3A%29.json'
content_hash: 'sha256:cce84f0b41e969b2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISearchTextField](../uisearchtextfield.md)

# removeToken(at:)

<sub>Instance Method</sub>

Removes a particular search token from the search text field.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
func removeToken(at tokenIndex: Int)
```

## Parameters

- `tokenIndex` — Within the [tokens](tokens.md) array, the index of the token you want to remove.

## See Also

### Adding and removing tokens

- [tokens](tokens.md) — The collection of tokens in the search text field.
- [- insertToken:atIndex:](<inserttoken(__at_).md>) — Adds a search token at a specific index.
