---
title: 'hasLearnedWord(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitextchecker/haslearnedword(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitextchecker/haslearnedword(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextchecker/haslearnedword%28_%3A%29.json'
content_hash: 'sha256:a47c05259d5ef874'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextChecker](../uitextchecker.md)

# hasLearnedWord(_:)

<sub>Type Method</sub>

Returns whether the text checker has learned the specified word.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
class func hasLearnedWord(_ word: String) -> Bool
```

## Parameters

- `word` — A string representing a word.

## Return Value

[true](../../swift/true.md) if the class has learned the word, otherwise [false](../../swift/false.md).

## See Also

### Learning and Ignoring Words

- [- ignoreWord:](<ignoreword(__).md>) — Tells the text checker to ignore the specified word when spell-checking.
- [ignoredWords](ignoredwords.md) — Returns the words that the text checker ignores when spell-checking.
- [+ learnWord:](<learnword(__).md>) — Tells the text checker to learn the specified word so that it doesn’t evaluate it as misspelled.
- [+ unlearnWord:](<unlearnword(__).md>) — Tells the text checker to unlearn the specified word.
