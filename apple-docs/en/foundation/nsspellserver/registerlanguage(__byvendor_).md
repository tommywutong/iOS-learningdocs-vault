---
title: 'registerLanguage(_:byVendor:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsspellserver/registerlanguage(_:byvendor:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsspellserver/registerlanguage(_:byvendor:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsspellserver/registerlanguage%28_%3Abyvendor%3A%29.json'
content_hash: 'sha256:dbfb0c0a025421ff'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSSpellServer](../nsspellserver.md)

# registerLanguage(_:byVendor:)

<sub>Instance Method</sub>

Notifies the receiver of a language your spelling checker can check.

<sub>Mac Catalyst, macOS</sub>

```swift
func registerLanguage(_ language: String?, byVendor vendor: String?) -> Bool
```

## Parameters

- `language` — A string specifying the English name of a language on Apple’s list of languages.

- `vendor` — A string that identifies the vendor (to distinguish your spelling checker from those that others may offer for the same language).

## Return Value

Returns [true](../../swift/true.md) if the language is registered, [false](../../swift/false.md) if for some reason it can’t be registered.

## Discussion

If your spelling checker supports more than one language, it should invoke this method once for each language. Registering a language-vendor combination causes it to appear in the Spelling panel’s pop-up menu of spelling checkers.

## See Also

### Providing Spelling Services

- [- run](<run().md>) — Causes the receiver to start listening for spell-checking requests.
