---
title: 'isEquivalent(to:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift, swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/locale/language-swift.struct/isequivalent(to:)'
source_url: 'https://developer.apple.com/documentation/foundation/locale/language-swift.struct/isequivalent(to:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/locale/language-swift.struct/isequivalent%28to%3A%29.json'
content_hash: 'sha256:3267af88a3769fee'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [Locale](../../locale.md) · [Language](../language-swift.struct.md)

# isEquivalent(to:)

<sub>Instance Method</sub>

Returns a Boolean value that indicates whether this language and another language are equivalent after expanding missing components.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func isEquivalent(to language: Locale.Language) -> Bool
```

## Parameters

- `language` — A language to compare equivalence with.

## Return Value

`true` if the two languages are equivalent; `false` otherwise.

## Discussion

The following example shows equivalence tests run on various ways of expressing the US English language, followed by a test against UK English.

```swift
let en = Locale.Language(identifier: "en")
let enUS = Locale.Language(identifier: "en-US")
let enLatn = Locale.Language(identifier: "en-Latn")
let enLatnUS = Locale.Language(identifier: "en-Latn-US")

let test1 = en.isEquivalent(to: enUS) // true
let test2 = en.isEquivalent(to: enLatn) // true
let test3 = en.isEquivalent(to: enLatnUS) // true

let enUK = Locale.Language(identifier: "en-UK")
let test4 = en.isEquivalent(to: enUK) // false
```

## See Also

### Examining language relationships

- [parent](parent.md) — The parent language of this language, if available.
- [hasCommonParent(with:)](<hascommonparent(with_).md>) — Returns a Boolean value that indicates if the given language shares a common parent with this language.
