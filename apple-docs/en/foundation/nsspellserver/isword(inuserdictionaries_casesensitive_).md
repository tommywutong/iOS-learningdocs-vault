---
title: 'isWord(inUserDictionaries:caseSensitive:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsspellserver/isword(inuserdictionaries:casesensitive:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsspellserver/isword(inuserdictionaries:casesensitive:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsspellserver/isword%28inuserdictionaries%3Acasesensitive%3A%29.json'
content_hash: 'sha256:8952ebf49be3c54f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSSpellServer](../nsspellserver.md)

# isWord(inUserDictionaries:caseSensitive:)

<sub>Instance Method</sub>

Indicates whether a given word is in the user’s list of learned words or the document’s list of words to ignore.

<sub>Mac Catalyst, macOS</sub>

```swift
func isWord(inUserDictionaries word: String, caseSensitive flag: Bool) -> Bool
```

## Parameters

- `word` — The word to compare with those in the user dictionaries.

- `flag` — Specifies whether the comparison is case sensitive.

## Return Value

A Boolean value indicating whether the word is in the user dictionaries. If [true](../../swift/true.md), the word is acceptable to the user.
