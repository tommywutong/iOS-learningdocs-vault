---
title: 'guesses(forWordRange:in:language:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitextchecker/guesses(forwordrange:in:language:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitextchecker/guesses(forwordrange:in:language:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextchecker/guesses%28forwordrange%3Ain%3Alanguage%3A%29.json'
content_hash: 'sha256:1b047746f8cb4889'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextChecker](../uitextchecker.md)

# guesses(forWordRange:in:language:)

<sub>Instance Method</sub>

Returns a list of words that are possible valid replacements for a misspelled word.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func guesses(forWordRange range: NSRange, in string: String, language: String) -> [String]?
```

## Parameters

- `range` — The range of a misspelled word in `string`.

- `string` — A string in which there is a misspelled word, as located by `range`.

- `language` — The language of the of the words that are possible corrections. This string is from the ISO 639-1 standard, for example `es` (Spanish).

## Return Value

An array of strings each of which might be a correct substitute (that is, a guess) for a misspelled word in the given range of the string. If no possible guesses are found,  the method returns an empty array.

## Discussion

The strings in the array are in the order they should be presented to the user—that is, more probable guesses come first in the array.

## See Also

### Obtaining Word Guesses and Completions

- [- completionsForPartialWordRange:inString:language:](<completions(forpartialwordrange_in_language_).md>) — Returns an array of strings that are possible completions for a partially entered word.
