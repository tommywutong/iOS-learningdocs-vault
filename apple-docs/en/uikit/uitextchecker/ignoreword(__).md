---
title: 'ignoreWord(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitextchecker/ignoreword(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitextchecker/ignoreword(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextchecker/ignoreword%28_%3A%29.json'
content_hash: 'sha256:533ff1d39074b5fd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextChecker](../uitextchecker.md)

# ignoreWord(_:)

<sub>Instance Method</sub>

Tells the text checker to ignore the specified word when spell-checking.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func ignoreWord(_ wordToIgnore: String)
```

## Parameters

- `wordToIgnore` — A string that is a word the receiver should ignore when it is spell-checking a document.

## Discussion

The spell checker excludes ignored words as misspelled words during the current spell-checking session only.

## See Also

### Learning and Ignoring Words

- [ignoredWords](ignoredwords.md) — Returns the words that the text checker ignores when spell-checking.
- [+ learnWord:](<learnword(__).md>) — Tells the text checker to learn the specified word so that it doesn’t evaluate it as misspelled.
- [+ unlearnWord:](<unlearnword(__).md>) — Tells the text checker to unlearn the specified word.
- [+ hasLearnedWord:](<haslearnedword(__).md>) — Returns whether the text checker has learned the specified word.
