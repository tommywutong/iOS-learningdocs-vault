---
title: 'rangeOfMisspelledWord(in:range:startingAt:wrap:language:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitextchecker/rangeofmisspelledword(in:range:startingat:wrap:language:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitextchecker/rangeofmisspelledword(in:range:startingat:wrap:language:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextchecker/rangeofmisspelledword%28in%3Arange%3Astartingat%3Awrap%3Alanguage%3A%29.json'
content_hash: 'sha256:64afdcbabffab2c1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextChecker](../uitextchecker.md)

# rangeOfMisspelledWord(in:range:startingAt:wrap:language:)

<sub>Instance Method</sub>

Initiates a search of a range of a string for a misspelled word.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func rangeOfMisspelledWord(in stringToCheck: String, range: NSRange, startingAt startingOffset: Int, wrap wrapFlag: Bool, language: String) -> NSRange
```

## Parameters

- `stringToCheck` — The string to check for misspelled words.

- `range` — The range of `stringToCheck` to check for a misspelled word.

- `startingOffset` — The offset within `range` of `stringToCheck` to begin checking for misspelled words.

- `wrapFlag` — [true](../../swift/true.md) to continue checking from the beginning of `range` if no misspelled word is found between `startingOffset` and the end of `range`. Specify [false](../../swift/false.md) to have spell-checking end at the end of `range`.

- `language` — The language of the of words to be checked for correct spelling. This string is a ISO 639-1 language code or a combined ISO 639-1 language code and ISO 3166-1 regional code (for example, `fr_FR`).

## Return Value

The range of the first misspelled word encountered or `{NSNotFound, 0}` if none is found.

## Discussion

To search an entire string or a range within that string, call this method in a loop, resetting `startingOffset` from each returned range, until you reach the end of the string or specified range within the string.
