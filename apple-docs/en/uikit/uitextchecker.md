---
title: UITextChecker
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitextchecker
source_url: 'https://developer.apple.com/documentation/uikit/uitextchecker'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextchecker.json'
content_hash: 'sha256:434e91973137953d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UITextChecker

<sub>Class</sub>

An object to check a string (usually the text of a document) for misspelled words.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor class UITextChecker
```

## Overview

[UITextChecker](uitextchecker.md) spell-checks using a lexicon for a specific language. You can tell it to ignore specific words when spell-checking a particular document and you can have it learn words, which adds those words to the lexicon. You generally use one instance of [UITextChecker](uitextchecker.md) per document, although you can use a single instance to spell-check related pieces of text if you want to share ignored words and other state.

You may also use a text checker to obtain completions for partially entered words, as well as possible replacements for misspelled words, which you then can present to users.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md)

## Topics

### Initiating a Spell Check

- [- rangeOfMisspelledWordInString:range:startingAt:wrap:language:](<uitextchecker/rangeofmisspelledword(in_range_startingat_wrap_language_).md>) — Initiates a search of a range of a string for a misspelled word.

### Obtaining Word Guesses and Completions

- [- guessesForWordRange:inString:language:](<uitextchecker/guesses(forwordrange_in_language_).md>) — Returns a list of words that are possible valid replacements for a misspelled word.
- [- completionsForPartialWordRange:inString:language:](<uitextchecker/completions(forpartialwordrange_in_language_).md>) — Returns an array of strings that are possible completions for a partially entered word.

### Learning and Ignoring Words

- [- ignoreWord:](<uitextchecker/ignoreword(__).md>) — Tells the text checker to ignore the specified word when spell-checking.
- [ignoredWords](uitextchecker/ignoredwords.md) — Returns the words that the text checker ignores when spell-checking.
- [+ learnWord:](<uitextchecker/learnword(__).md>) — Tells the text checker to learn the specified word so that it doesn’t evaluate it as misspelled.
- [+ unlearnWord:](<uitextchecker/unlearnword(__).md>) — Tells the text checker to unlearn the specified word.
- [+ hasLearnedWord:](<uitextchecker/haslearnedword(__).md>) — Returns whether the text checker has learned the specified word.

### Getting the Available Languages

- [availableLanguages](uitextchecker/availablelanguages.md) — Returns the languages that the text checker’s class can perform spell-checking for.

### Instance Methods

- [- ignoreGrammarRange:inSentence:](<uitextchecker/ignoregrammarrange(__insentence_).md>) _(beta)_
- [- requestGrammarCheckingOfString:range:waitForAllResults:completionHandler:](<uitextchecker/requestgrammarchecking(of_range_waitforallresults_completionhandler_).md>) _(beta)_
