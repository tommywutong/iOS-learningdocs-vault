---
title: ignoredWords
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitextchecker/ignoredwords
source_url: 'https://developer.apple.com/documentation/uikit/uitextchecker/ignoredwords'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextchecker/ignoredwords.json'
content_hash: 'sha256:ea55eba3e31e0a7c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextChecker](../uitextchecker.md)

# ignoredWords

<sub>Instance Property</sub>

Returns the words that the text checker ignores when spell-checking.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var ignoredWords: [String]? { get set }
```

## Return Value

An array of strings, each of which specifies a word the receiver ignores when it is spell-checking a document.

## Discussion

The spell checker excludes ignored words as misspelled words during the current spell-checking session only.

## See Also

### Learning and Ignoring Words

- [- ignoreWord:](<ignoreword(__).md>) — Tells the text checker to ignore the specified word when spell-checking.
- [+ learnWord:](<learnword(__).md>) — Tells the text checker to learn the specified word so that it doesn’t evaluate it as misspelled.
- [+ unlearnWord:](<unlearnword(__).md>) — Tells the text checker to unlearn the specified word.
- [+ hasLearnedWord:](<haslearnedword(__).md>) — Returns whether the text checker has learned the specified word.
