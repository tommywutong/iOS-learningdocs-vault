---
title: parent
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift, swift, swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/locale/language-swift.struct/parent
source_url: 'https://developer.apple.com/documentation/foundation/locale/language-swift.struct/parent'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/locale/language-swift.struct/parent.json'
content_hash: 'sha256:eac5a5caea15ef40'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [Locale](../../locale.md) · [Language](../language-swift.struct.md)

# parent

<sub>Instance Property</sub>

The parent language of this language, if available.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var parent: Locale.Language? { get }
```

## Discussion

For example, the parent language of `en_US_POSIX` is `en_US`.

If the system can’t determine a parent language, this value is `nil`.

## See Also

### Examining language relationships

- [hasCommonParent(with:)](<hascommonparent(with_).md>) — Returns a Boolean value that indicates if the given language shares a common parent with this language.
- [isEquivalent(to:)](<isequivalent(to_).md>) — Returns a Boolean value that indicates whether this language and another language are equivalent after expanding missing components.
