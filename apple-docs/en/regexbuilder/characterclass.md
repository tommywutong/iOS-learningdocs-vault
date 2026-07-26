---
title: CharacterClass
framework: RegexBuilder
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/regexbuilder/characterclass
source_url: 'https://developer.apple.com/documentation/regexbuilder/characterclass'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/regexbuilder/characterclass.json'
content_hash: 'sha256:42349152d9d25f0a'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [RegexBuilder](../regexbuilder.md)

# CharacterClass

<sub>Structure</sub>

A class of characters that match in a regex.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct CharacterClass
```

## Overview

A character class can represent individual characters, a group of characters, the set of character that match some set of criteria, or a set algebraic combination of all of the above.

## Relationships

- **Conforms To**: [Copyable](../swift/copyable.md), [Escapable](../swift/escapable.md), [RegexComponent](../swift/regexcomponent.md)

## Topics

### Instance Properties

- [inverted](characterclass/inverted.md) — A character class that matches any character that does not match this character class.

### Instance Methods

- [intersection(_:)](<characterclass/intersection(__).md>) — Returns a character class from the intersection of this class and the given class.
- [subtracting(_:)](<characterclass/subtracting(__).md>) — Returns a character class by subtracting the given class from this class.
- [symmetricDifference(_:)](<characterclass/symmetricdifference(__).md>) — Returns a character class matching elements in one or the other, but not both, of this class and the given class.
- [union(_:)](<characterclass/union(__).md>) — Returns a character class from the union of this class and the given class.

### Type Methods

- [generalCategory(_:)](<characterclass/generalcategory(__).md>) — Returns a character class that matches any element with the given Unicode general category.

## See Also

### Components

- [Anchor](anchor.md) — A regex component that matches a specific condition at a particular position in an input string.
- [Lookahead](lookahead.md) — A regex component that allows a match to continue only if its contents match at the given location.
- [NegativeLookahead](negativelookahead.md) — A regex component that allows a match to continue only if its contents do not match at the given location.
- [ChoiceOf](choiceof.md) — A regex component that chooses exactly one of its constituent regex components when matching.
