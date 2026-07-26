---
title: 'hasCommonParent(with:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift, swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/locale/language-swift.struct/hascommonparent(with:)'
source_url: 'https://developer.apple.com/documentation/foundation/locale/language-swift.struct/hascommonparent(with:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/locale/language-swift.struct/hascommonparent%28with%3A%29.json'
content_hash: 'sha256:df58853b83baeb5e'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [Locale](../../locale.md) · [Language](../language-swift.struct.md)

# hasCommonParent(with:)

<sub>Instance Method</sub>

Returns a Boolean value that indicates if the given language shares a common parent with this language.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func hasCommonParent(with language: Locale.Language) -> Bool
```

## Parameters

- `language` — A language to compare parentage with.

## Return Value

`true` if this language and language share a common parent; `false` otherwise.

## See Also

### Examining language relationships

- [parent](parent.md) — The parent language of this language, if available.
- [isEquivalent(to:)](<isequivalent(to_).md>) — Returns a Boolean value that indicates whether this language and another language are equivalent after expanding missing components.
