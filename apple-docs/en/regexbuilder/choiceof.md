---
title: ChoiceOf
framework: RegexBuilder
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/regexbuilder/choiceof
source_url: 'https://developer.apple.com/documentation/regexbuilder/choiceof'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/regexbuilder/choiceof.json'
content_hash: 'sha256:1ccdea21c155af7f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [RegexBuilder](../regexbuilder.md)

# ChoiceOf

<sub>Structure</sub>

A regex component that chooses exactly one of its constituent regex components when matching.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct ChoiceOf<Output>
```

## Overview

You can use `ChoiceOf` to provide a group of regex components, each of which can be exclusively matched. In this example, `regex` successfully matches either a `"CREDIT"` or `"DEBIT"` substring:

```swift
let regex = Regex {
    ChoiceOf {
        "CREDIT"
        "DEBIT"
    }
}
let match = try regex.prefixMatch(in: "DEBIT    04032020    Payroll $69.73")
print(match?.0 as Any)
// Prints "DEBIT"
```

## Relationships

- **Conforms To**: [Copyable](../swift/copyable.md), [Escapable](../swift/escapable.md), [RegexComponent](../swift/regexcomponent.md)

## Topics

### Initializers

- [init(_:)](<choiceof/init(__).md>) — Creates a regex component that chooses exactly one of the regex components provided by the builder closure.

## See Also

### Components

- [CharacterClass](characterclass.md) — A class of characters that match in a regex.
- [Anchor](anchor.md) — A regex component that matches a specific condition at a particular position in an input string.
- [Lookahead](lookahead.md) — A regex component that allows a match to continue only if its contents match at the given location.
- [NegativeLookahead](negativelookahead.md) — A regex component that allows a match to continue only if its contents do not match at the given location.
