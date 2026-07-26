---
title: Anchor
framework: RegexBuilder
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/regexbuilder/anchor
source_url: 'https://developer.apple.com/documentation/regexbuilder/anchor'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/regexbuilder/anchor.json'
content_hash: 'sha256:85aec351a32be180'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [RegexBuilder](../regexbuilder.md)

# Anchor

<sub>Structure</sub>

A regex component that matches a specific condition at a particular position in an input string.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct Anchor
```

## Overview

You can use anchors to guarantee that a match only occurs at certain points in an input string, such as at the beginning of the string or at the end of a line.

## Relationships

- **Conforms To**: [Copyable](../swift/copyable.md), [Escapable](../swift/escapable.md), [RegexComponent](../swift/regexcomponent.md)

## Topics

### Instance Properties

- [inverted](anchor/inverted.md) — The inverse of this anchor, which matches at every position that this anchor does not.

### Type Properties

- [endOfLine](anchor/endofline.md) — An anchor that matches at the end of a line, including at the end of the input string.
- [endOfSubject](anchor/endofsubject.md) — An anchor that matches at the end of the input string.
- [endOfSubjectBeforeNewline](anchor/endofsubjectbeforenewline.md) — An anchor that matches at the end of the input string or at the end of the line immediately before the end of the string.
- [firstMatchingPositionInSubject](anchor/firstmatchingpositioninsubject.md) — An anchor that matches at the first position of a match in the input string.
- [startOfLine](anchor/startofline.md) — An anchor that matches at the start of a line, including the start of the input string.
- [startOfSubject](anchor/startofsubject.md) — An anchor that matches at the start of the input string.
- [textSegmentBoundary](anchor/textsegmentboundary.md) — An anchor that matches at a grapheme cluster boundary.
- [wordBoundary](anchor/wordboundary.md) — An anchor that matches at a word boundary.

## See Also

### Components

- [CharacterClass](characterclass.md) — A class of characters that match in a regex.
- [Lookahead](lookahead.md) — A regex component that allows a match to continue only if its contents match at the given location.
- [NegativeLookahead](negativelookahead.md) — A regex component that allows a match to continue only if its contents do not match at the given location.
- [ChoiceOf](choiceof.md) — A regex component that chooses exactly one of its constituent regex components when matching.
