---
title: 'learnWord(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitextchecker/learnword(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitextchecker/learnword(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextchecker/learnword%28_%3A%29.json'
content_hash: 'sha256:c1973a062543d2c9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextChecker](../uitextchecker.md)

# learnWord(_:)

<sub>Type Method</sub>

Tells the text checker to learn the specified word so that it doesn’t evaluate it as misspelled.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
class func learnWord(_ word: String)
```

## Parameters

- `word` — A string representing the word for the class to learn.

## Discussion

When a `UITextChecker` object learns a word, it is added to the dictionary. It is global across languages.

## See Also

### Learning and Ignoring Words

- [- ignoreWord:](<ignoreword(__).md>) — Tells the text checker to ignore the specified word when spell-checking.
- [ignoredWords](ignoredwords.md) — Returns the words that the text checker ignores when spell-checking.
- [+ unlearnWord:](<unlearnword(__).md>) — Tells the text checker to unlearn the specified word.
- [+ hasLearnedWord:](<haslearnedword(__).md>) — Returns whether the text checker has learned the specified word.
