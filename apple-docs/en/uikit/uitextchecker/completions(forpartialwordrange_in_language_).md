---
title: 'completions(forPartialWordRange:in:language:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitextchecker/completions(forpartialwordrange:in:language:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitextchecker/completions(forpartialwordrange:in:language:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextchecker/completions%28forpartialwordrange%3Ain%3Alanguage%3A%29.json'
content_hash: 'sha256:fbe3e31d8c3fd9a1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextChecker](../uitextchecker.md)

# completions(forPartialWordRange:in:language:)

<sub>Instance Method</sub>

Returns an array of strings that are possible completions for a partially entered word.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func completions(forPartialWordRange range: NSRange, in string: String, language: String) -> [String]?
```

## Parameters

- `range` — The range of a partially entered word in `string`.

- `string` — A string in which there is a partially entered word, as located by `range`.

- `language` — The language of the of the words that are possible corrections. This string is a ISO 639-1 language code or a combined ISO 639-1 language code and ISO 3166-1 regional code (for example, `fr_CA`).

## Return Value

An array of strings, each of which is a completion of a partially entered word represented by `range` in `string`. If no possible completions are found,  the method returns an empty array.

## Discussion

The strings in the array are in the order they should be presented to the user—that is, more probable completions come first in the array.

## See Also

### Obtaining Word Guesses and Completions

- [- guessesForWordRange:inString:language:](<guesses(forwordrange_in_language_).md>) — Returns a list of words that are possible valid replacements for a misspelled word.
