---
title: 'unlearnWord(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitextchecker/unlearnword(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitextchecker/unlearnword(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextchecker/unlearnword%28_%3A%29.json'
content_hash: 'sha256:b0b2c54225ff0e48'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextChecker](../uitextchecker.md)

# unlearnWord(_:)

<sub>Type Method</sub>

Tells the text checker to unlearn the specified word.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
class func unlearnWord(_ word: String)
```

## Parameters

- `word` — A string representing the word for the class to unlearn.

## Discussion

When a `UITextChecker` object unlearns a word, it is removed from the dictionary.

## See Also

### Learning and Ignoring Words

- [- ignoreWord:](<ignoreword(__).md>) — Tells the text checker to ignore the specified word when spell-checking.
- [ignoredWords](ignoredwords.md) — Returns the words that the text checker ignores when spell-checking.
- [+ learnWord:](<learnword(__).md>) — Tells the text checker to learn the specified word so that it doesn’t evaluate it as misspelled.
- [+ hasLearnedWord:](<haslearnedword(__).md>) — Returns whether the text checker has learned the specified word.
